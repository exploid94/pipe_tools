import sys
import os
from PySide2 import QtCore, QtWidgets, QtGui

import launcher

class BlenderLauncherWindow(launcher.LauncherWindow):
    def __init__(self, software="blender"):
        super().__init__(software)

    def launchSoftware(self):
        self.setPackageEnvironments()
        self.setProjectEnvironments()
        if self.file_tree.currentItem().text(0).endswith(".blend"):
            os.startfile(self.file_tree.currentItem().data(32, 0))
        else:
            os.startfile("C:/Program Files/Blender Foundation/Blender 3.1/blender-launcher.exe")


app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")

# set the color scheme
dark_palette = QtGui.QPalette()
dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25,25,25))
dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
app.setPalette(dark_palette)

window = BlenderLauncherWindow()
window.show()

app.exec_()
