import urllib
import webbrowser 
from qgis.PyQt import QtWidgets

'''
This action is to be used with a vector layer that contains a field named 'wikipedia'.
It should be added with the 'Feature' action scope.
When the user triggers the action, a browser will be opened, which shows the corresponding wikipedia entry for the value in that field.

Here we use the value of the 'wikipedia' field to compose the url.
We use the expressions notation, and the [%wikipedia%] string will be replaced
with the value of the 'wikipedia' field before the code is executed.
'''
url = "https://en.wikipedia.org/wiki/" + "[%wikipedia%]"
try:
	urllib.request.urlopen(url)
	webbrowser.open(url, new=0, autoraise=True)
except:
	QtWidgets.QMessageBox.warning(None, "Wrong value", "The corresponding Wikipedia page does not exist")
	

