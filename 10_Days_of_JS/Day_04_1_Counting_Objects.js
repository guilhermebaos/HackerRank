// Return a count of the total number of objects 'o' satisfying o.x == o.y.

function getCount(objects) {
    let c = 0
    let o
    for (let pos in objects) {
        o = objects[pos]
        if (o.x == o.y) {
            c++
        }
    }
    return c
}

function main() {
    const n = +(readLine());
    let objects = [];
    
    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(' ');
        
        objects.push({x: +(a), y: +(b)});
    }
    
    console.log(getCount(objects));
}