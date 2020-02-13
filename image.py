import random

nums = [[20,60], [80, 120], [140, 180], [200, 240], [260,300], [320, 360], [380, 420], [440, 480]]

randColors = []
for i in range(8):
    randColor = str(random.randint(0,255)) + " " + str(random.randint(0,255)) + " " + str(random.randint(0,255)) + " "
    randColors.append(randColor)

print randColors

arr = []
for y in range(500):
    x = []
    for i in range(500):
        x.append("255 0 0 ")
    arr.append(x)

for num in nums:
    randColor = randColors[random.randint(0,7)]
    for y in range(500):
        for x in range(500):
            if y>=num[0] and y<=num[1] and x>=num[0] and x<=num[1]:
                arr[y][x] = randColor

fp = open("image.ppm", "w+")
fp.write("P3\n500 500\n255\n")
for y in range(500):
    for x in range(500):
        fp.write(arr[x][y])

fp.close()
