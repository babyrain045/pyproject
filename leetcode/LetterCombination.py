
    
my_dict = {}
my_dict = {
    2:['a','b','c'],
    3:['d','e','f'],
    4:['g','h','i'],
    5:['j','k','l'],
    6:['m','n','o'],
    7:['p','q','r','s'],
    8:['t','u','v'],
    9:['w','x','y','z'],
}

dig = list(input())
print(dig)
result = ['']

def letter_combination(current_rst , digit, my_dict):

    rest = []


    for m in current_rst:
        for n in my_dict[digit]:
            rest.append(m + n)
    return rest


for i in dig:
    result = letter_combination(result, int(i), my_dict)
print(result)


