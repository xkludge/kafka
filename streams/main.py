from typing import List
import faust

#{"key": "value", "key1": "value", "keyList": [0,1,3,4]}

class Grade(faust.Record):
    grade: str
    score: int

class Topic(faust.Record):
    key: str
    key1: str
    keyList:  List[Grade]


app = faust.App('test_stream', broker='kafka://kafka:9092')
topic = app.topic('test_topic', value_type=Topic)

@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        print(f'Hello from {greeting.key1} to {greeting.keyList}')


if __name__ == '__main__':
    app.main()
