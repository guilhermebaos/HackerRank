let res = document.getElementById('res')

let btn0 = document.getElementById('btn0')
let btn1 = document.getElementById('btn1')

let btnClr = document.getElementById('btnClr')
let btnEql = document.getElementById('btnEql')

let btnSum = document.getElementById('btnSum')
let btSub = document.getElementById('btnSub')
let btnMul = document.getElementById('btnMul')
let btnDiv = document.getElementById('btnDiv')


// Add numbers to calculator
btn0.onclick = function() {
    res.innerText += '0'
}
btn1.onclick = function() {
    res.innerText += '1'
}

// Clear calculator
btnClr.onclick = function() {
    res.innerText = ''
}

// Evaluate expression
btnEql.onclick = function() {
    // Separate de expression
    let expression = res.innerText
    let operands = expression.split(/[+\-*\/]/)
    let operator = expression[expression.search(/[+\-*\/]/)]
    operand1 = operands[0]
    operand2 = operands[1]

    // Calculate the result
    let result
    if (operator == '+') result = numToBinary(numToDecimal(operand1) + numToDecimal(operand2))
    else if (operator == '-') result = numToBinary(numToDecimal(operand1) - numToDecimal(operand2))
    else if (operator == '*') result = numToBinary(numToDecimal(operand1) * numToDecimal(operand2))
    else if (operator == '/') result = numToBinary(Math.floor(numToDecimal(operand1) / numToDecimal(operand2)))
    res.innerText = result
}

// Add operators to calculator
btnSum.onclick = function() {
    res.innerText += '+'
}
btnSub.onclick = function() {
    res.innerText += '-'
}
btnMul.onclick = function() {
    res.innerText += '*'
}
btnDiv.onclick = function() {
    res.innerText += '/'
}


// Binary Representation
function numToBinary(num) {
    let binString = ''
    while (num != 0) {
        binString = num % 2 + binString
        num = Math.floor(num / 2)
    }
    return binString
}


// Decimal Representation
function numToDecimal(binString) {
    let pos,
    binLen = binString.length,
    numDec = 0
    for (pos = binLen - 1; pos >= 0; pos--) {
        numDec += binString[pos] * 2**(binLen - pos - 1)
    }
    return numDec
}
