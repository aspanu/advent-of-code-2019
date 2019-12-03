import math

input = """83285
96868
121640
51455
128067
128390
141809
52325
68310
140707
124520
149678
87961
52040
133133
52203
117483
85643
84414
86558
65402
122692
88565
61895
126271
128802
140363
109764
53600
114391
98973
124467
99574
69140
144856
56809
149944
138738
128823
82776
77557
51994
74322
64716
114506
124074
73096
97066
96731
149307
135626
121413
69575
98581
50570
60754
94843
72165
146504
53290
63491
50936
79644
119081
70218
85849
133228
114550
131943
67288
68499
80512
148872
99264
119723
68295
90348
146534
52661
99146
95993
130363
78956
126736
82065
77227
129950
97946
132345
107137
79623
148477
88928
118911
75277
97162
80664
149742
88983
74518"""

def getFuel(mass: int):
    return math.floor(mass/3) - 2

def getAllFuel(input: str):
    sum = 0
    for line in input.splitlines():
        sum += getFuel(int(line))

    return sum

print("Sum is: " + str(getAllFuel(input)))

'''
--- Part Two ---
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
'''

def getFuelRecursive(mass: int):
    fuelMass = getFuel(mass)

    if fuelMass <= 0:
        return 0
    
    return fuelMass + getFuelRecursive(fuelMass)

def getAllFuelRecursive(input: str):
    sum = 0
    for line in input.splitlines():
        sum += getFuelRecursive(int(line))

    return sum

print ("Recursive (1b) sum is: " + str(getAllFuelRecursive(input)))

