#!/usr/bin/node
function findSecondLargest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < numbers.length; i++) {
    const currentNumber = parseInt(numbers[i]);

    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber < largest) {
      secondLargest = currentNumber;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));
const secondLargest = findSecondLargest(numbers);
console.log(`${secondLargest}`);
