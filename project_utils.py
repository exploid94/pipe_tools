import os

def getProjectLibrary():
    """
    Returns the project library folder.

    :return: The project library folder
    :rtype: str
    """
    return "D:/pipeline/projects"

def listProjects():
    """
    Returns a list of the project folders, as strings.

    :return: List of projects
    :rtype: list
    """
    return os.listdir(getProjectLibrary())

def listAssetTypes(project):
    """
    Returns a list of the asset types, as strings.

    :param project: The name of the project
    :type project: str
    :return: List of asset types
    :rtype: list
    """
    directory = "{}/{}/assets".format(getProjectLibrary(), project)
    if os.path.isdir(directory):
        return [d for d in os.listdir(directory) if os.path.isdir("{}/{}".format(directory, d))]
    else:
        return []

def listAssets(project, asset_type):
    """
    Returns a list of the assets, as strings.

    :param project: The name of the project
    :type project: str
    :param asset_type: The asset type
    :type asset_type: str
    :return: List of assets
    :rtype: list
    """
    directory = "{}/{}/assets/{}".format(getProjectLibrary(), project, asset_type)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []

def listAssetDepartments(project, asset_type, asset, stage="work"):
    """
    Returns a list of the asset department folders, as strings.

    :param project: The name of the project
    :type project: str
    :param asset_type: The asset type
    :type asset_type: str
    :param asset: The name of the asset
    :type asset: str
    :param stage: The stage folder to look through. Accepts `work` or `publish`
    :type stage: str
    :return: List of asset departments
    :rtype: list
    """
    directory = "{}/{}/assets/{}/{}/{}/".format(getProjectLibrary(), project, asset_type, asset, stage)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []

def listAssetMayaScenes(project, asset_type, asset, stage="work", department="default"):
    """
    Returns a list of maya scenes under the given asset, as strings.

    :param project: The name of the project
    :type project: str
    :param asset_type: The asset type
    :type asset_type: str
    :param asset: The name of the asset
    :type asset: str
    :param stage: The stage folder to look through. Accepts `work` or `publish`
    :type stage: str
    :param department: The department name
    :type department: str
    :return: List of maya scenes
    :rtype: list
    """
    directory = "{}/{}/assets/{}/{}/{}/{}/maya/scenes".format(getProjectLibrary(), project, asset_type, asset, stage, department)
    if os.path.isdir(directory):
        return [f for f in os.listdir(directory) if f.endswith(".ma")]
    else:
        return []

def listAssetBlenderScenes(project, asset_type, asset, stage="work", department="default"):
    """
    Returns a list of blender scenes under the given asset, as strings.

    :param project: The name of the project
    :type project: str
    :param asset_type: The asset type
    :type asset_type: str
    :param asset: The name of the asset
    :type asset: str
    :param stage: The stage folder to look through. Accepts `work` or `publish`
    :type stage: str
    :param department: The department name
    :type department: str
    :return: List of blender scenes
    :rtype: list
    """
    directory = "{}/{}/assets/{}/{}/{}/{}/blender/scenes".format(getProjectLibrary(), project, asset_type, asset, stage, department)
    if os.path.isdir(directory):
        return [f for f in os.listdir(directory) if f.endswith(".blend")]
    else:
        return []

def listSequences(project):
    """
    Returns a list of the sequences, as strings.

    :param project: The name of the project
    :type project: str
    :return: List of sequences
    :rtype: list
    """
    directory = "{}/{}/shots".format(getProjectLibrary(), project)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []

def listShots(project, sequence):
    """
    Returns a list of the shots, as strings.

    :param project: The name of the project
    :type project: str
    :param sequence: The name of the sequence
    :type sequence: str
    :return: List of shots
    :rtype: list
    """
    directory = "{}/{}/shots/{}".format(getProjectLibrary(), project, sequence)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []

def listShotDepartments(project, sequence, shot, stage="work"):
    """
    Returns a list of the shot department folders, as strings.

    :param project: The name of the project
    :type project: str
    :param sequence: The name of the sequence
    :type sequence: str
    :param shot: The name of the shot
    :type shot: str
    :param stage: The stage folder to look through. Accepts `work` or `publish`
    :type stage: str
    :return: List of asset departments
    :rtype: list
    """
    directory = "{}/{}/shots/{}/{}/{}/".format(getProjectLibrary(), project, sequence, shot, stage)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []

def listShotMayaScenes(project, sequence, shot, stage="work", department="default"):
    """
    Returns a list of maya scenes under the given shot, as strings.

    :param project: The name of the project
    :type project: str
    :param sequence: The name of the sequence
    :type sequence: str
    :param shot: The name of the shot
    :type shot: str
    :param stage: The stage folder to look through. Accepts `work` or `publish`
    :type stage: str
    :param department: The department name
    :type department: str
    :return: List of maya scenes
    :rtype: list
    """
    directory = "{}/{}/shots/{}/{}/{}/{}/maya/scenes".format(getProjectLibrary(), project, sequence, shot, stage, department)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []

def listShotBlenderScenes(project, sequence, shot, stage="work", department="default"):
    """
    Returns a list of blender scenes under the given shot, as strings.

    :param project: The name of the project
    :type project: str
    :param sequence: The name of the sequence
    :type sequence: str
    :param shot: The name of the shot
    :type shot: str
    :param stage: The stage folder to look through. Accepts `work` or `publish`
    :type stage: str
    :param department: The department name
    :type department: str
    :return: List blender scenes
    :rtype: list
    """
    directory = "{}/{}/shots/{}/{}/{}/{}/blender/scenes".format(getProjectLibrary(), project, sequence, shot, stage, department)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []
