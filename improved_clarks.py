def improved_clarks(genotype_list, window_size, bootstrap_value):
	windows = len(genotype_list[0].genotype) // window_size
	for window_idx in xrange(windows):
		window = window_idx * window_size
		master_set = []
		for attempt in xrange(bootstrap_value):
			haplotype_set = set()
			genotype_idx = range(len(genotype_list))
			random.shuffle(genotype_idx)
			for genotype in genotype_idx:
				clarks_method(genotype_list[genotype], genotype_list[genotype].genotype[window:window + window_size], haplotype_set)
			master_set.append(frozenset(haplotype_set))
		most_parsimonious_set = master_set[0]
		for test_set in master_set:
			if (len(test_set) < len(most_parsimonious_set)):
				most_parsimonious_set = test_set
			elif (len(test_set) == len(most_parsimonious_set)):
				choose = random.choice([0,1])
				if choose == 0:
					most_parsimonious_set = test_set
		for genotype in genotype_list:
			assign_haplotype(genotype, genotype.genotype[window:window + window_size], most_parsimonious_set)
	if (len(genotype_list[0].genotype) % window_size) != 0:
		window = windows * window_size
		master_set = []
		for attempt in xrange(bootstrap_value):
			haplotype_set = set()
			genotype_idx = range(len(genotype_list))
			random.shuffle(genotype_idx)
			for genotype in genotype_idx:
				clarks_method(genotype_list[genotype], genotype_list[genotype].genotype[window:], haplotype_set)
			master_set.append(frozenset(haplotype_set))
		most_parsimonious_set = master_set[0]
		for test_set in master_set:
			if (len(test_set) < len(most_parsimonious_set)):
				most_parsimonious_set = test_set
			elif (len(test_set) == len(most_parsimonious_set)):
				choose = random.choice([0,1])
				if choose == 0:
					most_parsimonious_set = test_set
		for genotype in genotype_list:
			assign_haplotype(genotype, genotype.genotype[window:window + window_size], most_parsimonious_set)