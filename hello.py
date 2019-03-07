
print("hello world")
print("你好")

import random
# print random.randint(1,100)


import pymysql

conn = pymysql.connect()
cursor = conn.cursor()
cursor.execute()

result = cursor.fetchall()
for i in result:
    tmp = "%s,%s,%s" % (r[1],r[2],r[3])
    print(tmp)

print("查询完成！")
cursor.close()
conn.close()