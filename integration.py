
from manim import *
config.pixel_height = 1080
config.pixel_width = 1920


class BasicIntegrationSlideshow(Scene):
    def construct(self):
        # Start playing the audio for the explanation
        self.add_sound("integration_explanation.mp3")

        # Slide 1: Introduce the general formula for integration
        general_formula = MathTex(r"\int f(x) \, dx", font_size=56)
        self.play(Write(general_formula))
        self.wait(4)  # Duration for the explanation of the general formula
        self.play(FadeOut(general_formula))  # Transition to next slide

        # Slide 2: Display the specific integration problem
        specific_equation = MathTex(r"\int x^2 \, dx", font_size=56)
        self.play(Write(specific_equation))
        self.wait(4)  # Duration for the specific problem explanation
        self.play(FadeOut(specific_equation))  # Transition to next slide

        # Slide 3: Graph the function
        axes = Axes(x_range=[-3, 3], y_range=[0, 9],
                    x_length=6, y_length=6, axis_config={"color": BLUE})
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(lambda x: x**2, color=WHITE)
        graph_label = axes.get_graph_label(graph, label='x^2')

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(6)  # Duration for graph explanation
        self.play(FadeOut(axes), FadeOut(labels), FadeOut(graph),
                  FadeOut(graph_label))  # Transition to next slide

        # Slide 4: Show the area under the curve
        axes = Axes(x_range=[-3, 3], y_range=[0, 9],
                    x_length=6, y_length=6, axis_config={"color": BLUE})
        graph = axes.plot(lambda x: x**2, color=WHITE)
        area = axes.get_area(graph, x_range=[0, 2], color=BLUE, opacity=0.3)

        self.play(Create(axes), Create(graph), FadeIn(area))
        self.wait(6)  # Duration for area explanation
        # Transition to next slide
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(area))

        # Slide 5: Write the solution
        solution = MathTex(r"\frac{1}{3}x^3 + C", font_size=56)
        self.play(Write(solution))
        self.wait(4)  # Duration for solution explanation
        self.play(FadeOut(solution))  # End of slideshow

        self.wait(2)  # Wait before ending the scene
