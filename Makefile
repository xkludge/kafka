.PHONY: help start migrate loaddata

.DEFAULT: help
help:
	@echo "make start"
	@echo "       starts the db then starts identity and downstream apps"

start:
	docker-compose up -d zookeeper kafka
	docker-compose up -d --build consumer


