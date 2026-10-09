from graphics import *

def buttonClicked(point, button):
    if (button.getP1().getX() <= point.getX() <= button.getP2().getX()
        and button.getP1().getY() <= point.getY() <= button.getP2().getY()):
        return True
    else:
        return False


def main():
    win = GraphWin("Button Click", 400, 300)

    # Draw the rectangular button
    button = Rectangle(Point(100, 100), Point(300, 160))
    button.draw(win)
    label = Text(Point(200, 130), "Click Here")
    label.draw(win)

    message = Text(Point(200, 220), "")
    message.draw(win)

    # Check 10 mouse clicks
    for i in range(10):
        point = win.getMouse()

        if buttonClicked(point, button):
            message.setText("Button was clicked!")
        else:
            message.setText("Button was NOT clicked.")

    win.getMouse()
    win.close()


main()