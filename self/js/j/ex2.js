// 엄격 모드 -> 모던 방식 실행 -> 적용시 취소 불가
"use strict";
let a = 45;
console.log(a)

let message = 'Hello!'; // 변수를 정의하고 값을 할당합니다.
alert(message); // Hello!
// 한줄에 여러변수 할당 가능
let user = 'John', age = 25, message1 = 'Hello';

let x = 10; // 전역 변수

function showX() {
  console.log(x); // x에 접근 가능
}

showX(); // 10 출력