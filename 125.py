def isPalindrome(s):
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()
    for i in range(len(new_s) // 2):
        if new_s[i] != new_s[-i - 1]:
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))