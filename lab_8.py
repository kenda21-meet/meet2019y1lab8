import turtle
import random



size_x=800
size_y=500
turtle.setup(size_x,size_y)

turtle.penup()

square_size=20

#lists
trash_pos=[]
trash_stamps=[]

turtle.hideturtle() #hide the arrows">"

'''
turtle.register_shape("")
'''

trash=turtle.clone()
trash.shape("circle")



for pos in trash_pos:
    trash.goto(pos)
    trash_stamps.append(trash.stamp())
    trash.hideturtle



def make_trash():
    min_x=-int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    min_y=-int(size_y/2/square_size)+1
    max_y=int(size_y/2/square_size)-1
    trash_x = random.randint(min_x,max_x)*square_size
    trash_y = random.randint(min_y,max_y)*square_size
    trash.goto(trash_x,trash_y)
    trash_pos.append(trash.pos())
    trash_stamps.append(trash.stamp())



for i in range(31):
    make_trash()
    




