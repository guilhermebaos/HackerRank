// The function should return a RegEx that matches a string that starts and ends with the same vowel


function regexVar() {
    let re = /(^[aeiou]).*\1(?=$)/
    return re
}

console.log('abcda'.match(regexVar()))