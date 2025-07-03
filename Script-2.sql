DROP TABLE book;
CREATE TABLE book (
 book_id NUMBER(10),
 title VARCHAR2(100) NOT NULL,
 pubs VARCHAR2(100),
 pub_date DATE,
 author_id NUMBER(10),
 PRIMARY KEY(book_id),
 CONSTRAINT c_book_fk FOREIGN KEY (author_id)
 REFERENCES author(author_id)
 );
 
SELECT * FROM book ORDER BY book_id;
DELETE FROM book;

INSERT INTO book
 VALUES (seq_book_id.nextval, '우리들의 일그러진 영웅', '다림', '1998-02-22', 1);
INSERT INTO book
 VALUES (seq_book_id.nextval, '삼국지', '민음사', '2002-03-01', 1);
INSERT INTO book
 VALUES (seq_book_id.nextval, '토지', '마로니에북스', '2012-08-15', 2);
INSERT INTO book
 VALUES (seq_book_id.nextval, '유시민의 글쓰기 특강', '생각의길', '2015-04-01', 3);
INSERT INTO book
 VALUES (seq_book_id.nextval, '패션왕', '중앙북스(books)', '2012-02-22', 4);
INSERT INTO book
 VALUES (seq_book_id.nextval, '순정만화', '재미주의', '2011-08-03', 5);
INSERT INTO book
 VALUES (seq_book_id.nextval, '오직두사람', '문학동네', '2017-05-04', 6);
INSERT INTO book
 VALUES (seq_book_id.nextval, '26년', '재미주의', '2012-02-04', 5);

DROP SEQUENCE seq_book_id;
CREATE SEQUENCE seq_book_id
 INCREMENT BY 1
START WITH 1 ;

------------------------------

DROP TABLE author;
CREATE TABLE author (
 author_id NUMBER(10),
 author_name VARCHAR2(100) NOT NULL , 
 author_desc VARCHAR2(500),
 PRIMARY KEY(author_id)
 );

SELECT * FROM author;

INSERT INTO author
 VALUES (1, '박경리', '토지 작가');

INSERT INTO author( author_id, author_name )
 VALUES (2, '이문열' );

UPDATE author
 SET author_name = '기안84', 
author_desc = '웹툰작가, 태어난김에 세계일주' 
WHERE AUTHOR_ID = 1;

DELETE FROM author;
TRUNCATE TABLE author;

DROP SEQUENCE seq_author_id;
CREATE SEQUENCE seq_author_id
 INCREMENT BY 1
START WITH 1 ;

SELECT seq_author_id.nextval FROM dual;
SELECT seq_author_id.currval FROM dual;

INSERT INTO author
 VALUES (seq_author_id.nextval, '박경리', '경상남도 통영');

INSERT INTO author 
VALUES (seq_author_id.nextval, '이문열', '경북 영양');
INSERT INTO author 
VALUES (seq_author_id.nextval, '유시민', '17대 국회의원');
INSERT INTO author 
VALUES (seq_author_id.nextval, '기안84', '기안동에서 산 84년생');
INSERT INTO author 
VALUES (seq_author_id.nextval, '강풀', '온라인 만화가 1세대');
INSERT INTO author 
VALUES (seq_author_id.nextval, '김영하', '알쓸신잡');

SELECT b.BOOK_ID, b.TITLE, b.PUBS, b.PUB_DATE, b.AUTHOR_ID, a.AUTHOR_NAME, a.AUTHOR_DESC
FROM book b, author a
WHERE b.AUTHOR_ID = a.AUTHOR_ID 
ORDER BY b.BOOK_ID;

SELECT * FROM book;
SELECT * FROM author;

UPDATE author
 SET author_desc = '서울특별시' 
WHERE author_id = 5 ;

SELECT * FROM book b LEFT JOIN AUTHOR a ON b.AUTHOR_ID = a.AUTHOR_ID ORDER BY b.BOOK_ID;
SELECT * FROM AUTHOR a LEFT JOIN book b ON b.AUTHOR_ID = a.AUTHOR_ID ORDER BY b.BOOK_ID;