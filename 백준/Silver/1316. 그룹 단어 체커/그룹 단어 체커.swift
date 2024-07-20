import Foundation

let N = Int(readLine()!)!
let wordArray = stride(from: 0, to: N, by:1).map { _ in  readLine()! }

func isWordGroup(_ word: String) -> Bool {
    let characterArray = Array(word)
    var charaterSet: Set<Character> = [characterArray.first!]
    for i in stride(from:1, to:characterArray.endIndex, by:1) {
        let character = characterArray[i]
        if !charaterSet.insert(character).inserted && characterArray[i-1] != character { return false }
    }
    return true
}

print(wordArray.filter { isWordGroup($0) }.count)