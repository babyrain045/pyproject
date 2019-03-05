num = int(input())
#埃氏筛选法：
#1.去掉1（1既不是质数也不是合数
#2.去掉2的倍数
#3.去掉3的倍数
#4.去掉5的倍数
#迭代以上步骤直至全部完成
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def dismissNum(ele):
    return lambda x:x%ele>0

def prime():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(dismissNum(n),it)
primes = []
for i in prime():
    if i <= num and num%i==0:
        num_it = num
        while num_it%i == 0:
            num_it = num_it/i
            print(i, end=' ')
    elif i > num:
        break
    else:
        continue



