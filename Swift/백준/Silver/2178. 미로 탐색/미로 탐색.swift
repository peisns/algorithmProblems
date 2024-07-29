import Foundation

let nm = readLine()!.components(separatedBy: " ").compactMap { Int($0) }, N = nm[0]-1, M = nm[1]-1,
    cellArrays = (0..<N+1).map { _ in Array(readLine()!) }
typealias Element = (n: Int, m: Int, count: Int)
var queue: [Element] = [(0, 0, 1)], result = -1,
    isVisitedArray = cellArrays.map { $0.map { $0 == "0" ? true : false } }
func spread(_ n: Int, _ m: Int, _ count: Int) {
    if n < 0 || m < 0 || n > N || m > M { return }
    queue.append((n, m, count+1))
}

while !queue.isEmpty {
    let element = queue.removeFirst()
    if isVisitedArray[element.n][element.m] { continue }
    if element.n == N && element.m == M { result = element.count; break }
    isVisitedArray[element.n][element.m].toggle()
    spread(element.n-1, element.m, element.count)
    spread(element.n, element.m-1, element.count)
    spread(element.n+1, element.m, element.count)
    spread(element.n, element.m+1, element.count)
}

print(result)