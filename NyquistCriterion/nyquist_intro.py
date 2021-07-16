#!/usr/bin/env python

from manimlib import *

# To watch one of these scenes, run the following:
# python -m manim VideoIRT.py [scene]
# add -n [number] to skip first n animations

class intro(Scene):
    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):
        
        texTitle = TexText("\\underline{The Nyquist Criterion}")
        texTitle.set_color("#ffff00")
        texTitle.scale(2)
        
        self.play(Write(texTitle))

class controlLoop(Scene):
    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):
        
        ###########################################################
        ###########################################################
        # Parameter

        length_box = 5
        length_line = 2
        y_diff = 2
        y_shift = -1
        x_shift = 4.5
        scale = .5

        ###########################################################
        # Plant
        ###########################################################

        plantInputLine = Line(LEFT*0,RIGHT*length_line, color=WHITE)
        plantInputLine.shift(UP*y_diff+UP*y_shift+LEFT*x_shift)

        plantOutputLine = Line(LEFT*0,RIGHT*length_line, color=WHITE)
        plantOutputLine.next_to(plantInputLine.get_corner(RIGHT), RIGHT,buff=0)
        plantOutputLine.shift(RIGHT*(length_box))

        plantBox = Rectangle(height=y_diff*1.5, width=length_box)
        plantBox.next_to(((plantInputLine.get_corner(RIGHT))), RIGHT,buff=0)
        
        plantText = TexText("Plant", "$P_{(s)}$")
        plantText[1].scale(1.5)

        plantText[0].next_to(plantBox.get_center(), LEFT*0)
        plantText[0].shift(UP)
        plantText[1].next_to(plantBox.get_center(), LEFT*0)
        plantText[1].shift(DOWN*0)

        self.play(Write(plantInputLine))
        self.play(Write(plantBox))
        self.play(Write(plantText))
        self.play(Write(plantOutputLine))
 
        plant = VGroup(plantInputLine, plantOutputLine, plantBox, plantText)

        self.play(plant.scale, scale,
                  plant.shift, UP+3*RIGHT, runtime = 2)

        ###########################################################
        # Controller
        ###########################################################
        controllerInputLine = Line(LEFT*0,RIGHT*length_line, color=WHITE)
        controllerInputLine.shift(UP*y_diff+UP*y_shift+UP+1*LEFT+LEFT*x_shift)
        #controllerInputLine.next_to(plantInputLine.get_corner(RIGHT)+length_box, RIGHT,buff=0)
        
        controllerOutputLine = Line(LEFT*0,RIGHT*length_line, color=WHITE)
        controllerOutputLine.next_to(controllerInputLine.get_corner(RIGHT), RIGHT,buff=0)
        controllerOutputLine.shift(RIGHT*(length_box))

        controllerBox = Rectangle(height=y_diff*1.5, width=length_box)
        controllerBox.next_to(((controllerInputLine.get_corner(RIGHT))), RIGHT,buff=0)
        
        controllerText = TexText("Controller", "$C_{(s)}$")
        controllerText[1].scale(1.5)

        controllerText[0].next_to(controllerBox.get_center(), LEFT*0)
        controllerText[0].shift(UP)
        controllerText[1].next_to(controllerBox.get_center(), LEFT*0)
        controllerText[1].shift(DOWN*0)

        controller = VGroup(controllerInputLine, controllerOutputLine, 
                            controllerBox, controllerText)

        controller.scale(scale)

        self.play(Write(controllerInputLine))
        self.play(Write(controllerBox))
        self.play(Write(controllerText))
        self.play(Write(controllerOutputLine))

        ###########################################################
        # Loop
        ###########################################################
        hgt = length_line
        cRadius = length_line / 10

        loopLineDown = Line(LEFT*0, RIGHT*0+DOWN*hgt, color=WHITE)
        loopLineDown.next_to(plantOutputLine.get_corner(RIGHT), DOWN*hgt/2,buff=0)

        lgth = (4*length_line + 2*length_box) / 2 - 1.5*cRadius
        loopLineBottom = Line(LEFT*0, -lgth*RIGHT, color=WHITE)
        loopLineBottom.next_to(loopLineDown.get_corner(BOTTOM), -lgth/2,buff=0)

        hgt = hgt - cRadius;
        loopLineUp = Line(LEFT*0, RIGHT*0+UP*hgt, color=WHITE)
        loopLineUp.next_to(loopLineBottom.get_corner(LEFT), UP*hgt/2,buff=0)

        connectionCircle = Circle(radius = cRadius, color=WHITE)
        connectionCircle.next_to(loopLineUp.get_corner(TOP), UP*2*cRadius,buff=0)

        minusText = TexText("-")        
        minusText.next_to(connectionCircle.get_corner(BOTTOM) + 1.5*cRadius*RIGHT, RIGHT,buff=0)
        minusText[0].scale(1.5)

        arrowLgth = length_line/10
        referenceLine = Line(length_line*LEFT, 0*LEFT, color=WHITE)
        referenceArrow = Arrow(arrowLgth*RIGHT, 0*LEFT, color=WHITE, fill_color=WHITE, stroke_width=0.03)
        referenceLine.next_to(connectionCircle.get_corner(LEFT), LEFT,buff=0)
        referenceArrow.next_to(connectionCircle.get_corner(LEFT), LEFT,buff=0)
        
        referenceText = TexText("r")        
        referenceText.next_to(referenceLine.get_corner(LEFT) + length_line/2*RIGHT + .35*UP, LEFT,buff=0)
        #referenceText[0].scale(1.5)

        controllerArrow = Arrow(arrowLgth*RIGHT, 0*LEFT, color=WHITE, fill_color=WHITE)
        controllerArrow.next_to(controllerInputLine.get_corner(RIGHT), LEFT,buff=0)
        plantArrow = Arrow(arrowLgth*RIGHT, 0*LEFT, color=WHITE, fill_color=WHITE)
        plantArrow.next_to(plantInputLine.get_corner(RIGHT), LEFT,buff=0)
        loopArrow = Arrow(0*RIGHT+arrowLgth*UP, 0*LEFT, color=WHITE, fill_color=WHITE)
        loopArrow.next_to(loopLineUp.get_corner(TOP), BOTTOM,buff=0)
                
        runTime = .2
        self.play(Write(loopLineDown), runtime = runTime)
        self.play(Write(loopLineBottom), runtime = runTime)
        self.play(Write(loopLineUp), runtime = runTime)
        self.play(Write(connectionCircle), runtime = runTime)
        self.play(Write(minusText),
                  Write(referenceArrow), Write(referenceLine),
                  Write(referenceText),
                  Write(controllerArrow), Write(plantArrow), Write(loopArrow),
                  runtime = runTime)