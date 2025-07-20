def find_longest_word(words=["сонце", "дерево", "комп'ютер", "ніч"]):
    if not words:
        return ""
    return max(words, key=len)


longest = find_longest_word()
print("Найдовше слово:", longest)
