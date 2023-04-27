# Example Docker-based Sematic Pipelines

This repo contains examples of how to build and submit a Sematic pipelines using the
native Python+Docker build system, as opposed to [using
Bazel](https://github.com/sematic-ai/example_bazel).

See the [Sematic
documentation](https://docs.sematic.dev/cloud-execution/container-images#docker)
for more details.

## Usage

All these examples require a running Sematic Server:
```bash
$ sematic start
```

### Basic

To run a pipeline directly locally, without building or submitting a cloud execution:

```bash
$ sematic run basic/main.py
```

Running pipelines locally is only supported when using [`LocalResolver` or
`SilentResolver`](https://docs.sematic.dev/diving-deeper/local-execution).

### Intermediate

This command will build a Docker image starting from the Sematic worker base image, and
run a remote pipeline in the cloud (given all steps in the docs have been completed):

```bash
$ sematic run intermediate/main.py --build -- /intermediate/data/message.txt
```

This example also shows how to package data files and pass arguments to the pipeline
execution.

### Advanced

This command will build a Docker image from scratch using a build script and Dockerfile,
and run a remote pipeline in the cloud (given all steps in the docs have been completed):

```bash
$ sematic run advanced/main.py --build -- /advanced/data/message.txt
```

This example also shows how to package data files and pass arguments to the pipeline
execution.
