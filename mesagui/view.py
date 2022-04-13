# implements the app's GUI. 
# It hosts all the widgets the end-user would need to interact with the application. 
# The view also receives user actions and events. 
# Here, the view will be the window you’ll see on your screen.

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QComboBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

__version__ = '0.1'
__author__ = 'Claire Guerin'

# Create a subclass of QMainWindow to setup the calculator's GUI
class ViewGUI(QMainWindow):
    """Mesa's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Mesa: Individual Based Model')
        #self.setFixedSize(2000, 1000)
        self.showMaximized()
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        
        # Set the general layout
        self.generalLayout = QHBoxLayout()
        self._centralWidget.setLayout(self.generalLayout)
        
        self._createSelectorEditor()
        self._createWebView()
        

    def _createSelectorEditor(self):
        """Create the left hand side model selector and editor."""
        layout = QVBoxLayout()
        selectText = QLabel('Select model')
        self._createDropDownMenu()
        self._createModelEditor()
        self._createUpdateButton()
        
        layout.addWidget(selectText)
        layout.addWidget(self._dropDownMenu)
        layout.addWidget(self.updateButton)
        self.generalLayout.addLayout(layout)
        
    def _createDropDownMenu(self):
        menu = QComboBox()
        menu.addItem('Boids')
        menu.addItem('Wolf-Sheep')
        menu.addItem('Virus Infection')
        menu.addItem('Viral Network')
        self._dropDownMenu = menu
        
    def _createModelEditor(self):
        pass
        
    def _createUpdateButton(self):
        self.updateButton = QPushButton('Update Code')
        
    def _createWebView(self):
        webEngineView = QWebEngineView() # create the webview widget
        webEngineView.setHtml('<h1>Web view</h1>')
        self.generalLayout.addWidget(webEngineView)