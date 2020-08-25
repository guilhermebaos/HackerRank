/*
Determine the original side lengths and return an array:
    - The first element is the length of the shorter side
    - The second element is the length of the longer side
*/

function sides(literals, ...expressions) {
    let sides = []

    let A = expressions[0]
    let P = expressions[1]

    sides.push(Math.floor((P + (P**2 - 16*A)**0.5)/4))
    sides.push(Math.floor((P - (P**2 - 16*A)**0.5)/4))

    sides.sort((a, b) => a - b)

    return sides
}


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}