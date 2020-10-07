// Return maximum a & b < k, so that 0 < a < b <= n, and a, b are integers

function getMaxLessThanK(n, k) {
    let a, b, AND, bitA, bitB, bitAND, pos, newMaxi,
    maxi = 0,
    bitMaxi = '000000000'
    for (b = n; b > 0 /* k*0.9*/; b--) {
        bitB = numToBinary(b)
        for (a = b - 1 < k ? b - 1 : k; a > 0; a--) {
            bitA = numToBinary(a)
            bitAND = ''
            newMaxi = false
            for (pos = 0; pos < bitA.length; pos++) {
                if (bitA[pos] == 1 & bitB[pos] == 1) {
                    bitAND += '1'
                    if (bitMaxi[pos] == '0') newMaxi = true
                } else {
                    bitAND += '0'
                    if (bitMaxi[pos] == '1' & !newMaxi) break
                }
            }
            AND = numToDecimal(bitAND)
            if (AND < k & AND > maxi) {maxi = AND; bitMaxi = bitAND}
            if (maxi == k - 1) return maxi
        }
    }
    return maxi
}


function numToBinary(num) {
    // Binary Representation
    let binString = ''
    while (num != 0) {
        binString = num % 2 + binString
        num = Math.floor(num / 2)
    }
    
    // '32-bit' representation
    binString = binString.padStart(9, '0')
    return binString
}


function numToDecimal(binString) {
    let pos,
    binLen = binString.length,
    numDec = 0
    for (pos = binLen - 1; pos >= 0; pos--) {
        numDec += binString[pos] * 2**(binLen - pos - 1)
    }
    return numDec
}


console.log(getMaxLessThanK(407, 143))