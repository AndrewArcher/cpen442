__author__ = 'andrew'

import hashlib

sha1 = lambda msg : hashlib.sha1(msg).hexdigest().upper()

def pw_gen(pw_len, alphabet, start=None):
    alpha_len = len(alphabet)
    pw_idxs = [0] * pw_len
    if start is not None and \
                    len(start) == pw_len and \
            all([char in alphabet for char in start]):
        pw_idxs = [alphabet.find(char) for char in start]
    inc_idx = -1
    yield bytes([alphabet[ii] for ii in pw_idxs])
    print('starting at: ' + str(bytes([alphabet[ii] for ii in pw_idxs])))
    while True:
        roll_over = bool((pw_idxs[inc_idx] + 1) // alpha_len)
        pw_idxs[inc_idx] = (pw_idxs[inc_idx] + 1) % alpha_len
        if roll_over:
            inc_idx -= 1
            if inc_idx + alpha_len < 0:
                raise StopIteration()
        else:
            inc_idx = -1
            yield bytes([alphabet[ii] for ii in pw_idxs])

