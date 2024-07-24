import Foundation

let word = readLine()!

func solution(_ word: String) -> Bool {
    let characterArray = Array(word),
        halfCount = characterArray.count / 2
    for i in (0..<halfCount) {
        let oppositeI = characterArray.count - (i + 1)
        if characterArray[i] != characterArray[oppositeI] {
            return false
        }
    }
    
    return true
}

print(solution(word) ? 1 : 0)