from distutils.core import setup

setup(
    name="localrecipes",
    version='1.0',
    description='Local Recipes',
    author='Zach Goldberg',
    author_email='zach@zachgoldberg.com',
    url='zachgoldberg.com',
    entry_points={
        'zc.buildout': [
            'mongodb = mongodb:Recipe',
            'nginx = nginx:Recipe',
            ]
        },
    )
