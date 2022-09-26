from turtle import*

speed('fast')
i = 1
while True:
    fd (10+i)

    for j in range (6):
        fd(100)
        lt(360/6)

    lt(360/6)
    i+=5
    write(i)

    if i>100:
        break

mainloop()