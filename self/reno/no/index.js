// npx nodemon index.js -> 서버 실행(수정 사항 반영 저장시 자동 서버 재실행)
// node index.js -> 서버 실행(1회성->저장 후 반영x)

const express = require('express');
const oracledb = require('oracledb');
const cors = require('cors');

// Oracle Client 경로 (oci.dll 위치 경로)
oracledb.initOracleClient({
  libDir: 'C:\\oraclexe\\app\\oracle\\product\\11.2.0\\server\\bin'
});

const app = express();
const PORT = 5000;
app.use(cors());

app.get('/users', async (req, res) => {
  try {
    const conn = await oracledb.getConnection({
      user: 'myuser',
      password: 'mypass',
      connectString: 'localhost:1521/XE'
    });

    const result = await conn.execute(`SELECT * FROM users`);
    console.log('🟢 DB 응답:', result.rows);

    await conn.close();
    res.json(result.rows.map((row) => ({
      ID: row[0],
      NAME: row[1]
    })));

  } catch (err) {
    console.error('🔴 에러 발생:', err);
    res.status(500).send('DB 오류');
  }
});

app.listen(PORT, () => {
    console.log(`백엔드 서버 실행 중: http://localhost:${PORT}`);
});

// async function connectDB() {
    //   try {
        //     const conn = await oracledb.getConnection({
            //       user: 'myuser',
            //       password: 'mypass',
            //       connectString: 'localhost:1521/XE'
//     });

//     const result = await conn.execute(`SELECT * FROM users`);
//     console.log(result.rows);

//     await conn.close();
//   } catch (err) {
    //     console.error('DB 연결 실패:', err);
    //   }
    // }
    // connectDB();