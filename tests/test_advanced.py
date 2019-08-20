# -*- coding: utf-8 -*-

import unittest

from sample import core


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(core.hmm())


if __name__ == '__main__':
    unittest.main()
