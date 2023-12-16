class InsertionSort:
    def __init__(self,array):
        self.array = array
    

    def sort(self,array):
        for i in range(1,len(array)):
            current = array[i]
            j = i - 1
            while (j >= 0 and current < array[j]):
                array[j + 1] = array[j]
                j -= 1
            
            array[j + 1] = current


if __name__ == "__main__":
    myArray = [4, 2, 7, 1, 9, 5]
    sorter = InsertionSort(myArray)
    sorter.sort(myArray)

    print(myArray)