# -*- coding: utf-8 -*-
#filename：using_file.py

poem = '''\
Programming is fun
When the  work is done
if you wanna make your work also fun:
            use Python!
'''

f = open(r'E:\poem.txt','w')
f.write(poem)
f.close()

f = open(r"E:\poem.txt")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()