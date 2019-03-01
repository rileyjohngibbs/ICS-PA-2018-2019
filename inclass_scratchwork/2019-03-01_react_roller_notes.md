# Looking at react-roller

## Retrieving react-roller

Available on Github. Click [here](https://github.com/rileyjohngibbs/react-roller).

### Running react-roller

Use `git clone` to copy it to your computer:
```bash
git clone https://github.com/rileyjohngibbs/react-roller.git
```
Then use `cd` to navigate into that project's directory:
```bash
cd react-roller
```
Use `npm` to install dependencies:
```bash
npm install
```
And run the application with `npm`:
```bash
npm start
```
This should launch a development server and open a browser window to see the application. If you make changes to the application, your page will automatically reload with the changes.

### Reading the source code

Most of the code for this application is in `src/App.js`. There is a little bit more defined in `src/Die.js`. The styling is in the `src/App.css` file. All other files can be pretty much ignored for now.

## Notes from class

- Lots of use of "key." What is that?
  - Unique identifiers for lists of things in React apps.
- Lots of HTML in the JavaScript.
  - Yes! This is the hallmark of a React application.
- Lots of anonymous functions.
  - Indeed, this is very common in modern JavaScript. They're very useful for use as callback functions, which is what you use to define the behavior of `.map`, `.forEach`, `.reduce`, `onClick`, and a whole host of other things in JavaScript.
- How does calcSum work?
  - The `.reduce` inside of `calcSum` is like a `for` loop that successively adds the dice values, starting at zero. The `acc` argument in the anonymous function is the running total, and the `die` argument is the current item in the `dice` array.
- What does .splice do?
  - Remove item(s) from an array.
  - Two arguments: where do we start; how many items to remove.
- What does .length do?
  - Gives the length of the array.
    ```javascript
    const myArray = [1, 2, 3];
    myArray.length;  // returns 3
    ```
- What does .push do?
  - Adds a value to an array:
    ```javascript
    const myArray = [1, 2, 3];
    myArray.push(4);
    myArray;  // [1, 2, 3, 4]
    ```
- Line 70: The underscore? What is that?
  - Example:
    ```javascript
    const myArray = ["a", "b", "c"];
    myArray.forEach((_, index) => console.log(index));
    ```
  - Underscore is a convention for "I don't care about this."
- Line 26: `dice[key].value` <-- What is that syntax?
  - `dice[key]` accesses an element in the array `dice`.
  - `.value` retrieves the `value` attribute from that object (`Die`, defined in `Die.js`).
- `.map`: What does this do?
  - It constructs a new array by running the function it is given on each element of the original array.
  - For example, here the `.map` will create a new array whose elements are each two times the corresponding element in `myArray`:
    ```javascript
    const myArray = [1, 2, 3];
    myArray.map((x) => {return x * 2;});  // [2, 4, 6]
    ```