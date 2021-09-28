from manim import *

class Add_Axes(Scene):
    def construct(self):
        k = Axes()

        f = FunctionGraph(lambda x: x**2, x_min =  -1, x_max = 1, color=BLUE_A)
        self.add(k, f)
        self.wait(2)
