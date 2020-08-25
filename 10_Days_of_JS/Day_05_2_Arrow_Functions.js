// Modify and return the array so that all even elements are doubled and all odd elements are tripled.

function modifyArray(nums) {
    let newNums = nums.map(n => n % 2 == 0 ? n * 2 : n * 3)

    return newNums
}


function main() {
    const n = +(readLine());
    const a = readLine().split(' ').map(Number);
    
    console.log(modifyArray(a).toString().split(',').join(' '));
}