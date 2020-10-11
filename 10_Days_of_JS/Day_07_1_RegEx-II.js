// The function should return a RegEx that matches a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.', followed by one or more letters.


function regexVar() {
    let re = /[MDE][rs]\w?\.\w*\w(?=$)/
    return re
}