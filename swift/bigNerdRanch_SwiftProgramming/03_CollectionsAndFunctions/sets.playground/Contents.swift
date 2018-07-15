//: Playground - noun: a place where people can play

import Cocoa

var groceryBag: Set = ["Apples", "Oranges", "Pineapple"]

groceryBag = Set<String>()
groceryBag.insert("Apples")
groceryBag.insert("Oranges")
groceryBag.insert("Pineapple")

groceryBag = Set(["Apples", "Oranges", "Pineapple"])

groceryBag = ["Apples", "Oranges", "Pineapple"]

for  item in groceryBag {
    print(item)
}

let hasBananas = groceryBag.contains("Bananas")

let friendsGroceryList: Set = ["Bananas", "Cereal", "Oranges", "Milk"]
let commonGroceryList = groceryBag.union(friendsGroceryList)

let roommatesGroceryBag = Set(["Apples", "Bananas", "Cereal", "Toothpaste"])
let itemsToReturn = roommatesGroceryBag.intersection(commonGroceryList)

let yourSecondBag = Set(["Berries", "Yogurt"])
let roommatesSecondBag = Set(["Grapes", "Honey"])
let disjoint = yourSecondBag.isDisjoint(with: roommatesSecondBag)
