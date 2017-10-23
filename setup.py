
import os
from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

with open(os.path.join('requirements', 'dist.txt')) as requirements_file:
    # Read in requirements file and split on newlines
    requirements = requirements_file.read().split()

setup(
    name='hotsocket-api',
    version='0.0.01',
    description="API wrapper for Hotsocket Recharge service",
    long_description=readme + '\n\n' + changelog,
    author='Flickswitch Engineering',
    author_email='engineering@flickswitch.co.za',
    url='https://github.com/flickswitch/hotsocket-python-client',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)