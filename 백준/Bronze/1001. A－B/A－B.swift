import Foundation
let input = readLine()
var number: Int = 0
if let i = input {
    var first = i[i.index(i.startIndex, offsetBy: 0)]
    var second = i[i.index(i.startIndex, offsetBy: 2)]
    number = first.wholeNumberValue ?? 0
    number -= second.wholeNumberValue ?? 0
}
print(number)