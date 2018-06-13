

a = ''
def palindrome(s):
    for i in range(len(s)//2):
        if s[i] == s[-(i+1)]:
            continue
        else:
            return False
    return True
b = palindrome(a)
print(b)

for i in a:
    sub_str = [a.index(i)+1:]