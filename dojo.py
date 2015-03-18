#!/usr/bin/env python

import unittest
from jokenpo import jokenpo, test_cases

class TestSequenceFunctions(unittest.TestCase):
	def test_1(self):
		for k,v in test_cases:
			self.assertEqual(jokenpo(k[0], k[1]), v)		

 
if __name__ == '__main__':
	unittest.main() 
