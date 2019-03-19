

x = int(input())
a = x%1000
b = a%100
c = b%10
m_str=''
d_str=''
e_str=''
g_str=''
if int(x/1000) != 0:
    count = int(x/1000)
    m_str = 'M'*count
if int(a/100) != 0:
    count = int(a/100)
    if count <= 3:
        d_str = 'C' * count
    elif count == 4:
        d_str = 'CD'
    elif count == 5:
        d_str = 'D'
    elif count == 9:
        d_str = 'CM'
    else:
        d_str = 'D'+'C'*(count - 5)
if int(b/10) != 0:
    count = int(b/10)
    if count <= 3:
        e_str = 'X' * count
    elif count == 4:
        e_str = 'XL'
    elif count == 5:
        e_str = 'L'
    elif count == 9:
        e_str = 'XC'
    else:
        e_str = 'L'+'X'*(count - 5)
if int(c) != 0:
    if c <= 3:
        g_str = 'I'*c
    elif c == 4:
        g_str = 'IV'
    elif c == 9:
        g_str = 'IX'
    else:
        g_str = 'V'+'I'*(c - 5)
print(m_str+d_str+e_str+g_str)



