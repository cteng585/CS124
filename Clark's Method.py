import itertools
import random

def phase_haplotypes(filename):
	genotypes = parse_data(filename)


def improved_clarks(genotype_list, window_size, bootstrap_value):

	# assume all genotypes are the same length
	windows = len(genotype_list[0].genotype) // window_size

	for window_idx in xrange(windows):
		window = window_idx * window_size

		# make sure all sets of unique haplotypes are unique
		master_set = set()

		# create multiple haplotype banks to find the one with the fewest unique haplotypes
		for attempt in xrange(bootstrap_value):
			haplotype_set = set()

			# utilize clark's method in a random order of genotypes
			genotype_idx = range(100)
			random.shuffle(genotype_idx)

			for genotype in genotype_idx:
				clarks_method(genotype_list[genotype], genotype.genotype[window:window + window_size], haplotype_set)

			master_set.add(haplotype_set)

		most_parsimonious_set = master_set.pop()

		# choose the most parsimonious haplotype set
		for test_set in master_set:
			if (len(test_set) < len(most_parsimonious_set)):
				most_parsimonious_set = test_set
			elif (len(test_set) == len(most_parsimonious_set)):
				choose = random.choice([0,1])
				if choose == 0:
					most_parsimonious_set = test_set

		# assign compatible haplotypes to genotypes
		for genotype in genotype_list:
			assign_haplotype(genotype, genotype.genotype[window:window + window_size], most_parsimonious_set)


def assign_haplotype(genotype, window, parsimonious_set):
	haplotype_bank = list(parsimonious_set)

	for haplotype1 in xrange(len(haplotype_bank)):
			for haplotype2 in xrange(haplotype1, len(haplotype_bank)):
				haplotype1_arr = np.array(haplotype_bank[haplotype1])
				haplotype2_arr = np.array(haplotype_bank[haplotype2])
				
				if (haplotype1_arr + haplotype2_arr).all() == np.array(window).all():
					genotype.haplotype1 += haplotype_bank[haplotype1]
					genotype.haplotype2 += haplotype_bank[haplotype2]
					return

def clarks_method(genotype, window, haplotype_set):

	# if the haplotype bank is empty, construct two compatible haplotypes
	haplotype_bank = list(haplotype_set)

	if len(haplotype_bank) == 0:
		haplotype1 = []
		haplotype2 = []
		for snp in window:
			if snp == 0:
				haplotype1.append(0)
				haplotype2.append(0)
			elif snp == 1:
				haplotype1.append(0)
				haplotype2.append(1)
			elif snp == 2:
				haplotype1.append(1)
				haplotype2.append(1)
		haplotype_set.add(tuple(haplotype1))
		haplotype_set.add(tuple(haplotype2))

	else:
		found_haplotypes = False

		# look for compatible haplotypes in the haplotype bank

		for haplotype1 in xrange(len(haplotype_bank)):
			for haplotype2 in xrange(haplotype1, len(haplotype_bank)):
				haplotype1_arr = np.array(haplotype_bank[haplotype1])
				haplotype2_arr = np.array(haplotype_bank[haplotype2])
				
				if (haplotype1_arr + haplotype2_arr).all() == np.array(window).all():
					haplotype_set.add(tuple(haplotype1))
					haplotype_set.add(tuple(haplotype2)) 
					return

		# if a PAIR of compatible haplotypes in the bank cannot be found, make compatible haplotype
		# based off of one compatible haplotype (in order from the top of the bank)

		for haplotype1 in haplotype_bank:
			check_compatible = np.array(window) - np.array(haplotype1)
			if (-1 not in check_compatible):
				genotype.haplotype1 = haplotype1
				genotype.haplotype2 = check_compatible.tolist()
				haplotype_set.add(tuple(haplotype1))
				haplotype_set.add(tuple(check_compatible))
				return

		# if there are no compatible haplotypes in the bank, make a pair of compatible haplotypes

		haplotype1 = []
		haplotype2 = []
		for snp in window:
			if snp == 0:
				haplotype1.append(0)
				haplotype2.append(0)
			elif snp == 1:
				haplotype1.append(0)
				haplotype2.append(1)
			elif snp == 2:
				haplotype1.append(1)
				haplotype2.append(1)
		haplotype_set.add(tuple(haplotype1))
		haplotype_set.add(tuple(haplotype2))






