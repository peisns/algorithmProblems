import Foundation

let heightArray = stride(from:0, to:9, by:1)
.map { _ in Int(readLine()!)! }
.sorted(by:<)

var queue: [(totalHeight: Int, heightArray: [Int])] = [(heightArray.reduce(0, +), heightArray)]

var result = [Int]()

var isEnd = false

while !isEnd {
    let element = queue.removeFirst()
    for i in element.heightArray.indices {
        var heightArray = element.heightArray
        let num = heightArray[i]
        let totalHeight = element.totalHeight - num
        heightArray.remove(at: i)
        if heightArray.count == 7 && totalHeight == 100 {
            result = heightArray
            isEnd.toggle()
        } else if heightArray.count != 7 {
            queue.append((totalHeight, heightArray))
        }
    }
}

result.forEach { print($0) }