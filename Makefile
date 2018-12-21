.PHONY: help start consumertest produce cat stop

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

start:
	docker-compose up -d zookeeper kafka
	sleep 3
	docker-compose up -d --build consumer
	docker-compose up -d --build streams

stop:
	docker-compose down

logs:
	docker-compose logs -f --tail 200 kafka consumer producer streams 

consumertest:
	@echo "consumer test.."
	@kafkacat -P -b 127.0.0.1:9094 -t test_topic

produce:
	@echo "Produce.."
	docker-compose up --build producer

cat:
	@echo "kafkacat peek.."
	@kafkacat -C -b 127.0.0.1:9094 -t test_topic
