def bubble_sort(string):
    n = len(string)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if string[j] > string[j + 1]:
                string[j], string[j + 1] = string[j + 1], string[j]

    return string


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_list = list(first_string)
    second_string_list = list(second_string)

    sorted_first_string = bubble_sort(first_string_list)
    sorted_second_string = bubble_sort(second_string_list)

    is_anagram = sorted_first_string == sorted_second_string

    return (
        "".join(sorted_first_string),
        "".join(sorted_second_string),
        is_anagram,
    )
