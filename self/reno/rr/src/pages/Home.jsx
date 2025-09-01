import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>홈 페이지</h1>
      <p>React + Node.js + Oracle 연동 프로젝트</p>

      <nav style={{ marginTop: '1rem' }}>
        <Link to="/users" style={{ textDecoration: 'none', color: 'blue' }}>
          👉 사용자 목록 보기
        </Link>
      </nav>
    </div>
  );
}

export default Home;
