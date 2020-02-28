def duplicate_count(text):
    count = 0
    for duplicate in set(text.lower()):
        if text.lower().count(duplicate) > 1:
            count += 1
    return count

if __name__ == "__main__":
    print(duplicate_count("aA11"))