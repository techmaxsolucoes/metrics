from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in metrics/__init__.py
from metrics import __version__ as version

setup(
	name="metrics",
	version=version,
	description="Metrics Monitoring Platform",
	author="TechMax Solucoes",
	author_email="info@techmaxsolucoes.com.br",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
