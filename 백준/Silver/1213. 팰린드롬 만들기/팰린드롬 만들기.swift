func getPalindrome(from name: String) -> String {
    var characterDictionary = [Character : Int]()
    
    Array(name).forEach { characterDictionary[$0, default: 0] += 1 }

    var halfPalindrome = "",
        centerCharacter = "",
        oddCase = 0
    
    for (key, value) in characterDictionary.sorted(by:<) {
        if !value.isMultiple(of:2) { 
            oddCase += 1
            if oddCase > 1 { return "I'm Sorry Hansoo" }
            centerCharacter = String(key)
        }
        halfPalindrome.append(String(repeating: key, count: value / 2))
    }
    
    
    return halfPalindrome + centerCharacter + String(halfPalindrome.reversed())
}

print(getPalindrome(from: readLine()!))