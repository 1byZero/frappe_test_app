from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_test_app/__init__.py
from frappe_test_app import __version__ as version

setup(
	name="frappe_test_app",
	version=version,
	description="Frappe theme testing app for worf",
	author="Amit Kumar",
	author_email="amit@worf.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
