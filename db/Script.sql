SELECT sysdate FROM dual;

-- 전체 직원 조회
SELECT * FROM employees;

-- 전체 직원 조회(자동완성 : ctrl + space bar)
SELECT * FROM EMPLOYEES e ;

-- 회사 모든 부서, 부서명, 부서장 조회
SELECT * FROM DEPARTMENTS d ;

SELECT employee_id, first_name, last_name
FROM EMPLOYEES e ;

-- 사원 이름, 전화번호, 입사일, 연봉
SELECT e.FIRST_NAME,
e.PHONE_NUMBER,
e.HIRE_DATE,
e.SALARY
FROM EMPLOYEES e ;

-- 사원 이름, 전화번호, 입사일, 연봉
SELECT e.FIRST_NAME,
e.LAST_NAME ,
e.SALARY,
e.EMAIL,
e.PHONE_NUMBER,
e.HIRE_DATE
FROM EMPLOYEES e ;

-- 사원번호, 이름, 성, 급여, 전화번호, 이메일, 입사일로 변경
SELECT e.FIRST_NAME "이름",
e.LAST_NAME "성",
e.SALARY "연봉",
e.EMAIL "이메일",
e.PHONE_NUMBER "전화번호",
e.HIRE_DATE "입사일"
FROM EMPLOYEES e ;

-- 글자 합친 후 사이 공백 넣기
SELECT first_name ||' '|| last_name
FROM EMPLOYEES e ;

-- concat : 문자열 합침(인자 2개) -> 1개 문자열로 반환
SELECT concat(first_name,concat(' ',last_name))
FROM employees;

-- 글자 합친 후 사이 공백 넣기
SELECT first_name ||' hire date is '|| hire_date
FROM EMPLOYEES e ;

-- 전체직원 정보 출력
SELECT first_name ||' - '|| last_name "성명",
salary "급여",
salary*12 "연봉",
salary*12+5000 "연봉2",
phone_number "전화번호"
FROM EMPLOYEES e ;

--------------------------------------------------------------0630

SELECT first_name
FROM EMPLOYEES e
WHERE e.DEPARTMENT_ID = 10;

-- 급여 15000 이상 사원들 이름,급여,연봉
SELECT first_name, salary, salary*12
FROM EMPLOYEES e 
WHERE e.SALARY >= 15000; 

-- 07/01/01 이후 입사한 사원 이름, 입사일
SELECT first_name, hire_date
FROM EMPLOYEES e
WHERE e.HIRE_DATE >= '2007/01/01';

-- Lex 직원 연봉
SELECT first_name, salary*12
FROM EMPLOYEES e
WHERE e.FIRST_NAME like 'Lex';

-- 급여가14000 이상 17000이하인 사원의 이름,연봉
select first_name, salary
 from employees
 where salary >= 14000 
and salary <= 17000;

-- 연봉이 14000 이하이거나 17000 이상인 사원의 이름, 연봉
SELECT first_name, salary, salary*12 "조건검증"
FROM EMPLOYEES e 
WHERE e.SALARY*12 >= 14000 or e.SALARY*12 <=17000;

-- 입사일이04/01/01 에서 05/12/31 사이에 입사한 사원의 이름, 입사일
SELECT first_name,
		hire_date
FROM EMPLOYEES e 
WHERE e.HIRE_DATE >= '2004/01/01'
and e.HIRE_DATE <= '2005/12/31'
ORDER BY e.HIRE_DATE asc;

-- 연봉이14000 이상 17000이하인 사원의 이름, 연봉(between:값 포함, 느린 연산)
select first_name, salary
 from employees
 where salary between 14000 and 17000;

-- 연봉이14000 이상 17000이하인 사원의 이름, 연봉
select first_name, salary
 from employees
 where salary >= 14000 
and salary <= 17000;

-- 여러 조건 검색
select first_name, last_name, salary
 from employees
 where first_name in ('Neena', 'Lex', 'John');

-- 급여가 2100, 3100, 4100, 5100 인 사원의 이름과 급여
select FIRST_NAME, SALARY
 from employees
 where salary in (2100, 3100, 4100, 5100);

-- 유사 단어 검색
select first_name, last_name, salary
 from employees
 where first_name like 'L%';

-- 이름에 am 포함한 사원의 이름, 연봉
select first_name, salary*12
 from employees
 where first_name like '%am%';

-- 이름의 두번째 글자가 a인 사원의 이름, 연봉
select first_name, salary*12
 from employees
 where first_name like '_a%';

-- 이름의 네번째 글자가 a인 사원의 이름
SELECT first_name
FROM EMPLOYEES e 
WHERE first_name LIKE '___a%';

-- 이름이 4글자인 사원 중 끝에서 두번째 글자가 a인 사원의 이름
SELECT first_name
FROM EMPLOYEES e 
WHERE first_name LIKE '__a_';

-- null
 select first_name, salary, commission_pct, salary*commission_pct
 from employees;

-- 커미션 비율이 있는 사원의 이름, 연봉 커미션비율
 select first_name, salary, commission_pct*salary*12
 from employees
 where commission_pct is NOT null;

-- 담당 매니저가 없고 커미션비율이 없는 직원의 이름
select first_name
 from employees
 where commission_pct is NULL AND MANAGER_ID IS null;
SELECT * FROM EMPLOYEES e ;

-- order by 절을 사용
select first_name, salary
 from employees
 order by salary desc;

-- 부서번호 기준 오름차순 정렬 / 부서번호, 급여, 이름
select DEPARTMENT_ID, salary, first_name || ' ' || last_name
 from employees
 order by DEPARTMENT_ID asc;

SELECT * FROM EMPLOYEES e ;

-- 급여가 5000 이상인 직원의 이름, 급여 / 급여 큰직원부터
select  first_name || ' ' || last_name, salary
 from employees
 WHERE SALARY  >= 5000
 order by salary desc;

----------------------------------------------------------------------------0701오전

-- 부서번호를 오름차순으로 정렬하고 부서번호가 같으면 급여가 높은사람부터 / 부서번호, 급여, 이름
select  department_id, salary, first_name || ' ' || last_name
 from employees
 WHERE SALARY  >= 5000
 order BY department_id ASC, salary DESC;

SELECT chr(65)
FROM dual;

SELECT ascii('s') FROM dual;

SELECT initcap('adfg') FROM dual;

select email, initcap(email), department_id, first_name, lower(first_name), upper(first_name), first_name, substr(first_name,1,3), substr(first_name,-3,2)
 from employees
 where department_id = 100;

select first_name, 
lpad(first_name,10,'*'), 
lpad('pfqojfdnag456',10,'*'), 
rpad('pfqojfdnag456',10,'*'), 
rpad(first_name,10,'*')
 from employees;

select first_name, 
replace(first_name, 'a', '*') 
from employees
 where department_id =100;

select first_name, 
replace(first_name, 'a', '*'), 
replace(first_name, substr(first_name, 2, 3), '***')
 from employees
 where department_id =100;

SELECT sign(-1294) FROM dual;

select round(123.346, 2) "r2",
 round(123.456, 0) "r0",
 round(123.456, -1) "r-1",
 round(123.456, -2)
 from dual;

select trunc(123.346, 2) "r2",
 trunc(123.456, 0) "r0",
 trunc(129.456, -1) "r-1"
 from dual;

SELECT MONTHS_BETWEEN ('1995.09.01','1994.01.11') FROM dual;

select months_between(sysdate, hire_date) 
from employees
 where department_id = 110;

SELECT MONTHS_BETWEEN(sysdate, '1000.01.01') FROM dual;

SELECT to_char(9876, '0000000999999') FROM dual;

 select first_name, to_char(salary*12, '$999,999.99') "SAL"
 from employees
 where department_id =110;
 
 select sysdate, 
to_char(sysdate, 'YYYY-MM-DD HH24:MI:SS')
 from dual;
 
 select commission_pct, nvl(commission_pct, 0)
 from employees;
 
 select commission_pct, nvl2(commission_pct, 100, 0)
 from employees;
 
 -- 담당 매니저o, 커미션x, 월급 3000 초과 인원의 이름, 매니저아이디, 커미션비율, 월급
 SELECT first_name, manager_id, COMMISSION_PCT, salary
 FROM EMPLOYEES e 
 WHERE e.MANAGER_ID IS NOT NULL AND e.COMMISSION_PCT IS NULL AND e.SALARY > 3000;
 
 SELECT j.JOB_TITLE , j.MAX_SALARY 
 FROM JOBS j 
 WHERE j.MAX_SALARY >= 10000
 ORDER BY max_salary DESC;

 SELECT max(salary), min(salary), max(salary)-min(salary) "최고임금-최저임금"
 FROM EMPLOYEES e ;
 
 SELECT count(salary), count(commission_pct) FROM EMPLOYEES e ;
 
 SELECT sum(salary),avg(salary),max(salary),min(salary) FROM EMPLOYEES e ;

 select department_id, salary
 from employees
 order by department_id asc;
 
 -- 부서별 평균 급여
 select department_id, avg(salary), max(salary), min(salary)
 from employees
 group by department_id
 order by department_id ASC;
 
 SELECT salary, count(department_id), count(first_name)
 FROM EMPLOYEES e 
 GROUP BY e.SALARY 
 ORDER BY e.SALARY DESC;
 
  ---------------------------과제
  -- 마지막 신입 사원 들어온 날 언제?
 SELECT to_char(max(hire_date), 'YYYY"년 "MM"월 "DD"일"') "입사일"
 FROM EMPLOYEES e ;

 -----------------------------------------------------------------------------0701오후

 SELECT e.DEPARTMENT_ID  , avg(salary), max(salary), min(salary)
 FROM EMPLOYEES e 
 GROUP BY e.DEPARTMENT_ID 
 ORDER BY e.DEPARTMENT_ID DESC;
 
 SELECT e.JOB_ID , max(salary), min(salary)
 FROM EMPLOYEES e 
 GROUP BY e.JOB_ID 
 ORDER BY e.JOB_ID DESC;
 
 SELECT to_char(min(hire_date),'yyyy"년" mm"월" dd"일"') FROM employees;
 
 SELECT department_id,sum(salary)
 FROM employees
 GROUP BY department_id
 HAVING sum(salary) > 20000;

SELECT department_id, count(job_id)
 FROM employees
 GROUP BY department_id;

select department_id, count(*), sum(salary)
 from employees
 group by department_id
 having sum(salary) > 20000;

-- 평균임금 최저임금 차이 2000 미만 부서의 부서아이디,평균임금,최저임금,(평균-최저) 출력/ (평균-최저)내림차순 정렬
SELECT department_id,avg(salary),min(salary),(avg(salary)-min(salary)) "차이"
FROM EMPLOYEES e 
GROUP BY department_id
HAVING (avg(salary)-min(salary)) < 2000
ORDER BY "차이" DESC;

-- 업무별 최고임금-최저임금 차이, 내림차순 정렬
SELECT job_id,max(salary)-min(salary)
FROM EMPLOYEES e  
GROUP BY e.JOB_ID 
ORDER BY max(salary)-min(salary) DESC;

SELECT employee_id, 
		salary,
 CASE WHEN job_id = 'AC_ACCOUNT' THEN salary + salary * 0.1
 WHEN job_id = 'AC_MGR' THEN salary + salary *0.2
 ELSE salary
 END job_id
FROM employees;

-- 직원의 이름, 부서, 팀을 출력하세요 팀은 부서코드로 결정하며 부서코드가10~50 이면‘A-TEAM’
-- 60~100이면 ‘B-TEAM’  110~150이면 ‘C-TEAM’ 나머지는 ‘팀없음’ 으로 출력
 SELECT first_name, department_id,
 	CASE
	 	WHEN department_id BETWEEN 10 AND 50 THEN 'A-TEAM'
	 	WHEN department_id BETWEEN 60 AND 100 THEN 'B-team'
	 	WHEN department_id BETWEEN 110 AND 150 THEN 'C-team'
	 	ELSE '팀없음'
 	END AS 팀
 FROM EMPLOYEES e ;

select first_name, department_name
 from employees, departments;

select first_name, em.department_id, 
department_name, de.department_id
 from   employees em, departments de
 where  em.department_id = de.department_id;

select * FROM employees;
select * FROM DEPARTMENTS d ;

SELECT e.FIRST_NAME || ' ' || e.LAST_NAME AS 이름, j.JOB_TITLE , j.JOB_ID
FROM EMPLOYEES e , jobs j
where  e.JOB_ID = j.JOB_ID;

SELECT e.FIRST_NAME || ' ' || e.LAST_NAME, d.DEPARTMENT_ID, j.JOB_TITLE 
FROM EMPLOYEES e , DEPARTMENTS d , JOBS j 
WHERE e.JOB_ID = j.JOB_ID and e.DEPARTMENT_ID = d.DEPARTMENT_ID;

SELECT 
  e.FIRST_NAME || ' ' || e.LAST_NAME AS 이름,
  d.DEPARTMENT_ID,
  j.JOB_TITLE
FROM EMPLOYEES e
LEFT JOIN DEPARTMENTS d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
JOIN JOBS j ON e.JOB_ID = j.JOB_ID;

 -----------------------------------------------------------------0702오전

SELECT e.first_name, m.FIRST_name
FROM employees e, employees m
WHERE e.manager_id = m.employee_id;

-- Right outer join / 오라클 방식 : (+)
select e.department_id, e.first_name, d.department_name
 from employees e right outer join departments d
 on e.department_id = d.department_id ;

select e.department_id, e.first_name, d.department_name
 from employees e, departments d
 where e.department_id(+) = d.department_id ; 

-- Left outer join / 오라클 방식 : (+)
select e.department_id, e.first_name, d.department_name
 from employees e left outer join departments d
 on e.department_id = d.department_id ;

select e.department_id, e.first_name, d.department_name
 from employees e, departments d
 where e.department_id = d.department_id(+) ; 

-- Full outer join
select e.department_id, e.first_name, d.department_name
 from employees e full outer join departments d
 on e.department_id = d.department_id ;

-- self join 예시
SELECT 
  e.first_name AS 직원이름,
  m.first_name AS 상사이름
FROM employees e
LEFT JOIN employees m
  ON e.manager_id = m.employee_id;

-- 각 사원에 대한 사번,이름,부서명,매니저 이름 조회
SELECT e.employee_id, e.FIRST_NAME, d.DEPARTMENT_NAME, e.MANAGER_ID, m.FIRST_NAME
FROM EMPLOYEES e
LEFT JOIN DEPARTMENTS d ON d.DEPARTMENT_ID = e.DEPARTMENT_ID 
JOIN EMPLOYEES m ON e.manager_id = m.employee_id;

SELECT 
  e.employee_id AS 사번,
  e.first_name AS 이름,
  d.department_name AS 부서명,
  m.first_name AS 매니저이름
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN employees m ON e.manager_id = m.employee_id;

SELECT 
  e.employee_id, 
  e.first_name, 
  d.department_name, 
  e.manager_id, 
  m.first_name AS manager_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN employees m ON e.manager_id = m.employee_id;

-- 지역에 속한 지역이름, 나라이름 출력 / 지역이름,나라이름 순서대로 내림차순
SELECT * FROM LOCATIONS l ;
SELECT * FROM COUNTRIES c  ;
SELECT * FROM regions r  ;
SELECT * FROM EMPLOYEES e ;
SELECT * FROM jobs j ;
SELECT * FROM JOB_HISTORY jh  ;

SELECT r.region_name,c.country_name
FROM REGIONS r, COUNTRIES c
WHERE c.REGION_ID = r.REGION_ID
ORDER BY region_name desc, country_name desc;

SELECT * FROM jobs;
SELECT e.FIRST_NAME , e.EMPLOYEE_ID 
FROM JOB_HISTORY jh,employees e 
JOIN jobs j ON e.JOB_ID = j.JOB_ID 
WHERE jh.job_id='AC_ACCOUNT';

-- public accountant 직책으로 과거 근무 이력 있는 모든 사원 이름, 사번 출력/현재는 x
SELECT e.FIRST_NAME , e.EMPLOYEE_ID, j.JOB_TITLE
FROM employees e 
JOIN JOB_HISTORY jh ON e.EMPLOYEE_ID = jh.EMPLOYEE_ID
JOIN JOBS j ON jh.JOB_ID = j.JOB_ID
WHERE jh.job_id='AC_ACCOUNT';

SELECT e.first_name, e.employee_id
FROM employees e
JOIN job_history jh ON e.employee_id = jh.employee_id
WHERE jh.job_id = 'AC_ACCOUNT'
  AND e.job_id != 'AC_ACCOUNT';

SELECT e.EMPLOYEE_ID ,
       e.FIRST_NAME || ' ' || e.LAST_NAME name
FROM hr.JOB_HISTORY jh, 
     hr.EMPLOYEES e , 
     hr.JOBS j 
WHERE jh.EMPLOYEE_ID = e.EMPLOYEE_ID 
AND   jh.JOB_ID = j.JOB_ID 
AND   j.JOB_TITLE = 'Public Accountant';

-- 과제 : 각 사원의 사번, 이름, 부서명, 직속상관 이름, 부서장 이름 조회
-- employees e, department d, employee m

SELECT * FROM EMPLOYEES e ;
SELECT * FROM DEPARTMENTS d ;
SELECT * FROM employees m;

SELECT d.MANAGER_ID , md. FIRST_NAME 
FROM DEPARTMENTS d , EMPLOYEES md
WHERE d.MANAGER_ID = md.EMPLOYEE_ID;

SELECT 
  e.employee_id     AS "사번",
  e.first_name      AS "사원이름",
  d.department_name AS "부서명",
  m.first_name      AS "직속상관",
  md.first_name     AS "부서장"
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
JOIN departments d ON e.department_id = d.department_id
JOIN employees md ON d.manager_id = md.employee_id
ORDER BY employee_id asc;


SELECT e.employee_id "사번",e.FIRST_NAME "사원이름", m.FIRST_NAME "직속상관", md.first_name "부서장"
FROM employees e, employees m, employees md, DEPARTMENTS d
WHERE e.MANAGER_ID = m.EMPLOYEE_ID
	AND m.DEPARTMENT_ID = d.DEPARTMENT_ID
	AND e.MANAGER_ID = md.EMPLOYEE_ID
	AND d.MANAGER_ID = md.EMPLOYEE_ID;

SELECT e.employee_id "사번",e.FIRST_NAME "사원이름", m.FIRST_NAME "직속상관", e.DEPARTMENT_ID "부서장"
FROM employees e, employees m, employees md
LEFT JOIN DEPARTMENTS d ON d.MANAGER_ID = md.EMPLOYEE_ID
WHERE e.MANAGER_ID = m.EMPLOYEE_ID
	AND m.DEPARTMENT_ID = d.DEPARTMENT_ID
	AND e.MANAGER_ID = md.EMPLOYEE_ID;


SELECT e.EMPLOYEE_ID , e.FIRST_NAME , d.DEPARTMENT_NAME    
FROM EMPLOYEES e JOIN DEPARTMENTS d ON e.EMPLOYEE_ID = d.MANAGER_ID
WHERE e.DEPARTMENT_ID = d.DEPARTMENT_ID ;

SELECT e.EMPLOYEE_ID "사번", e.first_name "이름", d.DEPARTMENT_name "부서명", m.FIRST_NAME "직속상관", dm. first_name "부서장"
FROM employees e, departments d, employees m, employees dm 
WHERE e.department_id=d.department_id
AND e.manager_id=m.employee_id
AND d.manager_id=dm.employee_id;

------------------------------------------------------------------0702오후

 