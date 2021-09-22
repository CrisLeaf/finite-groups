import pytest

import numpy as np
np.random.seed(5)
from numpy.testing import assert_array_almost_equal
import random
import itertools

from fgroups.groups import PermutationGroup


def test_permutation_groups():
	# Test generate_group
	# on empty set
	elements_list = [[]]
	perm_group = PermutationGroup(elements_list).generate_group()
	assert_array_almost_equal(perm_group.group_, [[]])
	# on S_2
	elements_list = [[1, 0]]
	perm_group = PermutationGroup(elements_list).generate_group()
	assert_array_almost_equal(perm_group.group_, [[0, 1], [1, 0]])
	# on S_3
	elements_list = [[2, 1, 0], [1, 0, 2]]
	perm_group = PermutationGroup(elements_list).generate_group()
	assert_array_almost_equal(perm_group.group_, [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])

	# Test generate_subgroup
	# on empty set
	elements_list = [[]]
	perm_group = PermutationGroup(elements_list).generate_subgroup()
	assert_array_almost_equal(perm_group.subgroup_, [[]])
	# on S_3
	elements_list = [[1, 2, 0], [2, 0, 1]]
	perm_group = PermutationGroup(elements_list).generate_subgroup()
	assert_array_almost_equal(perm_group.subgroup_, [[0, 1, 2], [1, 2, 0], [2, 0, 1]])
	# on S_4
	elements_list = [[1, 3, 0, 2]]
	perm_group = PermutationGroup(elements_list).generate_subgroup()
	assert_array_almost_equal(perm_group.subgroup_, [[0, 1, 2, 3], [1, 3, 0, 2], [2, 0, 3, 1], [3, 2, 1, 0]])
	# on S_5
	elements_list = [[1, 3, 4, 0, 2]]
	perm_group = PermutationGroup(elements_list).generate_subgroup()
	assert_array_almost_equal(perm_group.subgroup_, [[0, 1, 2, 3, 4], [0, 1, 4, 3, 2], [1, 3, 2, 0, 4], [1, 3, 4, 0, 2], [3, 0, 2, 1, 4], [3, 0, 4, 1, 2]])
	
	# Test is_permutation_group
	# on empty set
	elements_list = [[]]
	perm_group = PermutationGroup(elements_list)
	assert perm_group.is_permutation_group() == True
	# on S_2
	elements_list = [[0, 1], [1, 0]]
	perm_group = PermutationGroup(elements_list)
	assert perm_group.is_permutation_group() == True
	# on subsets of S_3
	elements_list = [[0, 1, 2]]
	perm_group = PermutationGroup(elements_list)
	assert perm_group.is_permutation_group() == True
	elements_list = [[1, 2, 0], [2, 0, 1]]
	perm_group = PermutationGroup(elements_list)
	assert perm_group.is_permutation_group() == False
	# on subsets of S_4
	elements_list = [[0, 1, 2, 3], [3, 2, 1, 0]]
	perm_group = PermutationGroup(elements_list)
	assert perm_group.is_permutation_group() == True
	elements_list = [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1]]
	perm_group = PermutationGroup(elements_list)
	assert perm_group.is_permutation_group() == False

	# Automated singleton test
	# Test generate_subgroup + is_permutation_group
	for iteration in range(100):
		n = 8
		random_number = random.sample(range(n), 1)
		random_perm = random.sample(range(random_number[0]+2), random_number[0]+2)
		perm_group = PermutationGroup([random_perm])
		_subgroup = perm_group.generate_subgroup().subgroup_
		perm_group_ = PermutationGroup(_subgroup)
		assert perm_group_.is_permutation_group() == True

	# Test generate_group
	for iteration in range(100):
		n = 8
		random_number = random.sample(range(n), 1)
		random_perm = random.sample(range(random_number[0]+2), random_number[0]+2)
		perm_group = PermutationGroup([random_perm])
		n_group = perm_group.generate_group().group_
		S_n = [item for item in itertools.permutations(np.arange(random_number[0]+2))]
		assert_array_almost_equal(n_group, S_n)