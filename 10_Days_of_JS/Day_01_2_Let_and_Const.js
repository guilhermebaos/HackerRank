function main() {
    const PI = Math.PI

    let r = readLine()
    console.log(PI * r**2)
    console.log(2 * PI * r)

    try {    
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}