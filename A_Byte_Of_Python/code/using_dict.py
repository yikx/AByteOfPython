# -*- coding: utf-8 -*-
#filename:using_dict.py

#'ab' is short for ' a address book'

ab = {
      'zhangsan':'zhangsan@qq.com',
      'lisi':'lisi@mail.org',
      'wangwu':'wangwu@ruby-lang.org',
      'zhaoliu':'zhaoliu@163.com'
      }
print("zhangsan's address is " + ab['zhangsan'])

#addding a key/value pair
ab['Guido'] = 'guido@python.org'

#deleting a key/value pair
del ab['zhaoliu']

print("\nThere are {} contacts in the address-book.\n".format(len(ab)))
for name,address in ab.items():
    print("Contact {} at {}".format(name,address))
    
if "Guido" in ab:
    print("\nGuido's address is ", ab['Guido'])