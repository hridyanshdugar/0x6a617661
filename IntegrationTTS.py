from gtts import gTTS

tts_script = """
Integration is a fundamental concept in calculus. The general form of an indefinite integral is represented as the integral of f of x with respect to x.
Let's consider a specific example: the integral of x squared.
Here's the graph of the function x squared. It forms a parabolic shape.
The integral represents the area under the curve. We are shading the area from x equals zero to x equals two.
The solution to our integral, one third x cubed plus C, where C is the constant of integration.
This concludes our example of integrating x squared.
"""

tts = gTTS(text=tts_script, lang='en')
tts.save("integration_explanation.mp3")
