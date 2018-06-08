def cat_haplotypes(data, window_size):
	windows = data.shape[1] // window_size
	haplo_list = []
	for window_idx in xrange(windows):
		window = window_idx * window_size
		haplo_list.append(process_window(data[:,window:window + window_size]))
	if (data.shape[1] % window_size) != 0:
		window = windows * window_size
		haplo_list.append(process_window(data[:,window:]))
	haplo_output = np.concatenate(haplo_list, axis = 1)
	return haplo_output