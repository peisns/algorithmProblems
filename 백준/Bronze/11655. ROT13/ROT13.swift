import Foundation

let alphabetDictionary = Dictionary(uniqueKeysWithValues: zip(
        Array("abcdefghijklmnopqrstuvwxyz"), 
        Array("nopqrstuvwxyzabcdefghijklm"))),
    others = Array(" 0123456789")

func solution(_ characterList: [Character]) -> String {
    return characterList.map { char -> Character in 
        if others.contains(char) { return char }
                              
        if char.isLowercase { return alphabetDictionary[char]! } 
        else {
            let key = Character(char.lowercased())
            return Character(alphabetDictionary[key]!.uppercased())
        }
    }.reduce("") { $0 + String($1) }
}

print(solution(Array(readLine()!)))