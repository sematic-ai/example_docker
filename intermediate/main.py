import sys

from sematic import CloudRunner

from intermediate.pipeline import pipeline


if __name__ == "__main__":
    future = pipeline(sys.argv[1]).set(
        name="Intermediate Docker Example Pipeline",
        tags=["examples", "docker", "intermediate"],
    )
    print(CloudRunner().run(future))
