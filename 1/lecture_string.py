name = input("Enter your name: ")
"""
print("hello ", end="")
print(name)

print("hello", name)
print("hello %s" % name)
"""

print(f"hello {name}")

# "   sasha    " -> "sasha"
name = name.strip()
print(f"hello {name}")

name = name.upper()
print(f"hello {name}")

name = name.capitalize()
print(f"hello {name}")

name = name.title()
print(f"hello {name}")


name = input("Enter your name: ").strip().title()
print(f"hello {name}")

x = 1
y = 2
z = x + y
print(z)


x = int(input("Enter x: "), base=7)
print(x)
y = int(input("Enter y: "), base=16)
print(y)
#z = x + y
#print(type(x), type(y), type(z))
print(x + y)

# 4951934 = 4*10^6 + 9*10^5 + 5*10^4 ....
# 6543210
# osnova: 10, numbers: 0..9
# osnova: n, nubmers: 0..n-1
#
# osnova: 2, numbers: 0, 1
#
# 101 -> 4 + 1 = 5
#
# osnova:7, numbers: 0..6
# 6612451
#
# osnova:16, numbers: 0..9, A 10,B 11,C 12 ,D 13,E 14,F 15
# AF1 = A*16^2 + F*16 + 1 = 2560 + 240 + 1 = 2801

#  3 32222222 22211111111110000000000
#  1 09876543 21098765432109876543210
# +-+--------+-----------------------+
# | |        |                       |
# +-+--------+-----------------------+
#  ^    ^                ^
#  |    |                |
#  |    |                +-- significand
#  |    |
#  |    +------------------- exponent
#  |
#  +------------------------ sign bit
# sign (0,1) * 0.9485817357 (3 byte int) * 2*2 (1byte)
# +- * 0.345 * 10^23
# +- 0.3434E13 = ....*10^13
# numpy -> bfloat8, bfloat16 ...


