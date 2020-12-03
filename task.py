import mysql.connector as m

def getConnection():
    connection=m.connect(host="localhost",user="root",password="aranattukara",port="3306",database="mytask_db")
    return connection
getConnection()


"""con=getConnection()
cursor=con.cursor()
cursor.execute("insert into product values(%s,%s,%s)",(5,"Xiomi",10000))
con.commit()
con.close()"""

#inserting records with the help of function.
"""def insert(pid,pname,price):
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("insert into product values(%s,%s,%s)", (pid,pname,price))
    con.commit()
    con.close()
insert(6,"Vivo",20000)"""

#Retreiving the records from database table.
con=getConnection()
cursor=con.cursor()
cursor.execute("select * from product")
table=cursor.fetchall()
print(table)
con.commit()
con.close()

#deleting record from table.
con = getConnection()
cursor = con.cursor()
cursor.execute("delete from product where pid=6")
con.commit()
con.close()

def update(pname,pid):
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("update product set pname=%s where pid=%s",(pname,pid))
    con.commit()
    con.close()
update("Vivo",4)
