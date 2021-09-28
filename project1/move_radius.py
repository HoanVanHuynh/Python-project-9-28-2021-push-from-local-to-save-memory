
from manim import *
from math import degrees

class MoveCamera(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min" :-10,
            "x_max" : 10,
            "y_min" : -9,
            "y_max" : 9,
            "z_min" : -9,
            "z_max" : 9, 
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi=100*DEGREES, theta=-50*DEGREES, distance=6)
        square = Square()


        # text3d = Line(np.array([1,2,0]), np.array([2,4,0]) )
        # text3d.rotate(PI/2, axis =RIGHT)
        self.add(square)
        self.play(ShowCreation(axes))
        self.move_camera(theta=120 * DEGREES)
        self.wait(6)
        
        #self.play(ShowCreation(text3d))