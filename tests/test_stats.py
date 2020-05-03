#!/usr/bin/env python

import os
import tempfile
import unittest
import util


class TestMisc(unittest.TestCase):
    def runTest(self):
        # getNumCardsReviewedToday
        result = util.invoke('getNumCardsReviewedToday')
        self.assertIsInstance(result, int)


if __name__ == '__main__':
    unittest.main()
