-- 1. 먼저 계정(myuser)로 로그인했다고 가정

-- 2. 테이블 생성
CREATE TABLE users (
  id NUMBER PRIMARY KEY,
  name VARCHAR2(100) NOT NULL
);

CREATE SEQUENCE users_seq
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE OR REPLACE TRIGGER users_trigger
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
  SELECT users_seq.NEXTVAL INTO :new.id FROM dual;
END;

SELECT * FROM v$version;
-- 3. 초기 데이터 삽입
INSERT INTO users (name) VALUES ('Alice');
INSERT INTO users (name) VALUES ('Bob');
INSERT INTO users (name) VALUES ('Charlie');

SELECT * FROM USERS u ;
