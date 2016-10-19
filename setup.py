# coding: utf8
import codecs
import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='rc4-python3',
    version=find_version('rc4', '__init__.py'),
    author='Ryan Kung',
    url='https://github.com/RyanKung/rc4-python3',
    py_modules=find_packages(exclude=['tests', 'docs']),
    packages=find_packages(exclude=['tests', 'docs']),
    package_dir={'': '.'},
    author_email='ryankung@ieee.org',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points={
        'console_scripts': [
            'pyrc4=rc4.rc4:main'
        ]
    }
)
