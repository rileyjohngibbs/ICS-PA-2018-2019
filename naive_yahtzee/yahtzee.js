class Die {
  constructor() {
    this.locked = false;
    this.face = 0;
    this.roll();
  }

  roll() {
    if (!this.locked) {
      this.face = Math.ceil(Math.random() * 6);
    }
    return this;
  }

  toggleLock() {
    this.locked = !this.locked;
    return this;
  }

  updateDom() {
    this.domDie.innerText = this.face;
    this.domDie.classList.value = 'die ' + (this.locked ? 'locked' : 'unlocked');
    return this;
  }
}

// Build models
const modelDice = [new Die(), new Die(), new Die(), new Die(), new Die()];

// Get view elements
const domDice = document.querySelectorAll('.die');

let rollCount = 0;
const counter = document.getElementById('counter');
let score = 0;

// Connect models to view elements
for (let i = 0; i < modelDice.length; i++) {
  domDice[i].modelDie = modelDice[i];
  modelDice[i].domDie = domDice[i];
  domDice[i].addEventListener('click', () => {
    domDice[i].modelDie.toggleLock().updateDom();
  });
}

// Click handler for Roll Dice button
function rollDice() {
  modelDice.forEach((die) => {
    !die.locked ? die.roll().updateDom() : '';
  });
  rollCount++;
  counter.innerHTML = rollCount;
  if (rollCount >= 3) {
    document.getElementById('roll-btn').disabled = true;
  }
  const faces = modelDice.map((die) => die.face);
  checkScoring(faces);
}

function reset() {
  rollCount = 0;
  modelDice.forEach((die) => {die.locked = false});
  rollDice();
  document.getElementById('roll-btn').disabled = false;
}

function checkScoring(arr) {
  document.getElementById('three-kind-btn').disabled = !hasSet(arr, 3) || hasScoredThreeKind;
  document.getElementById('four-kind-btn').disabled = !hasSet(arr, 4) || hasScoredFourKind;
  document.getElementById('yahtzee-btn').disabled = !hasSet(arr, 5) || hasScoredYahtzee;
}

function hasSet(arr, num) {
  const counts = new Array(6).fill(0);
  for (let a of arr) {
    counts[a]++;
  }
  for (let c of counts) {
    if (c >= num) {
      return true;
    }
  }
  return false;
}

function scoreThreeKind() {
  const sum = modelDice.reduce((a, b) => a + b.face, 0);
  score += sum;
  hasScoredThreeKind = true;
  document.getElementById('score').innerHTML = score;
  reset();
}

function scoreFourKind() {
  const sum = modelDice.reduce((a, b) => a + b.face, 0);
  score += sum + 10;
  hasScoredFourKind = true;
  document.getElementById('score').innerHTML = score;
  reset();
}

function scoreYahtzee() {
  score += 50;
  hasScoredYahtzee = true;
  document.getElementById('score').innerHTML = score;
  reset();
}

let hasScoredThreeKind = false;
let hasScoredFourKind = false;
let hasScoredYahtzee = false;

// Initial roll
rollDice();
