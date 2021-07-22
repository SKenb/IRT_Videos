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
        
        if False:
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

        if False:
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

        if False:
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

        self.play(argIndicator.animate.move_to(axes.c2p(2+indicatorOffset, 0)))
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