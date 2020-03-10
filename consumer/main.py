from kafka import KafkaConsumer

def worker():
    print("starting worker..")
    consumer = KafkaConsumer(
        'answers_stream',
        bootstrap_servers=['example_kafka:9092'],
        group_id="super_group")
    print("Connected..")
    for msg in consumer:
        print("reading msg")
        print (msg)
        print("finished msg")

    print("Ooops")


if __name__ == "__main__":
    worker()
