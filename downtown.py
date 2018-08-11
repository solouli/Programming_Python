#!/usr/bin/env python

print("\n> Welcome!")
print("> If you want to know if you can drive downtown safely, answer the following question(s): \n")

f = input("A) How much fuel do you have?: $")
fuel = int(f)

#if isinstance(f, basestr):
#    print("\n W A R N I N G: Expected numeric, try again!")

if fuel > 3:
  print("\n> It's OK")
  print("> You can drive downtown.")
else:
    print("\n> Sorry, you're out of fuel...\n")
    m = input("B) How much money do you have?: $")
    money = int(m)
    if money > 10:
        print("\nA T T E N T I O N: You better buy some gas at the next gas station.")
    else:
        print("\nA T T E N T I O N: You better stay at home.")

print("\n> You're welcome!\n")
