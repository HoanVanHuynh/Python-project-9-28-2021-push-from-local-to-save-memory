from manim import *
import numpy as np

class hello3dworld(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min" :-5,
            "x_max" : 5,
            "y_min" : -5,
            "y_max" : 5,
            "z_min" : -5,
            "z_max" : 5, 
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi=100*DEGREES, theta=-50*DEGREES, distance=6)

        text3d = Line(np.array([1,2,0]), np.array([2,4,0]) )
        text3d.rotate(PI/2, axis =RIGHT)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(text3d))