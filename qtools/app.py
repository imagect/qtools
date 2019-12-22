
from qtpy.QtWidgets import QApplication
import sys

qtApp = None
def mkQApp():
    global qtApp    
    qtApp = QApplication.instance()
    if qtApp is None:
        qtApp = QApplication(sys.argv)
    return qtApp

if qtApp is None :
    mkQApp()