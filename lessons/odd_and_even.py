"""Returns a list of numbers that are odd with an even idx."""

def odd_and_even(input_list: list[int])-> list[int]:
    output_list = []
    idx = 0
    for item in input_list:
        if item % 2 != 0 and idx % 2 == 0:
            output_list.append(item)
        idx += 1
    return output_list

print(odd_and_even([2,3,4,5]))