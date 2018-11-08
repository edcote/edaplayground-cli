from setuptools import setup

setup(
    name='edaplayground',
    version='1.0',
    description='Command line interface to edaplayground.com',
    author='Edmond Cote',
    author_email='edmond.cote@gmail.com',
    packages=['edaplayground'],
    install_requires=['selenium', 'urllib3'],
)
