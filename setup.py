from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='search_system',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    include_package_data=True,
    install_requires=[
        'Flask==1.1.1',
        'elasticsearch==7.10.1',
        'pandas==0.25.1'
    ],
)
