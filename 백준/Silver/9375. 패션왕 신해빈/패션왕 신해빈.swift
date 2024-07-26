func getCaseCount() {
    let clothCount = Int(readLine()!)!
    var typeDictionary = [Substring : Int]()
    (0..<clothCount).forEach { _ in
        let type = readLine()!.split(separator:" ")[1]
        typeDictionary[type, default: 0] += 1
    }
    let caseCount = typeDictionary.reduce(1) { $0 * ($1.value + 1) } - 1
    print(caseCount)
}

(0..<Int(readLine()!)!).forEach { _ in getCaseCount() }