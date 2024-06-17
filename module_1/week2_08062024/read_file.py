def read_file(url = '../../data/week2_08062024.txt'):
    with open(url, 'r') as f:
        document = f.read().lower().split()
    result = {}
    for i in document:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    print(result)
if __name__ == "__main__":
    read_file()