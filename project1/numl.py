from manim import *
class NumberLineTest(Scene):
    def construct(self):
        n = NumberLine(x_min = -3, x_max = 3, include_tip=True, include_numbers=True)
        self.add(n)
        self.wait(2)

class Add_Axes(Scene):
    def construct(self):
        k = Axes()
        self.add(k)
        self.wait(2)