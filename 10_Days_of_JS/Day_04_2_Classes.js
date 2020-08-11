class Polygon {
    constructor(sides) {
        this.sides = sides
    }
    perimeter() {
        let total = 0
        let sides = this.sides
        for (let pos in sides) {
            total += sides[pos]
        }
        return total
    }
}