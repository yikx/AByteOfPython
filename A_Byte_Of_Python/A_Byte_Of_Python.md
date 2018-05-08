# A Byte Of Python

标签（空格分隔）： python  笔记 入门 基础

---

## chapter1 简介
### 1 简介
python是一个简单、但是功能强大的编程语言。
创作者：Guido van Rossum，因为喜欢英国广播公司的节目“蟒蛇飞行马戏"命令这个语言。
1.1 python的特色
- 简单
- 易学
- 免费、开源
- 可移植性高
    python已经被移植到很多平台上，只需要经过简单改动能够在不同平台上工作，这些平台包括（Linux、windows、FreeBSD、Macintosh、Soloar等等平台）
- 解释性语言
- 面向对象的
- 可扩展性
- 可嵌入性
- 第三方库丰富
### 2 Python之禅
```
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
## chapter2 安装Python
**1.1 Linux和BSD用户**
Linux系统上基本都已经默认安装了Python 2版本，可以使用python -V来查看安装的版本。
```
$python -V
python 2.3.4
```
如果没有安装的话，可以使用系统自带的包管理软件进行安装，比如Fedora Linux的yum、Mandrake linux的urpmi,Debian Linux的apt-get。
还可以使用源码进行安装

**1.2 Windows用户**
 可以直接到[python官方网站](https://www.python.org/downloads/)针对自己系统的类型进行选择安装包并下载进行安装。
 在安装过程需要注意一点的是，选中add PATH...自动将python的环境变量自动添加到系统中。
 
## chapter3 第一个程序
### 1 第一个hello world程序
```
>>>print('hello world')
hell world
```
### 2 挑选要一个编辑器
windows用户建议使用python官方网站安装包自带的IDLE，不建议使用notepad，Linux/FreeBSD用户建议使用Vim/Emacs。

其他可选编辑器可参考[Python编辑器列表](https://wiki.python.org/moin/PythonEditors),选择自己喜欢的编辑器。

### 3 获得帮助
如果你需要某个python函数或语句的快速信息帮助，可以使用oyhton的内建函数help功能。
```
help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
```
可以使用q来退出帮助文件。还可以使用help()来获得help本身的信息。

## chapter4 基本变量
### 1 字面意义上的常量
如：5，1.23，9.24e-3这样的，还有"this is a string"等
### 2 数
在python中有3种类型的数据-整数(整数、长整数 python3中已经合成整数）、浮点数和复数
- 整数例子：2，3
- 长整数不过是一些比较大的整数
- 浮点数：数学上的实数，如2.34,5.3E2(530),E标记为10的幂
- 复数：5+4j 
### 3 字符串
1. 使用单引号来还表示
如：'this is a string'
2. 使用双引号来表示
如 "Tis is a string"
3. 使用三引号("""或'''）
如 
```
'''this is a multi-line string. This is the first line.
This is the second line.
This is the third line.
'''
```
4. 转义符
如果文本中包含'或"可以通过\字符来表示，如：'what\'s your name?'
> 注意：如果要想表达\本身，可以通过\\来表示反斜杠本身
> 如果文本比较长，可以在句尾加上\表示字符串在下一行继续，而不是重新开始一行。
```
"This is the first line.\
This is the second line."
Out[38]: 'This is the first line.This is the second line.'
```
5. 自然字符串
如果不想通过转义字符来处理特别的字符串，那么可以通过前缀r或R来指定
```
path = r"C:/code/"
print(path)
C:/code/
```
6. Unicode字符串
Unicode是书写国际文本的标准方法。如果想要你的母语如北印度语或者阿拉伯语写文本。那么你需要有一个支持Unicode的编辑器。
python中只需要在字符串前面加上前缀U或u即可。
```
u"This is a Unicode string
```
> 字符串是不可变的，意味着创造了一个字符串后，就不能再改变它了。即使使用replace方法实质也没有改变原有字符串的值。

### 3 变量
1 标识符的命名
- 标识符的第一个字符必须是字母或者一个下划线（"_")
- 标识符的其他部分可以有字母、下划线或数字组成
- 标识符大小写敏感
- 有效例子:_myfunc, name_23,或者a1b2_c3
- 无效例子：1abc, this is spaced out 或者my-name

### 4 缩进
 缩进在python是非常重要的，意味着在Python中同一个层次的语句块必须有相同的缩进。
> 不要混合使用制表符和空格来缩进，建议在每个缩进层次使用单个制表符或者两个或四个空格。最重要的是选择一个风格，然后一贯使用它。大多数都是使用4个空格。

## chapter5 运算符和表达式
### 1 运算符

| 运算符| 名称| 例子  |
|:--  |----- |---------:|
| +   |加法  |3+5得到8  |
| -   |减法  |5-2等到3  |
| \*\*|幂次方| 3**4=81  |
| \*  |乘法  | 3* 4=12  |
|/    | 除法 |12/3.0=4.0|
|//   |地板除| 12/4=3   |
| %   |取余数| 12%5=2   |
|\>>  |右移  | 11/>>1=5 |
|<<   |左移  |11<<1=3   |
|^    |异或  | 5^3=6    |
|~    |翻转  | ~5=6     |
|True |布尔值真| 5>3== True|
|False|布尔值假| 5>3  False|
|and  |逻辑与 | 5>3 and 5<6|
|or   | 逻辑或 | 5>3 or 4<5 |
|not  | 逻辑非| not True|

### 2 运算符优先级
以下优先级顺序从低到高
| 运算符| 描述  | 
|-------|-------|
| lambda| lambad表达式|
|or | 布尔或|
|and| 布尔与|
|not x| 布尔非|
|in,not| 成员测试|
|is，is not| 统一性测试|
|<,<=,>,>=,!=,==| 比较|
|`|`|
|^| 按位异或|
|&| 按位与|
|<<,>>| 移位|
|+,-|加法与减法|
|*，/，%|乘法、除法、与取余|
|+x，-x|正好，负号|
|~x| 按位翻转|
|**|指数|

## chapter6 控制流
### 1 if语句
if语句用来检验一个条件，如果条件为真，则运行语句块，否则我们处理另外一个语句块。
语法：
```
if condition1:  # 如果condition1为真，则执行语句块1
    语句块1
elif  condition2：#如果condition2为真，则执行语句块2
    语句块2
else:    #如果condition1和condition2均为假，则执行语句块3
    语句块3
```
**1. 使用if语句**
```
import random
number = random.randint(1,10)
print(number)
guess = int(input('Enter an integer:' ))
if guess == number:
    print("Congratulations，you guessed it.")
    print("but you  do not win any prizes!")
elif guess <= number:
    print("NO, It is a little heigher than that")
else:
    print("No,It is a little lower than that.")
print("Done")
```
output:
```
9
Enter an integer:9
Congratulations，you guessed it.
but you  do not win any prizes!
Done

10
Enter an integer:11
No,It is a little lower than that.
Done

6
Enter an integer:4
NO, It is a little heigher than that
Done
```
>注：在Python中没有switch语句，可以使用if..elif...else语句来完成
### 2. while语句
只要在一个条件为真的情况下，while语句允许你重复执行一块语句。
语法：
```
while condition11:
    语句块1
else：  # else语句块是可选的
    语句块2
```
 # -*- coding: utf-8 -*-
 #Filename: while_else.py
```
number = 23
running = True
while running:
    guess = int(input('Enter an integer:' ))
    
    if guess == number:
        print("Congratulations，you guessed it.")
        running = False
    elif guess <= number:
        print("NO, It is a little heigher than that")
    else:
        print("No,It is a little lower than that.")
else:  #当循环正常结束的时候则会执行该语句块
    print("The while loop is over")
    
print("Done")
```
OUTPUT:
```
Enter an integer:12
NO, It is a little heigher than that

Enter an integer:44
No,It is a little lower than that.

Enter an integer:23
Congratulations，you guessed it.
The while loop is over
Done
```
### 3.for循环
for...in是另外一个循环语句，在一个序列的对象上递归，逐一使用队列中的咩咯项目。
```
for x in range(1,5):
    print(x)
else:
    print("The for loop is over")
```
OUTPUT:
```
1
2
3
4
The for loop is over
```
### 4.break语句
break语句是用来终止循环语句的。
>注意：for和while循环中使用break终止循环，任何else语句块就将不执行
```
# -*- coding: utf-8 -*-
# filename:break.py
while True:
    s = input("Enter something:")
    if s == "q":
        break
    print("length of the string is:", len(s))
else:
    print("will not run")
print("done")
```
OUTPUT:
```
Enter something:python
length of the string is: 6

Enter something:q
done
```
### 5. continue语句
continue语句用来告诉Python跳过当前循环块中剩下的语句，然后继续进行下一次的循环。
```
# -*- coding: utf-8 -*-
# filename:continue.py
while True:
    s = input("Enter something:")
    if s == "q":
        break
    if (len(s) < 3):
        continue
    print("input is of sufficient length")

print("done")
```
OUOPUT:
```
Enter something:ab

Enter something:python
input is of sufficient length

Enter something:q
done
```

## chapter7 函数
### 1 函数的定义
函数通过关键字def来定义，def后面跟着一个函数的标识符，然后跟一对圆括号，圆括号内可以包括一些变量，最后以冒号结尾。接下来是函数体。
```
def function_name(argument1，argument2,...,argumentN):
    语句块
    return  #可选，没写的话默认是return None
```
实例1 没有参数的函数：
```
# -*- coding: utf-8 -*-
#filename:function1.py

def sayHello():
    print("hello world")

sayHello() # 调用函数
OUTPUT:
hello world
```
实例2:带有参数的函数
```
# -*- coding: utf-8 -*-
#filename:function2.py

def printMax(a,b):
    if a > b:
        print(a,"is maximum")
    else:
        print(b,"is maximum")
printMax(3,4) #直接调用函数
x = 4
y = 5
printMax(x,y) # 给定变量作为参数
OUTPUT:
4 is maximum
5 is maximum
```
### 2.参数类型
**1 默认参数**
对于一些函数，可能希望某些的参数用户不想为这些参数提供的话，这些参数就可以使用默认参数。 在Python中只需要在定义函数的参数后面加个赋值运算符=和默认值就好。
>注意：默认参数值应该是不可变。放在其他正常参数的后面。
```
# -*- coding: utf-8 -*-
#filename:func_default.py
def say(message,time=1):
    print(message * time)
say('hello')
say('hello', 3)
OUTPUT:
hello
hellohellohello
```
**2 关键字参数**
如果函数有很多个参数的时候，我们在调用参数的时候可以通过使用命令来为这些参数赋值——称为关键字参数。
>关键字参数的优势：
- 不必担心参数的位置，只需要知道参数名称即可
- 其他参数有默认值，我们可以给我们想要的哪些参数赋值就好
```
# -*- coding: utf-8 -*-
#filename:func_key.py

def func(a,b=2,c=3):
    print("a is ", a , " and b is ", b, "c is ", c)
func(1)         # ab使用的是默认值2，3
func(3,7)       # c使用的是默认值3
func(c=30,a=10) # b使用的是默认值2
OUTPUT:
a is  1  and b is  2 c is  3
a is  3  and b is  7 c is  3
a is  10  and b is  2 c is  30
```
### 3. 变量的作用域
**1.局部变量**
在函数定义内部声明的变量的时候，它们与外部具有相同名称的变量没有任何关系，定义在函数内的变量为局部变量，作用于只在函数内部，函数执行完毕后变量即消除。
例子：
```
# -*- coding: utf-8 -*-
# filename:func_local.py

def func(x):
    print("x is", x )
    x = 2         #函数内部定义一个局部变量x=2
    print("Changed local x to", x) #
x = 50 # 在函数外部定义一个全局变量 x=50
func(x)
print("the glbal x is:", x) # 全局变量x并没有改变
OUTPUT:
x is 50
Changed local x to 2
the glbal x is: 50
```
**2.使用global语句**
如果想要为定义在函数外的变量赋值，那么就得告诉Python这个变量不是局部变量，而是全局变量，可以使用global语句来完成
实例：
```
# -*- coding: utf-8 -*-
# filename:func_global.py

def func():
    global x  # 将x定义为全局变量
    print("x is", x )
    x = 2         #函数内部定义一个局部变量x=2
    print("Changed local x to", x) #
x = 50 # 在函数外部顶一个全局变量 x=50
func()
print("the global x is:", x) # 全局变量x别修改为2
OUTPUT:
x is 50
Changed local x to 2
the global x is: 2
```
## 4.DocStrings函数文档
python有一个很奇妙的特性，在函数内第一个行最好写上函数文档，DocStrings是一个重要的工具，它可以帮助用户更好的理解程序，应该尽量使用它。
```
# -*- coding: utf-8 -*-
#filename:func_doc.py

def printMax(x,y):
    '''Prints the maximum of two numbers.
    the two values must be integers.'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, "is maximum")
    else:
        print(y, "is maximum")
printMax(3,5)
print(printMax.__doc__) #查看printMax函数的函数文档
OUTPUT:
5 is maximum
Prints the maximum of two numbers.
    the two values must be integers.
```
## chapter8 模块
### 1 标准模块
**1.1 sys模块**
import sys # 导入sys模块，python会在sys.path路径中寻找sys模块。
sys模块中的argv变量通过使用点号指明-sys.argv.
sys.argv变量是一个字符串的列表，包含了命令行参数的列表，即使用命令行传递给程序的参数。
>注：脚本的名称总是sys.argv列表的第一个参数。
例子：
```
# -*- coding: utf-8 -*-
#filename:sys_module.py
import sys

print("The commadnd line arguments are: ")
for i in sys.argv:# 打印sys.argv的参数列表
    print(i)
print("\n\nThe PYTHONPATH is:", sys.path,"\n")
OUTPUT:
E:\>python sys_module.py argu1 argu2 argu3
The commadnd line arguments are:
sys_module.py
argu1
argu2
argu3
The PYTHONPATH is: ['E:\\', 'd:\\ProgramData\\Anaconda3\\python36.zip', 'd:\\ProgramData\\Anaconda3\\DLLs', 'd:\\ProgramData\\Anaconda3\\lib', 'd:\\ProgramData\\Anaconda3', 'd:\\ProgramData\\Anaconda3\\lib\\site-packages', 'd:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32', 'd:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib', 'd:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin']
```
**2.from...import语句**
除了使用import moudle外，还可以使用from...import
例如：想要直接输入argv变量到程序中，不想每次都要打sys，那么可以就可以使用from sys import argv，甚至还可以使用from syts import *（导入sys模块中所有的函数或方法）
> 注：不过一般来说，应该避免使用from...import，而应该使用import语句，这样程序更加容易读懂，避免不必要的冲突。

**3.模块的\__name__**
每个模块都有自己的名称，在模块中可以通过语句来找出模块的名称。
例子：
```
# -*- coding: utf-8 -*-
#filename:using_name.py

if __name__ == "__main__":
    print("The program is being run by itself.")
else:
    print("I am being imported from another module.")
OUTPUT:
The program is being run by itself.
```
>注意:每个python模块都有自己的\__name__,若他是\__main__，说明这个模块被用户单独使用，可以进行相对应的操作。

**4.制造自己的模块**
创建一个自己的模块很简单，其实每个程序都是一个模块，只需要确保它就有.py扩展名。
例子:
```
定义一个自己的module
# -*- coding: utf-8 -*-
# filename:mymodule.py
def sayHello():
    'my first module demo'
    
    print("Hi, This is mymodule speaking.")
version = 0.1
# End of mymoudle.py
引用自己的module
# -*- coding: utf-8 -*-
#filename:using_mymodule.py
import mymodule   # 导入mymodule
mymodule.sayHello()  # 使用mymodule的函数
print("version:", mymodule.version) # 打印mymodule的变量
OUTPUT：
Hi, This is mymodule speaking.
version: 0.1
```
**5. dir()函数**
可以是使用内建的dir函数来查看模块定义的标识符（函数，类和变量等）
例子：
```
# -*- coding: utf-8 -*-
#filename:using_mymodule.py
import mymodule
mymodule.sayHello()
print("version:", mymodule.version)
print(dir(mymodule))  #使用dir函数查看mymodule模块中的标识符
OUTPUT：
Hi, This is mymodule speaking.
version: 0.1
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sayHello', 'version']
```
## chapter9 数据结构
在python中有三个内建的数据结构——列表，元组和字典。
### 1列表list
列表是处理一组有序项目的数据结构，列表使用[]括起来，每个元素用逗号隔开。列表允许对其进行添加、删除或者搜索等操作。
> 列表类型是可变的

**1 使用列表**
```
# -*- coding: utf-8 -*-
# filenamne:using_list.py

#This is my shopping list
shoplist = ['apple', 'mango','carrot', 'banana']

print("I have ", len(shoplist),'items to purchase')

for item in shoplist:
    print(item, end=',')
print("\nI also have tyo buy rise.")
shoplist.append("rise")
print("My shopping list is now:", shoplist)

print("I will sort my list now")
shoplist.sort()
print("Sorted shoppling list is:", shoplist)

print("The first item I will buy is:" , shoplist[0])

olditem = shoplist[0]
del shoplist[0]
print("I bought the", olditem)
print("My shoplist is now", shoplist)
OUTPUT:
I have  4 items to purchase
apple,mango,carrot,banana,
I also have tyo buy rise.
My shopping list is now: ['apple', 'mango', 'carrot', 'banana', 'rise']
I will sort my list now
Sorted shoppling list is: ['apple', 'banana', 'carrot', 'mango', 'rise']
The first item I will buy is: apple
I bought the apple
My shoplist is now ['banana', 'carrot', 'mango', 'rise']
```
>注：Python的索引都是从0开始，另外可以通过helo(list)来获得更多list的完整知识

### 2元组 tuple
元组和列表十分类似，只不过元组是不可变的。即一旦创建就能在修改。元祖是通过圆括号和逗号来定义（主要通过是逗号来区分）
**1 使用元组**
```
# -*- coding: utf-8 -*-
#filemane:using_tuple.py
zoo = ('wolf','elephant','penguin')
print("Number of animals in the zoo is:", len(zoo))

new_zoo = ('Monkey','Dolphin',zoo) #元祖中包含另外一个元祖
print("Numbers of the animals in  the new zoo is:", len(new_zoo))
print("All animals in new zoo are:", new_zoo)
print("Animals brought from old zoo are", new_zoo[2])
print("Last  animals brougth from old zoo is:", new_zoo[2][2]) #二维
OUTPUT:
Number of animals in the zoo is: 3
Numbers of the animals in  the new zoo is: 3
All animals in new zoo are: ('Monkey', 'Dolphin', ('wolf', 'elephant', 'penguin'))
Animals brought from old zoo are ('wolf', 'elephant', 'penguin')
Last  animals brougth from old zoo is: penguin
```
**2元组和打印语句**
元组最通常的用法是用在打印语句中。
```
# -*- coding: utf-8 -*-
# filename:print_tuple.py
age = 22
name = 'zhangsan'
print("{} is {} years old.".format(name, age))
print("Why is {} playing with that pyhton?".format(name))
OUTPUT:
zhangsan is 22 years old.
Why is zhangsan playing with that pyhton?
```
###3 字典 dict
字典类似与通过联系人名字查找地址和联系人的地址簿，即键值对，且键必须是唯一的。

- 只能使用不可变对象作为字典的键。
- 字典是无序的，
- 是dict类的实例 

`语法：d = {key1:value1,key2:value2}`
实例：
```
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
OUTPUT:
zhangsan's address is zhangsan@qq.com

There are 4 contacts in the address-book.

Contact zhangsan at zhangsan@qq.com
Contact lisi at lisi@mail.org
Contact wangwu at wangwu@ruby-lang.org
Contact Guido at guido@python.org

Guido's address is  guido@python.org
```
- 可以使用del语句来删除字典的键值对
- 通过使用字典的items方法来获得字典中的每个键值对，返回一个元组的列表，其中每个元组都包含——键对应的值。
- 使用in来判断一个键/值是否存在一个字典中，还可以通过dict类的has_key方法。
- 更多信息可以通过help(dict)来获得
 
### 4 序列
列表、元组和字符串都是序列，序列最主要的两个特点是：

- 可以通过索引操作，获得一个特定的项目
- 切片操作来获得序列的一个切片
```
# -*- coding: utf-8 -*-
#filename:seq.py

shoplist = ['apple','mango','carrot','banana']

#Indexing or "subscription' operation
print("Item 0 is ", shoplist[0])
print("Item 1 is ", shoplist[1])
print("Item -1 is ", shoplist[-1])
print('Item -2 is ', shoplist[-2])

# Slicing on a list
print("Item 1 to Item 3 is ", shoplist[1:3])
print("Item 2 to end is ", shoplist[2:])
print("Item 1 to -1 is ", shoplist[1:-1])
print("start to end is ", shoplist[:])

# Slicing on a string

name = 'swaroop'
print("characters 1 to 3 is ", name[1:3])
print("characters 2 to end is ", name[2:])
print("characters start to end is ", name[:])
OUTPUT：
Item 0 is  apple
Item 1 is  mango
Item -1 is  banana
Item -2 is  carrot
Item 1 to Item 3 is  ['mango', 'carrot']
Item 2 to end is  ['carrot', 'banana']
Item 1 to -1 is  ['mango', 'carrot']
start to end is  ['apple', 'mango', 'carrot', 'banana']
characters 1 to 3 is  wa
characters 2 to end is  aroop
characters start to end is  swaroop
```
>注意：
- python索引从0开始计算，这点需要注意。即shoplist{2]应该是第一个项目
- 索引同样可以使用负数，即从末尾开始往回计算。 shoplist[-1]表示最后一个元素。
- 切片符号的第一个数表示切片的开始位置，第二个数表示切片到哪里结束（不包括第二个数本身）

### 5 参考
当创建一个对象并给他赋一个变量的时候，这个变量仅仅参考那个对象，而不是表示这个变量本身。也就是说，变量名指向计算机存储那个对象的内存，这被称作名称到对象的绑定。
```
# -*- coding: utf-8 -*-
#filename:reference.py

print("Simple Assignmet")

shoplist = ['apple','mango','carrot', 'banana']
mylist = shoplist  
print("The id of mylist is ",id(mylist))
print("The id of shoplist is ",id(shoplist))
del shoplist[0]
print("shoplist is ", shoplist)
print("my list is ", mylist)

print("copy by making a full slice")
mylist = shoplist[:] # 内存中备份一份shoplist的内容，然后mylist指向改地址，mylist和shoplist两个完全不同、
print("The id of mylist is ",id(mylist))
print("The id of shoplist is ",id(shoplist))
del mylist[0] 
print("shoplist is ", shoplist)
print("my list is ", mylist)
OUTPUT:
Simple Assignmet
The id of mylist is    2597586330568
The id of shoplist is  2597586330568
shoplist is  ['mango', 'carrot', 'banana']
my list is  ['mango', 'carrot', 'banana']
copy by making a full slice
The id of mylist is    2597586330632
The id of shoplist is  2597586330568
shoplist is  ['mango', 'carrot', 'banana']
my list is  ['carrot', 'banana']
```
>注：如果只是需要复制一个列表或者类似的序列的话，使用切片操作符来取得拷贝即可，如果想要使用另外一个变量名，两个名称都参与同一个对象，如果不小心则会带来各种麻烦。
### 6 更多字符串的内容
```
# -*- coding: utf-8 -*-
#filename:str_method.py
name = "Swaroop"
if name.startswith('Swa'): # 判断字符串是否以"Swa:"开头
    print("Yes, the String starts with 'Swa'")
if 'a' in name: #判断a是否是name字符串的一部分
    print("Yes,it contains the string 'a'")
if name.find('war') !=-1: #是否能在name字符串中找到war，-1表示找不到子字符串
    print("Yes, it contains the string 'war'")
delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print (delimiter.join(mylist))
OUTPUT:
Yes, the String starts with 'Swa'
Yes,it contains the string 'a'
Yes, it contains the string 'war'
Brazil_*_Russia_*_India_*_China
```
## chapter10 编写第一个Python程序
**1 问题**
**问题**：想要为自己所有重要的文件进行备份的程序
**分析**：如何确定该备份哪些文件、备份文件存放在哪里，我们该怎么存储备份?
1. 需要备份的而文件和目录由一个列表指定
2. 备份应该保存在主目录中
3. 文件备份成一个zip文件
4. zip存档的名称应该是当前的日期和时间
5. 可以使用标准的zip命令，linux/unix发行版默认提供，windows用户可以使用Info-Zip程序。
**解决方案**
### Version 1
```
# -*- coding: utf-8 -*-
#filename:backup_ver1.py

import os
import time
#1. the files and directories to be backed up are specified in a list.
source = [r'E:\code', r'E:\books']
#2. the backup must be stored in a mina backup directory
target_dir = r'E:\backup'
#3. The files are backed up to a zip file.
#4. the name of the zip archive is the current date and time.
target = target_dir + time.strftime('%Y%m%d%H%M%S')+ '.zip'
#5. Use the bandizip command to put the files in a zip  archive
#在自己电脑中安装7zip压缩软件，并把安装目录添加到系统PATH中
zip_command = '7z a {} {}'.format(target,' '.join(source))
# Run the backup
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup Failed")
OUTPUT:
Successful backup to E:\backup20180506165041.zip
```

### Version2
优化：使用时间作为文件名，而当前日期作为文件夹，存放在主备份目录中。
```
# -*- coding: utf-8 -*-
#filename:backup_ver2.py
import os
import time
#1. the files and directories to be backed up are specified in a list.
source = [r'E:\code', r'E:\books']
#2. the backup must be stored in a mina backup directory
target_dir = r'E:\backup'
#3. The files are backed up to a zip file.
#4. the name of the zip archive is the current date and time.
today = target_dir + time.strftime('%Y%m%d')
# The current day is the name fof the subdirectory in the main directory
now = time.strftime("%H%M%S")
# Create the subdirectory  if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make a directory
    print("Successfully created directory", today)
# the name of the zip file
target = today + os.sep + now + '.zip'
#5. Use the bandizip command to put the files in a zip  archive
#在自己电脑中安装7zip压缩软件，并把安装目录添加到系统PATH中
zip_command = '7z a {} {}'.format(target,' '.join(source))
# Run the backup
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup Failed")
OUTPUT:
Successful backup to E:\backup20180506\190956.zip
```
### Version 3 报错 不工作
```
# -*- coding: utf-8 -*-
#filename:backup_ver3.py

import os
import time

#1. the files and directories to be backed up are specified in a list.
source = [r'E:\code', r'E:\books']

#2. the backup must be stored in a mina backup directory
target_dir = r'E:\backup'

#3. The files are backed up to a zip file.
#4. the name of the zip archive is the current date and time.
today = target_dir + time.strftime('%Y%m%d')
# The current day is the name fof the subdirectory in the main directory
now = time.strftime("%H%M%S")

#Take a comment from the user to create the name of the zip file
comment = input("Enter a commment--->")
if len(comment)  == 0:
    target  = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + 
    comment.replace(' ', '_') + '.zip'

# Create the subdirectory  if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make a directory
    print("Successfully created directory", today)

# the name of the zip file
target = today + os.sep + now + '.zip'

#5. Use the bandizip command to put the files in a zip  archive
#在自己电脑中安装7zip压缩软件，并把安装目录添加到系统PATH中
zip_command = '7z a {} {}'.format(target,' '.join(source))
# Run the backup
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup Failed")
OUTPUT：
  File "E:/backup_ver3.py", line 24
    target = today + os.sep + now + '_' +
                                          ^
SyntaxError: invalid syntax

提示语法错误，因为发现操作符 + 右边没有任何操作数，因此不知道该如何执行。如果一行不够写需要多行来写的话，需要在末尾加上反斜杠/来表示下一行继续。
```
### Version4 修改Version3的错误
```
# -*- coding: utf-8 -*-
#filename:backup_ver3.py
import os
import time
#1. the files and directories to be backed up are specified in a list.
source = [r'E:\code', r'E:\books']
#2. the backup must be stored in a mina backup directory
target_dir = r'E:\backup'

#3. The files are backed up to a zip file.
#4. the name of the zip archive is the current date and time.
today = target_dir + time.strftime('%Y%m%d')
# The current day is the name fof the subdirectory in the main directory
now = time.strftime("%H%M%S")
#Take a comment from the user to create the name of the zip file
comment = input("Enter a commment--->")
if len(comment)  == 0:
    target  = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'
# Create the subdirectory  if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make a directory
    print("Successfully created directory", today)
#5. Use the bandizip command to put the files in a zip  archive
#在自己电脑中安装7zip压缩软件，并把安装目录添加到系统PATH中
zip_command = '7z a {} {}'.format(target,' '.join(source))
# Run the backup
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup Failed")
OUTPUT:
Enter a commment--->add new examples
Successful backup to E:\backup20180506\192629_add_new_examples.zip
Enter a commment--->
Successful backup to E:\backup20180506\192643.zip
```
### 进一步优化
- 可以在程序中包含交互程序——可以用-V选项来是你的程序更具交互性
- 另一个可以改进的是使得文件和目录能够通过命令行直接传递给程序，可以使用sys.argv 列表获取它们，然后使用list的append方法把它们添加到source列表中。
- 还可以使用tar命令提花zip命令，这样做的一个优势实在你结合tar和gzip命令的时候，备份会更快更小，如果想要在windows中是哦有那个这样的归档，Winzip也能方便的处理这些.tar.gz文件。 tar命令大多数Linux/Unix系统中默认可用的。Windows用户也可以下载安装。

命令字符串现在将改为：
tar = 'tar -cvzf %s %s -X /home/swaroop/excludes.txt' %(target,' '.join(srcdir))
其中：

- -c：表示创建一个归档
- -v 表示表示交互，即命令更具有交互性
- -z表示使用gzip
- -f表示强制性创建归档，即如果已经有一个同名文件，它会被替换掉
- -X表示含在文件名列表中的我呢见会被排除在备份外。例如，你可以可以在文件中指定*，从而不让备份包括所有以结尾的文件。

> **重要**
>最理想的创建这些归档的方法分别是使用zipfile和tarfile。它们是Python的标准库的一部分，使用这些库就避免了使用os.system这个不推荐使用的函数，它容易引发严重的错误。

## 软件开发过程
1. 什么（分析）
2. 如何（设计）
3. 编写（实施）
4. 测试（测试和调试）
5. 使用（实施或开发）
6. 维护（优化）
> 重要:
我们创建这个备份脚本的过程是编写程序的推荐方法——进行分析与设计。开始时实施一个简单的版本。对它进行测试与调试。使用它以确信它如预期那样地工作。再增加任何你想要的特性，根据需要一次次重复这个编写－测试－使用的周期。记住“软件是长出来的，而不是建造的”。

## chapter11 面向对象的编程
### 1 简介
到目前为止，我们之前程序中，都是根据操作数据的函数或语句来设计程序的，这被称为面向过程的编程。python是一种把数据和功能相结合，用称为对象的东西包裹起来组织程序的方法，被称为面向对象的编程。
在大多数情况下可以使用过程性编程。但有时候你想要编程大型程序或者寻求一个更加适合的解决方案的时候，就得使用面向对象的编程。
**类和对象是面向对象编程的两个重要方面。类创建一个新类型，对象是类的一个实例。**

- 对象可以使用普通的属于对象的变量存储数据。属于一个对象或类的变量称为域。对象也可以使用属于类的函数来具有功能，这样的函数被称为类的方法。
- 域有两种类型——属于每个实例/类或属于类本身。分别称为实例变量和类变量
- 类使用class关键字来创建。类的域和方法被列在一个缩进块中。

### 2 self
类的方法和普通的函数只有一个特别的区别——即类的方法必须有一个额外的第一个参数，但是你在调用这个方法的时候不需要为其赋值，Python会提供这个值，这个特别的变量指对象本身，按惯例它的名称为**self**

>建议：虽然这个self名称可以是其他任意标识符。但是强烈建议使用self。可以避免很多麻烦。
### 3 创建一个类
```
# -*- coding: utf-8 -*-
#filename:simplestclass.py

class Person():
    pass # An empty block
    
p = Person() # 创建一个实例p
print(p)
OUTPUT:
<__main__.Person object at 0x000001F5C1E80208>
```
### 4 使用对象的方法
类和对象可以拥有和函数一样的方法，这些方法和函数的区别只是一个self变量的。
```
#! /usr/bin/env python3
# filename:method.py
class Person():
    def sayHi(self):
        print("hello, how are you?")
p = Person()
p.sayHi()
OUTPUT:
hello, how are you?
```
>注意：调用sayHi方法时没有任何参数，但仍需在函数定义的时候写上self。

### 5 \__init__方法
在Python的类中有很多的方法的名字有特殊的意义，比如\__init__.
\__init__方法在类的一个对象被建立，马上运行，这个方法用来对你的对象做一些你希望的初始化。
>注意，这个名称两边都是双下划线
```
#! usr/bin/env python
#filename:class_init.py
class Person():
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print("Hello, my name is ", self.name)
p = Person("zhangsan")
p.sayHi()
OUTPUT:
Hello, my name is  zhangsan
```
**如何工作的？**
\__init__方法定义时候取了一个参数name（以及必须的参数self）。在这个\__init__里面，只是创建了一个新的域，也称为name。虽然它们名称一样，但是它们是两个不同的变量，通过点号来区分它们。
最重要的是，我们没有专门调用\__init__方法，只是在创建实例的时候，把参数阔在圆括号内跟在类名的后面，从而传递给\__init__方法。这是这种方法的重要之处。
### 6 类和对象的方法
数据部分事实上只是与类和对象的名称空间绑定的普通变量，即这些名称只在这些类和对象的前提下有效。
实例：
```
#!/usr/bin/env python
#filename:objvar.py
class Person():
    """Represents a person."""
    population = 0  # population这个变量是属于Person类的

    def __init__(self, name):
        '''Initalizes the person's data.'''
        self.name = name
        print("(Initializing {})".format(self.name))
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
    def __del__(self):    #当对象不在被调用的时候，Python会自动运行该函数，但是无法保证这个方法何时才会运行，如果想要指明它运行，就得使用del语句。
        '''I am dying'''
        print("{} says bye.".format(self.name))
        Person.population -= 1
        if Person.population == 0:
            print("I am the last one.")
        else:
            print("There are still {} people left.".format(Person.population))
    def sayHi(self):
        '''
            Greeting by the person
            Really, that's all it does.
        '''
        print("Hi, my name is {}".format(self.name))
    def howMany(self):
        '''Prints the current population'''
        if Person.population == 1:
            print("I am the only person here.")
        else:
            print("We have {} persons here.".format(Person.population))
swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()
kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()
del swaroop #原文采用的是Python的自动回收机制，
            #但是自己测试时无法获得一样结果且
            #无法知道Python自动回收具体时间，因此采用手动删除
swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()
OUTPUT:
(Initializing Swaroop)
Hi, my name is Swaroop
I am the only person here.
(Initializing Abdul Kalam)
Hi, my name is Abdul Kalam
We have 2 persons here.
Swaroop says bye.
There are still 1 people left.
(Initializing Swaroop)
Hi, my name is Swaroop
We have 2 persons here.
```
### 7 继承
面向对象的编程带来的主要好处之一就是代码的重用，实现这个重用的方法之一就是通过 继承 机制。继承完全可以理解为类之间的类型和子类型关系
```
# -*- coding: utf-8 -*-
#filename:inherit.py

class SchoolMember(object):
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized SchoolMember: {}".format(self.name))
    def tell(self):
        '''Tell my details.'''
        print("Name:{} Age {}".format(self.name, self.age))
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher: {}".format(self.name))
        
    def tell(self):
        SchoolMember.tell(self) #调用了父类ShoolMember的tell方法
        print("Salary：{}".format(self.salary))
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initialized Student: {}".format(self.name))
    def tell(self):
        SchoolMember.tell(self) #调用了父类ShoolMember的tell方法
        print("Marks: {}".format(self.marks))        
        
t = Teacher('Mrs.zhang', 40, 30000)
s = Student('lisi',20,100)
print # print a blank line

members = [t,s]
for member in members:
    member.tell()   #works for both Teachers and Students
OUTPUT:
Initialized SchoolMember: Mrs.zhang
Initialized Teacher: Mrs.zhang
Initialized SchoolMember: lisi
Initialized Student: lisi
Name:Mrs.zhang Age 40
Salary：30000
Name:lisi Age 20
Marks: 100
```
## chapter12 输入和输出
想要程序和用户交互，你会从用户哪里得到输入，然后打印一些结果，我们可以使用input和print语句来实现这些功能，对于输出，可以使用多种多样的str类，例如能够使用rjust方法来得到一个按照一定宽度右对齐的字符串，可以利用help(str)来获得更多详情。

### 1 文件
可以通过创建一个文件file类的对象来打开一个文件，分别使用file类的open、read、readline或write方法来恰当地读写文件。对于文件的读写能力依赖于你在打开文件时候指定的模式。最后，当你完成对文件的额操作的时候，调用close方法来告诉python关闭文件。
实例：
```
# -*- coding: utf-8 -*-
#filename：using_file.py
poem = '''\
Programming is fun
When the  work is done
if you wanna make your work also fun:
            use Python!
'''
f = open(r'E:\poem.txt','w')#以写的方式打开文件，文件若不存在则创建一个文件
f.write(poem)
f.close()
f = open(r"E:\poem.txt") #默认模式为r，即只读
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()
OUTPUT:
Programming is fun
When the  work is done
if you wanna make your work also fun:
            use Python!
```
>更多文件的帮助文件可以通过help(file)来获得

### 2 存储器
python提供一个标准的模块pickle，使用它你可以在一个文件中存储任何python对象，还可以把它完整无缺地取出来。
还有一个称为cPickle模块，功能和pickle模块完全相同，只不过使用C语言编写的，因此要快很多。
```
#filename:pickling.py
import pickle as p
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
OUTPUT:
['apple', 'mango', 'carrot']
```
>备注：
1. 在Python3中cPickle和pickle模块合并，直接引入pickle即可
2. Python3中想要用存储器的话，那么读写文件都要用二进制模式，即‘rb’或‘wb’
3. python3中不能用file打开文件，改为open
### chapter13 异常
当程序出现某些异常的状况的时候，异常就发生了，例如：想要打开某个文件，而这个文件不存在，或者在运行的过程中，你不小心把它删除了，这些情况就可以使用异常来处理。
### 1.处理异常
1.python自发告诉你哪里出现错误
```
>>> print 'hello,world'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello,world')?
>>> print('hello,world')
hello,world
```
2. 使用try...except
通常把要判断是否会出现异常的语句放在try语句中，而把错误处理语句放在except中
```
#_*_coding:utf-8_*_
#filename:try_except.py
import sys
try:
    s = int(input('Enter something---> '))
    num = 10
    print(num/s)
except (ValueError，EOFError): 
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
    print('done'))
OUTPUT:
1. Enter something---> 0
除数不能为0，请修改！
   done
2. Enter something---> a
   请输入一个整数！
3.Enter something---> 2
  5.0
  all OK
 done
```
 >except语句可以专门处理单一的错误或异常，甚至可以使用一组包括在圆括号内的错误异常。如果没有给出错误/异常的名，就会处理所有的错误和异常。对于每个try语句至少要关联一个except语句。
>try...except还可以关联else，当没有异常发生的时候，则执行else语句，关联finally语句的话，不管是否有异常发生（适用于文件关闭），都会执行。
###2.引发异常
可以使用raise语句引发异常，需要指明错误/异常的名称和伴随异常出发的一场对象，可以引用的错误或异常应该分别是一个Error或Exception的直接或间接导出类。
1.如何引发异常
实例：
```
#_*_coding:utf-8_*_
#filename:raising.py
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self,length,atleast)
        self.length = length
        self.atleast = atleast
try:
    s = input("Enter something--> ")
    if (len(s)) < 3:
        raise ShortInputException(len(s),3)
    # Other work can continue as usual here
except EOFError:
    print("\nWhy did you do an EOF on me?")
except ShortInputException as x:
    print("ShortInputException: The input was of length {},\
          was excepting at least {}".format(x.length, x.atleast))
else:
    print("No exception was raised.")
```
OUTPUT:
```
1. 按下CTRL+D的结果：
Enter something--> 
Why did you do an EOF on me?
2. 输入少于3个字符的结果：
Enter something--> ab
ShortInputException: The input was of length 2,          was excepting at least 3
3. 输入多于3个字符的结果：
Enter something--> abc
No exception was raised.
```
## chapter14 Python标准库
python标准库是随python安装的，包含大量极其有用的模块，熟悉Python标准库是十分重要的。
###1.sys模块
sys模块包含系统对应的功能，如学了sys.argv列表，包含命令行参数
实例：
```
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
```
OUTPUT:
```
E:\>python cat.py
No action specified.
E:\>python cat.py --help
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version : Prints the version number
    --help : Display this help
E:\>python cat.py --version
Version 1.2
E:\>python cat.py abc.txt
124
```
### 2.更多sys的内容
sys.version字符串提供安装的Python的版本信息，sys.version_info元组则提供一个更加简单的方法来获得Python版本信息
```
>>> import sys
>>> sys.version
'3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]'
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0)
```
对于有经验的程序眼，sys模块中有其它令人感兴趣的项目有sys.stdin,sys.stdout,和sys.stderr分别是标准输入，标准输出和标准错误流。

### 3. OS模块
os模块包含普遍的操作系统功能，如果希望程序能够于平台无关，这个模块尤为重要。即它允许一个程序在编写后不需要任何改动，也不会发生任何问题，就可以在Windows和Linux下运行。例如：os.sep就可以取代操作系统的特定的路径分隔符。
- os.name 获得正在使用的平台， windows：nt，Linux/Unix：posix
- os.getcwd()函数得到当前的工作目录，即当前Python脚本工作的目录路径
- os.getenv()和os.putenv()函数分别用来读取和设置环境变量
- os.listdir()函数返回指定目录下的所有文件和目录名
- os.remove() 用来删除一个文件
- os.system()用来运行shell命令
- os.linesep字符串给出当前平台使用的行终止符 例如：windows使用'\r\n',Linux使用'\n'而Mac使用'\r'
- os.path.split()返回一个路径的目录名和文件名。
```
>>> import os
>>> os.path.split(r"E:\2_Study\English\english through pictures book1.pdf")
('E:\\2_Study\\English', 'english through pictures book1.pdf')
```
- os.path.isfile()和os.path.isdir()分别检验给出的路径是一个文件还是目录。类似的，os.path.existe()用来检验给出的目录是否真的存在。
## chapter15 更多Python的内容
### 1.特殊的方法
在类中有一些特殊的方法具有特殊的意义，比如\__init__和\__del__
列表：一些特殊的方法
|  名称|  说明   |
|------|---------|
|\__init__(self,...)|这个方法在新建对象时候恰好被返回使用之前被调用|
|\__del__(self,...)|恰好在对象要被删除之前调用|
|\_str_(self)|在我们对对象使用print语句或者使用str()的时候调用|
|\_lt_(self,other)|当使用小于(<）的时候调用，类似地，对于所有的运算符（+，>等等）都有特殊的方法|
|\_getitem_(self,key)|使用x[key]索引操作符的时候使用|
|\_len_(self)|对序列对象使用内建的len()函数的时候调用|

### 2.单语句块
 如果你的语句只包含一句，那么可以在条件或循环语句的同一行指明它，如：
```
 >>> if True: print('YES')
YES
```
注：单个语句虽然可以使得程序变得小一些，但是除了检验错误之外还是建议不要使用这种缩略方式。
### 3.使用列表综合
```
#_*_ coding:utf-8 _*_
#filename:list_comprehension.py
listone = [2,3,4]
listtwo = [ 2*i for i in listone if i > 2]
print(listtwo)  # [6,8]
OUTPUT:
[6,8]
```
### 4.在函数中接收元组和字典
当要想函数接受元组或字典形式的参数的时候，有一种特殊的方法，分别使用\*和\*\*前缀，这种方法在函数需要获取可变数量的参数的时候特别有用。
实例：
```
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
OUTPUT:
25
100
```
### 5.lambda形式
lambda语句被用来创建新的 **函数对象**，也称为匿名函数
```
# _*_ coding:utf-8 _*_
#filename:lambda.py
def make_repeater(n):
    return lambda s:s*n  # 创建一个函数对象
twice = make_repeater(2)
print(twice('word'))
print (twice(5))
OUTPUT：
wordword
10
```
### 6.exec和eval语句
exec语句用来执行存储在字符串或文件中的python语句，例如，可以在运行时生成一个包含python代码的字符串，然后用exec语句执行这些语句。
```
>>> exec('print("helloworld")')
helloworld
```
eval语句用来计算存储在字符串中的有效的python表达式
```
>>> eval('2*3')
6
```
### 7.assert语句
assert语句用来声明某个条件是真的，例如你非常确定某个你使用的列表中至少有一个元素，而你先要检验这一点，并且在它非真的时候引发一个错误，那么assert语句应用在这种情形下的理想语句，当assert语句失败的时候，会引发一个AssertionError。
```
>>> mylist = ['item']
>>> assert (len(mylist) >=1)
>>> mylist.pop()
'item'
>>> assert(len(mylist) >= 1)  #当mylist<1 assert失败，则报错
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    assert(len(mylist) >= 1)
AssertionError
```
### 8. repe函数
repe函数用来取得对象的规范字符串表示。反引号（也称转换符）可以完成相同的功能。
>注意：在大多数时候有eval(repr(object)) == object
```
>>> i = []
>>> i.append('item')
>>> `i`                # 在python3中不再支持
  File "<stdin>", line 1
    `i`
    ^
SyntaxError: invalid syntax
>>> repr(i)
"['item']"
```
## chapter16 接下来学什么
学完这整本书并且跟着编写了一些程序，那么接下来学习什么？
1.我会建议你先解决这样一个问题：创建你自己的命令行 地址簿 程序。在这个程序中，你可以添加、修改、删除和搜索你的联系人（朋友、家人和同事等等）以及它们的信息（诸如电子邮件地址和/或电话号码）。这些详细信息应该被保存下来以便以后提取。
思考一下我们到目前为止所学的各种东西的话，你会觉得这个问题其实相当简单。如果你仍然希望知道该从何处入手的话，那么这里也有一个提示。
提示（其实你不应该阅读这个提示） 创建一个类来表示一个人的信息。使用字典储存每个人的对象，把他们的名字作为键。使用cPickle模块永久地把这些对象储存在你的硬盘上。使用字典内建的方法添加、删除和修改人员信息。
一旦你完成了这个程序，你就可以说是一个Python程序员了。现在，请立即寄一封信给我感谢我为你提供了这本优秀的教材吧。是否告知我，如你所愿，但是我确实希望你能够告诉我。

2. 继续python之路
**图形软件**
使用Python的GUI库——需要使用这些库来用python语句创建自己的图形程序。使用GUI和它们的Python绑定，你可以创建自己的IrfanView、KuicksShow软件或任何别的类似的东西。
有很多可供选择的python的GUI：
- PyQt只是Qt工具包的Python绑定，Qt工具包是构建KDE的基石。一个很好的PyQt资源的是[《使用Pytho语言的GUI编程：Qt版》](http://www.opendocs.org/pyqt/)请查阅[官方主页](http://www.riverbankcomputing.co.uk/pyqt/index.php)来获取更多信息。
- PyGTK 这是GTK+工具包的Python绑定。GTK+工具包是构建GNOME的基石。GTK+在使用上有很多怪癖的地方，不过一旦你习惯了，你可以非常快速地开发GUI应用程序。Glade图形界面设计器是必不可少的，而文档还有待改善。GTK+在Linux上工作得很好，而它的Windows接口还不完整。你可以使用GTK+开发免费和具有产权的软件。请查阅[官方主页](http://www.pygtk.org/)以获取更多详情。
- wxPython 这是wxWidgets工具包的Python绑定。wxPython有与它相关的学习方法。它的可移植性极佳，可以在Linux、Windows、Mac甚至嵌入式平台上运行。有很多wxPython的IDE，其中包括GUI设计器以及如[SPE（Santi's Python Editor）](http://spe.pycs.net/)和[wxGlade](http://wxglade.sourceforge.net/)那样的GUI开发器。你可以使用wxPython开发免费和具有产权的软件。请查阅[官方主页](http://www.wxpython.org/)以获取更多详情。
- TkInter 这是现存最老的GUI工具包之一。如果你使用过IDLE，它就是一个TkInter程序。在[PythonWare.org](http://www.pythonware.com/library/tkinter/introduction/index.htm)上的TkInter文档是十分透彻的。TkInter具备可移植性，可以在Linux/Unix和Windows下工作。重要的是，TkInter是标准Python发行版的一部分
要获取更多选择，请参阅[Python.org上的GUI编程wiki页](http://www.python.org/cgi-bin/moinmoin/GuiProgramming)。
**更多内容**
- Python标准库是一个丰富的库，在大多数时候，你可以在这个库中找到你所需的东西。这被称为Python的“功能齐全”理念。我强烈建议你在开始开发大型Python程序之前浏览一下[Python标准文档](http://docs.python.org/)。
- [Python.org](http://www.python.org/)——Python编程语言的官方主页。你可以在上面找到Python语言和解释器的最新版本。另外还有各种邮件列表活跃地讨论Python的各方面内容。
- comp.lang.python是讨论Python语言的世界性新闻组。你可以把你的疑惑和询问贴在这个新闻组上。可以使用[Google群](http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&group=comp.lang.python)在线访问这个新闻组，或加入作为新闻组镜像的[邮件列表](http://mail.python.org/mailman/listinfo/python-list)。
- [《Python实用大全》](http://aspn.activestate.com/ASPN/Python/Cookbook/)是一个极有价值的秘诀和技巧集合，它帮助你解决某些使用Python的问题。这是每个Python用户必读的一本书。
- [《迷人的Python》](http://gnosis.cx/publish/tech_index_cp.html)是David Mertz编著的一系列优秀的Python相关文章。
- [《深入理解Python》](http://www.diveintopython.org/)是给有经验的Python程序员的一本很优秀的书。如果你已经完整地阅读了本书，那么我强烈建议你接下来阅读《深入理解Python》。它覆盖了包括XML处理、单元测试和功能性编程在内的广泛的主题。
- [Jython](http://www.jython.org/)是用Java语言实现的Python解释器。这意味着你可以用Python语言编写程序而同时使用Java库！Jython是一个稳定成熟的软件。如果你也是一个Java程序员，我强烈建议你尝试一下Jython。
- [IronPython](http://www.ironpython.com/)是用C#语言实现的Python解释器，可以运行在.NET、Mono和DotGNU平台上。这意味着你可以用Python语言编写程序而使用.NET库以及其他由这三种平台提供的库！IronPython还只是一个前期alpha测试软件，现在还只适合用来进行试验。Jim Hugunin，IronPython的开发者，已经加入了微软公司，将在将来全力开发一个完整版本的IronPython。
- [Lython](http://www.caddr.com/code/lython/)是Python语言的Lisp前段。它类似于普通的Lisp语言，会被直接编译为Python字节码，这意味着它能与我们普通的Python代码协同工作。
- 另外还有很多很多的Python资源。其中比较有趣的有[Daily Python-URL](http://www.pythonware.com/daily/)!，它使你保持与Python的最新进展同步。另外还有[Vaults of Parnassus](http://www.vex.net/parnassus/)、[ONLamp.com Python DevCenter](http://www.onlamp.com/python/)、[dirtSimple.org](http://dirtsimple.org/)、[Python Notes](http://pythonnotes.blogspot.com/)等等。