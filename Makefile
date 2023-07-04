.PHONY: setup restart clean

setup:
	@docker-compose up -d

restart:
	@docker-compose restart

clean:
	@docker-compose down --volumes --remove-orphans