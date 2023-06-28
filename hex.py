from turtle import*
speed('fastest')
pencolor('brown')
pensize(2)
for i in range(100):
    fd(100 - i)
    rt(60)
    circle(80,300)
    dot(10,'blue')

mainloop()
