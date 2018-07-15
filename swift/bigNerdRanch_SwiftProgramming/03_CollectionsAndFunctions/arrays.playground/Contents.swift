//: Playground - noun: a place where people can play

import Cocoa

var bucketList: Array<String> = ["Climb Mt. Everest"]
var bucketList2: [String] = ["Climb Mt. Everest"]
var bucketList3 = ["Climb Mt. Everest"]

bucketList.append("Fly Hot air baloon to Fiji.")
bucketList.append("Watch the Lord of the rings in one day.")
bucketList.append("Go on a Walkabout.")
bucketList.append("Scuba Dive in the Great Blue Hole.")
bucketList.append("Fomd a triple rainbow.")

bucketList.remove(at: 2)
bucketList

print(bucketList.count)
print(bucketList.capacity)
print(bucketList[0...2])
print(bucketList[2])

print("")

var newItems = [
    "Fly Hot air baloon to Fiji.",
    "Watch the Lord of the rings in one day.",
    "Go on a Walkabout",
    "Scuba Dive in the Great Blue Hole.",
    "Find a triple rainbow."
]

for item in newItems {
    bucketList3.append(item)
}

print(bucketList.count)
print(bucketList.capacity)
print(bucketList[0...2])
print(bucketList[2])

bucketList3[2] += " in Australia."
bucketList3[0] = "Climb Mt. Kilimanjaro."
bucketList3


print("")

newItems = [
    "Fly Hot air baloon to Fiji.",
    "Watch the Lord of the rings in one day.",
    "Go on a Walkabout.",
    "Scuba Dive in the Great Blue Hole.",
    "Find a triple rainbow."
]

bucketList2 += newItems
bucketList3

print(bucketList.count)
print(bucketList.capacity)
print(bucketList[0...2])
print(bucketList[2])

bucketList3[0] = "Climb Mt. Kilimanjaro."
bucketList3
bucketList3.insert("Toboggan accross America", at: 2)
bucketList3

var myronsList: [String] = bucketList3

let arrayEquals = (bucketList3 == myronsList)

