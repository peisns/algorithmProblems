import Foundation
let input = readLine()
var number: Int = 0
if let i = input {
    for n in i {
        if n != " " {
            number += n.wholeNumberValue ?? 0
        }
    }
}
print(number)