# copied from https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip
import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
