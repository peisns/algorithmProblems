var characterDictionary = [Character : Int]()
(0..<Int(readLine()!)!).forEach { _ in
    let character = Array(readLine()!)[0]
    characterDictionary[character, default: 0] += 1
}

let result = characterDictionary.filter { $0.value >= 5 }
.map {$0.key }
.sorted(by: <)
.reduce("") { $0 + String($1) }

print(result.isEmpty ? "PREDAJA" : result)