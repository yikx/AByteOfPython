#_*_coding:utf-8_*_
#filename:try_except.py
import sys
try:
    s = int(input('Enter something---> '))
    num = 10
    print(num/s)
except (ValueError,EOFError):
    print("\n请输入一个整数！")
    sys.exit() #exit the program
except ZeroDivisionError:
    print("除数不能为0，请修改！")
except:
    print("\nSome error/exception occurred.")
    #here,we are not exiting the program.
else:               #若没有异常发生，则会执行
    print("all OK") 
finally:            #不管是否有异常，都会执行 
    print('done')

