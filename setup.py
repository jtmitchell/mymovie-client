#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


requirements = [
    'requests==2.7.0',
]

test_requirements = [
    'mock==1.0.1',
]

setup(
    name='mymovie',
    version='0.1.0',
    description="Python commandline client for the MyMovie service",
    long_description=readme + '\n\n' + history,
    author="James Mitchell",
    author_email='james.mitchell@maungawhau.net.nz',
    url='https://github.com/jtmitchell/mymovie-client',
    packages=[
        'mymovie',
    ],
    entry_points={
        'console_scripts': [
            'mymovie = mymovie.__main__:main'
        ]
    },
    package_dir={'mymovie':
                 'mymovie'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='mymovie',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
