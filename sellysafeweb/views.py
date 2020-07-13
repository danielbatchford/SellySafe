import datetime as dt

from django.shortcuts import render, redirect

from SellySafe import settings
from sellysafeweb.forms import ReportForm, FeedbackForm
from sellysafeweb.models import Report

# Redirect for empty sub-domain to /map
def redirect_to_map(request):
    return redirect('sellysafeweb:map')


# Main map view
def map(request):

    # Assign the submitted form or create one if it doesn't exist
    form = ReportForm(request.POST or None)

    # If user submits the form
    if request.method == 'POST':
        if form.is_valid():

            # Integer representing form choices ['just now', '5 minutes ago', ...] etc
            date_choice = form.cleaned_data['datetime']

            # Assign the corresponding time offsets from the current time
            if int(date_choice) > 4:
                datetime = dt.datetime.now() - dt.timedelta(minutes=int(date_choice))
            else:
                datetime = dt.datetime.now() - dt.timedelta(hours=int(date_choice))

            # Account for BST times
            datetime += dt.timedelta(hours = settings.BST_OFFSET)

            # Create a report object from the form data
            report = Report.objects.create(contents=form.cleaned_data['contents'],
                                           lat=form.cleaned_data['lat'],
                                           long=form.cleaned_data['long'],
                                           datetime=datetime)

            # Save the form to the database
            report.save()
            return redirect('sellysafeweb:map')

    # Filter the reports by n days ago. +1 needed as date duration is inclusive.
    cutoff_date = dt.date.today() - dt.timedelta(days=settings.SHOW_DURATION + 1)
    reports = Report.objects.filter(datetime__gte=cutoff_date)

    # Render the HTML file with the following parameters
    return render(request, 'sellysafeweb/map.html', {
        'reports': reports,
        'form': form,
        'map_box_key': settings.MAPBOX_KEY,
        'city_center': settings.CITY_CENTER,
        'bounds': settings.BOUNDS,
        'duration': settings.SHOW_DURATION,
    })


# About page rendering
def about(request):
    return render(request, 'sellysafeweb/about.html')


# Render an HTML feedback form view and handle form generating and posting
def feedback(request):
    form = FeedbackForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=True)
            return redirect('sellysafeweb:feedback_confirmation')
    return render(request, 'sellysafeweb/feedback.html', {'form': form})


# Render a confirmation that the form submission was successful
def feedback_confirmation(request):
    return render(request, 'sellysafeweb/feedback_confirmation.html')
