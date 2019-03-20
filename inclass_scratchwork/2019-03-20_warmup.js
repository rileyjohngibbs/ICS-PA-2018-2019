// Given this JavaScript function:

function add(x, y) {
    return x + y;
}

// What happens if we run this function with no arguments, one argument, two arguments, or three arguments? Use numbers for all the arguments.

console.log('No arguments');
none = add();
console.log(none);

console.log('One argument');
one = add(3);
console.log(one);

console.log('Two arguments');
two = add(3, 5);
console.log(two);

console.log('Three arguments');
three = add(3, 5, 7);
console.log(three);


const myList = [10, 10, 10];

const someMappedList = myList.map((ten) => {return ten + 5;});
console.log('Mapped list:');
console.log(someMappedList);

const someDoubleMappedList = myList.map((ten, i) => {return ten + i;});
console.log('Double mapped list:');
console.log(someDoubleMappedList);








































