import oracledb

# Thin 모드 활성화
oracledb.init_oracle_client()  # 필요 없는 경우도 있음

# 접속
conn = oracledb.connect(
    user="hr",
    password="hr",
    dsn="localhost:1521/XE"  # 기본 Oracle XE 설정
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")

for row in cursor:
    print(row)

cursor.close()
conn.close()