from cmath import acos
print ("this is test python.");
work = 'work ...'
num = 10.0
sentens = "sentens"
pat = """这是一个段落。
包含了多个语句"""
print (work)
print (str(num) + "\n")
'''
这是多行注释，使用单引号。
'''
"""
这是多行注释，使用双引号。
"""
def raw_input(str):
    print(str)
raw_input("\n\nPress the enter key to exit.")
# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n');
if True :
    print("this true");
# 多变量赋值
a, b, c = 1, 2, "john"
a = b = c = 1;
print (b);
s = 'ilovepython'
print(s[1:5]);
print(s[1:]);
print(s[1])


str = 'inlovepython'
print (str)  # 输出完整字符串
print (str[0])  # 输出字符串中的第一个字符
print (str[2:5])  # 输出字符串中第三个至第五个之间的字符串
print (str[2:])  # 输出从第三个字符开始的字符串
print (str * 2, "\n")  # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串

# 列表的跟字符串的一致

# 元组,不能二次赋值，相当于只读列表,跟字符串的一致
tuple = ('abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')

# tuple[2] = 1000 # 元组中是非法应用
# list[2] = 1000 # 列表中是合法应用
print(tuple)
print(tuple[0])

# 字典
dict = {}  # 必须先定义成字典类型
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}

print (dict['one'])  # 输出键为'one' 的值
print (dict[2])  # 输出键为 2 的值
print (tinydict)  # 输出完整的字典
print (tinydict.keys())  # 输出所有键
print (tinydict.values())  # 输出所有值
print (tinydict['name'])

if True and True:
    print ("and")
    if True or True:
        print ("or")
if not False :
    print("not")
if 'name' in tinydict :
    print('in')
if 'nameSS' not in tinydict :
    print('not in')
if a is b:
    print("is");
if dict['one'] is not dict[2] :
    print("is not")
if str == 'inlovepython':
    print("==")

count = 0;
while count < 9 :
    print("while is " , count);
    count += 1;
    if count == 5:
        break;
else : print (count, "is not lass than 9")
# while count : print ('Given flag is really true!')

for let in 'python' :
    print ("for 首字母", let);
fruits = ['banana', 'apple', 'mango']
for fruit in fruits : 
    print ("for " + fruit);
for index in range(len(fruits)) :
    print ('for 当前水果 :', fruits[index])
    
for let in 'python' :
    if let == 't':
        pass
        print ("this pass块")
    print ("for 当前字母", let);
    
var1 = "hello world !"
print ("更新字符串 : ", var1[:6] + 'Runoob!');

print("字符串格式化: My name is %s and weight is %d kg!" % ('Zara', 21))
fruits[2] = 'mango1';
print ("update mango", fruits)
del fruits[2]
print ("del mango1", fruits)
import time
print (time.time())
print (time.localtime())
import myPythonUtil
print ("CurrentTime: ", myPythonUtil.getCurrentTime());

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

import calendar

cal = calendar.month(2016, 8)
print ("以下输出2016年1月份的日历:")
print (cal);

def printinfo(name , age):
    print ("name: ",name)
    print ("age: ",age)

printinfo(age=22, name="lll") ###参数位置可以不一致
# printinfo("lij")#不可行

#缺省参数 3.0后不支持缺省了
# def printinfo1(name, age = 20):
#     print ("name: ",name)
#     print ("age: ",age)
#     
# printinfo(name = "lij")

#不定长参数
def printinfo2(var, *vartuple):
    "打印任何输入参数"
    print ("已命名参数: ")
    print (var)
    if len(vartuple)>0 :
        print ("不定长参数: ")
    for var1 in vartuple:
        print (var1)
    return
printinfo2(10)
printinfo2(10,20,30)

#lambda定义匿名函数
sums = lambda agr1, agr2 : agr1 + agr2

print ("相加后的值为 : ", sums( 10, 20))

#全局变量 跟 局部变量
total = 0;
def sum3(var1 , var2):
#     global total #定义total使用全局
    total = var1 + var2 # total在这里是局部变量.
    print ("方法体内 ：total=",total)
    return total;
sum3(10, 20);
print ("方法体外 ：total=",total)

#输出在一个模块里定义的所有模块，变量和函数
import math
content = dir(math)
print (content)

print ("--------I/O--------")
# strinput = raw_input("请输入：") #3.x班版本好像不行了
# strinput = input("请输入：")
# print ("你输入的内容是: ",strinput);

import os

#fo = open("a.txt", "wb")
#fo.write(myPythonUtil.str2Bytes("www.runoob.com!\nVery good site!\n"));
fo = open("a.txt", "a+")
#fo.write("i love python!\nevery day!\n");
print("文件名: ",fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
try:
    print(fo.next())
except Exception :
    print ("errors :")
finally:
    print("finally")
    
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行
    return
try:
    print(fo.next())
except Exception :
    print ("errors :")
finally:
    print("finally")
    
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行
    return

try:
    mye(0)                # 触发异常
except Exception:
    print (1)
else:
    print (2)

try:
    mye(0)                # 触发异常
except Exception:
    print (1)
else:
    print (2)

try:
    raise Exception("Bad hostname")
except Exception:
#except Exception, e: #3.x版本后不行了
    print (sys.exc_info()[0],sys.exc_info()[1])
#    print ('e.message:\t', e.message)
try:
    raise Exception("Bad hostname")
except Exception:
#except Exception, e: #3.x版本后不行了
    print (sys.exc_info()[0],sys.exc_info()[1])
#    print ('e.message:\t', e.message)
# print("读取内容：",fo.read(10))
# print("末尾是否强制加空格 : ", fo.softspace )
fo.close();

class Employee : 
    empCount = 0; #公有变量     类似    类静态变量
    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;
        Employee.empCount += 1;
    def displayCount(self):
        print ("Total employee %d ." % Employee.empCount);
    def displayEmployee(self):
        print ("name: ",self.name, "; salary: ", self.salary);

emp1 = Employee("abc", 1000);
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
emp2.displayCount()
print ("Total Employee %d" % Employee.empCount)
#添加或修改属性
emp1.age = 7;
emp1.age = 8;
print (emp1.age)
#访问对象属性
print ("hasattr " , hasattr(emp1, "name"))
print ("getattr " , getattr(emp1, "name"))
setattr(emp1, "name", "bca")
print ("setattr " , emp1.name)
delattr(emp1, "age")
# print ("delattr " , emp1.age)
#内置类属性
print (Employee.__name__)

print ("---------exception-----------")
try:
    print(fo.next())
except Exception :
    print ("errors :")
finally:
    print("finally")
    
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行
    return

try:
    mye(0)                # 触发异常
except Exception:
    print (1)
else:
    print (2)

try:
    #自定义异常
    raise Exception("Bad hostname")
except Exception:
#except Exception, e: #3.x版本后不行了
    print (sys.exc_info()[0],sys.exc_info()[1])
#    print ('e.message:\t', e.message)
# print("读取内容：",fo.read(10))
# print("末尾是否强制加空格 : ", fo.softspace )
fo.close();