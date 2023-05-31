from sematic import func


@func(inline=False)
def pipeline(data_file_path: str) -> str:
    with open(data_file_path, "r") as f:
        return f.readline()
