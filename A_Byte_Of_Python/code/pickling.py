
#filename:pickling.py

import pickle as p
#import cPickle as p

shoplistfile = 'shoplist.data'
#the name of the file where we will store the object.

shoplist = ['apple','mango','carrot']

#write to the file

f = open(shoplistfile,'wb')
p.dump(shoplist, f)
f.close()

f = open(shoplistfile,'rb')
storedlist = p.load(f)
print(storedlist)
