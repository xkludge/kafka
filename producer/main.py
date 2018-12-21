import time
import json
import random
from kafka import KafkaProducer
from faker import Faker

def randBool():
    if random.randint(0,1000) % 2 == 0:
        return "true"
    return "false"


def factoryAnswer(userId):
    fake = Faker()
    return {
            "skillId": str(random.randint(100,200)),
            "questionID": str(random.randint(200,1000)),
            "userAnswer": fake.sentence(),
            "wasCorrect": randBool(),
            "timezooneOffset": 300,
            "respTime": str(random.randint(5,500)),
            "hintID": "-1",
            "hwID": "0",
            "ownersIDs": ["12345","42195"],
            "timestamp": time.time(),
            "chances": [{
              "chance": "1",
              "userAnswer": ["b"],
              "wasCorrect": "false",
              "respTime": "5",
            }],
            "userID": userId,
            "schoolID": "123",
    }


def worker():
    print("starting worker..")
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    print("Connected..")

    usersId = ['123','345','678',
                '789', '123','345',
                '678','789', '123',
                '345','678','789',
                '123','345','678',
                '789', '123','345',
                '678','789']
    for uId in usersId:
        print("sending msg")
        msg = factoryAnswer(uId)
        print (msg)
        producer.send('test_topic', json.dumps(msg).encode('utf-8'))
        #producer.send('test_topic', msg)
        print("finished send msg")

    print("Done")


if __name__ == "__main__":
    worker()
