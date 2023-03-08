#!/usr/bin/env python3
from totesttest import tolower
import unittest

class TestTotesttest(unittest.TestCase):
   def test_basic(self):
      testcase="AbHIRamI"
      expected="abhirami"
      self.assertEqual(tolower(testcase),expected)
   def test_empty(self):
      testcase=""
      expected=""
      self.assertEqual(tolower(testcase),expected)
   def test_digit(self):
      testcase="abhi123"
      expected="ERROR : digits found"
      self.assertEqual(tolower(testcase),expected)
unittest.main()
