FROM ubuntu:jammy
SHELL [ "bash", "-c" ]
RUN set -eux; apt-get update; apt-get install -y \
  python3-dev \
  python3-pip \
  git

RUN pip install toml pygithub

COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
