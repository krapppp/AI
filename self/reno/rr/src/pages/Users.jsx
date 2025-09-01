import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // 백엔드 서버에서 사용자 목록 가져오기
    axios.get('http://localhost:5000/users')
      .then((res) => {
        setUsers(res.data);
      })
      .catch((err) => {
        console.error('데이터 불러오기 실패:', err);
      });
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>사용자 목록</h1>
      <ul>
        {users.length > 0 ? (
          users.map((user, index) => (
            <li key={index}>
              <strong>ID:</strong> {user.ID || user.id}, <strong>이름:</strong> {user.NAME || user.name}
            </li>
          ))
        ) : (
          <p>불러올 데이터가 없습니다.</p>
        )}
      </ul>

      <nav style={{ marginTop: '1rem' }}>
        <Link to="/" style={{ textDecoration: 'none', color: 'green' }}>
          ⬅ 홈으로
        </Link>
      </nav>
    </div>
  );
}

export default Users;
