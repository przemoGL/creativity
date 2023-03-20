def check(target: str, list_: list):
    target = target.lower()
    new_list = []
    for word in list_:
        word = word.lower()
        new_list.append(word)
    if target in new_list:
        return True
    else:
        return False


print(check("a", ["A", "b", "c"]))  # True
print(check("abc", ["AbC", "b", "c"]))  # True
print(check("aBc", ["AbC"]))  # True
print(check("abc", ["a", "b", "c"]))  # False
print(check("abc", []))  # False
