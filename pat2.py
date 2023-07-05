from turtle import*
speed('slowest')
bgcolor('black')
colors = ['blue','red','orange','purple','green','red']

i= 0
while True:
    pencolor(colors[i%6])
    fd(10+i)
    lt(70)
    i += 1
mainloop()