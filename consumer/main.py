from kafka import KafkaConsumer

def worker():
    print("starting worker..")
    consumer = KafkaConsumer(
        'test_topic',
        bootstrap_servers=['kafka:9092'],
        group_id="super_group")
    print("Connected..")
    for msg in consumer:
        print("reading msg")
        print (msg)
        print (msg['value'])
        print("finished msg")

    print("Ooops")


if __name__ == "__main__":
    worker()
