/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const n = parseInt(readline()); // the number of temperatures to analyse
var inputs = readline().split(' ');
var proche = 0;
for (let i = 0; i < n; i++) {
    const t = parseInt(inputs[i]);// a temperature expressed as an integer ranging from -273 to 5526
    if (proche === 0) {
        proche = t;
    } else if (t > 0 && t <= Math.abs(proche)) {
        proche = t;
    } else if (t < 0 && -t < Math.abs(proche)) {
        proche = t;
    }
}

// Write an answer using console.log()
// To debug: console.error('Debug messages...');
console.log(proche)