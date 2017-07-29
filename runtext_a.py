#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase_a import SampleBase
from rgbmatrix import graphics
import time
import random


class RunText(SampleBase):
    def __init__(self, text):
        super(RunText, self).__init__()
        self.text = text
        #self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./fonts/7x13.bdf")
        textColor = graphics.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pos = offscreen_canvas.width
        my_text = self.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function

def runTheText(text):
    if __name__ == "__main__":
        run_text = RunText(text)
        if (not run_text.process()):
            run_text.print_help()


runTheText('test')