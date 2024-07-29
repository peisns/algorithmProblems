import Foundation

func check(N: Int, M: Int, n: Int, m: Int, field: inout [[Int]]) {
    if n < 0 || m < 0 || n == N || m == M || field[n][m] == 0 { return }
    field[n][m] = 0
    
    check(N: N, M: M, n: n, m: m+1, field: &field)
    check(N: N, M: M, n: n+1, m: m, field: &field)
    check(N: N, M: M, n: n-1, m: m, field: &field)
    check(N: N, M: M, n: n, m: m-1, field: &field)
}

func solution(M: Int, N: Int, kimchiCabbages: [[Int]]) -> Int {
    var field = Array(repeating: Array(repeating: 0, count: M), count: N)
    kimchiCabbages.forEach { field[$0[1]][$0[0]] = 1 }
    var worms = 0
    for n in stride(from: 0, to: N, by: 1) {
        for m in stride(from: 0, to: M, by: 1) {
            if field[n][m] == 0 { continue }
            worms += 1
            
            check(N: N, M: M, n: n, m: m, field: &field)
        }
    }
    return worms
}

let T = Int(readLine()!)!
let result = stride(from: 0, to: T, by: 1).map { _ -> Int in
    let MNK = readLine()!.components(separatedBy: " ").compactMap { Int($0) }
    let kimchiCabbages = stride(from: 0, to: MNK[2], by: 1).map { _ in readLine()!.components(separatedBy: " ").compactMap { Int($0) } }
    return solution(M: MNK[0], N: MNK[1], kimchiCabbages: kimchiCabbages)
}
result.forEach { print($0) }