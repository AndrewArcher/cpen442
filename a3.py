#! /usr/bin/python3

from tools import sha1, pw_gen

q1a_hash = '15396F23938CD8E523F85D0C16A7D3BF4C922E5E'
q1a_salt = b'eH'

def q1():
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

def q2(guess=b'aaaaaa'):
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
        
q2(b'ag&a%*')
