import time
import json
import random
from kafka import KafkaProducer
from faker import Faker

def randBool():
    if random.randint(0,100) % 2 == 0:
        return "true"
    return "false"


def factoryAnswer(userId):
    fake = Faker()
    schools = ["123","456","789"]
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
            "schoolID": random.choice(schools),
    }


def worker():
    print("starting worker..")
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    print("Connected..")
    counter = 0

    users_id = ['123','345','678',
                '789', '123','345',
                '678','789', '123',
                '345','678','789',
                '123','345','678',
                '789', '123','345',
                '678','789']

    random.shuffle(users_id)

    start_time = time.time()
    for uId in users_id:
        print("sending msg")
        for _ in range(random.randint(1,50)):
            counter += 1
            msg = factoryAnswer(uId)
            print (msg)
            producer.send('answers', json.dumps(msg).encode('utf-8'))
            print("finished send msg")

    print("Sent {} in {} seconds".format(counter, time.time() - start_time))


if __name__ == "__main__":
    worker()
