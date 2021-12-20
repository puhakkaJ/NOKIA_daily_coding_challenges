"""Created 27.5.2021
Challenge from https://edabit.com/challenge/pa65DgwG5HMbtf6iY
Classes For Fetching Information on a Sports Player

Explanation:
Create a class that takes the following four arguments for a particular football player: name, age, height and weight.
Also, create three functions for the class that returns the following strings:
get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"."""


class Athlete:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def get_age(self):
        return self.name + " is age " + str(self.age)

    def get_height(self):
        return self.name + " is " + str(self.height) + "cm"

    def get_weight(self):
        return self.name + " weights " + str(self.weight) + "kg"

