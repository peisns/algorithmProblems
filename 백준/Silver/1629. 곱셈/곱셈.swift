let ABC = readLine()!.split(separator: " ").compactMap { Int($0) },
    a = ABC[0],
    c = ABC[2]
    
var b = ABC[1],
    remainder = a % c,
    remainderStack = [Int]()
    
while b != 1 {
    if !b.isMultiple(of: 2) { remainderStack.append(remainder) }
    remainder = remainder * remainder % c
    b = b / 2
}

while !remainderStack.isEmpty {
    remainder = remainder * remainderStack.removeLast() % c
}

print(remainder)