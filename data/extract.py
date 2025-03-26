def extract(sourcepath: str):
    assert sourcepath.split(".")[-1] == "txt", "Only txt files are supported"
    raw_data = []
    with open(sourcepath, "r") as f:
        for line in f:
            line = [w.strip("'") for w in line.strip("()\n").split(", ")]
            if len(line) != 3:
                continue
            raw_data.append(line)

    return raw_data
