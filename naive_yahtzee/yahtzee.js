class Die {
  constructor() {
    this.locked = false;
    this.value = 0;
    this.roll();
  }

  roll() {
    if (!this.locked) {
      this.value = Math.ceil(Math.random() * 6);
    }
    return this;
  }

  toggleLock() {
    this.locked = !this.locked;
    return this;
  }

  updateDom() {
    this.domDie.innerText = this.value;
    this.domDie.classList.value = 'die ' + (this.locked ? 'locked' : 'unlocked');
    return this;
  }
}

// Build models
const modelDice = [new Die(), new Die(), new Die(), new Die(), new Die()];

// Get view elements
const domDice = document.querySelectorAll('.die');

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
}

// Initial roll
rollDice();
