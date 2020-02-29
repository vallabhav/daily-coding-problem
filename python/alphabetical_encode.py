#problem statement:

#Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
#Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

import math
def encode(ch):
    return ord(ch) - ord('A') + 1;


def alphabetical_encode(s):
    base = 26
    encode_val = 0 
    s  = s.upper()
    for i in range(len(s)):
        encode_val += math.pow(base, len(s) - i - 1) * encode(s[i])
    return encode_val
