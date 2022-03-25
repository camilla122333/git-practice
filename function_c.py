def merge_lists(list_a, list_b):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    return list(set(list_a) | set(list_b))


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# print(merge_lists(list1, list2))

if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
