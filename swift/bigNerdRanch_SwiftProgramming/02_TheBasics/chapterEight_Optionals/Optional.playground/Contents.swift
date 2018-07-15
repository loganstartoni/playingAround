//: Playground - noun: a place where people can play

import Cocoa

var errorCodeString: String?
if errorCodeString != nil {
    let theError = errorCodeString!
    print(theError)
}

errorCodeString = "404"

// Explicit Error String
if let theError = errorCodeString {
    if let errorCodeInteger = Int(theError) {
        print("\(theError): \(errorCodeInteger)")
    }
}

// Unwrapping with chained binding
if let theError = errorCodeString, let errorCodeInteger = Int(theError) {
        print("\(theError): \(errorCodeInteger)")
}

// This is with an implicitly unwrapped variable
var errorCodeString2: String! = "Boo Boo"
let anotherErrorString: String = errorCodeString2
let yetAnotherErrorString: String = anotherErrorString
