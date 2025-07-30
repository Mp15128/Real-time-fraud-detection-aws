import time
import random
import json
from datetime import datetime

def generate_transaction():
    return {
        "transaction_id": random.randint(1000000000, 9999999999),
        "user_id": random.randint(1000, 1100),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "timestamp": datetime.utcnow().isoformat(),
        "location": random.choice(["New York", "California", "Texas", "Florida", "Illinois"]),
        "is_fraud": random.choices([0, 1], weights=[0.98, 0.02])[0]  # 2% fraud
    }

if __name__ == "__main__":
    while True:
        txn = generate_transaction()
        print(json.dumps(txn))  # Simulates real-time data stream
        time.sleep(1)  # 1 transaction per second


