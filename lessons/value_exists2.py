def value_exists(inp_dict: dict[str, int], check: int) ->bool:
    exists: bool = False
    for elem in inp_dict:
        if inp_dict[elem] == check:
            exists = True
    return exists