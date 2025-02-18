DOCKER_IMAGE = "ghcr.io/abc10946/$(shell basename $(CURDIR)):$(shell git describe --tags --always --dirty)"

docker-build:
	docker build -t $(DOCKER_IMAGE) .

docker-push:
	docker push $(DOCKER_IMAGE)

docker-run:
	docker run -p 8000:8000 -it --rm $(DOCKER_IMAGE)