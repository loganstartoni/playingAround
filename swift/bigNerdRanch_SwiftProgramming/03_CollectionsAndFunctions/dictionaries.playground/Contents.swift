//: Playground - noun: a place where people can play

import Cocoa

var movieRatings = ["Donnie Darko": 4, "Chungking Express": 5, "Dark City": 4]

print("I have rated \(movieRatings.count) movies!")

let darkoRating = movieRatings["Donnie Darko"]
let BraveHeartRating = movieRatings["Brave Heart"]

movieRatings["Dark City"] = 5
movieRatings
let oldRating: Int? = movieRatings.updateValue(5, forKey: "Donnie Darko")

if let lastRating = oldRating, let currentRating = movieRatings["Donnie Darko"] {
    print("Old Rating: \(lastRating); currentRating: \(currentRating)")
}


movieRatings["The Cabint of Dr Caligari"] = 5
//movieRatings.removeValue(forKey: "Dark City")
movieRatings["Dark City"] = nil
movieRatings

for (key, value) in movieRatings {
    print("The movie \(key) was rated \(value).")
}

print("")

for key in movieRatings.keys {
    print("The user has rated \(key)")
}

let moviesRated = Array(movieRatings.keys)

