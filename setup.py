from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_health_ec/__init__.py
from frappe_health_ec import __version__ as version

setup(
	name="frappe_health_ec",
	version=version,
	description="Frappe Health System Ec",
	author="Lugo S.A.S",
	author_email="lpillaga@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
