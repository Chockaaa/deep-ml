import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""

	from numpy.linalg import norm
	# Implement your code here
	cosine = np.dot(v1, v2) / (norm(v1) * norm(v2))

	return cosine
