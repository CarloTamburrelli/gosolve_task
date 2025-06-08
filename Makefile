up:
	docker-compose up --build

up-detached:
	docker-compose up -d --build

test:	
	docker-compose run --rm backend make test 
