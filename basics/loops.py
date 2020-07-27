countdown=5

while countdown:
    print(countdown)
    countdown=countdown-1

print("happy new year")

for letter in 'abcdefghijk':
    print(letter.upper())

names=['swathi','rekha','quit','bhanu','visaka']

for name in names:
    if name=='quit':
        break
    print(name)

for name in names:
    if name=='quit':
        continue
    print(name)