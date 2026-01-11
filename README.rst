####################################################
Python Module for Scraping Email Addresses from HTML
####################################################

The `email_scraper` module provides a simple method that extracts email addresses from HTML. It is able to find emails
in plain text, links, `atob()` obfuscation and HTML entities obfuscation.

The library uses a list of TLDs_ (top level domains) to find real email addresses. Make sure to frequently update the `tlds` library to get an up-to-date list of TLDs.

Available on PyPI_.

.. _PyPI: https://pypi.org/pypi/email-scraper/

.. _TLDs: https://github.com/kichik/tlds/

.. image:: https://github.com/kichik/email-scraper/workflows/Build/badge.svg
   :target: https://github.com/kichik/email-scraper/actions

.. image:: https://badge.fury.io/py/email-scraper.svg
   :target: https://badge.fury.io/py/email-scraper

Usage
-----

  >>> from email_scraper import scrape_emails
  >>> scrape_emails('<html><body><a href="mailto:hello@world.com">email me</a></body></html>')
  {'hello@world.com'}
  >>> scrape_emails('<a href="javascript:window.location.href=atob(\'bWFpbHRvOmVtYWlsQGV4YW1wbGUuY29t\')">E-Mail</a>')
  {'email@example.com'}
