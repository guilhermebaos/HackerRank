function reverseString(s) {
    let s_split
    try {
        s_split = s.split()
        let new_s = ''
        for (let pos = s.length - 1; pos >= 0; pos--) {
            new_s += s[pos]
        }
        s = new_s
    } catch (e) {
        console.log(e.message)
    } finally {
        console.log(s)
    }
}