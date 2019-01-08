from http import client
import time

#level7 문제에 접속
conn = client.HTTPConnection('suninatas.com',80)
GET_headers={'Cookie': 'ASPSESSIONIDQQCQAAQS=MDOIJMNCGKDLIFAGHHECJICL'}
GET_url = '/Part_one/web07/web07.asp'
GET_body = ''    
conn.request('GET',GET_url,GET_body,GET_headers)
conn.close()

#YES버튼을 누른것과 같은 효과의 POST요청을 보냄
conn = client.HTTPConnection('suninatas.com',80)
POST_headers={'Content-Type': 'application/x-www-form-urlencoded',
              'Cookie': 'ASPSESSIONIDQQCQAAQS=MDOIJMNCGKDLIFAGHHECJICL'}
POST_url = '/Part_one/web07/web07_1.asp'
POST_body = 'web07=Do+U+Like+girls%3F'
conn.request('POST',POST_url,POST_body,POST_headers)

#마지막 POST요청의 결과값을 받아옴.
#문제에 접속하자마자 POST요청을 보냈으므로 인증키를 얻을 수 있다.
res=conn.getresponse()
resData=res.read()
strRes = str(resData)

print(strRes)

conn.close()
