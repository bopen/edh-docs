FROM ghcr.io/astral-sh/uv:alpine3.23

ENV UV_NO_DEV=1

EXPOSE 8000
WORKDIR /src/edh-docs

RUN apk add git make pandoc

RUN uv venv

COPY . /src/edh-docs

RUN uv pip install -e .

CMD ["make", "prod-serve"]