//: Playground - noun: a place where people can play

import Cocoa

func printGreeting() {
    print("Hello World!")
}
printGreeting()

func printPersonalGreeting(to name: String) {
    print("Hello \(name), welcome to your playground.")
}
printPersonalGreeting(to: "Logan")

func divisionDescriptionFor(numerator: Double, denominator: Double, withPunctuation punctuation: String = ".") {
    print("\(numerator) divided by \(denominator) equals \(numerator / denominator)\(punctuation)")
}
divisionDescriptionFor(numerator: 40, denominator: 5)
divisionDescriptionFor(numerator: 40, denominator: 5, withPunctuation: "!")

func printMultiPersonalGreeting(to names: String...) {
    for name in names {
        print("Hello \(name), welcome to your playground.")
    }
}
printMultiPersonalGreeting(to: "Logan", "Austin")


var error = "The Request failed:"
func appendErrorCode(_ code: Int, toErrorString errorString:  inout String) {
    if code == 400 {
        errorString += " bad request"
    }
}
appendErrorCode(400, toErrorString: &error)
error

func divisionDescriptionForReturned(numerator: Double, denominator: Double, withPunctuation punctuation: String = ".") -> String {
    return "\(numerator) divided by \(denominator) equals \(numerator / denominator)\(punctuation)"
}
print(divisionDescriptionForReturned(numerator: 60, denominator: 5))


func areaOfTriangle(base: Double, height: Double) -> Double {
    let numerator = base * height
    func divide() -> Double {
        return numerator / 2
    }
    return divide()
}
areaOfTriangle(base: 3.0, height: 5.0)


func sortedEvenOddNumbers(_ numbers: [Int]) -> (evens: [Int], odds: [Int]) {
    var evens = [Int]()
    var odds = [Int]()
    for number in numbers {
        if number % 2 == 0 {
            evens.append(number)
        } else {
            odds.append(number)
        }
    }
    return (evens, odds)
}

let justaBunchOfNumbers = [21, 34, 65, 76, 2, 1, 54, 78, 35, 43, 09]
let sortedNumbers = sortedEvenOddNumbers(justaBunchOfNumbers)

print("The even numbers are: \(sortedNumbers.evens); The odd numbers are: \(sortedNumbers.odds).")


func grabMiddleName(fromFullName name: (first: String, middle: String?, last: String)) -> String? {
    return name.middle
}
var middleName = grabMiddleName(fromFullName: (first: "Logan", middle: nil, last: "Startoni"))
if let theName = middleName {
    print(theName)
}
middleName = grabMiddleName(fromFullName: (first: "Logan", middle: "Tyler", last: "Startoni"))
if let theName = middleName {
    print(theName)
}

func greetByMiddleName(fromFullName name: (first: String, middle: String?, last: String)) {
    guard let middleName = name.middle else {
        print("Hey There!")
        return
    }
    print("Hey \(middleName)")
}
greetByMiddleName(fromFullName: (first: "Logan", middle: nil, last: "Startoni"))
greetByMiddleName(fromFullName: (first: "Logan", middle: "Tyler", last: "Startoni"))
