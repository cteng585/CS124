def assign_haplotype(genotype, window, parsimonious_set):
	haplotype_bank = list(parsimonious_set)
	for haplotype1_idx in xrange(len(haplotype_bank)):
			for haplotype2_idx in xrange(haplotype1_idx, len(haplotype_bank)):
				haplotype1 = haplotype_bank[haplotype1_idx]
				haplotype2 = haplotype_bank[haplotype2_idx]
				if (lists_equal(map(operator.add, haplotype1, haplotype2), window)):
					genotype.haplotype1 += haplotype1
					genotype.haplotype2 += haplotype2
					return