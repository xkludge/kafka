# kafka

kafka playground

## How to run

Open two shell Terminal's, one for commands one for logging

Terminal 1

```
make start
```

Terminal 2

```
make logs
```

Terminal 1

```
make produce
```

## Topics in kafka

-   answers --> ingestion
-   student_topic --> per student stats
-   school_topic --> per school stats

sample stream

```
streams      | [2018-12-31 19:28:23,570: WARNING]: processing..
streams      | [2018-12-31 19:28:23,571: WARNING]: uid: 678  total_correct: 47 total_wrong: 64
streams      | [2018-12-31 19:28:23,571: WARNING]: schoolId: 456  total_correct: 81 total_wrong: 93
streams      | [2018-12-31 19:28:23,571: WARNING]: avg Response: 98.39132227765285
streams      | [2018-12-31 19:28:23,573: WARNING]: finished...
```

sample student_topic

```
{"student_id": "678", "total_correct": "44", "total_wrong": "62", "average_response_time": "143.52231288489085"}
{"student_id": "678", "total_correct": "43", "total_wrong": "61", "average_response_time": "298.0892515395634"}
{"student_id": "678", "total_correct": "44", "total_wrong": "63", "average_response_time": "123.26115644244543"}
{"student_id": "678", "total_correct": "45", "total_wrong": "63", "average_response_time": "162.13057822122272"}
{"student_id": "678", "total_correct": "46", "total_wrong": "63", "average_response_time": "149.56528911061136"}
```

sample school_topic

```
{"school_id": "123", "total_correct": "89", "total_wrong": "79", "average_response_time": "174.45359174679118"}
{"school_id": "123", "total_correct": "90", "total_wrong": "79", "average_response_time": "155.7267958733956"}
{"school_id": "789", "total_correct": "91", "total_wrong": "110", "average_response_time": "140.18674439673518"}
{"school_id": "456", "total_correct": "81", "total_wrong": "93", "average_response_time": "130.1975173688384"}
```
