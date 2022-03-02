def strStr_naive(haystack: str, needle: str) -> int:
    """
    Naive algorithm; compare every windows
    """
    if needle is None or len(needle) == 0:
        return 0
    if haystack is None or len(haystack) < len(needle):
        return -1


    need_len = len(needle)

    i = 0
    while i < len(haystack):
        if i + need_len > len(haystack):
            return -1
        sub = haystack[i:i + need_len]
        if sub == needle:
            return i
        i += 1

#############

def pre(pattern):
    """
    Find the longest prefix that's also suffix /
    Find repeating pattern
    return: helper array
    """
    i, j = 0, 1 # j to loop through pattern, i to construct
    lps = [None] * len(pattern)
    lps[0] = 0 # first slot is always 0 since no pattern here
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            lps[j] = 0
            if i != 0:
                i = lps[i-1] #matcching with lps[0:i-1]
            else:
                # if back to the beginning, meaning there's no prefix = sufix
                j += 1
    return lps

def strStr_kmp(haystack: str, needle: str):
    if needle is None or len(needle) == 0:
        return 0
    if haystack is None or len(haystack) < len(needle):
        return -1

    # helper array to keep track of matching prefix in pattern
    # note that lps is of the same length of needle
    lps = pre(needle)

    # i for pattern (needle), j for string (haystack)
    i, j = 0, 0
    while j < len(haystack):
        if needle[i] == haystack[j]:
            i += 1
            j += 1
        else:
            if i != 0:
                i = lps[i-1]
            else:
                j +=1
        # if at any point loop through the needle, means pattern is found
        if i >= len(needle):
            return j - len(needle)
    return -1

def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0] # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps

if __name__ == '__main__':
    a = []
    a.append(strStr_kmp("aabaaabaaac", "aabaaac"))
    a.append(strStr_kmp("hello", "lo"))
    a.append(strStr_kmp("hello", "ll"))
    a.append(strStr_kmp("hello", "helli"))
    a.append(strStr_kmp("hello", "hello"))
    a.append(strStr_kmp("hello", ""))
    a.append(strStr_kmp("", "asdf"))
    a.append(strStr_kmp("hello", "elli"))
    a.append(strStr_kmp("hello", "ell"))
    a.append(strStr_kmp("aaaaa", "bba"))
    a.append(strStr_kmp("", ""))
    print(a)

    # print(computeLPSArray("aabaaac", 7, [0]*7))
    # print(pre("aabaaac"))


    # print(pre("lo"))
    # print(pre("AAACAAA"))
    # print(pre("ACAC"))
    # print(pre("ABCDABEABF"))
    # print(pre("ABCDEABFABC"))
    # print(pre("AABCADAABE"))
    # print(pre("AAAABAACD"))
    # print(pre("abcdefg"))
