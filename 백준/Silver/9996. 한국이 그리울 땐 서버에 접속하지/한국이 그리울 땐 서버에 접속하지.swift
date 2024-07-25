import Foundation

let N = Int(readLine()!)!,
    pattern = readLine()!.split(separator: "*"),
    (front, end) = (pattern[0], pattern[1]),
    (frontCount, endCount) = (front.count, end.count),
    patternCount = frontCount + endCount

func isMatch(_ word: String) -> Bool {
    if patternCount > word.count { return false }
    if front != word.prefix(frontCount) { return false }
    if end != word.suffix(endCount) { return false }
    
    return true
}

(0..<N).forEach { _ in print(isMatch(readLine()!) ? "DA" : "NE") }