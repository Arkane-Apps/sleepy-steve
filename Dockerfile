ARG BUILD_PLATFORM=amd64
FROM --platform=${BUILD_PLATFORM} python:3.11 as builder

WORKDIR /build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt

FROM --platform=${BUILD_PLATFORM} python:3.11

WORKDIR /sleepy-steve

COPY --from=builder /build/wheels /wheels
COPY --from=builder /build/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY sleepy-steve .

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
