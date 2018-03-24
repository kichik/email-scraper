import unittest

from email_scraper.scrape import extract_emails, deobfuscate_html, scrape_emails


class TestExtractor(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(extract_emails('hello world'), [])
        self.assertEqual(extract_emails('hello test@test.com world'), ['test@test.com'])
        self.assertEqual(extract_emails('test@test.com test@test.com'), ['test@test.com', 'test@test.com'])
        self.assertEqual(extract_emails('test@test.com test@example.com'), ['test@test.com', 'test@example.com'])
        self.assertEqual(extract_emails('test@test.com,test@example.com'), ['test@test.com', 'test@example.com'])
        self.assertEqual(extract_emails('hello test@test.com. i have been waiting for you.'), ['test@test.com'])

    def test_basic_html(self):
        self.assertEqual(extract_emails('<a href="mailto:test@test.com">boo</a>'), ['test@test.com'])
        self.assertEqual(extract_emails('<a href=\'mailto:test@test.com\'>boo</a>'), ['test@test.com'])
        self.assertEqual(extract_emails('<a href="mailto:test@test.com?subject=meh">boo</a>'), ['test@test.com'])

    def test_tlds(self):
        self.assertEqual(extract_emails('hello@something.com'), ['hello@something.com'])
        self.assertEqual(extract_emails('hello@something.pizza'), ['hello@something.pizza'])
        self.assertEqual(extract_emails('hello@something.notarealtld'), [])


class TestDeobfuscate(unittest.TestCase):
    def test_entities(self):
        self.assertEqual(deobfuscate_html('&#121;&#111;&#117;&#114;&#110;&#097;&#109;&#101;&#064;&#100;&#111;&#109;'
                                          '&#097;&#105;&#110;&#046;&#099;&#111;&#109;'), 'yourname@domain.com')

    def test_atob(self):
        atob = 'atob(\'bWFpbHRvOmVtYWlsQGV4YW1wbGUuY29t\')'
        self.assertEqual(deobfuscate_html(atob), 'mailto:email@example.com')


class TestScraping(unittest.TestCase):
    def test_basic(self):
        html = """<html>
        <body>
        <a href="mailto:hello@test.com">something@test.com</a>
        </body>
        </html>"""
        self.assertEqual(scrape_emails(html), {'hello@test.com', 'something@test.com'})

    def test_atob(self):
        atob = '<a href="javascript:window.location.href=atob(\'bWFpbHRvOmVtYWlsQGV4YW1wbGUuY29t\')">E-Mail</a>'
        self.assertEqual(scrape_emails(atob), {'email@example.com'})

    def test_entities(self):
        html = """<p>For more information, send email to <A HREF="mailto:
                  &#121;&#111;&#117;&#114;&#110;&#097;&#109;&#101;&#064;&#100;&#111;&#109;&#097;&#105;&#110;&#046;&#099;&#111;&#109;">
                  &#121;&#111;&#117;&#114;&#110;&#097;&#109;&#101;&#064;&#100;&#111;&#109;&#097;&#105;&#110;&#046;&#099;&#111;&#109;
                  </A></p>"""
        self.assertEqual(scrape_emails(html), {'yourname@domain.com'})
