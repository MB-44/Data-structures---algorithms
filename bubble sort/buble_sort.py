class BubleSort:
    def __init__(self,array):
        self.array = array
    
    
    def swap(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp
    
    def sort(self, array):
        for i in range(len(array)):
            isSorted = True
            for j in range(1, len(array)-i):
                if array[j] < array[j - 1]:
                    self.swap(array, j, j - 1)
                    isSorted = False

            if isSorted:
                return



if __name__ == "__main__":
    myArray = [4, 2, 7, 1, 9, 5]
    sorter = BubleSort(myArray)
    sorter.sort(myArray)

    print(myArray)