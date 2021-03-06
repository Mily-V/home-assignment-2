#!/usr/bin/env python2

import sys
import unittest
from tests.test_authorize import TestAuth
from tests.test_creat_topic import TestCreateTopic


if __name__ == '__main__':
    suite = unittest.TestSuite((
       unittest.makeSuite(TestAuth),
       unittest.makeSuite(TestCreateTopic),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
