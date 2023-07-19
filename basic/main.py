from sematic import func, LocalRunner


@func
def pipeline() -> str:
    return "Hello, world!"


if __name__ == "__main__":
    future = pipeline().set(
        name="Basic Example Pipeline", tags=["examples", "local", "advanced"]
    )
    print(LocalRunner().run(future))
