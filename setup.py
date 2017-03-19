
from setuptools import setup, find_packages

from accounts import __version__


setup(
    name='django-mp-accounts',
    version=__version__,
    description='',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-accounts',
    download_url='https://github.com/pmaigutyak/mp-accounts/archive/%s.tar.gz' % __version__,
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'django-allauth',
        'django-widget-tweaks'
    ]
)
