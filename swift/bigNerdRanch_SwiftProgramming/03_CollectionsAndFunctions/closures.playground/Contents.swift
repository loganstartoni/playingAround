//: Playground - noun: a place where people can play

import Cocoa

let volunteerCounts = [1, 3, 40, 32, 2, 53, 77, 13]

func sortAscending(_ i: Int, _ j: Int) -> Bool {
    return i < j
}
func sortDescending(_ i: Int, _ j: Int) -> Bool {
    return i > j
}

let ascendingVolunteers = volunteerCounts.sorted(by: sortAscending)
let descendingVolunteers = volunteerCounts.sorted(by: sortDescending)

let ascendingVolunteersClosure = volunteerCounts.sorted(by: { (i: Int, j: Int) -> Bool in return i < j })
let descendingVolunteersClosure = volunteerCounts.sorted(by: { (i: Int, j: Int) -> Bool in return i > j })

let ascendingVolunteersClosure2 = volunteerCounts.sorted(by: { i, j in i < j })
let descendingVolunteersClosure2 = volunteerCounts.sorted(by: { i, j in i > j })

let ascendingVolunteersClosure3 = volunteerCounts.sorted(by: { $0 < $1 })
let descendingVolunteersClosure3 = volunteerCounts.sorted(by: { $0 > $1 })

let ascendingVolunteersClosure4 = volunteerCounts.sorted { $0 < $1 }
let descendingVolunteersClosure4 = volunteerCounts.sorted { $0 > $1 }
