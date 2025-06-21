from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

orders = []

@app.route('/order', methods=['POST'])
def receive_order():
    data = request.get_json()
    if not data or 'items' not in data or 'total' not in data or 'customerName' not in data:
        return jsonify({'message': '잘못된 요청입니다.'}), 400

    order_id = int(datetime.now().timestamp() * 1000)
    order_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    order = {
        'id': order_id,
        'customerName': data['customerName'],
        'items': data['items'],
        'total': data['total'],
        'timestamp': order_time
    }

    orders.append(order)

    print("="*40)
    print(f"🛒 새 주문 수신 - 주문번호: {order_id}")
    print(f"시간: {order_time}")
    print(f"이름: {data['customerName']}")
    print("주문 항목:")
    for item in data['items']:
        print(f" - {item['name']} x {item['count']}개 (₩{item['price']:,} each)")
    print(f"총합: ₩{data['total']:,}")
    print("="*40)

    return jsonify({'message': '주문이 완료되었습니다!', 'orderId': order_id}), 200

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)