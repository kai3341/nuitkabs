#!/usr/bin/env python

import setuptools


packages = setuptools.find_packages(
    where='.',
)

entry_points = {
    'console_scripts': (
        'nbuild=nbuild:NBuilder.execute'
    ),
}

# Warning: 'classifiers' should be a list, got type 'tuple'
classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: GNU GPL v3',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
]

keywords = 'nuitka build'

install_requires = (
    'nuitka',
)

setuptools.setup(
    name='nbuild',
    version='0.0.1',
    description='Nuitka build system',
    url='https://github.com/kai3341/nbuild',
    author='kai3341',
    author_email='noreplay@example.com',
    license='GNU GPL v3',
    packages=packages,
    entry_points=entry_points,
    classifiers=classifiers,
    keywords=keywords,
    install_requires=install_requires,
)
