
x = "aaa"
y = "b"
z = "是的ccc"

x = x.ljust(20, " ")
y = y.ljust(20, " ")
z = z.ljust(20-4, " ")

print(x, end="")
print(y)
print(z, end="")
print(y)