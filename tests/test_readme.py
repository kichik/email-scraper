import os.path
import unittest

import rstcheck


class TestReadmeClass(unittest.TestCase):
    def test_readme(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'README.rst')
        with open(path) as f:
            results = list(rstcheck.check(f.read()))
        self.assertEqual(results, [])
