import sys

from sematic import CloudResolver

from intermediate.pipeline import pipeline


if __name__ == "__main__":
    print(pipeline(sys.argv[1]).resolve(CloudResolver()))
