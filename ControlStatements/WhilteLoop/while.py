a = 0
while a < 10:
    print("Hello")
    a = a + 1

a = 0
while a < 10:
    print("Hey Sri.!", a)
    a = a + 1
else:
    print("else block")
    print("process done")

a = 0
while a < 10:
    print("Print numbers", a)
    a = a + 1
    if a == 2:
        break
else:
    print("else block after while")
    print("process done")

# Break & Continue
# 1.
# Break is used
# to
# stop
# the
# execution
# 2.
# Continue is used
# to
# skip
# the
# particular
# execution

for i in range(1, 10):
    if i == 4:
        break
    print(i)

for i in range(1, 10):
    if i == 4:
        continue
    print(i)

for letter in 'Srihari':
    if letter == 'S' or letter == 'h':
        continue
    elif letter == 'i':
        break
    print('Current Letter :', letter)
