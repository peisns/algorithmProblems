import Foundation

let nm = readLine()!.split(separator:" ").compactMap { Int($0) },
    n = nm[0],
    m = nm[1]
var numberPokemonDictionary = [Int : String](),
    pokemonNumberDictionary = [String : Int]()
    
for i in (1..<(n+1)) {
    let pokemon = readLine()!
    numberPokemonDictionary[i] = pokemon
    pokemonNumberDictionary[pokemon] = i
}

func search(_ text: String) -> String {
    if text.first!.isNumber, let number = Int(text) {
        return numberPokemonDictionary[number, default: ""]
    } else {
       return String(pokemonNumberDictionary[text, default:1]) 
    }
}

for _ in (0..<m) {
    print(search(readLine()!))
}