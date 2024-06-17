def sliding_window(k = 3, array = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]):
    result = []
    for index, _ in enumerate(array):
        if len(array) - index >= k:
            result.append(max(array[index:index+k]))
    print(result)

if __name__ == "__main__":
    sliding_window()