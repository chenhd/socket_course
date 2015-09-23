import socket

HOST = '10.20.78.204'    
PORT = 80              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #?
s.connect((HOST, PORT))

send_data = '''GET /xampp/ HTTP/1.1
Host: 10.20.78.204
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8

'''

print repr(send_data)

s.send(send_data)
data = s.recv(10240)
s.close()

print '-' * 100
print data


