from turtle import*
speed('fastest')
colors = ['red', 'purple']
bgcolor('black')
for i in range(8):
    pencolor('red')
    pensize('2')
    fd(100)
   
    
    
    for i in range(8):
        pencolor('blue')
        pensize('2')
        fd(50)
        fillcolor(colors[i%2])
        begin_fill()
    
        for i in range(8):
            pencolor('black')
            pensize('2')
            fd(25)
            lt(360/8)
        end_fill()
        lt(360/8)
    lt(360/8)

        
        

mainloop()
