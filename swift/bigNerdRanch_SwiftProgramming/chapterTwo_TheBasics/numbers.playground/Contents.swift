//: Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"

print("The Minimum Int Value is \(Int.min)")
print("The Maximum Int Value is \(Int.max)")
print("The Minimum Int32 Value is \(Int32.min)")
print("The Maximum Int32 Value is \(Int32.max)")

print("The Minimum UInt Value is \(UInt.min)")
print("The Maximum UInt Value is \(UInt.max)")
print("The Minimum UInt32 Value is \(UInt32.min)")
print("The Maximum UInt32 Value is \(UInt32.max)")

let numberOfPeople: UInt = 40
let volumeAdjustment:Int32 = -1000

// Trouble Ahead
//let firstBadValue: UInt = -1
//let secondBadValue: Int8 = 200

print(10 + 20)
print(30 - 5)
print(5 * 6)

print((10 + 2) * 5)
print(30 - (5 - 5))

print(11 / 3)
print(11 % 3)
print(-11 % 3)

var x = 10
x += 10
print("x has had 10 added to it and is now \(x)")
x -= 5
print("x has had 5 subtracted from it and is now \(x)")

let y: Int8 = 120
let z: Int8 = y &+ 10

print("wraparound value \(z)")
