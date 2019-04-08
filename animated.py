from graphics import GraphWin, Point, Rectangle, Circle, Text
from time import sleep

win = GraphWin("Animation", 500, 500)
win.setCoords(0,0,50,50)

#####begin() BEGINS THE SEQUENCE######

def begin():
    #Ready? Text
    begText1 = Text(Point(25,20), "Ready?")
    begText1.setFace("times roman")
    begText1.draw(win)
    sleep(1.5)
    begText1.undraw()
    sleep(0.5)

    #"Here's a point" Text and Plotting first point
    begText2 = Text(Point(25,20), "Here's a point.")
    begText2.setFace("times roman")
    begText2.draw(win)
    point1 = Point(25,25)
    point1.draw(win)
    sleep(1.5)
    begText2.undraw()
    sleep(0.5)

    #moving First point
    clickAnywhere = Text(Point(25, 20),
        "Press 'l' or 'r' to move the point off the screen in either direction.")
    clickAnywhere.setFace("times roman")
    clickAnywhere.draw(win)
    #win.getMouse()
    key = win.getKey()
    clickAnywhere.undraw()
    if key == "r":
        for i in range(55):
            point1.move(.5,0)
            sleep(0.05)
    if key == "l":
        for i in range(55):
            point1.move(-.5,0)
            sleep(0.05)
    point1.undraw()

    #First Congrats Text and Transition
    greatxt = Text(Point(25,20), "Great!")
    greatxt.setFace("times roman")
    greatxt.draw(win)
    sleep(1.5)
    greatxt.undraw()
    tranText = Text(Point(25,20), "Now, click your mouse on the window to create a red circle")
    tranText.setFace("times roman")
    tranText.draw(win)
    win.getMouse()
    tranText.undraw()
    #call to next function
    drawCircle()

def drawCircle():
    #draws the red circle
    radius = 5
    circle1 = Circle(Point(25, 25), radius)
    circle1.setFill("red")
    circle1.draw(win)

    #good job text
    goodJob = Text(Point(25, 35), "Good Job!")
    goodJob.setFace("times roman")
    goodJob.draw(win)
    sleep(2)
    goodJob.undraw()

    #grow text
    grow = Text(Point(25,35), "Now we will grow our circle.")
    grow.setFace("times roman")
    grow.draw(win)
    sleep(1.5)
    grow.undraw()
    sleep(.5)

    #click on the window text
    clickToGrow = Text(Point(25,35), "Click on the window")
    clickToGrow.setFace("times roman")
    clickToGrow.draw(win)
    
    
    win.getMouse()
    circle1.undraw()
    clickToGrow.undraw()
    
    #grow your circle
    for i in range(10):
        radius = radius + 1
        circle2 = Circle(Point(25, 25), radius)
        circle2.setFill("red")
        circle2.draw(win)
        circle2.undraw()
    circle2.draw(win)

    #WOW text for growing your circle
    wow = Text(Point(25, 43), "WOW!")
    wow.setSize(30)
    wow.setFace("times roman")
    wow.draw(win)
    sleep(2)
    wow.undraw()

    #Shrink the circle prompt
    thenText = Text(Point(25, 43), "Now, click to shrink it back down!")
    thenText.setFace("times roman")
    thenText.setSize(25)
    thenText.draw(win)
    
    win.getMouse()
    thenText.undraw()
    circle2.undraw()

    #Shrink your circle Function
    for i in range(10):
        radius = radius - 1
        circle3 = Circle(Point(25, 25), radius)
        circle3.setFill("red")
        circle3.draw(win)
        circle3.undraw()
    circle3.draw(win)


    #small wow
    wow2 = Text(Point(25, 33), "wow")
    wow2.setFace("times roman")
    wow2.draw(win)
    sleep(.35)
    wow2.undraw()

    wow2 = Text(Point(25, 33), "wow.")
    wow2.setFace("times roman")
    wow2.draw(win)
    sleep(.5)
    wow2.undraw()

    wow2 = Text(Point(25, 33), "wow..")
    wow2.setFace("times roman")
    wow2.draw(win)
    sleep(.5)
    wow2.undraw()

    wow2 = Text(Point(25, 33), "wow...")
    wow2.setFace("times roman")
    wow2.draw(win)
    sleep(2)
    wow2.undraw()

    circle3.undraw()
    #call to next function
    moveCircle()

def moveCircle():
    #first move circle text
    moveCircle = Text(Point(25, 33), "Now lets create and move circles wherever you'd like")
    moveCircle.setFace("times roman")
    moveCircle.draw(win)
    sleep(1.5)
    moveCircle.undraw()

    #second move circle text
    moveCircle2 = Text(Point(25, 33), "When the red circle appears, move it by pressing 'w' 'a' 's' 'd'")
    moveCircle2.setFace("times roman")
    moveCircle2.draw(win)
    sleep(6)
    moveCircle2.undraw()

    #third color circle text
    moveCircle2 = Text(Point(25, 33), "You can create a new circle with a different color by pressing 'r', 'g', 'b'")
    moveCircle2.setFace("times roman")
    moveCircle2.draw(win)
    sleep(6)
    moveCircle2.undraw()

    #new circle def
    circle = Circle(Point(25, 25), 5)
    setfill = "red"
    circle.setFill(setfill)
    circle.draw(win)

    #move circle with for loops and an if function
    for i in range(1000):
        key = win.getKey()
        if key == "w":
            for w in range(1):
                circle.move(0,2)
        if key == "s":    
            for s in range(1):
                circle.move(0,-2)
        if key == "d":
            for d in range(1):
                circle.move(2,0)
        if key == "a":
            for a in range(1):
                circle.move(-2,0)
        
        if key == "r":
            circle = Circle(Point(25, 25), 5)
            setfill = "red"
            circle.setFill(setfill)
            circle.draw(win)
        if key == "g":
            circle = Circle(Point(25, 25), 5)
            setfill = "green"
            circle.setFill(setfill)
            circle.draw(win)
        if key == "b":
            circle = Circle(Point(25, 25), 5)
            setfill = "blue"
            circle.setFill(setfill)
            circle.draw(win)
        if key == "x":
            win.close()
            begin()
        #circle.undraw()
            
    win.close()


    
begin()
#moveCircle()


