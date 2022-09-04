from flat_generator import flat_generator


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


if __name__ == "__main__":
    for item in flat_generator(nested_list):
        print(item)
