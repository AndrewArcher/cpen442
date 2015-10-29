#! /usr/bin/python3

import hashlib

sha1 = lambda msg : hashlib.sha1(msg).hexdigest().upper()

q1a_hash = '15396F23938CD8E523F85D0C16A7D3BF4C922E5E'
q1a_salt = b'eH'

def q1a():
    # prints solution: 2203 15396F23938CD8E523F85D0C16A7D3BF4C922E5E
    ans = -1
    for ii in range(10000):
        ii_hash = sha1(q1a_salt + str(ii).zfill(4).encode('utf-8'))
        if ii_hash == q1a_hash:
            ans = ii
            print(ii, ii_hash)
    return ans

q1b_alpha = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
q1b_hash = 'A4C2A684DD06AA2FAAD621CB833A3E9D7E729B07'
q1b_salt = b'HX'

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

def q1b(guess=b'aaaaaa'):
    try:
        for guess in pw_gen(6, q1b_alpha, start=guess):
            guess_hash = sha1(q1b_salt + guess)
            if guess_hash == q1b_hash:
                print(guess, guess_hash)
                return guess
    except KeyboardInterrupt:
        print(guess)
        raise
    return None
        
q1b(b'adWq%=')
