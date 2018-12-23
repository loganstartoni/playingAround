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

func makeTownGrand() -> (Int, Int) -> Int {
    func buildRoads(byAddingLights lights: Int,
                    toExistingLights existingLights: Int) -> Int {
        return lights + existingLights
    }
    return buildRoads
}
var stoplights = 4
let townPlanByAddingLightsToExistingLights = makeTownGrand()
stoplights = townPlanByAddingLightsToExistingLights(4, stoplights)
print("Knowhere has \(stoplights) stoplights.")

func makeTownGrand2(withBudget budget: Int,
                    condition: (Int) -> Bool) -> ((Int, Int) -> Int)? {
    if condition(budget) {
        func buildRoads(byAddingLights lights: Int,
                        toExistingLights existingLights: Int) -> Int {
            return lights + existingLights
        }
        return buildRoads
    } else {
        return nil
    }
}
func evaluate(budget: Int) -> Bool {
    return budget > 10_000
}
stoplights = 4
if let townPlanByAddingLightsToExistingLights2 = makeTownGrand2(withBudget: 1_001, condition: evaluate) {
    stoplights = townPlanByAddingLightsToExistingLights2(4, stoplights)
}
print("Knowhere has \(stoplights) stoplights.")

if let townPlanByAddingLightsToExistingLights2 = makeTownGrand2(withBudget: 10_001, condition: evaluate) {
    stoplights = townPlanByAddingLightsToExistingLights2(4, stoplights)
}
print("Knowhere has \(stoplights) stoplights.")


func makePopulationTracker(forInitialPopulation population: Int) -> (Int) -> Int {
    var totalPopulation = population
    func populationTracker(growth: Int) -> Int {
        totalPopulation += growth
        return totalPopulation
    }
    return populationTracker
}

var currentPopulation = 5_422
let growby = makePopulationTracker(forInitialPopulation: currentPopulation)

growby(500)
growby(500)
growby(500)
currentPopulation = growby(500)
