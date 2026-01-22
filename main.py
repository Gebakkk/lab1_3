def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def main():
    n = int(input("Введите количество чисел n: "))
    numbers = []

    for i in range(n):
        x = float(input(f"Введите число {i + 1}: "))
        numbers.append(x)

    bubble_sort(numbers)

    print("Отсортированный список (по возрастанию):")
    print(*numbers)


if __name__ == "__main__":
    main()
