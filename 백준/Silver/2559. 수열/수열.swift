import Foundation

let NK = readLine()!.split(separator:" ").compactMap { Int($0) },
    n = NK[0],
    k = NK[1],
    temperatures = readLine()!
    .split(separator: " ")
    .compactMap { Int($0) }
    
var sumTemperature = temperatures[0..<k].reduce(0, +),
    maxTemperature = sumTemperature

for i in (k..<n) {
    sumTemperature += temperatures[i] - temperatures[i-k]
    maxTemperature = max(maxTemperature, sumTemperature)
}

print(maxTemperature)