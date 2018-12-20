from kafka import KafkaConsumer

def worker():
    print("starting worker..")
    consumer = KafkaConsumer(
        'test_topic',
        bootstrap_servers=['kafka:9092'],
        group_id="super_group")
    print("Connected")
    for msg in consumer:
        print (msg)

    print("end of world")


if __name__ == "__main__":
    worker()
