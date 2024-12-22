from manim import *


class TextToVideo(Scene):
    def construct(self):
        text = Text("Hello Dennis, Welcome to Manim!")

        self.play(Write(text))
        self.wait(5)

        # Step 3: Transform the text into a new message
        new_text = Text("Python animations made easy!")
        self.play(Transform(text, new_text))
        self.wait(5)
        #Add sound 
        self.add_sound("/Users/air/Gig/audio/hello_music.mp3")

        # Step 4: Fade out the text

        self.play(FadeOut(text))
