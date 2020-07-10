html css js python


# SellySafe
The website is hosted [here](http://danielbatchford1.pythonanywhere.com/about).
## About
This is a Django based web app allowing users to add reports of issues in the student accomodation
area of the University of Birmingham. Currently, issues are usually posted on Facebook where they
are not always seen. This app allows users to view recent reports in the area on a map, as well
 as clicking on the map to quickly add a report at that location.

## Languages / Frameworks
This app uses the full stack Python framework Django to serve both front and back-end. It utilises Mapbox GL JS
for the map rendering, marker and popup rendering as well as converting between user clicks and corresponding
latitude and longitude co-ordinates. Other UI elements use Materialize.css as well as Animate.css to allow easy use of dynamic
web page elements.

Reports / Feedback is stored on an sqlite database.

The website is hosted on PythonAnywhere, allowing python to run on a virtual linux environment.

## Credits
- [PythonAnywhere](https://www.pythonanywhere.com/) for Python online hosting.
- [MapBox GL JS](https://www.mapbox.com/) for the map framework.
- [Materialize.css](https://materializecss.com/) for the CSS styling.
- [Animate.css](https://animate.style/) for the website's animation.
- [django-material](https://pypi.org/project/django-material/0.5.1/) to allow Django form radio buttons to work nicely with materialize.css.