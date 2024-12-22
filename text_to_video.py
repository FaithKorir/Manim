from manim import *


class TextToVideo(Scene):
    def construct(self):
        text = Text("Hello Dennis, Welcome to Manim!")
        
        self.play(Write(text))
        self.wait(5)
        
        new_text = Text("Python animations made easy!")
        self.play(Transform(text, new_text))
        self.wait(5)
        
        self.add_sound("/Users/air/Gig/audio/hello_music.mp3")

        self.play(FadeOut(text))
