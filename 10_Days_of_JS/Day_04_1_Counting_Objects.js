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