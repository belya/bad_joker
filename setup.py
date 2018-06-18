from setuptools import setup

setup(name='bad_joker',
      version='0.1',
      description='Jokes really bad about your code',
      url='https://github.com/belya/bad_joker',
      license='MIT',
      packages=['bad_joker', 'tests'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,
      scripts=['bin/bad_joker'])