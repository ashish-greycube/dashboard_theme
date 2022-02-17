from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dashboard_theme/__init__.py
from dashboard_theme import __version__ as version

setup(
	name="dashboard_theme",
	version=version,
	description="Theme for dash-bu",
	author="GreyCube Technologies",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
