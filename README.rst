####################################################
Python Module for Scraping Email Addresses from HTML
####################################################

The `email_scraper` module provides a simple method that extracts email addresses from HTML. It is able to find emails
in plain text, links, `atob()` obfuscation and HTML entities obfuscation.

Available on PyPI_.

.. _PyPI: https://pypi.python.org/pypi/email-scraper/

.. image:: https://travis-ci.org/kichik/email-scraper.svg?branch=master
   :target: https://travis-ci.org/kichik/email-scraper

.. image:: https://badge.fury.io/py/email-scraper.svg
    :target: https://badge.fury.io/py/email-scraper

Usage
-----

  >>> from email_scraper import scrape_emails
  >>> scrape_emails('<html><body><a href="mailto:hello@world.com">email me</a></body></html>')
  {'hello@world.com'}
  >>>
