const { readFileSync } = require("fs");
// split file into lines and then from those lines into a choice array
const lines = readFileSync("./input.txt", 'utf8').split("\n").map(x => x.split(" "));

const choiceRatings = { X: 1, Y: 2, Z: 3 };
const choiceMapping = { "A": "X", "B": "Y", "C": "Z" };
const winningCombos = { "X": "Y", "Y": "Z", "Z": "X" };

// Part 1

function gameScore(p1, p2) {
	// turn "A" -> "X" and so on
	const mp1 = choiceMapping[p1];

	// draw
	if (mp1 === p2) return 3;

	// win
	if (winningCombos[mp1] === p2) return 6;

	// loss 
	return 0;
}

// total up each rounds scores
const partOneScore = lines.reduce((acc, [enemy, player]) => acc + gameScore(enemy, player) + choiceRatings[player], 0);
console.log(`[Part1] Total Score: ${partOneScore}`);

// Part 2

function decision(p1, p2) {
	const mp1 = choiceMapping[p1];
	// win
	if (p2 === "Z") return [winningCombos[mp1], 6]

	// lose
	if (p2 === "X") {
		if (p1 === "A") return ["Z", 0]
		if (p1 === "B") return ["X", 0]
		return ["Y", 0]
	}

	// draw
	return [mp1, 3];
}

const partTwoScore = lines.reduce((acc, [enemy, player]) => {
	const [response, score] = decision(enemy, player)
	return acc + score + choiceRatings[response];
}, 0);
console.log(`[Part2] Total Score: ${partTwoScore}`);

