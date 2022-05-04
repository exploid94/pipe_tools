import sys
import os
from functools import partial
from PySide2 import QtCore, QtWidgets, QtGui

import project_utils
import code_utils

class MayaLauncherWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maya Launcher")

        # create a menu bar
        self.menu = QtWidgets.QMenuBar()
        self.pkg_menu = self.menu.addMenu("&Pkg")
        self._populatePackages()

        # create layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.project_layout = QtWidgets.QGridLayout()
        self.file_layout = QtWidgets.QGridLayout()
        self.main_layout.addLayout(self.project_layout)
        self.main_layout.addLayout(self.file_layout)
        self.setLayout(self.main_layout)

        # create main widgets
        self.project_label = QtWidgets.QLabel("Project:")
        self.project_cb = QtWidgets.QComboBox()
        self.data_type_label = QtWidgets.QLabel("Data Type:")
        self.data_type_cb = QtWidgets.QComboBox()
        self.asset_type_label = QtWidgets.QLabel("Asset Type:")
        self.asset_type_cb = QtWidgets.QComboBox()
        self.asset_label = QtWidgets.QLabel("Asset:")
        self.asset_cb = QtWidgets.QComboBox()
        self.sequence_label = QtWidgets.QLabel("Sequence:")
        self.sequence_cb = QtWidgets.QComboBox()
        self.shot_label = QtWidgets.QLabel("Shot:")
        self.shot_cb = QtWidgets.QComboBox()
        self.stage_label = QtWidgets.QLabel("Stage:")
        self.stage_cb = QtWidgets.QComboBox()
        self.file_tree = QtWidgets.QTreeWidget()
        self.file_tree.setHeaderHidden(True)
        self.launch_button = QtWidgets.QPushButton("Launch Maya")

        # populate the widgets
        self._updateAll()

        # Add the widgets to the layout
        self.project_layout.addWidget(self.project_label, 0, 0, 1, 1)
        self.project_layout.addWidget(self.project_cb, 0, 1, 1, 5)
        self.project_layout.addWidget(self.data_type_label, 1, 0, 1, 1)
        self.project_layout.addWidget(self.data_type_cb, 1, 1, 1, 5)
        self.project_layout.addWidget(self.asset_type_label, 2, 0, 1, 5)
        self.project_layout.addWidget(self.asset_type_cb, 2, 1, 1, 5)
        self.project_layout.addWidget(self.asset_label, 3, 0, 1, 5)
        self.project_layout.addWidget(self.asset_cb, 3, 1, 1, 5)
        self.project_layout.addWidget(self.sequence_label, 4, 0, 1, 5)
        self.project_layout.addWidget(self.sequence_cb, 4, 1, 1, 5)
        self.project_layout.addWidget(self.shot_label, 5, 0, 1, 5)
        self.project_layout.addWidget(self.shot_cb, 5, 1, 1, 5)
        self.project_layout.addWidget(self.stage_label, 6, 0, 1, 5)
        self.project_layout.addWidget(self.stage_cb, 6, 1, 1, 5)
        self.file_layout.addWidget(self.file_tree, 0, 0, 5, 5)
        self.file_layout.addWidget(self.launch_button, 6, 0, 1, 5)
        self.main_layout.setMenuBar(self.menu)

        # Connect the widgets to signals
        self.project_cb.currentIndexChanged.connect(self._updateDataType)
        self.data_type_cb.currentIndexChanged.connect(self._updateDataTypeWidgets)
        self.asset_type_cb.currentIndexChanged.connect(self._updateAsset)
        self.asset_cb.currentIndexChanged.connect(self._updateStage)
        self.stage_cb.currentIndexChanged.connect(self._updateFileTree)
        self.launch_button.clicked.connect(self.launchMaya)

    def _updateDataTypeWidgets(self):
        if self.data_type_cb.currentText() == "assets":
            self.asset_type_label.show()
            self.asset_type_cb.show()
            self.asset_label.show()
            self.asset_cb.show()
            self.sequence_label.hide()
            self.sequence_cb.hide()
            self.shot_label.hide()
            self.shot_cb.hide()
            self._updateAssetType()
        elif self.data_type_cb.currentText() == "shots":
            self.sequence_label.show()
            self.sequence_cb.show()
            self.shot_label.show()
            self.shot_cb.show()
            self.asset_type_label.hide()
            self.asset_type_cb.hide()
            self.asset_label.hide()
            self.asset_cb.hide()
            self._updateSequence()

    def _updateProject(self):
        self.project_cb.clear()
        self.project_cb.addItems(project_utils.listProjects())

        # get the environments
        if "PROJECT" in os.environ:
            project = os.environ["PROJECT"]
        else:
            project = None
        
        if project:
            index = self.project_cb.findText(project)
            self.project_cb.setCurrentIndex(index)

    def _updateDataType(self):
        self.data_type_cb.clear()
        self.data_type_cb.addItems(["assets", "shots"])

    def _updateAssetType(self):
        self.asset_type_cb.clear()
        self.asset_type_cb.addItems(project_utils.listAssetTypes(self.project_cb.currentText()))

    def _updateAsset(self):
        self.asset_cb.clear()
        self.asset_cb.addItems(project_utils.listAssets(self.project_cb.currentText(), self.asset_type_cb.currentText()))
    
    def _updateSequence(self):
        self.sequence_cb.clear()
        self.sequence_cb.addItems(project_utils.listSequences(self.project_cb.currentText()))
    
    def _updateShot(self):
        self.shot_cb.clear()
        self.shot_cb.addItems(project_utils.listShots(self.project_cb.currentText(), self.sequence_cb.currentText()))

    def _updateStage(self):
        self.stage_cb.clear()
        self.stage_cb.addItems(["work", "publish"])
        self._updateFileTree()

    def _updateFileTree(self):
        # clear the tree
        self.file_tree.clear()

        # get the parameters
        project = self.project_cb.currentText()
        data_type = self.data_type_cb.currentText()
        asset_type = self.asset_type_cb.currentText()
        asset = self.asset_cb.currentText()
        stage = self.stage_cb.currentText()

        if data_type == "assets":
            for dept in project_utils.listAssetDepartments(project, asset_type, asset, stage):
                dept_tree_item = QtWidgets.QTreeWidgetItem()
                dept_tree_item.setText(0, dept)
                self.file_tree.addTopLevelItem(dept_tree_item)

                for scene in project_utils.listAssetMayaScenes(project, asset_type, asset, stage, dept):
                    scene_tree_item = QtWidgets.QTreeWidgetItem()
                    scene_tree_item.setText(0, scene)
                    filepath = "{}/{}/assets/{}/{}/{}/{}/maya/scenes/{}".format(project_utils.getProjectLibrary(), project, asset_type, asset, stage, dept, scene)
                    scene_tree_item.setData(32, 0, filepath)
                    dept_tree_item.addChild(scene_tree_item)

    def _updateAll(self):
        self._updateProject()
        self._updateDataType()
        self._updateDataTypeWidgets()
        self._updateAssetType()
        self._updateAsset()
        self._updateStage()

    def _populatePackages(self):
        for repo in code_utils.listRepos():
            action = self.pkg_menu.addAction("Set all to {}".format(repo))
            action.triggered.connect(partial(self.setAllPackages, repo))
        self.pkg_menu.addSeparator()
        
        # add all packages within the master repo
        for pkg in code_utils.listPackages("master"):
            pkg = self.pkg_menu.addMenu(pkg)
            action_group = QtWidgets.QActionGroup(self.pkg_menu)
            for repo in code_utils.listRepos():
                action = QtWidgets.QAction(repo)
                action.setCheckable(True)
                pkg.addAction(action)
                action_group.addAction(action)
                if repo == "master":
                    action.setChecked(True)

    def getPackages(self):
        return [pkg.title() for pkg in self.pkg_menu.findChildren(QtWidgets.QMenu)]
    
    def getPackageRepos(self):
        return [action_group.checkedAction().text() for action_group in self.pkg_menu.findChildren(QtWidgets.QActionGroup)]

    def setPackageEnvironments(self):
        packages = self.getPackages()
        repos = self.getPackageRepos()

        os.environ["PACKAGES"] = ";".join(packages)

        code_lib = code_utils.getCodeLibrary()
        package_paths = ""
        for x, repo in enumerate(repos):
            package_paths += "{}/{}/{};".format(code_lib, repo, packages[x])

        os.environ["PACKAGE_PATHS"] = package_paths

    def setProjectEnvironments(self):
        os.environ["PROJECT"] = self.project_cb.currentText()
        if self.data_type_cb.currentText() == "assets":
            os.environ["ASSET"] = self.asset_cb.currentText()
            os.environ["ASSET_TYPE"] = self.asset_type_cb.currentText()
        elif self.data_type_cb.currentText() == "shots":
            os.environ["SEQUENCE"] = self.sequence_cb.currentText()
            os.environ["SHOT"] = self.shot_cb.currentText()

        current = self.file_tree.currentItem()
        if current:
            if current.parent():
                os.environ["DEPARTMENT"] = current.parent().text(0)
            else:
                os.environ["DEPARTMENT"] = current.text(0)
        else:
            os.environ["DEPARTMENT"] = "default"

    def setAllPackages(self, repo):
        for action_group in self.pkg_menu.findChildren(QtWidgets.QActionGroup):
            for action in action_group.actions():
                if action.text() == repo:
                    action.setChecked(True)

    def launchMaya(self):
        self.setPackageEnvironments()
        self.setProjectEnvironments()
        if self.file_tree.currentItem().text(0).endswith(".ma"):
            print("Launching Maya...")
            os.startfile(self.file_tree.currentItem().data(32, 0))
        else:
            os.startfile("C:/Program Files/Autodesk/Maya2020/bin/maya.exe")


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

window = MayaLauncherWindow()
window.show()

app.exec_()
