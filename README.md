# nids-golden-vectors

Generates int32 input samples and golden reference outputs for testing an
AI Engine kernel in an FPGA network intrusion detection system.

## Pipeline

- Every pull request: tests run in Docker on Python 3.11, 3.12, 3.13
- `main` is protected: pull requests can't merge unless all tests pass
- Every merge to `main`: image published to GHCR and golden vectors uploaded as an artifact

## Run it

docker pull ghcr.io/trichins2/nids-golden-vectors:latest
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD/out:/app/out" \
 ghcr.io/trichins2/nids-golden-vectors:latest python -m src.generate
