alert("JavaScript Again!")

// ; 작성시 같은 줄에 코드 작동 o
// alert('Hello'); alert('World');

// alert('Hello');
// alert('World');

// 줄바꿈 시 ; 생략 가능 (암시적)
alert('Hello')
alert('World')

// ; 생략 시 연산가능 여부
alert(3 +
1
+ 2);

// 코드 실행 x -> [] 앞 ; 자동 생성 작동 x
// [1, 2].forEach(alert)

// alert("에러가 발생합니다.")
// [1, 2].forEach(alert)

alert("제대로 동작합니다.");
[1, 2].forEach(alert)