# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
#
# z = x + y
# print(type(x), type(y), type(z))
#
# print(z)

"""
5827345 = 5*10^6 + 8*10^5 + 2*10^4 + 7*10^3 + 3*10^2 + 4*10^1 + 5*10^0
6543210
base = n => 0..n-1
base = 2 => 0, 1

1101 = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 8 + 4 + 0 + 1 = 13 
3210

base = 16 => 0..15, A=10, B=11, C=12, D=13, E=14, F=15
BF2 = 11*256 + 15*16 + 2 =  2816 + 240 + 2 = 3058
210 
"""
# x = int(input("Enter x: "), base=20)
# print(x)

# t = True  #  1
# f = False #  0
#
# print(t == 1)

"""
N: 1, 2, 3, 4.....
Z: N, -N, 0, Max 2^63-1

Q: p/q, p - N, q - Z; 1/3=0.(3)
I: ... pi, e, sqrt(2)..
R: Q + I
------------>
C: R + iR
^
|
|
------------->

    0 10000010 11001001000011111100111
    ^     ^               ^
    |     |               |
    |     |               +--- significand = 0.7853975...
    |     |
    |     +------------------- exponent = 2 (130 - 128)
    |
    +------------------------- sign = 0 (positive)

    value= -1(sign) * 2(exponent) * (significand)
    value= -10 * 22 * 0.7853975...
    value= 3.14159...
"""

x = float(input("Enter x: "))
y = float(input("Enter y: "))

print(f"{x + y}")
print(f"{round(x + y, 2)}")
print(f"{x + y:.3f}")
