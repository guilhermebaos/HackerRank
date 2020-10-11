// The function should return a RegEx that matches all occurrences of numbers in a string


function regexVar() {
    let re = /\d+/g
    return re
}

console.log('102, 1948948 and 1.3 and 4.5'.match(regexVar()))