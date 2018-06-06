def clarks_method(genotype, window, haplotype_set):
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
		for haplotype1 in xrange(len(haplotype_bank)):
			for haplotype2 in xrange(haplotype1, len(haplotype_bank)):
				haplotype1_arr = np.array(haplotype_bank[haplotype1])
				haplotype2_arr = np.array(haplotype_bank[haplotype2])
				if (np.array_equal((haplotype1_arr + haplotype2_arr), np.array(window))):
					return
		for haplotype1 in haplotype_bank:
			check_compatible = np.array(window) - np.array(haplotype1)
			if (2 not in abs(check_compatible)) and (-1 not in check_compatible):
				haplotype_set.add(tuple(abs(check_compatible)))
				return
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