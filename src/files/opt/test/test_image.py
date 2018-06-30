import unittest

import django


class ImageTestCase(unittest.TestCase):
    def test_django_installed(self):
        django_version = django.get_version()
        self.assertEqual(django_version, "2.0.6")
