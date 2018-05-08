#_*_coding:utf-8_*_
#filename: cat.py
import sys
def readfile(filename):     
    '''Print a file to the standard output.'''
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,) # # notice comma
    f.close()

# Script starts from here
if len(sys.argv) < 2:
    print("No action specified.")
    sys.exit()
if sys.argv[1].startswith('--'): #判断命令行的第二个参数是否以--开头
    option = sys.argv[1][2:] # 如果是以--开头，则option赋值为第二个参数第3个字符开始的字符串
    # fetch sys.argv[1] but without the first two characters.
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version : Prints the version number
    --help : Display this help''')
    else:
        print("Unknown option")
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
              
