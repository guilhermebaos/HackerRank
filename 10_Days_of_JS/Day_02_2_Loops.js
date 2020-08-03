function vowelsAndConsonants(s) {
    const vowels = ['a', 'e', 'i', 'o', 'u']

    let s_vowels = []
    let s_consonants = []

    let letter = ''
    for (let pos in s) {
        letter = s[pos]
        if (vowels.includes(letter)) {
            s_vowels.push(letter)
        } else {
            s_consonants.push(letter)
        }
    }
    
    for (let pos in s_vowels) {
        letter = s_vowels[pos]
        console.log(letter)
    }
    for (let pos in s_consonants) {
        letter = s_consonants[pos]
        console.log(letter)
    }
}