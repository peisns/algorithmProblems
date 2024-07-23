let ABC = readLine()!.split(separator:" ").compactMap { Int($0) },
    (a, b, c) = (ABC[0], ABC[1], ABC[2])
var (inTimeDictionary, outTimeDictionary) = ([Int : Int](), [Int : Int]()),
    (carCount, result) = (0, 0)

(0..<3).forEach { _ in
    let times = readLine()!.split(separator: " ").compactMap { Int($0) },
        (inTime, outTime) = (times[0], times[1])
    inTimeDictionary[inTime, default: 0] += 1
    outTimeDictionary[outTime, default: 0] += 1
}

(1..<101).forEach { time in
    carCount += inTimeDictionary[time, default: 0]
    carCount -= outTimeDictionary[time, default: 0]
    switch carCount {
        case 1: result += a
        case 2: result += b * 2
        case 3: result += c * 3
        default: break
    }
}

print(result)