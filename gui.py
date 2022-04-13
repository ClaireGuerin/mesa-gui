import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication
from mesagui.view import ViewGUI as View

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    mesagui = QApplication(sys.argv)
    # Show the GUI's view
    view = View()
    view.show()
    # Execute the GUI's main loop
    sys.exit(mesagui.exec_())

if __name__ == '__main__':
    main()