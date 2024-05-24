import turtle
import sys

sys.setrecursionlimit(10000)

class FractalPlant:
    def __init__(self, initial_word, iterations, angle, length):
        self.rules = {
            "X": "F+[[X]-X]-F[-FX]+X",
            "F": "FF"
        }
        self.initial_word = initial_word
        self.iterations = iterations
        self.angle = angle
        self.length = length

    def apply_rules(self, word):
        new_word = ""
        for char in word:
            new_word += self.rules.get(char, char)
        return new_word

    def generate_word(self):
        word = self.initial_word
        for _ in range(self.iterations):
            word = self.apply_rules(word)
        return word

    def draw(self, word):
        turtle.speed("fastest")
        turtle.bgcolor("white")
        turtle.color("green")
        turtle.width(3)
        turtle.hideturtle()

        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.setheading(90)

        stack = []
        for char in word:
            if char == "F":
                turtle.forward(self.length)
            elif char == "+":
                turtle.left(self.angle)
            elif char == "-":
                turtle.right(self.angle)
            elif char == "[":
                position = turtle.position()
                heading = turtle.heading()
                stack.append((position, heading))
            elif char == "]":
                position, heading = stack.pop()
                turtle.penup()
                turtle.setposition(position)
                turtle.setheading(heading)
                turtle.pendown()

    def run(self):
        final_word = self.generate_word()
        self.draw(final_word)
        turtle.done()

if __name__ == "__main__":
    plant_growth = FractalPlant("X", 5, 25, 3)
    plant_growth.run()
