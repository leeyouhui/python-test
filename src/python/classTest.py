class Parent:  # 定义父类
    parentAttr = 100
    def __init__(self):
        print ("调用父类构造函数")

    def parentMethod(self):
        print ('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("父类属性 :", Parent.parentAttr)
      
    def mymethod(self):
        print ("父类方法")

class Child(Parent):  # 定义子类
    def __init__(self):
        print ("调用子类构造方法")

    def childMethod(self):
        print ('调用子类方法 child method')
        
    def mymethod(self):
        print ("子类方法")


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法
c.getAttr()  # 再次调用父类的方法
c.mymethod()

#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
        
    def __count1(self):
        print ("私有方法")
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
# print (counter.__secretCount)  # 报错，实例不能访问私有变量
# counter.__count1() # 报错，实例不能访问私有方法

#匹配
import re
print (re.match("www", "www.baidu.com").span())  # 在起始位置匹配
print(re.match('www', 'www.runoob.com'))         # 在起始位置匹配
print (re.match("com", "www.baidu.com"))  # 不在起始位置匹配

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配


#检索和替换
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)

class test1:
    a = 0;
    def __init__(self,aa):
        print(aa)
    def initA(self):
        test1.a = 1;
    def getA(self):
        return test1.a;    
t1 = test1(None);
t1.initA()
print (test1.a)
print (t1.getA())