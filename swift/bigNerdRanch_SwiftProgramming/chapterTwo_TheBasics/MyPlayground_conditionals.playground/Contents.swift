//: Playground - noun: a place where people can play

import Cocoa

var population: Int = 5422
var hasPostOffice: Bool = true

var message: String

print("Ternary")
message = population < 10000 ? "\(population) is a small town." : "\(population) is a large town."

print(message)
message = ""

// IF ELSE Practice
print("IF/ELSE Nested")
if population < 10000 {
    message = "\(population) is a small town!"
} else {
    if population >= 10000 && population < 50000 {
        message = "\(population) is a medium town!"
    } else {
        message = "\(population) is pretty big!"
    }
}
print(message)

print("IF/ELSE IF/ELSE")
if population < 10000 {
    message = "\(population) is a small town!"
} else if population >= 10000 && population < 50000 {
    message = "\(population) is a medium town!"
} else if population > 150000{
    message = "\(population) is pretty big!"
} else {
    message = "\(population) is REALLY Large!"
}

print(message)

if !hasPostOffice {
    print("Where do we buy stamps?")
}
