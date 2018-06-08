import numba as nb


@nb.jit(nopython=True)
def arrays_equal(a, b):
    if a.shape != b.shape:
        return False
    for ai, bi in zip(a.flat, b.flat):
        if ai != bi:
            return False
    return True

def lists_equal(a, b):
	if len(a) != len(b):
		return False
	for ai, bi in zip(a, b):
		if ai != bi:
			return False
	return True