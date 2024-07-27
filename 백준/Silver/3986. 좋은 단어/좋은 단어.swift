func isGoodWord() -> Bool {
    let word = Array(readLine()!)
    if !word.count.isMultiple(of: 2) { return false }
    
    var queue = [Character]()
    
    for character in word {
        if let last = queue.last, last == character {
            queue.removeLast()
            continue
        }
        
        queue.append(character)
    }
    return queue.isEmpty ? true : false
}

print((0..<Int(readLine()!)!).filter { _ in isGoodWord() }.count)