import sys

from sematic import CloudRunner

from advanced.pipeline import pipeline


if __name__ == "__main__":
    future = pipeline(sys.argv[1]).set(
        name="Advanced Docker Example Pipeline", tags=["example", "docker", "advanced"]
    )
    print(CloudRunner().run(future))
