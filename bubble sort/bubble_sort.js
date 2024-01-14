class BubbleSort {
    constructor(array){
        this.array = array;
    }

    swap(array,index1, index2){
        let temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    sort(array){
        for (let i = 0; i < array.length; i++) {
            let isSorted = true;
            for (let j = 1; j < array.length-i; j++) {
                if (array[j] < array[j-1]){
                    this.swap(array, j,j-1);
                    isSorted = false;
                    }
                }
            if (isSorted){
                return;
            }
        }
    }
}

let myArray = [4,2,1,7,9,6];
let sorter = new BubbleSort(myArray);
sorter.sort(myArray);

console.log(myArray);