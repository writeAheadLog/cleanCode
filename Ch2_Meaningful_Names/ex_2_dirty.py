the_list = [[1, 2], [2, 3], [3, 4], [4, 5]]


def get_them():
    list1 = list()

    for x in the_list:
        if x[0] == 4:
            list1.append(x)
    return list1


if __name__ == "__main__":
    print(get_them())
