from manim import *
import numpy as np


class pro(Scene):
    def construct(self):
        func = ParametricFunction(lambda t: np.array([2*np.sin(3*t)*np.cos(t),2*np.sin(3*t)*np.sin(t), 0,]), t_min=0, t_max=2*PI).shift(LEFT*3)
        self.add(func)
        self.wait(4)