# -*- coding: utf-8 -*-
"""
Jaccard Index Implementation

@author: AniruddhaMaheshDave
"""

def jaccard_index(str1, str2, n_gram = 2):
	"""
	Computes the Jaccard Index between two strings
	`str1` and `str2`.
	#TODO : Write details about Jaccard Index
	"""
	if str1 == str2:
		return 1
	
	len1, len2 = len(str1), len(str2)
	
	if (len1 == 0) or (len2 == 0):
		return 0
	
	first_set = set()
	second_set = set()
	
	for i in range(len1 - 1):
		if (' ' not in str1[i:i+n_gram] and len(str1[i:i+n_gram]) == n_gram):
			first_set.add(str1[i:i+n_gram])

	for i in range(len2 - 1):
		if (' ' not in str2[i:i+n_gram] and len(str2[i:i+n_gram]) == n_gram):
			second_set.add(str2[i:i+n_gram])
			
	if first_set and second_set:
		intersection_cardinality = len(first_set.intersection(second_set))
		union_cardinality = len(first_set.union(second_set))
		return intersection_cardinality/float(union_cardinality)
	
	else:
		raise Exception("No n-grams found. Choose a lower value of n_gram")