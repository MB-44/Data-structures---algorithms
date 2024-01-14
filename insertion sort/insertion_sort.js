class InsertionSort {
    constructor(array){
        this.array = array;
    }

    sort(array) {
        for (let i = 1; i < array.length; i++) {
            let current = array[i];
            let j = i - 1;
            while (j >= 0 && current < array[j]){
                array[j+1] = array[j];
                j--;
            }
            array[j+1] = current;
        }
    }
}

let myArray = [4,2,1,7,9,5];
let sorter = new InsertionSort(myArray);
sorter.sort(myArray);

console.log(myArray);