#Hier soll BubbleSort defined werden

def bubble_sort(arr):
    n = len(arr)
    # Durchlaufe das Array n-1 mal
    for i in range(n - 1):
        # Bei jedem Durchlauf werden die größten Werte nach rechts "gebubbled"
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Tausche die Elemente, wenn sie in der falschen Reihenfolge sind
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[::-1]


if __name__ == "__main__":
    # Beispielaufruf
    example_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(example_array)
    print("Sorted array:", sorted_array)