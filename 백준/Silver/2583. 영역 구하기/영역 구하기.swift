let mnk = readLine()!.split(separator: " ").compactMap { Int($0) }
let (m, n, k) = (mnk[0], mnk[1], mnk[2])
let rectangles: [(leftY: Int, leftX: Int, rightY: Int, rightX:Int)] = (0..<k).map { _ in 
    let vertices = readLine()!.split(separator:" ").compactMap { Int($0) }
    return (vertices[1], vertices[0], vertices[3], vertices[2])
    }

var matrix = Array(repeating: Array(repeating: true, count: n), count: m)

for vertices in rectangles {
    for y in (vertices.leftY..<vertices.rightY) {
        for x in (vertices.leftX..<vertices.rightX) {
            matrix[y][x] = false
        }
    }
}

var count = 0
var areas = [Int]()

func getArea(_ i: Int, _ j: Int) -> Int {
    var area = 0
    var queue = [(y: i, x: j)]
    while !queue.isEmpty {
        let element = queue.removeFirst(), 
            y = element.y, 
            x = element.x
        
        if y < 0 || x < 0 || y >= m || x >= n || !matrix[y][x] {
            continue
        }
        matrix[y][x] = false
        
        area += 1
        
        queue.append((y+1, x))
        queue.append((y-1, x))
        queue.append((y, x+1))
        queue.append((y, x-1))
    }
    
    return area
}

(0..<m).forEach { i in 
    for j in (0..<n) where matrix[i][j] {
        count += 1
        
        areas.append(getArea(i, j))
    }
}
print(count)
print(areas.sorted(by: <).map { String($0) }.joined(separator: " "))