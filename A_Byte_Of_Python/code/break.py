# -*- coding: utf-8 -*-
# filename:continue.py
while True:
    s = input("Enter something:")
    if s == "q":
        break
    if (len(s) < 3):
        continue
    print("input is of sufficient length")

print("done")