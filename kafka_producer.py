
from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

products = ['Laptop','Phone','Tablet']
regions = ['North','South','East','West']

while True:
    data = {
        "order_id": random.randint(1000,9999),
        "timestamp": str(datetime.now()),
        "store_id": random.randint(1,10),
        "product": random.choice(products),
        "quantity": random.randint(1,5),
        "price": random.randint(100,1000),
        "region": random.choice(regions)
    }
    producer.send('smartgear_orders', data)
    time.sleep(2)
