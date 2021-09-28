from manim import *
import numpy as np
# x = lambda t: np.array([t**2-4, 2*t, 0])
# for t in range(-1,3,1):
#     print(x(t))
# print(x)
# print(x(100))

class PlotParametricFunction(Scene):
    def func(self, t):
        return np.array((t**2-4, 2*t, 0))
    def construct(self):
        func = ParametricFunction(self.func, t_min=-1, t_max = 2).set_color(RED)
        self.add(func)
        self.wait(2)