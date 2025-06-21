const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// 미들웨어
app.use(cors());
app.use(bodyParser.json());

// 주문 저장용 (메모리)
let orders = [];

app.post('/api/order', (req, res) => {
  const { items, total } = req.body;

  if (!items || !total) {
    return res.status(400).json({ message: '항목과 총합을 보내주세요.' });
  }

  const order = {
    id: Date.now(),
    items,
    total,
    date: new Date().toISOString(),
  };

  orders.push(order);
  console.log('새 주문:', order);

  res.json({ message: '주문이 완료되었습니다!', orderId: order.id });
});

// 주문 전체 확인 (디버그용)
app.get('/api/orders', (req, res) => {
  res.json(orders);
});

app.listen(PORT, () => {
  console.log(`✅ 주문 서버 실행 중: http://localhost:${PORT}`);
});