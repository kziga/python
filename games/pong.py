# pong game

import turtle # Turtle is a graphics library used here instead of pyGame
import os

win = turtle.Screen()

win.title( "PONG" )                # Set the title of the window
win.bgcolor( "black" )             # Set the background color to black
win.setup( width=800, height=600 ) # Set the size of the window

win.tracer( 0 ) # Stop the window from updating, forcing manual updating

# Paddle A
paddleA = turtle.Turtle() # Create a turtle object for the paddle
paddleA.speed( 0 ) # Set the animation speed to the max
paddleA.shape( "square" ) # default shape is 20x20 px
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.color( "white" )
paddleA.penup() # don't draw lines
paddleA.goto( -350, 0 )

# Paddle B
paddleB = turtle.Turtle() # Create a turtle object for the paddle
paddleB.speed( 0 ) # Set the animation speed to the max
paddleB.shape( "square" ) # default shape is 20x20 px
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.color( "white" )
paddleB.penup() # don't draw lines
paddleB.goto( +350, 0 )

# Ball
ball = turtle.Turtle() # Create a turtle object for the paddle
ball.speed( 0 ) # Set the animation speed to the max
ball.shape( "square" ) # default shape is 20x20 px
ball.color( "white" )
ball.penup() # don't draw lines
ball.goto( 0, 0 )
ball.dx = 0.25 # Change in the ball position
ball.dy = 0.25

# Create a Pen (Turtle)
pen = turtle.Turtle()
pen.speed( 0 )
pen.color( "white" )
pen.penup()
pen.hideturtle()
pen.goto( 0, 260 )
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal") )

scoreA = 0
scoreB = 0

# Functions
def paddleAUp():
	y = paddleA.ycor()
	y += 20 # move 20 pixels up
	paddleA.sety( y )

def paddleADown():
	y = paddleA.ycor()
	y -= 20 # move 20 pixels up
	paddleA.sety( y )

def paddleBUp():
	y = paddleB.ycor()
	y += 20 # move 20 pixels up
	paddleB.sety( y )

def paddleBDown():
	y = paddleB.ycor()
	y -= 20 # move 20 pixels up
	paddleB.sety( y )

# Keyboard binding
win.listen()
win.onkeypress( paddleAUp, "w" ) # on "w" press, call paddleAUp
win.onkeypress( paddleADown, "s" ) # on "w" press, call paddleAUp
win.onkeypress( paddleBUp, "Up" ) # on "w" press, call paddleAUp
win.onkeypress( paddleBDown, "Down" ) # on "w" press, call paddleAUp


# Main game loop
while True:
    win.update() # Update the window

    # Move the ball
    ball.setx( ball.xcor() + ball.dx )
    ball.sety( ball.ycor() + ball.dy )

    # Border checking, 290 because the ball is 20 px and the top is +300
    if ball.ycor() > 290:
    	ball.sety( 290 )
    	ball.dy *= -1 # reverse direction
    	os.system( "afplay bounce.wav&" )

    if ball.ycor() < -290:
    	ball.sety( -290 )
    	ball.dy *= -1 # reverse 
    	os.system( "afplay bounce.wav&" )

    if ball.xcor() > 390:
    	ball.goto( 0, 0 )
    	ball.dx *= -1
    	scoreA += 1
    	pen.clear()
    	pen.write("Player A: {}  Player B: {}".format( scoreA, scoreB ), align="center", font=("Courier",24,"normal") )

    if ball.xcor() < -390:
    	ball.goto( 0, 0 )
    	ball.dx *= -1
    	scoreB += 1
    	pen.clear()
    	pen.write("Player A: {}  Player B: {}".format( scoreA, scoreB ), align="center", font=("Courier",24,"normal") )

    # To detect a hit with a paddle we just need to compare the ball position to the paddle position including the paddle size

    if ( ball.xcor() > 340 and ball.xcor() < 350 ) and ( ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50 ):
    	# Hit paddleB
    	ball.setx( 340 )
    	ball.dx *= -1
    	os.system( "afplay bounce.wav&" )

    if ( ball.xcor() < -340 and ball.xcor() > -350 ) and ( ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50 ):
    	# Hit paddleA
    	ball.setx( -340 )
    	ball.dx *= -1
    	os.system( "afplay bounce.wav&" )







