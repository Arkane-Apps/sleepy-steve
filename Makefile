APP      := "sleepy-steve"
TAG      ?= "latest"
DEV_PORT ?= 8080

.PHONY: \
	dev \
	run

dev:
	@docker build -t ${APP}:dev-local .
	@docker run --rm -it \
		-v `pwd`/sleepy-steve:/sleepy-steve \
		-p 127.0.0.1:${DEV_PORT}:8080 \
		--entrypoint bash \
		${APP}:dev-local

run:
	@docker build -t ${APP}:local .
	@docker run --rm -it \
		-p 127.0.0.1:${DEV_PORT}:8080 \
		${APP}:dev-local