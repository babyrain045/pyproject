x = input()

num_900 = x.count('CM')
num_400 = x.count('CD')
num_90 = x.count('XC')
num_40 = x.count('XL')
num_9 = x.count('IX')
num_4 = x.count('IV')
num_1000 = x.count('M') - num_900
num_500 = x.count('D') - num_400
num_100 = x.count('C') - num_900 - num_400 - num_90
num_50 = x.count('L') - num_40
num_10 = x.count('X') - num_90 - num_40 - num_9
num_5 = x.count('V') - num_4
num_1 = x.count('I') - num_9 - num_4
sum = num_900*900 + num_400*400 + num_90*90 + num_40*40 + num_9*9 +num_4*4 + num_1000*1000 + num_500*500 + num_100*100 + num_50*50 + num_10*10 + num_1*1
print(sum)

