import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
    i=1
    sharma=turtle.Turtle()
    sharma.shape("turtle")
    sharma.color("black")
    sharma.speed(1)
    while(i<=4):
        
        sharma.forward(100)
        sharma.right(90)
        i=i+1
   

    vishal=turtle.Turtle()
    vishal.shape("arrow")
    vishal.color("blue")
    vishal.circle(100)
    vishal.speed(1)


    window.exitonclick()
draw_square()    
