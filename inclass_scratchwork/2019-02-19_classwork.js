/*
 * Warmup: Complete the function isGreaterThanThree
 */

function isGreaterThanThree(number) {
    // TODO:
    // Return true if number is greater than 3.
    // Return false if number is not greater than 3.
}

// This code will run your function on some randomly generated numbers to check its accuracy.
new Array(20).fill(0).map((x) => {
    return Math.ceil(Math.random() * 6);
}).forEach((num) => {
    const gtThree = isGreaterThanThree(num);
    console.log(num + ' is greater than 3: ' + gtThree);
});

/*
 * Extension:
 * The Die class below has a subset of the features of the Die class from the Yahtzee project.
 * Implement the dieIsGreaterThanThree function, similar to the isGreaterThanThree function, except that it must take a die, not a number, and must use the value on the face of the die.
 */

class Die {
  constructor() {
    this.face = 0;
    this.roll();
  }

  roll() {
    if (!this.locked) {
      this.face = Math.ceil(Math.random() * 6);
    }
    return this;
  }
}


function dieIsGreaterThanThree(die) {
    // TODO:
    // Return true if the face of the die is greater than 3.
    // Return false if the face of the die is not greater than 3.
}

// This code will create a bunch of dice (and roll them), and run your function on each one.
new Array(20).fill(0).map((x) => {
    return new Die();
}).forEach((d) => {
    const gtThree = dieIsGreaterThanThree(d);
    console.log('This die shows ' + d.face + ' on its face. Greater than 3: ' + gtThree);
})
