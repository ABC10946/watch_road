DOCKER_IMAGE = "ghcr.io/abc10946/$(shell basename $(CURDIR))"

docker-build:
	docker build -t $(DOCKER_IMAGE) .

docker-push:
	docker push $(DOCKER_IMAGE)