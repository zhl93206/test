import pymysql


class MySQLUtils:

    conn = ""
    url = "localhost"
    user = "root"
    pwd = "123456"
    db_name = "crm"

    def __init__(self):
        try:
            self.conn = pymysql.Connect(self.url,self.user,self.pwd,self.db_name);
        except:
            print("连接数据库失败！请检查链接字符串")

    def query_all(self,expr="",tname=""):
        if tname:
            try:
                cursor = self.conn.cursor()
                if expr:
                    sql = "SELECT *FROM"+tname+"where"+str(expr)
                    cursor.execute(sql)
                    return cursor.arraysize()
                else:
                    sql = "SELECT *FROM"+tname
                    cursor.execute(sql)
                    return cursor.arraysize()
            except:
                print(self.db_name+"中没有找到表"+tname)
        else:
            print("没有表名")
        cursor.close()
        self.conn.close()

    # #删除数据
    def delete_data(self,expr="",tname=""):
        if expr:
            sql = "DELETE FROM"+str(tname)+"WHERE"+expr
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()

    # #修改数据
    def update_data(self,expr1="",expr2="",tname=""):
        cursor = self.conn.cursor();
        sql = "UPDATE"+tname+"SET "+expr1+"WHERE"+expr2
        cursor.execute(sql)
        cursor.close()
        self.conn.close()

    # #添加数据
    def insert_data(self,tname=""):
        sql = "INSERT"+tname+"VALUES()"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.close()
        self.conn.close()





