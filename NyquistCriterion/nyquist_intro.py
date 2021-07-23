#!/usr/bin/env python

from os import set_blocking
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
        self.wait()
        self.play(texTitle.scale, 0)

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

        controlLoop = VGroup(plant, controller,
                             loopLineDown, loopLineBottom, loopLineUp,
                             connectionCircle, minusText, referenceLine, referenceText,
                             referenceArrow, controllerArrow, plantArrow, loopArrow)

class Ts(Scene):
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

        plant = VGroup(plantInputLine, plantOutputLine, plantBox, plantText)

        plant.scale(scale)
        plant.shift(UP+3*RIGHT)

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
                

        controlLoop = VGroup(plant, controller,
                             loopLineDown, loopLineBottom, loopLineUp,
                             connectionCircle, minusText, referenceLine, referenceText,
                             referenceArrow, controllerArrow, plantArrow, loopArrow)

        self.play(Write(controlLoop))

        ###########################################################
        # Ts
        ###########################################################

        textTs = Tex(   
                        "T_{(s)} =",
                        "{C_{(s)} P_{(s)}",
                        "\\over",
                        "1 + C_{(s)} P_{(s)}}",
                        color=WHITE
                    )

        textTsWithL = Tex(   
                        "T_{(s)} =",
                        "{L_{(s)}",
                        "\\over",
                        "1 + L_{(s)}}",
                        color=WHITE
                    )

        textMuNu = Tex(   
                        " =",
                        "{\\nu_{(s)}",
                        "\\over",
                        "\\mu_{(s)}}",
                        color=WHITE
                    )

        textTs.next_to(controlLoop.get_corner(BOTTOM), 6*DOWN)
        textTsWithL.next_to(controlLoop.get_corner(BOTTOM), 6*DOWN)
        textMuNu.next_to(textTsWithL.get_corner(RIGHT), 3*RIGHT)

        self.play(Write(textTs))


        ###########################################################
        # Forward
        ###########################################################
        self.play(
                    plantText.set_color, ORANGE,
                    controllerText.set_color, ORANGE,
                    textTs[1].set_color, ORANGE
                )

        self.wait(1)

        ###########################################################
        # Backward
        ###########################################################
        self.play(
                    plantText.set_color, BLUE,
                    controllerText.set_color, BLUE,
                    textTs[3].set_color, BLUE,
                    minusText.set_color, BLUE
                )

        self.wait(1)

        ###########################################################
        # Back and intro L
        ###########################################################
        self.play(
                    plantText.set_color, WHITE,
                    controllerText.set_color, WHITE,
                    textTs[1].set_color, WHITE,
                    textTs[3].set_color, WHITE,
                    minusText.set_color, WHITE
                )


        self.wait(1)

        self.play(
                ReplacementTransform(textTs[1],textTsWithL[1]),
                ReplacementTransform(textTs[3],textTsWithL[3])
        )

        ###########################################################
        # Mu und Nu
        ###########################################################
        self.play(Write(textMuNu))

        self.wait(1)
        self.play(
            textMuNu[3].set_color, ORANGE
        )


        ###########################################################
        # Hurwitz - Pole Zero Plor
        ###########################################################
        axes = Axes(
            x_range=(-3, 3), y_range=(-3, 3),
            height=6, width=6,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=30,
            num_decimal_places=0,
        )

        xLabel = Tex("\\Re\{s_{\mu}\}")
        xLabel.move_to(axes.c2p(4, 0))
        yLabel = Tex("\\Im\{s_{\mu}\}")
        yLabel.move_to(axes.c2p(1, 3))

        grid = VGroup(axes, xLabel, yLabel)

        #grid.scale(0)
        grid.shift(1.2*UP)


        ###########################################################
        self.play(controlLoop.scale, 0)
        self.play(FadeIn(grid), grid.scale, .75)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        # like so:
        dot = Dot(color=ORANGE)
        dot.move_to(axes.c2p(1, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(2, 0)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(0, 0)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(-2, 0)))
        self.wait()

        dot2 = Dot(color=ORANGE)
        dot2.move_to(axes.c2p(-2, 0))
        self.play(FadeIn(dot2, scale=0.5))

        self.play(
            dot.animate.move_to(axes.c2p(-1, 1)),
            dot2.animate.move_to(axes.c2p(-1, -1))
        )
        self.wait()
        self.play(
            dot.animate.move_to(axes.c2p(1, 1.5)),
            dot2.animate.move_to(axes.c2p(1, -1.5))
        )
        self.wait()
        self.play(
            dot.animate.move_to(axes.c2p(-1, .5)),
            dot2.animate.move_to(axes.c2p(-1, -.5))
        )


        self.wait()
        self.play(
            grid.scale, 0,
            textTsWithL.scale, 0,
            textTs.scale, 0,
            dot.scale, 0, dot2.scale, 0,
            textMuNu.scale, 0
        )

        ###########################################################
        # Possibilities
        ###########################################################


class PoleZero(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-3, 3), y_range=(-3, 3),
            height=6, width=6,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=30,
            num_decimal_places=0,
        )

        xLabel = Tex("\\Re\{s_{\mu}\}")
        xLabel.move_to(axes.c2p(4, 0))
        yLabel = Tex("\\Im\{s_{\mu}\}")
        yLabel.move_to(axes.c2p(1, 3))

        grid = VGroup(axes, xLabel, yLabel)

        grid.scale(.75)
        grid.shift(UP)


        self.add(grid)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        # like so:
        dot = Dot(color=ORANGE)
        dot.move_to(axes.c2p(1, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(2, 0)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(0, 0)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(-2, 0)))
        self.wait()

        dot2 = Dot(color=ORANGE)
        dot2.move_to(axes.c2p(-2, 0))
        self.play(FadeIn(dot2, scale=0.5))

        self.play(
            dot.animate.move_to(axes.c2p(-1, 1)),
            dot2.animate.move_to(axes.c2p(-1, -1))
        )
        self.wait()
        self.play(
            dot.animate.move_to(axes.c2p(1, 1.5)),
            dot2.animate.move_to(axes.c2p(1, -1.5))
        )
        self.wait()
        self.play(
            dot.animate.move_to(axes.c2p(-1, .5)),
            dot2.animate.move_to(axes.c2p(-1, -.5))
        )

class possibilities(Scene):
    def construct(self):
        
        texHeader = TexText("\\underline{How to check for Hurwitz?}")
        texHeader.set_color(ORANGE)

        self.add(texHeader)
        self.play(texHeader.scale, 1.8)
        self.play(
            texHeader.scale, .5,
            texHeader.shift, (3.2*UP+4*LEFT),
            texHeader.set_color,WHITE
        )

        textOptions = [ 
            TexText("Calcualte poles explicity"),
            TexText("Use the Routh-Schema"),
            TexText("Use Nyquist criterion"),
            TexText("...")
        ]

        for index, option in enumerate(textOptions):
            if index <= 0:
                textOptions[index].shift((len(textOptions) / 2) * UP)
            else:
                textOptions[index].next_to(textOptions[index-1].get_corner(BOTTOM), 2*DOWN)
            
            self.play(Write(textOptions[index]))
            self.wait()

        nyquistOption = TexText("\\underline{Nyquist criterion}");

        self.play(
            texHeader.scale, 0,
            textOptions[0].scale, 0,
            textOptions[1].scale, 0,
            textOptions[2].scale, 0,
            textOptions[3].scale, 0,
        )
        self.play(
            nyquistOption.scale, 1.2,
            nyquistOption.shift, (UP),
            nyquistOption.set_color, ORANGE,
        )

        fact1 = TexText("Graphical way")
        fact2 = TexText("It uses $L_{(j\omega)}$")
        fact3 = TexText("Less infomration necessary")
        fact4 = TexText("There is a simplified Nyquist criterion")

        fact1.shift(2*UP+3*LEFT)
        fact2.shift(2*DOWN+2*RIGHT)
        fact3.shift(3*UP+.8*LEFT)
        fact4.shift(1.2*DOWN+2*RIGHT)


        fact1.scale(1.1)
        fact2.scale(1.2)
        fact3.scale(.9)
        fact3.scale(.7)

        self.play(Write(fact1))
        self.wait()
        self.play(Write(fact2))
        self.wait()
        self.play(Write(fact3))
        self.wait()
        self.play(Write(fact4))

        self.play(
            fact1.shift, 5*UP+5*LEFT,
            fact2.shift, 5*DOWN+5*RIGHT,
            fact3.shift, 5*UP+1*LEFT,
            fact4.shift, 5*DOWN+3*RIGHT,
            nyquistOption.scale, 0
        )

class deltaArg(Scene):
    def construct(self):
        
        if True:
            textExample = Tex(   
                                "F_{(j\\omega)}",
                                ":=",
                                "(",
                                "j\\omega",
                                "- ",
                                "\\beta",
                                ")",
                                color=WHITE
                            )

            textBetaIn = Tex("\\qquad", "\\beta", " \\in \\mathbb{C}")
            textBetaIn[0].set_color(ORANGE)

            textBetaIn.next_to(textExample, RIGHT, 2+LEFT)

            self.play(Write(textExample))
            self.play(textExample[5].set_color, ORANGE)
            self.play(Write(textBetaIn))

            self.wait()
            self.play(
                textBetaIn[0].set_color, WHITE,
                textExample[5].set_color, WHITE
            )

            formula = VGroup(textExample, textBetaIn)

            self.play(
                formula.scale, .9, 
                formula.shift, 3.2*UP+4*LEFT
            )
        else:
            textExample = Tex(   
                                "F_{(j\\omega)}",
                                ":=",
                                "(",
                                "j\\omega",
                                "- ",
                                "\\beta",
                                ")",
                                color=WHITE
                            )

            textBetaIn = Tex("\\qquad", "\\beta", " \\in \\mathbb{C}")
            textBetaIn.next_to(textExample, RIGHT, 2+LEFT)

            formula = VGroup(textExample, textBetaIn)
            formula.scale(.9), 
            formula.shift(3.2*UP+4*LEFT)
            self.add(formula)

        # -----------------------------------------------
        axes = Axes(
            x_range=(-3, 3), y_range=(-3, 3),
            height=6, width=6,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        #axes.add_coordinate_labels(
        #    font_size=30,
        #    num_decimal_places=0,
        #)

        xLabel = Tex("\\Re\{\\beta\}")
        xLabel.move_to(axes.c2p(4, 0))
        xLabel2 = Tex("\\Re\{F_{(j\\omega)}\}")
        xLabel2.move_to(axes.c2p(4.2, 0))

        yLabel = Tex("\\Im\{\\beta\}")
        yLabel.move_to(axes.c2p(1, 3))
        yLabel2 = Tex("\\Im\{F_{(j\\omega)}\}")
        yLabel2.move_to(axes.c2p(1, 3.3))

        grid = VGroup(axes, xLabel, yLabel)
        gridAll = VGroup(grid, xLabel2, yLabel2)

        gridAll.scale(.9)
        gridAll.shift(2.2*RIGHT)

        if True:
            self.play(Write(grid))

            # Betas
            dot = Dot(color=ORANGE)
            textBeta = Tex("- \\beta")
            textBeta.scale(.7)
            textBeta.set_color(ORANGE)
            textBeta.next_to(dot)
            indicator = VGroup(dot, textBeta)

            betaOffset = .375
            infoTextScale = .5

            dotEx1 = Dot(color=BLUE_A)
            dotEx1.move_to(axes.c2p(-2, -1))
            textEx1 = Tex("\\Re\{\\beta\} > 0")
            textEx1.scale(infoTextScale)
            textEx1.next_to(dotEx1, DOWN, 2*UP)
            dotEx2 = Dot(color=RED_A)
            dotEx2.move_to(axes.c2p(0, 0))
            textEx2 = Tex("\\Re\{\\beta\} = 0")
            textEx2.scale(infoTextScale)
            textEx2.next_to(dotEx2, DOWN, 3*UP)
            dotEx3 = Dot(color=GREEN_A)
            dotEx3.move_to(axes.c2p(2, 1))
            textEx3 = Tex("\\Re\{\\beta\} < 0")
            textEx3.scale(infoTextScale)
            textEx3.next_to(dotEx3, DOWN, 4*UP)

            indicator.move_to(axes.c2p(-3+betaOffset, -2))
            self.play(FadeIn(indicator, scale=0.5))
            self.play(indicator.animate.move_to(axes.c2p(-2+betaOffset, -1)))
            self.play(FadeIn(dotEx1, scale=0.6))
            self.play(Write(textEx1))
            self.wait()
            self.play(indicator.animate.move_to(axes.c2p(0+betaOffset, 0)))
            self.play(FadeIn(dotEx2, scale=0.6))
            self.play(Write(textEx2))
            self.wait()
            self.play(indicator.animate.move_to(axes.c2p(2+betaOffset, 1)))
            self.play(FadeIn(dotEx3, scale=0.6))
            self.play(Write(textEx3))
            self.wait()
            self.play(
                FadeOut(indicator)
            )

            self.wait()

            self.play(
                ReplacementTransform(xLabel, xLabel2),
                ReplacementTransform(yLabel, yLabel2)
            )
        else:
            self.add(grid)

            # Betas
            dot = Dot(color=ORANGE)
            textBeta = Tex("- \\beta")
            textBeta.scale(.7)
            textBeta.set_color(ORANGE)
            textBeta.next_to(dot)
            indicator = VGroup(dot, textBeta)

            betaOffset = .375
            infoTextScale = .5

            dotEx1 = Dot(color=BLUE_A)
            dotEx1.move_to(axes.c2p(-2, -1))
            textEx1 = Tex("\\Re\{\\beta\} > 0")
            textEx1.scale(infoTextScale)
            textEx1.next_to(dotEx1, DOWN, 2*UP)
            dotEx2 = Dot(color=RED_A)
            dotEx2.move_to(axes.c2p(0, 0))
            textEx2 = Tex("\\Re\{\\beta\} = 0")
            textEx2.scale(infoTextScale)
            textEx2.next_to(dotEx2, DOWN, 3*UP)
            dotEx3 = Dot(color=GREEN_A)
            dotEx3.move_to(axes.c2p(2, 1))
            textEx3 = Tex("\\Re\{\\beta\} < 0")
            textEx3.scale(infoTextScale)
            textEx3.next_to(dotEx3, DOWN, 4*UP)

            dotEx1.scale(.6)
            self.add(dotEx1)
            self.add(textEx1)
            dotEx2.scale(.6)
            self.add(dotEx2)
            self.add(textEx2)
            dotEx3.scale(.6)
            self.add(dotEx3)
            self.add(textEx3)
            self.play(
                FadeOut(indicator)
            )



        # ----------------------------------------
        self.play(
            dotEx1.scale, 1.5,
            dotEx2.scale, 1.5,
            dotEx3.scale, 1.5,
        )

        if True:
            lines = [
                Line(dotEx1.get_bottom()+DOWN, dotEx1.get_center()),
                Line(dotEx1.get_center(), dotEx1.get_bottom()+3*UP),
                Line(dotEx2.get_bottom()+2*DOWN, dotEx2.get_center()),
                Line(dotEx2.get_center(), dotEx2.get_bottom()+2*UP),
                Line(dotEx3.get_bottom()+3*DOWN, dotEx3.get_center()),
                Line(dotEx3.get_center(), dotEx3.get_bottom()+UP)
            ]

            for offset in [0, 1]:
                lines[offset].set_color(BLUE_A)
                lines[offset+2].set_color(RED_A)
                lines[offset+4].set_color(GREEN_A)

                self.play(
                    Write(lines[offset]),
                    Write(lines[offset+2]),
                    Write(lines[offset+4])
                )

            ex1 = VGroup(dotEx1, lines[0], lines[1])
            ex2 = VGroup(dotEx2, lines[2], lines[3])
            ex3 = VGroup(dotEx3, lines[4], lines[5])

        else:

            ex1 = VGroup(dotEx1)
            ex2 = VGroup(dotEx2)
            ex3 = VGroup(dotEx3)

        # ----------------------------------------------

        self.play(
            FadeOut(ex2),
            FadeOut(ex3)
        )

        argDot = Dot()
        argDot.scale(0)
        argDot.move_to(axes.c2p(0, 0))
        argArrow = always_redraw(lambda: Arrow(axes.c2p(0, 0), argDot.get_center(), buff=0))
        argText = Tex("F_{(j\\omega)}")
        argText.scale(.7)
        argText.next_to(argDot, LEFT)
        argIndicator = VGroup(argDot, argText)

        indicatorOffset = -.5;
        self.add(argDot)
        self.play(FadeIn(argIndicator), FadeIn(argArrow))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, -1)))

        self.wait()
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, 2)))


        self.wait()
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, -2)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, 2)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, -2)))

        self.wait()
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, -300)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, -5)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, 5)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, 300)))


        self.wait()
        

        self.play(FadeOut(argIndicator), FadeOut(argArrow))


        # -----------------------------------------------------------------
        textDelta = Tex(
            "\\overset{\\infty}{\\underset{-\\infty}{\\Delta}}",
            "arg F_{(j\\omega)} = ", "- \\pi",
            "\\quad \\hdots \\quad", "\\Re\{\\beta\} > 0"
        )

        textDelta[2].set_color(BLUE)
        textDelta.shift(4*LEFT+2*UP)
        textDelta.scale(.7)

        self.play(Write(textDelta))

        self.wait()

        self.play(
            FadeOut(ex1),
            FadeIn(ex2)
        )

        # --------------------------------------------------
        # Delta 2
        self.play(argIndicator.animate.move_to(axes.c2p(0+indicatorOffset, 0)))
        self.play(FadeIn(argIndicator), FadeIn(argArrow))


        self.play(argIndicator.animate.move_to(axes.c2p(0+indicatorOffset, 2)))
        self.play(argIndicator.animate.move_to(axes.c2p(0+indicatorOffset, -2)))

        self.wait()


        self.play(argIndicator.animate.move_to(axes.c2p(0+indicatorOffset, -10)))
        self.play(argIndicator.animate.move_to(axes.c2p(0+indicatorOffset, 10)))

        textDelta2 = Tex(
            "\\overset{\\infty}{\\underset{-\\infty}{\\Delta}}",
            "arg F_{(j\\omega)} = ", "0",
            "\\quad \\hdots \\quad", "\\Re\{\\beta\} = 0"
        )

        textDelta2[2].set_color(RED_A)
        textDelta2.shift(4*LEFT+0*UP)
        textDelta2.scale(.7)

        self.play(Write(textDelta2))

        # --------------------------------------------------
        # Delta 3
        self.play(
            FadeOut(ex2),
            FadeIn(ex3)
        )

        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, 2)))
        self.play(FadeIn(argIndicator), FadeIn(argArrow))


        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, 2)))
        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, -2)))

        self.wait()


        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, -10)))
        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, -300)))
        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, 10)))
        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, 300)))

        textDelta3 = Tex(
            "\\overset{\\infty}{\\underset{-\\infty}{\\Delta}}",
            "arg F_{(j\\omega)} = ", "\\pi",
            "\\quad \\hdots \\quad", "\\Re\{\\beta\} = 0"
        )

        textDelta3[2].set_color(GREEN)
        textDelta3.shift(4*LEFT+2*DOWN)
        textDelta3.scale(.7)

        self.play(Write(textDelta3))

        self.wait()

        self.play(
            FadeOut(ex3), 
            FadeOut(argIndicator), 
            FadeOut(argArrow)
        )

        self.play(
            FadeOut(gridAll), 
            FadeOut(textDelta), FadeOut(textDelta2), FadeOut(textDelta3),
            FadeOut(textExample), 
            FadeOut(textEx1), FadeOut(textEx2), FadeOut(textEx3),
            FadeOut(textBetaIn)
        )

class derivation(Scene):
    def construct(self):

        # --------------------------------------------
        # List sevaral examples
        if False:
            textEx1 = Tex(   
                "\\overset{\\infty}{\\underset{-\\infty}{\\Delta}}",
                "F_{(j\\omega)}",
                ":=",
                "(",
                "j\\omega",
                "- ",
                "\\beta",
                ")"
            )

            textEx1Solution = Tex(   
                r"= \left. \begin{array}{ccc} - \pi & \hdots & \Re{\beta} > 0 \\- 0 & \hdots & \Re{\beta} = 0 \\+ \pi & \hdots & \Re{\beta} < 0 \\ \end{array} \right."
            )

            textEx1Solution.next_to(textEx1)

            ex1 = VGroup(textEx1, textEx1Solution)
            ex1.scale(.85)
            ex1.shift(LEFT)

            self.play(Write(textEx1))
            self.play(Write(textEx1Solution))

            self.play(
                ex1.shift, 3*UP+3*LEFT,
                ex1.scale, .7
            )

            self.play()

            # --------------------------------------------
            # Second examples
            
            textFjw = Tex("F_{(j\\omega)} :=")

            textEx2 = Tex(   
                "(j\\omega - \\beta)",
                "(j\\omega + \\alpha)"
            )

            textEx22 = Tex(   
                "{(j\\omega - \\beta)",
                "(j\\omega + \\alpha)",
                "\over",
                "(j\\omega - \\gamma) (j\\omega - \\epsilon)}"
            )

            textEx23 = Tex(   
                "{(j\\omega - \\beta)(j\\omega + \\alpha)(j\\omega + \\xi)",
                "\over",
                "(j\\omega - \\gamma) (j\\omega - \\epsilon)(j\\omega + \\delta)}"
            )

            textExPoints = Tex(r" = \hdots")

            textFjw.shift(2*LEFT)
            textEx2.next_to(textFjw)
            textEx22.next_to(textFjw)
            textEx23.next_to(textFjw)
            textExPoints.next_to(textEx23)

            self.play(Write(textFjw))
            self.play(
                Write(textEx2),
                ex1.shift, 5*UP+3*LEFT
            )

            self.wait()
            self.play(ReplacementTransform(textEx2, textEx22))
            self.play(ReplacementTransform(textEx22, textEx23))
            self.play(Write(textExPoints))

            textGeneral = Tex(
                r"K",
                r"\; {\displaystyle \prod_{i = 1}^{m} (j\omega - \beta_i)",
                r"\over",
                r"\displaystyle \prod_{k = 1}^{n} (j\omega - \alpha_k)}",
            )

            textGeneral.next_to(textFjw)
            self.play(
                ReplacementTransform(textEx23, textGeneral),
                FadeOut(textExPoints)
            )

            self.wait()

            textFacts = [
                Tex(r"F_{(j\omega)} \text{ is coprime}"),
                Tex(r"K \in \mathbb{R}"),
                Tex(r"\alpha_k, \beta_i \in \mathbb{C}"),
                Tex(r"m \hdots \text{ number of zeros}"),
                Tex(r"n \hdots \text{ number of poles}"),
            ]

            forumla = VGroup(textFjw, textGeneral)
            facts = VGroup(textFacts[0], textFacts[1], textFacts[2], 
                        textFacts[3], textFacts[4])

            self.play(
                forumla.shift, 2.5*LEFT
            )

            for index, textFact in enumerate(textFacts):
                textFact.shift((len(textFacts)/2 - index) * UP+4*RIGHT)
                self.play(Write(textFact))

            self.wait()
            self.play(
                facts.shift, 7*RIGHT
            )

            
        else:
            textFjw = Tex("F_{(j\\omega)} :=")
            textGeneral = Tex(
                r"K",
                r"\; {\displaystyle \prod_{i = 1}^{m} (j\omega - \beta_i)",
                r"\over",
                r"\displaystyle \prod_{k = 1}^{n} (j\omega - \alpha_k)}",
            )
            textGeneral.next_to(textFjw)


            forumla = VGroup(textFjw, textGeneral)
            forumla.shift(4.5*LEFT)
            self.add(forumla)

        if False:
            textArgFjw = Tex(r"arg \; F_{(j\omega)} = ")
            textArg = Tex(r"arg")
            textDeltaArg = Tex(r"\overset{\infty}{\underset{-\infty}{\Delta}} arg")

            textArgFjw.shift(5*LEFT)
            textArg.next_to(textArgFjw)
            textDeltaArg.next_to(textArgFjw)

            self.wait()
            self.play(ReplacementTransform(textFjw, textArgFjw))
            self.play(
                Write(textArg),
                textGeneral.shift, .6*RIGHT
            )

            textArgSum = Tex(
                r"arg K",
                r"+", 
                r"\displaystyle \sum_{i = 1}^{m} arg (j\omega - \beta_i)",
                r"-",
                r"\displaystyle \sum_{k = 1}^{n} arg (j\omega - \alpha_k)}"
            )

            for colorIndex in [1, 3]:
                textArgSum[colorIndex].set_color(ORANGE)

            textArgSum.next_to(textArgFjw)

            self.play(
                FadeOut(textArg),
                ReplacementTransform(textGeneral, textArgSum)
            )

            self.wait()
            self.play(
                textArgSum[1].set_color, WHITE,
                textArgSum[3].set_color, WHITE
            )

            oldStuff = VGroup(textArg, textDeltaArg, textArgFjw, textGeneral, textArgSum)
        else:
            oldStuff = VGroup(textGeneral, textFjw)

        if False:
            textDeltaArgFormula = Tex(
                    r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                    r"F_{(j\omega)} =",
                    r"\overset{\infty}{\underset{-\infty}{\Delta}} ",
                    r"arg K",
                    r"+ ",
                    r"\displaystyle \sum_{i = 1}^{m}",
                    r"\overset{\infty}{\underset{-\infty}{\Delta}} arg (j\omega - ",
                    r"\beta_i",
                    r")",
                    r" - ",
                    r"\displaystyle \sum_{k = 1}^{n}",
                    r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                    r"(j\omega - \alpha_k)"
                )

            textDeltaArgFormula.scale(0.75)

            denominator = VGroup(
                textDeltaArgFormula[-1],
                textDeltaArgFormula[-2],
                textDeltaArgFormula[-3]
            )

            minusSign = textDeltaArgFormula[-4]
                

            self.wait()
            self.play(
                ReplacementTransform(oldStuff, textDeltaArgFormula)
            )

            textKToZero = Tex("0")
            textKToZero.set_color(ORANGE)
            textKToZero.shift(2*LEFT)
            elemK = VGroup(textDeltaArgFormula[2], textDeltaArgFormula[3])
            # --------------------------------------------
            # K
            self.play(elemK.set_color, ORANGE)
            self.wait()
            self.play(ReplacementTransform(elemK, textKToZero))
            self.play(textKToZero.set_color, WHITE)

            # --------------------------------------------
            # Nominator
            allF = VGroup(textDeltaArgFormula, textKToZero)

            nominator = VGroup(textDeltaArgFormula[5], textDeltaArgFormula[6], 
                            textDeltaArgFormula[7], textDeltaArgFormula[8])
            self.wait()
            self.play(nominator.set_color, ORANGE)

            self.wait()
            self.play(
                textDeltaArgFormula[5].set_color, WHITE,
                textDeltaArgFormula[6].set_color, WHITE,
                textDeltaArgFormula[8].set_color, WHITE,
                allF.shift, 2*UP
            )

            # ----------------------------------------------
            # Add axis and text to visualize l, i and r
            axes = Axes(
                x_range=(-3, 3), y_range=(-3, 3),
                height=6, width=6,
                axis_config={
                    "stroke_color": GREY_A,
                    "stroke_width": 2,
                }
            )
            # Keyword arguments of add_coordinate_labels can be used to
            # configure the DecimalNumber mobjects which it creates and
            # adds to the axes
            axes.add_coordinate_labels(
                font_size=30,
                num_decimal_places=0,
            )

            xLabel = Tex("\\Re\{\}")
            xLabel.move_to(axes.c2p(4, 0))
            yLabel = Tex("\\Im\{\}")
            yLabel.move_to(axes.c2p(1, 3))

            grid = VGroup(axes, xLabel, yLabel)

            grid.scale(.6)
            grid.shift(DOWN + 3*RIGHT)


            self.play(FadeIn(grid))

            dotL1 = Dot() 
            dotL1.set_color(BLUE_A)
            dotL1.move_to(axes.c2p(-2, 0))
            dotL2 = Dot()
            dotL2.set_color(BLUE_A)
            dotL2.move_to(axes.c2p(-1, 0))
            dotIm = Dot()
            dotIm.set_color(RED_A)
            dotIm.move_to(axes.c2p(0, 0))
            dotR1 = Dot()
            dotR1.set_color(GREEN_A)
            dotR1.move_to(axes.c2p(1, 0))
            dotR2 = Dot()
            dotR2.set_color(GREEN_A)
            dotR2.move_to(axes.c2p(1.5, 0))

            schiftToLeft = 3 
            schiftUpDown = 1
            scaleFactor = 0.75
            textMLeft = Tex(r"m_l", r"\text{ zeros left to the Imaginary-Axis}")
            textMLeft[0].set_color(BLUE)
            textMLeft.scale(scaleFactor)
            textMLeft.shift(schiftToLeft*LEFT)

            textMOn = Tex(r"m_i", r"\text{ zeros on the Imaginary-Axis}")
            textMOn[0].set_color(RED)
            textMOn.scale(scaleFactor)
            textMOn.shift(schiftToLeft*LEFT+schiftUpDown*DOWN)

            textMRight = Tex(r"m_r", r"\text{ zeros right to the Imaginary-Axis}")
            textMRight[0].set_color(GREEN)
            textMRight.scale(scaleFactor)
            textMRight.shift(schiftToLeft*LEFT+2*schiftUpDown*DOWN)

            textSum = Tex(
                r"\rightarrow ", 
                r"m_l", r" + ", 
                r"m_i", r" + ", 
                r"m_r", r" = m")

            textSum[1].set_color(BLUE)
            textSum[3].set_color(RED)
            textSum[5].set_color(GREEN)
            textSum.scale(scaleFactor)
            textSum.shift(schiftToLeft*LEFT+3*schiftUpDown*DOWN)

            dot = Dot()
            dot.set_color(ORANGE)
            dot.move_to(axes.c2p(-3, 0))
            self.play(FadeIn(dot, scale=0.5))
            self.play(dot.animate.move_to(axes.c2p(-2, 0)))
            self.play(FadeIn(dotL1, scale=0.75))
            self.wait()
            self.play(dot.animate.move_to(axes.c2p(-1, 0)))
            self.play(FadeIn(dotL2, scale=0.75))
            self.wait()
            self.play(
                Write(textMLeft)
            )
            self.wait()
            self.play(dot.animate.move_to(axes.c2p(0, 0)))
            self.play(FadeIn(dotIm, scale=0.75))
            self.wait()
            self.play(
                Write(textMOn)
            )
            self.wait()
            self.play(dot.animate.move_to(axes.c2p(1, 0)))
            self.play(FadeIn(dotR1, scale=0.75))
            self.wait()
            self.play(dot.animate.move_to(axes.c2p(1.5, 0)))
            self.play(FadeIn(dotR2, scale=0.75))
            self.wait()
            self.play(
                Write(textMRight)
            )
            self.wait()


            self.play(
                Write(textSum)
            )

            textMLeftEffect = Tex(
                r"\Re{\beta} > 0"
                r"\rightarrow ",
                r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                r"F_{(j\omega)} = ", r"- \pi"
            )
            textMLeftEffect.next_to(textMLeft)
            textMLeftEffect.scale(scaleFactor)
            textMLeftEffect[3].set_color(BLUE)

            textMOnEffect = Tex(
                r"\Re{\beta} = 0"
                r"\rightarrow ",
                r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                r"F_{(j\omega)} = ", r"0"
            )
            textMOnEffect.next_to(textMOn)
            textMOnEffect.scale(scaleFactor)
            textMOnEffect[3].set_color(RED)

            textMRightEffect = Tex(
                r"\Re{\beta} < 0"
                r"\rightarrow ",
                r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                r"F_{(j\omega)} = ", r"+ \pi"
            )
            textMRightEffect.next_to(textMRight)
            textMRightEffect.scale(scaleFactor)
            textMRightEffect[3].set_color(GREEN)

            self.wait()

            self.play(
                FadeOut(grid), FadeOut(dotIm),
                FadeOut(dotR1), FadeOut(dotR2),
                FadeOut(dotL1), FadeOut(dotL2),
                FadeOut(dot)
            )

            self.play(
                Write(textMLeftEffect),
                Write(textMOnEffect),
                Write(textMRightEffect)
            )

            self.wait()

            mStuff = VGroup(
                textMLeftEffect, textMOnEffect, textMRightEffect,
                textMLeft, textMOn, textMRight,
                textSum
            )

            self.play(FadeOut(mStuff))

            textResult = Tex(
                r"\displaystyle \sum_{i = 1}^{m}",
                r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                r"(j\omega - \beta_i) = ",
                r"+\pi ", r"\cdot m_l",
                r"+ 0 ", r"\cdot m_i",
                r"- \pi ", r"\cdot m_r"
            )
            textResult.scale(scaleFactor)

            leftSide = VGroup(textResult[0], textResult[1], textResult[2])
            leftSide.set_color(ORANGE)

            textResult[4].set_color(BLUE)
            textResult[6].set_color(RED)
            textResult[8].set_color(GREEN)

            self.play(Write(leftSide))
            self.play(leftSide.set_color, ORANGE)

            self.play(
                Write(textResult[3]),
                Write(textResult[4])
            )

            self.play(
                Write(textResult[5]),
                Write(textResult[6])
            )

            self.play(
                Write(textResult[7]),
                Write(textResult[8])
            )

            self.wait()
            self.play(
                textResult.set_color, WHITE,
                leftSide.set_color, WHITE,
                nominator.set_color, WHITE
            )

            # ----------------------------------------------
            # Denominator part
            self.wait()
            self.play(denominator.set_color, PURPLE)

            textResult2 = Tex(
                r"- ",
                r"\displaystyle \sum_{k = 1}^{n}",
                r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                r"(j\omega - \alpha_k) = ",
                r"+", r"\pi ", r"\cdot n_l",
                r"+", r" 0 ", r"\cdot n_i",
                r"-", r" \pi ", r"\cdot n_r"
            )

            textResult2.shift(2*DOWN)
            textResult2.scale(scaleFactor)

            leftSide = VGroup(textResult2[1], textResult2[2], textResult2[3])
            leftSide.set_color(PURPLE)

            textResult2[6].set_color(BLUE)
            textResult2[9].set_color(RED)
            textResult2[12].set_color(GREEN)

            self.play(Write(leftSide))

            self.play(
                Write(textResult2[4]),
                Write(textResult2[5]),
                Write(textResult2[6])
            )

            self.play(
                Write(textResult2[7]),
                Write(textResult2[8]),
                Write(textResult2[9])
            )

            self.play(
                Write(textResult2[10]),
                Write(textResult2[11]),
                Write(textResult2[12])
            )

            self.wait()

            self.play(Write(textResult2[0]))

            leftDelta = .35
            signChange1 = Tex(" -")
            signChange1.scale(scaleFactor)
            signChange1.next_to(textResult2[4].get_center())
            signChange1.shift(leftDelta*LEFT)
            signChange2 = Tex(" -")
            signChange2.scale(scaleFactor)
            signChange2.next_to(textResult2[7].get_center())
            signChange2.shift(leftDelta*LEFT)
            signChange3 = Tex(" +")
            signChange3.scale(scaleFactor)
            signChange3.next_to(textResult2[10].get_center())
            signChange3.shift(leftDelta*LEFT)

            self.play(
                ReplacementTransform(textResult2[4], signChange1),
                ReplacementTransform(textResult2[7], signChange2),
                ReplacementTransform(textResult2[10], signChange3),
            )

            self.wait()
            self.play(
                textResult2.set_color, WHITE,
                denominator.set_color, WHITE
            )

            self.wait()
            self.play(
                textResult.shift, 12*LEFT,
                VGroup(textResult2, signChange2, signChange3, signChange1).shift, 12*RIGHT,
                VGroup(textDeltaArgFormula, textKToZero).shift, 4*UP
            )

        #---------------------------------------
        # Result with m
        self.play(FadeOut(oldStuff))

        textDeltaArgFormula = Tex(
            r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
            r"F_{(j\omega)} = ",
            r"+ \pi \cdot ", r"m_l",
            r"- \pi \cdot ", r"m_r",
            r"- \pi \cdot ", r"n_l",
            r"+ \pi \cdot ", r"n_r"
        )

        textDeltaArgFormula[3].set_color(RED_A)
        textDeltaArgFormula[5].set_color(RED_A)
        textDeltaArgFormula[7].set_color(BLUE_A)
        textDeltaArgFormula[9].set_color(BLUE_A)

        self.play(Write(textDeltaArgFormula))

        textUsingInfo = Tex(r"\text{using: }")
        textUsingAnd= Tex(r"\text{ and }")

        textUsingM = Tex(r"m = m_l + m_r + m_i \qquad")
        textUsingM.set_color(RED_A)
        textUsingN = Tex(r"\qquad n = n_l + n_r + n_i")
        textUsingN.set_color(BLUE_A)

        textUsingInfo.shift(DOWN+3*LEFT)
        textUsingM.shift(2*DOWN+4*LEFT)
        textUsingAnd.next_to(textUsingM, RIGHT, 2*RIGHT)
        textUsingN.next_to(textUsingAnd, RIGHT, 2*RIGHT)

        self.play(Write(textUsingInfo))
        self.play(Write(textUsingM))
        self.play(Write(textUsingAnd))
        self.play(Write(textUsingN))

        textDeltaArgFormula2 = Tex(
            r"\overset{\infty}{\underset{-\infty}{\Delta}}",
            r" arg F_{(j\omega)} = (",
            r"m", r" - ", r" n",
            r") \cdot ", r"\pi", " - (", 
            r"m_i", r" + 2", r"m_r",
            r") \cdot ", r"\pi", " + (", 
            r"n_i", r" + 2", r"n_r",
            r") \cdot ", r"\pi"
        )

        textDeltaArgFrom0 = Tex(r"\overset{\infty}{\underset{0}{\Delta}}")
        textDeltaArgFrom0.move_to(textDeltaArgFormula2[0])


        textPiHalf1 = Tex(r"\frac{\pi}{2}")
        textPiHalf1.move_to(textDeltaArgFormula2[6])

        textPiHalf2 = Tex(r"\frac{\pi}{2}")
        textPiHalf2.move_to(textDeltaArgFormula2[12])

        textPiHalf3 = Tex(r"\frac{\pi}{2}")
        textPiHalf3.move_to(textDeltaArgFormula2[-1])

        VGroup(
            textDeltaArgFormula2[2],
            textDeltaArgFormula2[8],
            textDeltaArgFormula2[10],
        ).set_color(RED_A)


        VGroup(
            textDeltaArgFormula2[4],
            textDeltaArgFormula2[14],
            textDeltaArgFormula2[16],
        ).set_color(BLUE_A)

        self.play(
            FadeOut(VGroup(
                textUsingInfo, textUsingM,
                textUsingN, textUsingAnd
            )),
            ReplacementTransform(textDeltaArgFormula, textDeltaArgFormula2)
        )

        self.wait()
        self.play(
            ReplacementTransform(textDeltaArgFormula2[0], textDeltaArgFrom0)
        )
        self.play(
            ReplacementTransform(textDeltaArgFormula2[6], textPiHalf1),
            ReplacementTransform(textDeltaArgFormula2[12], textPiHalf2),
            ReplacementTransform(textDeltaArgFormula2[-1], textPiHalf3)
        )
