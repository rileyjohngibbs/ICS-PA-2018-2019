from turtle import Turtle


class RileysTurtle(Turtle):

    def away(self, some_other_turtle):
        # The angle away from another turtle
        angle_toward = self.towards(some_other_turtle)
        angle_away = (angle_toward + 180) % 360
        return angle_away


riley = RileysTurtle()
leo = Turtle()

riley.left(90)
riley.forward(50)
leo.forward(50)

print(riley.towards(leo))  # Works fine!
print(leo.towards(riley))  # Works fine!
print(riley.away(leo))  # Works fine!
print(leo.away(riley))  # Does not work! Why?