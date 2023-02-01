from clickhouse_driver import Client

# conn=connect('clickhouse://default:ck@12345@172.20.8.110:32003/default')
# cursor = conn.cursor()
# data = cursor.execute('select * from p_6379846728438255616.d_6388571533542952960 order by id limit 20, 10;')
# print(data)

host='172.20.8.110'

client = Client(host=host, port=32654,database='default',password='ck@12345')
sql = 'select * from p_6379846728438255616.d_6388571533542952960 order by id limit 20, 10;'
res = client.execute(sql)
print(res)