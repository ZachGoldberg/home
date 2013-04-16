from distutils.core import setup

setup(name='zghome',
      version='1.0',
      description='Zach Goldberg',
      author='Zach Goldberg',
      author_email='zach@zachgoldberg.com',
      url='zachgoldberg.com',
      packages=[
          'home', ],
      package_dir={
          'home': 'home/',
      },
      install_requires=[
          'django==1.3',
          'django_debug_toolbar',
          'django_debug_toolbar_mongo',
          'django-mongodb-engine',
          'djangotoolbox',
          'simplejson',
      ],
      )
