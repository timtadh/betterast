try:
    from setuptools import setup
    # arguments that distutils doesn't understand
    setuptools_kwargs = {
        'install_requires': [
        ],
        'provides': ['betterast'],
        'zip_safe': False
    }
except ImportError:
    from distutils.core import setup
    setuptools_kwargs = {}

setup(name='betterast',
      version=0.4,
      description=(
        'A generic ast.'
      ),
      author='Tim Henderson',
      author_email='tadh@case.edu',
      url='https://github.com/timtadh/betterast',
      packages=['betterast'],
      platforms=['unix'],
      scripts=['bin/treedot'],
      **setuptools_kwargs
)

