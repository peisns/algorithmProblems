let _ = readLine(),
    m = Int(readLine()!)!,
    numberArray = readLine()!.split(separator: " ").compactMap { Int($0) }

var numberDictionary = [Int : Int]()

for number in numberArray {
    numberDictionary[number, default: 0] += 1
}

var armorCount = 0

if m.isMultiple(of: 2) {
    armorCount += numberDictionary[m / 2, default: 0] / 2
    numberDictionary[m / 2, default: 0] = 0
}

for (key, value) in numberDictionary {
    armorCount += min(value, numberDictionary[m-key, default: 0])
    numberDictionary[key] = 0
}

print(armorCount)