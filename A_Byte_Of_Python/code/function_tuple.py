# _*_ coding:utf-8 _*_
#filename: function_tuple.py

def powersum(power,*args):
    '''Return the sum of  each argument raised to a specified power.'''
    total = 0
    for i in args:
        total += pow(i,power)
    return total

print(powersum(2,3,4)) # power=2,args=(3,4)
print(powersum(2,10)) # powre=2,args=10
