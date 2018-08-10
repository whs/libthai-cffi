import unittest

import libthai_cffi

TEST_STR = "สวัสดีครับ กอ.รมน. นี่เป็นการทดสอบตัวเอง"


class BreakTestCase(unittest.TestCase):
    def test_find_breaks(self):
        self.assertEqual(libthai_cffi.find_breaks(TEST_STR), [6, 11, 19, 22, 26, 29, 34])

    def test_find_breaks_text(self):
        self.assertEqual(
            self.breaker.find_breaks_text(TEST_STR),
            ["สวัสดี", "ครับ ", "กอ.รมน. ", "นี่", "เป็น", "การ", "ทดสอบ", "ตัวเอง"],
        )


class BreakerTestCase(unittest.TestCase):
    def setUp(self):
        self.breaker = libthai_cffi.Breaker()

    def test_find_breaks(self):
        self.assertEqual(self.breaker.find_breaks(TEST_STR), [6, 11, 19, 22, 26, 29, 34])

    def test_find_breaks_text(self):
        self.assertEqual(
            self.breaker.find_breaks_text(TEST_STR),
            ["สวัสดี", "ครับ ", "กอ.รมน. ", "นี่", "เป็น", "การ", "ทดสอบ", "ตัวเอง"],
        )
