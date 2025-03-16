build-image:
	docker build --tag aguest_me:latest .

start-container:
	docker run -d -p 8000:8000 aguest_me:latest