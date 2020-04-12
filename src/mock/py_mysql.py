import pymysql

student = input("输入你想要获取的学生的名字：")
score = eval(input("输入你想要获取的学生的分数："))

#连接mysql数据库
conn = pymysql.connect(host='localhost',port=3306,database='lb',user='root',password='990509Leibo',charset='utf8')
cursor = conn.cursor()

sql1="update luquxibao set td_score={2} where name='{0}' and td_score={1};".format(student,score,score+1)

cursor.execute(sql1)
conn.commit()

sql2 = 'select * from luquxibao where td_score={0}'.format(score+1)
cursor.execute(sql2)

data = cursor.fetchall()
print(data)

cursor.close()
conn.close()
#创建数据库操作的对象
# class luquxibao():
#     def __init__(self,host,port,user,password,db,charset):
#         self.host = host
#         self.port = port
#         self.user = user
#         self.password = password
#         self.db = db
#         self.charset = charset

#     def connectLuquxibao(self):
#         conn = pymysql.connect(host=self.host,port=self.port,database=self.db,password=self.password,user=self.user,charset=self.charset)
#         return conn
    
#     def sqlLuquxibao(self):
#         conn = self.connectLuquxibao()
#         cursor = conn.cursor()
#         sql = 'select * from luquxibao;'
#         cursor.execute(sql)
#         data = cursor.fetchone()
#         print(data)
#         cursor.close()
#         conn.close()

#     def run(self):
#         self.sqlLuquxibao()

# if __name__ == "__main__":
#     host = 'localhost'
#     port = 3306
#     user = 'root'
#     password = '990509Leibo'
#     db = 'lb'
#     charset = 'utf8'
#     mysql_connect = luquxibao(host,port,user,password,db,charset)
#     mysql_connect.run()
