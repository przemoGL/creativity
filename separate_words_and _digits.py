def separate_string(string):
    """
    Function to separate alphabetical-only strings (words), numbers and all others from given string.
    :param string: string to separate [str]
    :return: separated elements by category [list]
    """
    result = {'words': [], 'numbers': [], 'other': []}
    for word in string.split():
        if word.isalpha():
            result['words'].append(word)
        elif word.isdigit():
            result['numbers'].append(int(word))
        else:
            result['other'].append(word)
    return list(result.values())


test_string = "Hello 123 Johnny B2 137"
print(separate_string(test_string))
