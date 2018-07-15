//: Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"
for char in str {
    print(char)
}

print("\n\n\n")

str += "\u{1F60E}"
for unicodeChar in str.unicodeScalars {
    print(unicodeChar, unicodeChar.value)
}
