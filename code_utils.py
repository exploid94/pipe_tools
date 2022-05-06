import os 

def getCodeLibrary():
    """
    Returns the code library folder.

    :return: The code library folder
    :rtype: str
    """
    return "D:/pipeline/code"

def listRepos():
    """
    Returns a list of the repo folders, as strings.

    :return: List of repos
    :rtype: list
    """
    return os.listdir(getCodeLibrary())

def listPackages(repo="local"):
    """
    Returns a list of the repo packages, as strings.

    :param repo: Which repo to get the packages of, run listRepos() to see which are available, defaults to 'local'
    :type repo: str, optional
    :return: List of packages
    :rtype: list
    """
    directory = "{}/{}".format(getCodeLibrary(), repo)
    if os.path.isdir(directory):
        return os.listdir(directory)
    else:
        return []

def getEnvironmentPackages():
    """
    Returns the packages loaded into the environment as a list.

    :return: Packages loaded into the environment
    :rtype: list
    """
    if "PACKAGES" in os.environ:
        return [pkg for pkg in os.environ["PACKAGES"].split(";")]
    else:
        return []

def getEnvironmentPackagePaths():
    """
    Returns the package paths loaded into the environment as a list.

    :return: Package paths loaded into the environment
    :rtype: list
    """
    if "PACKAGE_PATHS" in os.environ:
        return [path for path in os.environ["PACKAGE_PATHS"].split(";")]
    else:
        return []
