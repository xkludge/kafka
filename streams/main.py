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
    userID: str


app = faust.App('answers_stream', broker='kafka://kafka:9092',)

topic = app.topic('answers', value_type=Answer)
student_aggregate = app.Table('student_aggregate', default=int)
school_aggregate = app.Table('school_aggregate', default=int)
student_avg_response = app.Table('student_avg_response', default=int)
school_avg_response = app.Table('school_avg_response', default=int)
student_aggregate_wrong = app.Table('student_aggregate_wrong', default=int)
school_aggregate_wrong = app.Table('school_aggregate_wrong', default=int)

school_topic = app.topic('school_topic')
student_topic = app.topic('student_topic')

@app.agent(topic)
async def hello(stream):
    print('Connected....')
    print(stream)
    async for payload in stream:
        print('processing..')
        if payload.wasCorrect == 'true':
            student_aggregate[payload.userID] += 1
            school_aggregate[payload.schoolID] += 1
        else:
            student_aggregate_wrong[payload.userID] += 1
            school_aggregate_wrong[payload.schoolID] += 1

        student_avg_response[payload.userID] = (student_avg_response[payload.userID] + int(payload.respTime)) / 2
        school_avg_response[payload.schoolID]= (school_avg_response[payload.schoolID] + int(payload.respTime)) / 2

        print("uid: {}  total_correct: {} total_wrong: {}".format(
            payload.userID,
            student_aggregate[payload.userID],
            student_aggregate_wrong[payload.userID]))
        print("schoolId: {}  total_correct: {} total_wrong: {}".format(
            payload.schoolID,
            school_aggregate[payload.schoolID],
            school_aggregate_wrong[payload.schoolID]))
        print("avg Response: {}".format(student_avg_response[payload.userID]))

        await student_topic.send(value={
            'student_id': str(payload.userID),
            'total_correct': str(student_aggregate[payload.userID]),
            'total_wrong': str(student_aggregate_wrong[payload.userID]),
            'average_response_time': str(student_avg_response[payload.userID])
        })
        await school_topic.send(value={
            'school_id': str(payload.schoolID),
            'total_correct': str(school_aggregate[payload.schoolID]),
            'total_wrong': str(school_aggregate_wrong[payload.schoolID]),
            'average_response_time': str(school_avg_response[payload.schoolID])
        })

        print('finished...')


@app.page('/student/{userID}')
@app.table_route(table=student_aggregate, match_info='userID')
async def get_count(web, request, userID):
    return web.json({
        'hello': 'world',
    })


if __name__ == '__main__':
    app.main()
