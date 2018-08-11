#!/usr/bin/env python

import numpy as np

baseball = [[180, 78.4],[215, 102.7],[210, 98.5],[188, 75.2]] # lista de listas

updated = [[18],[21],[21],[18]] # lista de listas

###############################################################################

print("\n A) Variables: baseball y updated\n")

print(baseball)
print(updated)

print("\n B) Tipos de variables: baseball y updated\n")

print(type(baseball))
print(type(updated))

#print("\n C) Formas de variables: baseball y updated\n)

#print(baseball.shape)

#print(updated.shape)

###############################################################################

np_baseball = np.array(baseball)

print("\n A) Variable array: np_baseball\n")

print(np_baseball)

print("\n A) Tipo de variable array: np_baseball\n")

print(type(np_baseball))

print("\n B) Forma de variable array: np_baseball\n")

print(np_baseball.shape)

###############################################################################

print("\nAdición de array -> np_baseball + list -> updated\n")

print(np.append(updated))

print("\n A) La variable np_baseball cambió? (3)\n")

print(np_baseball)

print("\n B) La forma de np_baseball cambió? (3)\n")

print(np_baseball.shape)

print("\n C) El tipo de variable cambió?\n")

print(type(np_updated))

###############################################################################

print("\n Se define la variable conversion como array: ([0.0254, 0.453592, 1]\n")

conversion = np.array([0.0254, 0.453592, 1])

###############################################################################

#print("\n Se multiplican las variables np_baseball * conversion\n")

#print(np_baseball*conversion)

#print("\n A) La variable np_baseball cambió?\n")

#print(np_baseball)

#print("\n B) La forma de np_baseball cambió?\n")

#print(np_baseball.shape)

#print("\n C) El tipo de variable cambió?\n")

#print(type(np_updated))
