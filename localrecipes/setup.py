from distutils.core import setup

setup(
    name="localrecipes",
    version='1.0',
    description='Local Recipes',
    author='Zach Goldberg',
    author_email='zach@wifast.com',
    url='wifast.com',
    entry_points={
        'zc.buildout': [
            'mongodb = mongodb:Recipe',
            ]
        },
    )
