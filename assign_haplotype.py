def assign_haplotype(genotype, window, parsimonious_set):
	haplotype_bank = list(parsimonious_set)
	for haplotype1 in xrange(len(haplotype_bank)):
			for haplotype2 in xrange(haplotype1, len(haplotype_bank)):
				haplotype1_arr = np.array(haplotype_bank[haplotype1])
				haplotype2_arr = np.array(haplotype_bank[haplotype2])
				if (np.array_equal((haplotype1_arr + haplotype2_arr), np.array(window))):
					genotype.haplotype1 += haplotype_bank[haplotype1]
					genotype.haplotype2 += haplotype_bank[haplotype2]
					return