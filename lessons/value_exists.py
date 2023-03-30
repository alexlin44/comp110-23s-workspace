def value_exists(dict1: dict[str, int], check: int) -> bool:
    for key, value in dict1.items():
        if value == check:
            return True
    return False
        
test_dict: dict[str, int] = {"a": 2, "b": 4,"c": 7, "d": 1}
test_val: int = 4

print(value_exists(test_dict, test_val))