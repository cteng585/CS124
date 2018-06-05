import itertools

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
		genotype.haplotype1 = haplotype1
		genotype.haplotype2 = haplotype2
		haplotype_set.add(tuple(haplotype1))
		haplotype_set.add(tuple(haplotype2))

	else:
		found_haplotypes = False

		# look for compatible haplotypes in the haplotype bank

		for haplotype1 in xrange(len(haplotype_bank)):
			for haplotype2 in xrange(haplotype1, len(haplotype_bank)):
				haplotype1_arr = np.array(haplotype_bankp[haplotype1])
				haplotype2_arr = np.array(haplotype_bank[haplotype2])
				
				if (haplotype1_arr + haplotype2_arr).all() == np.array(window).all():
					genotype.haplotype1 = haplotype_bank[haplotype1]
					genotype.haplotype2 = haplotype_bank[haplotype2]
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
				haplotype_set.add(tuple(haplotype2))
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
		genotype.haplotype1 = haplotype1
		genotype.haplotype2 = haplotype2
		haplotype_set.add(tuple(haplotype1))
		haplotype_set.add(tuple(haplotype2))






