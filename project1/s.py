from manim import *
class SomeAnimations(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        # some animations display mobjects,...
        self.play(FadeIn(square))
        #...some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))
        # some animations remove mobjects from the screen
        self.play(FadeOut(square))
        self.wait(1)