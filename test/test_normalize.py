import unittest

import libthai_cffi


class NormalizeTestCase(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(libthai_cffi.normalize("คุุณปู่ซู่่ซ่่า"), "คุณปู่ซู่ซ่า")
