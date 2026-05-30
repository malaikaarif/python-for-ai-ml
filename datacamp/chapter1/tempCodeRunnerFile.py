# 0.1+0.2 != 0.3 becoz computers store no.s in bianry and 0.1 = 0.0001001010101 (infinite)
x = 0.1 + 0.2
print(x == 0.3)    # what prints and WHY?   -- it will print false beoz sum of 0.1 and 0.2 is 0.300000004

# Fix it using round()

print(round(0.1+0.2,1))
