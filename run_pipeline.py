import random
import uuid
import time
from datetime import datetime

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": random.randint(1000, 9999),
        "amount": round(random.uniform(10, 1000), 2),
        "timestamp": datetime.utcnow().isoformat(),
        "location": random.choice(["NY", "CA", "TX", "FL", "IL"]),
        "is_fraud": random.choice([True, False, False, False])
    }

def is_fraudulent(transaction):
    return transaction["is_fraud"] or transaction["amount"] > 900

def run():
    print("🚀 Real-Time Fraud Detection Started")
    while True:
        txn = generate_transaction()
        print("📦 Incoming:", txn)
        if is_fraudulent(txn):
            print("⚠️ Fraud Detected!", txn)
        time.sleep(1)  # simulate streaming delay

if __name__ == "__main__":
    run()
