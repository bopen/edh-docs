FROM ghcr.io/astral-sh/uv:alpine3.23

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    UV_PROJECT_ENVIRONMENT=/venv \
    UV_PROJECT=/src/bopen/edh-docs

WORKDIR /src/

# install git-clone-ref.py dependencies
RUN apt update && apt install -y git make pandoc \
    && apt clean

# get git-clone-ref.py script
COPY ./git-clone-ref.py /tmp/git-clone-ref.py

COPY edh-docs /src/bopen/edh-docs

# Download all dependencies into the uv cache.
# but delete the virtual environment to save space, it will be re-created during uv run.
RUN uv sync --frozen --all-extras \
    && rm -rf /venv

EXPOSE 8000

CMD ["make", "prod-serve"]
