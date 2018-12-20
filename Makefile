.PHONY: help start consumertest produce cat

.DEFAULT: help
help:
	@echo "make start"
	@echo "       starts the db then starts identity and downstream apps"
	@echo "make consumer-test"
	@echo "       Shortcut for kafkacat"

start:
	docker-compose up -d zookeeper kafka

consumertest:
	@echo "consumer test.."
	@echo "{test: 'hai thar'}" | kafkacat -P -b 127.0.0.1:9094 -t test_topic

produce:
	@echo "Produce.."
	@cat sample.json | kafkacat -P -b 127.0.0.1:9094 -t test_topic

cat:
	@echo "kafkacat peek.."
	@kafkacat -C -b 127.0.0.1:9094 -t test_topic
