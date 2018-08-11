#!/usr/bin/env python

print("\n> Welcome!")
print("> If you want to know your Body Mass Index (BMI) enter the following questions: \n")

h = input(" >> Enter your height (m): ")
height = float(h)

w = input(" >> Enter your weight (kg): ")
weight = float(w)

bmi = weight / height ** 2
print ("\n >Thank you, your BMI is: ", bmi)
