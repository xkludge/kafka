import json
import faust
from typing import Dict, List, Mapping

#{"key": "value", "key1": "value", "keyList": [0,1,3,4]}
#{"data": {"skillId": "173", "questionID": "557", "userAnswer": "Main follow position world.", "wasCorrect": "false", "timezooneOffset": 300, "respTime": "167", "hintID": "-1", "hwID": "0", 
#"ownersIDs": ["12345", "42195"], "timestamp": 1545363876.6810524, "chances": [{"chance": "1", "userAnswer": ["b"], "wasCorrect": "false", "respTime": "5"}


# [^-Agent*: __main__.hello]: Crashed reason=ValueDecodeError("__init__() missing 11 required positional arguments: 
# 'skillId', 'questionID', 'userAnswer', 'wasCorrect', 'timezooneOffset', 'respTime', 'hintID', 'hwID', 'owernersIDs', 'timestamp', and 'chances'",)

class Chance(faust.Record):
    chance: int
    wasCorrect: bool
    userAnswer: List[str]
    respTime: int


class Answer(faust.Record):
    skillId: int
    questionID: int
    userAnswer: str
    wasCorrect: bool
    timezooneOffset: int
    respTime: int
    hintID: str
    hwID: str
    ownersIDs: List[str]
    timestamp: str
    chances: List[Chance]
    schoolID: str



app = faust.App('test_stream', broker='kafka://kafka:9092')
topic = app.topic('test_topic', value_type=Answer)

@app.agent(topic)
async def hello(stream):
    print('Connected....')
    print(stream)
    async for payload in stream:
        print('processing..')
        print(payload)
        print('finished...')


if __name__ == '__main__':
    app.main()
