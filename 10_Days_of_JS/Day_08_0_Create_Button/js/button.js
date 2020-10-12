let btn = document.getElementById('btn')

btn.onclick = function updateBtn() {
    btn.innerText = Number(btn.innerText) + 1
}