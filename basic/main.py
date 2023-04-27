from sematic import func, LocalResolver


@func
def pipeline() -> str:
    return "Hello, world!"


if __name__ == "__main__":
    print(pipeline().resolve(LocalResolver()))
