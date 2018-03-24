import os

import sys
from setuptools import setup, find_packages

version = os.getenv('TRAVIS_TAG', '0.0')

if sys.version_info < (2, 7):
    sys.exit('Sorry, Python < 2.7 is not supported')

setup(name='email-scraper',
      version=version,
      description='Simple utility to extract email addresses from HTML, including obfuscated email addresses',
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
          'Topic :: Communications :: Email',
          'Topic :: Text Processing :: Markup :: HTML'
      ],
      keywords='email scraping web obfuscate',
      author='Amir Szekely',
      author_email='kichik@gmail.com',
      url='https://github.com/kichik/email-scraper',
      license='MIT',
      packages=find_packages(exclude=['examples', 'tests']),
      install_requires=['tlds'],
      include_package_data=True,
      zip_safe=True,
      tests_require=['rstcheck'],
      test_suite='tests',
      )
