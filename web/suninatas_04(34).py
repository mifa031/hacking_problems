from http import client
import time

conn = client.HTTPConnection('suninatas.com',80)

headers={'User-Agent' : 'SuNiNaTaS browser',
         'Content-Type': 'application/x-www-form-urlencoded',
         'Cookie': 'ASPSESSIONIDQQCSABRS=DOBFGEBDDNNNIBDNLJEIMFJI'}
url='/Part_one/web04/web04_ck.asp'
body = ''     

conn.request('POST',url,body,headers)

conn.close()
