import urllib.request as request
from bs4 import BeautifulSoup
import re
import MySQLdb
import os

#MySQL에 연결할 유저 비밀번호를 각자 입력하세요.
my_passwd = "비번입력"
url = "http://weather.naver.com/rgn/cityWetrMain.nhn"
req = request.urlopen(url)
soup = BeautifulSoup(req, "html.parser")

tbl_weather = soup.find(class_="tbl_weather tbl_today")
tbl_string = list(tbl_weather.stripped_strings)

city_weather = {}
for i in range(11) :
    city_weather[tbl_string[i*16+4] + tbl_string[i*16+5]] = " ".join(tbl_string[i*16+6:i*16+20])
city_weather[tbl_string[180]] = " ".join(tbl_string[181:196])

#연결 객체 conn. 연결된 데이터베이스를 동작시키는 역할
conn = MySQLdb.connect(user = 'root', passwd = my_passwd, host = 'localhost',
                       db = 'naver_weather', use_unicode=True, charset="utf8")
#커서 객체 cur. 실질적으로 데이터베이스에 SQL 문장을 수행하고,
#조회된 결과를 가져오는 역할
cur = conn.cursor()

#처음으로 테이블을 만들 때에는
#c_w_tbl이 이미 존재하는 테이블이 아니니 DROP TABLE 할 필요가 없다. 
cur.execute('DROP TABLE c_w_tbl')
cur.execute('''
CREATE TABLE c_w_tbl (
	city VARCHAR(15) PRIMARY KEY NOT NULL,
	weather VARCHAR(100) NOT NULL)
''')

for i, j in city_weather.items():
    cur.execute("INSERT INTO c_w_tbl(city,weather) VALUES(%s, %s)", (i,j))

cur.execute("INSERT INTO c_w_tbl(city,weather) VALUES('abcde', 'test')")
#변경 사항 커밋을 해줘야 합니다.
conn.commit()

cur.execute("SELECT * FROM c_w_tbl")
for row in cur.fetchall():
    print(row)
    

#작업 스케줄러로 실행시 출력되는 콘솔 창이 바로 꺼지지 않게.
os.system('pause')
