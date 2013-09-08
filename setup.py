from setuptools import setup, find_packages

dependencies = ['python3-ldap',]

setup(
    name = 'nusstalker',
    packages = ['nusstalker'],
    version = '0.7',
    description = 'Stalk people in NUS',
    author = 'Jason Yeo',
    author_email = 'jasonyeo88@gmail.com',
    url = 'https://github.com/jsyeo/nus-stalker',
    download_url = 'https://github.com/jsyeo/nus-stalker/tarball/master',
    keywords = ['ldap', 'nus'], # arbitrary keywords
    classifiers = [],
    install_requires = dependencies,
)
