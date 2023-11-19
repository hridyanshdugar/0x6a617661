from manim import *

# Set the window size and resolution
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.0

class Test3DShapes(ThreeDScene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes()
        
        # Define 3D objects
        sphere = Sphere(center=(0, 0, 0))
        cylinder = Cylinder(radius=1, height=3).next_to(sphere, RIGHT, buff=1)
        cube = Cube(side_length=2).next_to(cylinder, RIGHT, buff=1)

        # Define labels
        sphere_label = MathTex("Sphere").scale(0.5).next_to(sphere, DOWN)
        cylinder_label = MathTex("Cylinder").scale(0.5).next_to(cylinder, DOWN)
        cube_label = MathTex("Cube").scale(0.5).next_to(cube, DOWN)
        
        # Group all objects and labels
        shapes_group = Group(sphere, cylinder, cube, sphere_label, cylinder_label, cube_label)

        # Focus on the objects
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Begin animation sequence
        self.add_fixed_in_frame_mobjects(sphere_label, cylinder_label, cube_label)  # Keep the labels from moving with the shapes
        self.play(Create(axes), Create(sphere), Create(cylinder), Create(cube))
        self.play(Write(sphere_label), Write(cylinder_label), Write(cube_label))
        self.wait(2)

        # Change camera view
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=2)
        self.begin_ambient_camera_rotation(rate=0.2)  # Start rotating camera
        self.wait(4)

        # Conclude the scene
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=2)
        self.wait(2)