function createGreeting(name) {
    const greeting = 'Hello, ' + name + '!';
    return greeting;
}

const myName = 'Riley';

const greetingForMe = createGreeting(myName);

console.log(greetingForMe);

const friendNames = ['Erik', 'Zack', 'Nick', 'Bryan', 'Will'];

for (let friendName of friendNames) {
    const greetingForFriend = createGreeting(friendName);
    console.log(greetingForFriend);
}