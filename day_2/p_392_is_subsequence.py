def isSubsequence(s, t):
    s_pointer = 0
    t_pointer = 0

    s_len = len(s)
    t_len = len(t)

    while s_pointer < s_len and t_pointer < t_len:
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1

    return s_pointer == s_len



print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))