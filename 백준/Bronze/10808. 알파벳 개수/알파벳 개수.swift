var alphabetDictionary = [Character : Int]()
Array("abcdefghijklmnopqrstuvwxyz").forEach {
    alphabetDictionary[$0] = 0
}

Array(readLine()!).forEach {
    alphabetDictionary[$0, default:0] += 1
}

var result = alphabetDictionary
.sorted { $0.key < $1.key }
.reduce("") { $0 + "\($1.value) " }
result.removeLast()

print(result)