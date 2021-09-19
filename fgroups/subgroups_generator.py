from group_structure import is_permutation_group
import itertools
import numpy as np

def generate_subgroup(elements_array, n):
	"""Function that creates the minimum subgroup contaning all given elements.

	Inputs
	------
	- elements_array: numpy array of a list containing the elements of the given set.

	Outputs
	-------
	- elements_array: numpy array of the minimal permutation subgroup containing the given set.

	Tests
	-----
	>>> generate_subgroup(np.array([]), 0)
	array([], shape=(1, 0), dtype=int64)
	>>> generate_subgroup(np.array([[1, 2, 0], [2, 0, 1]]), 3)
	array([[0, 1, 2],
	       [1, 2, 0],
	       [2, 0, 1]])
	>>> generate_subgroup(np.array([[1, 3, 0, 2]]), 4)
	array([[0, 1, 2, 3],
	       [1, 3, 0, 2],
	       [2, 0, 3, 1],
	       [3, 2, 1, 0]])
	>>> generate_subgroup(np.array([[1, 3, 4, 0, 2]]), 5)
	array([[0, 1, 2, 3, 4],
	       [0, 1, 4, 3, 2],
	       [1, 3, 2, 0, 4],
	       [1, 3, 4, 0, 2],
	       [3, 0, 2, 1, 4],
	       [3, 0, 4, 1, 2]])
	"""
	elements_list = []
	pre_array = elements_array.copy()
	# Add Identity
	elements_list.append(np.arange(n))
	# Add Inverses
	for a in elements_array:
		elements_list.append(a)
		elements_list.append(np.argsort(a))
	while True:
		# Add Closure
		for a, b in itertools.product(elements_array, elements_array):
			c = a[b]
			elements_list.append(c)
		elements_array = np.unique(elements_list, axis=0)
		# Check Equality
		if all(any((a == b).all() for a in pre_array) for b in elements_array):
			break
		else:
			pre_array = elements_array.copy()
	return(elements_array)

if __name__ == "__main__":
	n = int(input("Enter n:"))
	cardinality = int(input("Enter Set cardinality:"))
	iterable_list = []
	for i in range(cardinality):
		element_string = input("Enter a list of elements separated by spaces:")
		element_split = element_string.split()
		element = list(map(int, element_split))
		iterable_list.append(element)
	elements_array = np.array(iterable_list)
	subgroup = generate_subgroup(elements_array)
	print(subgroup, type(subgroup))
	print(is_permutation_group(subgroup))