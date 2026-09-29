# Copyright 2026 European Union
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:latest AS uv
FROM --platform=linux/amd64 ubuntu:26.04
COPY --from=uv /uv /uvx /bin/

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
