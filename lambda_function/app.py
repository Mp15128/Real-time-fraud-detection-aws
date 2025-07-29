import json

def lambda_handler(event, context):
    fraud_events = []

    for record in event['Records']:
        # Kinesis data is base64 encoded → decode to string
        payload = json.loads(record['kinesis']['data'])

        user_id = payload['user_id']
        amount = payload['amount']
        location = payload['location']
        is_fraud_flag = False

        # Simple fraud detection logic:
        if amount > 1000:
            is_fraud_flag = True
        if location not in ['NY', 'CA', 'TX', 'MO', 'IL']:
            is_fraud_flag = True

        result = {
            "user_id": user_id,
            "amount": amount,
            "location": location,
            "is_fraud": is_fraud_flag,
            "original_data": payload
        }

        if is_fraud_flag:
            fraud_events.append(result)

        print(f"[INFO] Processed: {result}")

    return {
        'statusCode': 200,
        'body': json.dumps({
            "message": "Processed transactions",
            "frauds_detected": len(fraud_events),
            "fraud_samples": fraud_events
        })
    }
