def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    min_len = min(len(s) for s in strs)
    for i in range(min_len):
        if len({ s[i] for s in strs }) > 1:
            return strs[0][:i]
    return strs[0][:min_len]


print(longestCommonPrefix(["flower","flo","floghtioi"]))