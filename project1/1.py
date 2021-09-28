from manim import *
import numpy as np
class h(Scene):
    def construct(self):
        k = Axes()

        l = ParametricFunction(self.func, t_min =  -5, t_max = 5, color=BLUE_A)
        self.add(k, l)
        self.wait(2)
    def func(self, t):
        return [t, t**3, 0]

class k(Scene):
    def construct(self):
        func = ParametricFunction(lambda t: np.array([2*np.sin(3*t)*np.cos(t),2*np.sin(3*t)*np.sin(t), 0,]), t_min=0, t_max=2*PI).shift(LEFT*3)
        self.add(func)
        