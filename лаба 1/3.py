def lengthOfLongestSubstring(s):
    left = 0
    max_len = 0
    chars = set()
    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len

    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))