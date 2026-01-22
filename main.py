def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
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

    direction = input("Направление сортировки (asc/desc): ").strip().lower()
    ascending = True
    if direction in ("desc", "d", "убыв", "убывание", "down"):
        ascending = False

    bubble_sort(numbers, ascending=ascending)

    if ascending:
        print("Отсортированный список (по возрастанию):")
    else:
        print("Отсортированный список (по убыванию):")

    print(*numbers)


if __name__ == "__main__":
    main()

