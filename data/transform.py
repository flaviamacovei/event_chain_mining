def transform(raw_data: list[list[str]]):
    # TODO: make prettier
    assert raw_data and len(raw_data) > 0, "Data must not be empty"
    transformed_data = []
    prev_action = raw_data[0][0]
    attributes = []
    while raw_data:
        line = raw_data.pop(0)
        if len(line) != 3:
            continue
        current_action = line[0]
        if current_action == prev_action:
            attributes.append(line[-1:0:-1])
        else:
            transformed_data.append([prev_action] + attributes)
            attributes = [line[-1:0:-1]]
            prev_action = current_action
    transformed_data.append([prev_action] + attributes)
    return transformed_data
