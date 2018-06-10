import unittest
from jaccard_index.jaccard import jaccard_index

class TestJaccardIndex(unittest.TestCase):
	"""Tests for Jaccard_Index."""

	def test_empty_string(self):
		"""Test for empty string"""

		self.assertEqual(jaccard_index("abc",""), 0)
		self.assertEqual(jaccard_index("","abc"), 0)
        
	def test_bigram_string(self):
		"""Test for Jaccard Index based on bigram """
		self.assertEqual(jaccard_index("abc","abc"), 1)
		self.assertEqual(jaccard_index("abc","abd"), 1/3)
	
	def test_large_gram_string(self):
		"""Test for lage values of n """
		self.assertEqual(jaccard_index("abc","abc", 3), 1)
		self.assertEqual(jaccard_index("abc","abd", 3), 0)
		with self.assertRaises(Exception):
			jaccard_index("abc","abd", 4)
		with self.assertRaises(Exception):
			jaccard_index("abc","abd", 10)

if __name__ == '__main__':
    unittest.main()