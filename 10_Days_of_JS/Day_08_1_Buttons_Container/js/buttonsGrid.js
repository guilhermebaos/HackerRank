let div = document.getElementById('btns')
let btnArr = []
let valueArr = [1, 2, 3, 6, 9, 8, 7, 4]

for (let num = 1; num <= 9; num++) {
    let tempBtn = document.createElement('button')
    btnArr.push(tempBtn)
    tempBtn.setAttribute('id', `btn${num}`)
    tempBtn.innerText = num
    div.appendChild(tempBtn)
    if (num % 3 == 0) {
        div.appendChild(document.createElement('br'))
    }
}


let mainBtn = btnArr[4]

let newBtnArr = []
for (let pos in valueArr) {
    newBtnArr.push(btnArr[valueArr[pos] - 1])
}
btnArr = newBtnArr

mainBtn.onclick = function rotate() {
    valueArr.unshift(valueArr.pop())
    for (pos in btnArr) {
        btnArr[pos].innerText = valueArr[pos]
    }
}