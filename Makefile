.PHONY: help start consumertest produce cat stop student-topic school-topic

.DEFAULT: help
help:
	@echo "make start"
	@echo "       starts the db then starts identity and downstream apps"
	@echo "make consumertest"
	@echo "       Shortcut for interactive kafkacat -P"
	@echo "make producer"
	@echo "       launches container producer with a short life of producing"
	@echo "make cat"
	@echo "       peek at topic different group than consumer app"
	@echo "make stop"
	@echo "       docker-compose down"
	@echo "make logs"
	@echo "       docker-compose logs"
	@echo "make school-topic || student-topic"
	@echo "       kafkacat of the aggregate topic to be compacted"

start:
	docker-compose up -d --build example_zookeeper example_kafka
	sleep 3
	docker-compose up -d --build consumer node_consumer
	docker-compose up -d --build streams

stop:
	docker-compose down

logs:
	docker-compose logs -f --tail 200 example_kafka consumer producer streams node_consumer

consumertest:
	@echo "consumer test.."
	@kafkacat -P -b 127.0.0.1:9094 -t test_topic

produce:
	@echo "Produce.."
	docker-compose up --build producer

cat:
	@echo "kafkacat peek.."
	@kafkacat -C -b 127.0.0.1:9094 -t test_topic

student-topic:
	@kafkacat -C -b localhost:9094 -G test_agg1 student_topic

school-topic:
	@kafkacat -C -b localhost:9094 -G test_agg1 school_topic
