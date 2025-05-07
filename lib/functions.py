#!/usr/bin/env python3

def greet_programmer():

    print(f"Hello, programmer!")

greet_programmer()

def greet(name="Guido"):
    print(f"Hello, {name}!")

greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1, num2):
    return num1 + num2;
add(45,55)

def halve(number):
    return number / 2
