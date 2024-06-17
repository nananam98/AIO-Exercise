def count_chars(string = 'Happiness'):
    result = {}
    for i in string.lower():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    print(result)
if __name__ == "__main__":
    count_chars()