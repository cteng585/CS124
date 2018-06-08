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
				if (random.choice([0,1]) == 0):
					haplotype1.append(0)
					haplotype2.append(1)
				else:
					haplotype1.append(1)
					haplotype2.append(0)
			elif snp == 2:
				haplotype1.append(1)
				haplotype2.append(1)
		haplotype_set.add(tuple(haplotype1))
		haplotype_set.add(tuple(haplotype2))
	else:
		found_haplotypes = False
		for haplotype1_idx in xrange(len(haplotype_bank)):
			for haplotype2_idx in xrange(haplotype1_idx, len(haplotype_bank)):
				haplotype1 = haplotype_bank[haplotype1_idx]
				haplotype2 = haplotype_bank[haplotype2_idx]
				if (lists_equal(map(operator.add, haplotype1, haplotype2), window)):
					return
		for haplotype1 in haplotype_bank:
			check_compatible = map(operator.sub, window, haplotype1)
			if (2 not in check_compatible) and (-1 not in check_compatible) and (-2 not in check_compatible):
				haplotype_set.add(tuple(map(operator.abs, check_compatible)))
				return
		haplotype1 = []
		haplotype2 = []
		for snp in window:
			if snp == 0:
				haplotype1.append(0)
				haplotype2.append(0)
			elif snp == 1:
				if (random.choice([0,1]) == 0):
					haplotype1.append(0)
					haplotype2.append(1)
				else:
					haplotype1.append(1)
					haplotype2.append(0)
			elif snp == 2:
				haplotype1.append(1)
				haplotype2.append(1)
		haplotype_set.add(tuple(haplotype1))
		haplotype_set.add(tuple(haplotype2))