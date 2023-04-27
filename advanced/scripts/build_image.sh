#!/usr/bin/env bash
set -e

# build the image
# use the project root as the work directory; the Dockerfile uses project-relative paths
docker build \
    --platform linux/amd64 \
    --tag example_docker:default_advanced \
    -f ../docker/Dockerfile ../../ 1>&2

# output the URI in the required format
digest=`docker inspect --format='{{.Id}}' example_docker:default_advanced`
echo "example_docker:default_advanced@${digest}"
