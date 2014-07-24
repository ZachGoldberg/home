from setuptools import setup, find_packages

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet',
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: OS Independent',
]

setup(
    name='django-mongodb-engine',
    license='2-clause BSD',
    description= "MongoDB backend for Django",
    install_requires=['pymongo', 'djangotoolbox'],
    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    include_package_data=True,
    classifiers=CLASSIFIERS,
    test_suite='tests',
)
