import pymysql
import sys;
# pymysql.install_as_MySQLdb()
# import MySQLdb
defaultDBconfig = {
                'host':'127.0.0.1',
                'port':3306,
                'user':'root',
                'password':'root',
                'db':'test',
                'charset':'utf8mb4',
                'cursorclass':pymysql.cursors.DictCursor
                   }

class mysqlUtil:
#     conn = pymysql.connect("localhost","root","root","test")
    conn = None #连接
    cursor = None #游标
    def __init__(self,dbconfig):
        if dbconfig is not None:
            mysqlUtil.initDBconnection(dbconfig);
        else :
            mysqlUtil.initDBconnection(defaultDBconfig)
            
    #实例方法
    def getConnection(self):
        return mysqlUtil.conn;
    
    def getCursor(self):
        if mysqlUtil.cursor is None :
            mysqlUtil.cursor = mysqlUtil.conn.cursor();
        return mysqlUtil.cursor
    #静态方法
    @staticmethod
    def initDBconnection(config):
        if mysqlUtil.conn is None:
            mysqlUtil.conn = pymysql.connect(**config)
            
    @staticmethod
    def initDBcursor():
        mysqlUtil.initDBconnection(defaultDBconfig)
        if mysqlUtil.cursor is None :
            mysqlUtil.cursor = mysqlUtil.conn.cursor();
    
    @staticmethod
    def getDBConnection():
        mysqlUtil.initDBconnection(defaultDBconfig)
        return mysqlUtil.conn;
    
    @staticmethod
    def getDBCursor():
        mysqlUtil.initDBcursor()
        return mysqlUtil.cursor 
    
    @staticmethod
    def close():
        if mysqlUtil.cursor is not None :
            mysqlUtil.cursor.close()
        if mysqlUtil.conn is not None :
            mysqlUtil.conn.close()
        print ("db closed ...")

my = mysqlUtil(None)    
print (mysqlUtil.conn)
print (my.getConnection())
print (my.getCursor())
print (mysqlUtil.getDBConnection())

conn = mysqlUtil.getDBConnection()
mycursor = mysqlUtil.getDBCursor();
sql = 'SELECT * from user'
print (mycursor)
try:
    # 使用execute方法执行SQL语句
    # mycursor.execute("SELECT VERSION()")
    mycursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据库。
    data = mycursor.fetchone()
    data = mycursor.fetchall()

    print ("Database datas : %s " % data[1])
    conn.commit()
    raise Exception("db exception")
except Exception:
    print (sys.exc_info()[0],sys.exc_info()[1])
    conn.rollback()

mysqlUtil.close()


# SQL 插入语句
sql1 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
# SQL 更新语句
sql2 = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')