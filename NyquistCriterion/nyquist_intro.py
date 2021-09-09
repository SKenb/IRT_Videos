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
        self.wait(2)
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
        
        plantText = TexText("Plant", "$P(s)$")
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
        
        controllerText = TexText("Controller", "$C(s)$")
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

        self.wait(2)

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
        
        plantText = TexText("Plant", "$P(s)$")
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
        
        controllerText = TexText("Controller", "$C(s)$")
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

        textTsRight = Tex(   
                        "T(s) =",
                        "{C(s) P(s)",
                        "\\over",
                        "1 + C(s) P(s)}",
                        color=WHITE
                    )

        textTsRightWithL = Tex(   
                        "T(s) =",
                        "{L(s)",
                        "\\over",
                        "1 + L(s)}",
                        color=WHITE
                    )

        textMuNu = Tex(   
                        " =",
                        "{\\nu_T(s)",
                        "\\over",
                        "\\mu_T(s)}",
                        color=WHITE
                    )

        textTsRight.next_to(controlLoop.get_corner(BOTTOM), 6*DOWN)
        textTsRightWithL.next_to(controlLoop.get_corner(BOTTOM), 6*DOWN)
        textMuNu.next_to(textTsRightWithL.get_corner(RIGHT), 3*RIGHT)

        self.play(Write(textTsRight))


        ###########################################################
        # Forward
        ###########################################################
        self.play(
                    plantText.set_color, ORANGE,
                    controllerText.set_color, ORANGE,
                    textTsRight[1].set_color, ORANGE
                )

        self.wait(1)

        ###########################################################
        # Backward
        ###########################################################
        self.play(
                    plantText.set_color, BLUE,
                    controllerText.set_color, BLUE,
                    textTsRight[3].set_color, BLUE,
                    minusText.set_color, BLUE
                )

        self.wait(1)

        ###########################################################
        # Back and intro L
        ###########################################################
        self.play(
                    plantText.set_color, WHITE,
                    controllerText.set_color, WHITE,
                    textTsRight[1].set_color, WHITE,
                    textTsRight[3].set_color, WHITE,
                    minusText.set_color, WHITE
                )


        self.wait(1)

        self.play(
                ReplacementTransform(textTsRight[1],textTsRightWithL[1]),
                ReplacementTransform(textTsRight[3],textTsRightWithL[3])
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

        xLabel = Tex("\\Re\{s_{\mu_T}\}")
        xLabel.move_to(axes.c2p(4, 0))
        yLabel = Tex("\\Im\{s_{\mu_T}\}")
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
            textTsRightWithL.scale, 0,
            textTsRight.scale, 0,
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

        xLabel = Tex("\\Re\{s_{\mu_T}\}")
        xLabel.move_to(axes.c2p(4, 0))
        yLabel = Tex("\\Im\{s_{\mu_T}\}")
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
            TexText("Calculate poles explicit"),
            TexText("Use the Routh scheme"),
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

        self.wait(2)

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
        fact2 = TexText("It uses $L(j\omega)$")
        fact3 = TexText("Less information necessary")
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

        self.wait(2)

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
                                "F(j\\omega)",
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

            self.wait(2)
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
                                "F(j\\omega)",
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
        xLabel2 = Tex("\\Re\{(j\\omega)\}")
        xLabel2.move_to(axes.c2p(4.2, 0))

        yLabel = Tex("\\Im\{\\beta\}")
        yLabel.move_to(axes.c2p(1, 3))
        yLabel2 = Tex("\\Im\{F(j\\omega)\}")
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

                #self.play(
                #    Write(lines[offset]),
                #    Write(lines[offset+2]),
                #    Write(lines[offset+4])
                #)

            ex1 = VGroup(dotEx1, lines[0], lines[1])
            ex2 = VGroup(dotEx2, lines[2], lines[3])
            ex3 = VGroup(dotEx3, lines[4], lines[5])

        else:

            ex1 = VGroup(dotEx1)
            ex2 = VGroup(dotEx2)
            ex3 = VGroup(dotEx3)

        # ----------------------------------------------

        #self.play(
        #    FadeOut(ex2),
        #    FadeOut(ex3)
        #)

        argDot = Dot()
        argDot.scale(0)
        argDot.move_to(axes.c2p(0, 0))
        argArrow = always_redraw(lambda: Arrow(axes.c2p(0, 0), argDot.get_center(), buff=0))
        argText = Tex("F(j\\omega)")
        argText.scale(.7)
        argText.next_to(argDot, LEFT)
        argIndicator = VGroup(argDot, argText)

        indicatorOffset = -.61;
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

        self.play(Write(lines[0]), Write(lines[1]))
        self.wait(2)

        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, -300)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, -5)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, 5)))
        self.play(argIndicator.animate.move_to(axes.c2p(-2+indicatorOffset, 300)))


        self.wait()

        

        self.play(FadeOut(argIndicator), FadeOut(argArrow))


        # -----------------------------------------------------------------
        textDelta = Tex(
            "\\overset{\\infty}{\\underset{-\\infty}{\\Delta}}",
            "arg F(j\\omega) = ", "- \\pi",
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
            "arg F(j\\omega) = ", "0",
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
            "arg F(j\\omega) = ", "\\pi",
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
        if True:
            textEx1 = Tex(   
                "\\overset{\\infty}{\\underset{-\\infty}{\\Delta}}",
                "F(j\\omega)",
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
            
            textFjw = Tex("F(j\\omega) :=")

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
                r"\; {\displaystyle \prod_{i = 1}^{m}",
                r" (j\omega - \beta_i)",
                r"\over",
                r"\displaystyle \prod_{k = 1}^{n}",
                r" (j\omega - \alpha_k)}",
            )

            textGeneral.next_to(textFjw)
            self.play(
                ReplacementTransform(textEx23, textGeneral),
                FadeOut(textExPoints)
            )

            self.wait()

            textFacts = [
                Tex(r"F(j\omega) \text{ is coprime}"),
                Tex(r"K", r" \in \mathbb{R}"),
                Tex(r"\alpha_k, \beta_i \in \mathbb{C}"),
                Tex(r"m", r" \hdots \text{ number of zeros}"),
                Tex(r"n", r" \hdots \text{ number of poles}"),
            ]

            textFacts[1][0].set_color(GREEN_A)
            textFacts[3][0].set_color(BLUE_A)
            textFacts[4][0].set_color(RED_A)
            
            forumla = VGroup(textFjw, textGeneral)
            facts = VGroup(textFacts[0], textFacts[1], textFacts[2], 
                        textFacts[3], textFacts[4])

            self.play(
                forumla.shift, 2.5*LEFT
            )

            for index, textFact in enumerate(textFacts):
                textFact.shift((len(textFacts)/2 - index) * UP+4*RIGHT)
                self.play(Write(textFact))

            for index, color in {0: GREEN_A, 1: BLUE_A, 4: RED_A}.items():
                self.play(textGeneral[index].set_color, color)

            self.wait()
            self.play(
                facts.shift, 7*RIGHT,
                textGeneral.set_color, WHITE
            )

            
        else:
            textFjw = Tex("F(j\\omega) :=")
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

        if True:
            textArgFjw = Tex(r"arg \; F(j\omega) = ")
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
                r"arg", 
                r"K",
                r"+", 
                r"\displaystyle \sum_{i = 1}^{m}",
                r"arg",
                r"(j\omega - \beta_i)",
                r"-",
                r"\displaystyle \sum_{k = 1}^{n} ",
                r"arg",
                r" (j\omega - \alpha_k)}"
            )

            for colorIndex in [2, 6]:
                textArgSum[colorIndex].set_color(ORANGE)

            textArgSum.next_to(textArgFjw)

            self.play(
                FadeOut(textArg),
                ReplacementTransform(textGeneral, textArgSum)
            )

            self.wait()
            self.play(
                textArgSum[2].set_color, WHITE,
                textArgSum[6].set_color, WHITE
            )
            oldStuff = VGroup(textArg, textArgFjw, textGeneral, textArgSum)
        else:
            oldStuff = VGroup(textGeneral, textFjw)

        self.remove(textDeltaArg)

        if True:

            textDeltaArgFormula = Tex(
                    r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                    r"F(j\omega) =",
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

            #textDeltaArgFormula.scale(0.75)
            textDeltaArgFormula.scale(500)

            denominator = VGroup(
                textDeltaArgFormula[-1],
                textDeltaArgFormula[-2],
                textDeltaArgFormula[-3]
            )

            minusSign = textDeltaArgFormula[-4]
                
            self.wait()

            self.play(
                oldStuff.scale, 0,
                textDeltaArgFormula.scale, .75/500
            )

            self.wait()

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
                r"F(j\omega) = ", r"- \pi"
            )
            textMLeftEffect.next_to(textMLeft)
            textMLeftEffect.scale(scaleFactor)
            textMLeftEffect[3].set_color(BLUE)

            textMOnEffect = Tex(
                r"\Re{\beta} = 0"
                r"\rightarrow ",
                r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                r"F(j\omega) = ", r"0"
            )
            textMOnEffect.next_to(textMOn)
            textMOnEffect.scale(scaleFactor)
            textMOnEffect[3].set_color(RED)

            textMRightEffect = Tex(
                r"\Re{\beta} < 0"
                r"\rightarrow ",
                r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
                r"F(j\omega) = ", r"+ \pi"
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
        else:
            self.play(FadeOut(oldStuff))

        #---------------------------------------
        # Result with m
       

        textDeltaArgFormula = Tex(
            r"\overset{\infty}{\underset{-\infty}{\Delta}} arg ",
            r"F(j\omega) = ",
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
            r" arg F(j\omega) = (",
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

class nyquist(Scene):
    def construct(self):
        
        textTs = Tex("T(s) = ")
        textTs.shift(2*LEFT)

        textCP = Tex(
            r"{",
            r"C(s)P(s)",
            r"\over",
            r"1 + ",
            r"C(s)P(s)}",
            r" = "
        )
        textCP.next_to(textTs)

        self.play(Write(textTs))
        self.play(Write(textCP[0:4]))

        self.play(
            textCP[2].set_color, ORANGE,
            textCP[3].set_color, ORANGE
        )

        self.wait()
        self.play(textCP[0:4].set_color, WHITE)

        textL = Tex(
            r"{",
            r"L(s)",
            r"\over"
            r"1 + ",
            r"L(s)}"
        )
        textL.next_to(textCP)

        self.wait()
        self.play(
            Write(textCP[4]),
            Write(textL)
        )

        self.wait()
        self.play(
            FadeOut(textCP),
            textL.shift, 3.5*LEFT
        )

        COLOR_MU = RED_A
        COLOR_NU = BLUE_A

        def colorElements(elem, lst, clr):
            for idx in lst: elem[idx].set_color(clr)

        textLIs = Tex(
            r"L(s) = { ", 
            r"\mu(s)",
            r" \over ", 
            r"\nu(s) }",
            r" = C(s)P(s)"
        )

        
        colorElements(textLIs, [1], COLOR_MU)
        colorElements(textLIs, [3], COLOR_NU)

        textLIs.shift(2*DOWN)
        self.play(Write(textLIs[0:3]))
        self.play(Write(textLIs[3:5]))

        textLMuNu = Tex(
            r"\frac{ \mu(s) }{\nu(s)}",
            r"\over",
            r"1 + \frac{ \mu(s) }{\nu(s)}"
        )
    
        textLMuNu[0][0:4].set_color(COLOR_MU)
        textLMuNu[0][5:10].set_color(COLOR_NU)
        textLMuNu[2][2:6].set_color(COLOR_MU)
        textLMuNu[2][7:11].set_color(COLOR_NU)


        self.play(
            ReplacementTransform(textL, textLMuNu)
        )

        self.wait()

        textMuNuInT = Tex(
            r" = ",
            r"{\frac{ \mu(s) }{\nu(s)}",
            r"\over",
            r"\frac{ \nu(s) }{\nu(s)} + \frac{ \mu(s) }{\nu(s)}}"
        )
    
        textMuNuInT[1][0:4].set_color(COLOR_MU)
        textMuNuInT[1][5:10].set_color(COLOR_NU)
        textMuNuInT[3][0:4].set_color(COLOR_NU)
        textMuNuInT[3][5:9].set_color(COLOR_NU)
        textMuNuInT[3][10:14].set_color(COLOR_MU)
        textMuNuInT[3][15:19].set_color(COLOR_NU)

        textMuNuInT.next_to(textLMuNu)
        self.play(Write(textMuNuInT))

        textMuNuInT2 = Tex(
            r"{ \mu(s)",
            r"\over",
            r"\nu(s) + \mu(s)}"
        )
    
        textMuNuInT2[0][0:4].set_color(COLOR_MU)
        textMuNuInT2[2][0:4].set_color(COLOR_NU)
        textMuNuInT2[2][5:9].set_color(COLOR_MU)

        self.play(
            FadeOut(textLMuNu),
            ReplacementTransform(textMuNuInT, textMuNuInT2)
        )

        self.wait()

        self.play(
            textMuNuInT2.set_color, WHITE,
            textLIs.set_color, WHITE
        )

        self.wait()
        self.play(
            textMuNuInT2[2].set_color, ORANGE
        )

        self.wait()
        self.play(
            textMuNuInT2[2].set_color, WHITE
        )

        self.wait()
        self.play(
            VGroup(textTs, textMuNuInT2).shift, 14*LEFT
        )


class nyquist2(Scene):
    def construct(self):
    
        COLOR_MU = RED_A
        COLOR_NU = BLUE_A

        textLIs = Tex(
            r"L(s) = { ", 
            r"\mu(s)",
            r" \over ", 
            r"\nu(s) }",
            r" = C(s)P(s)"
        )

        textLIs[1].set_color(COLOR_MU)
        textLIs[3].set_color(COLOR_NU)

        textLIs.shift(2*DOWN)
        self.add(textLIs)
        self.wait()
        self.play(FadeOut(textLIs[4:5]))
        textLIs = textLIs[0:4]
        
        textF = Tex(r"F(s)")
        textF.shift(2*LEFT)

        textLs = Tex(":= 1 + ", "L(s)")
        textLs.next_to(textF)


        textMuNu = Tex(
            r"= { \nu(s) + \mu(s)",
            r"\over",
            r" \mu(s)}"
        )

        textMuNu[0][1:5].set_color(COLOR_NU)
        textMuNu[0][6:10].set_color(COLOR_MU)
        textMuNu[2][0:4].set_color(COLOR_MU)
         
        textMuNu.next_to(textF)

        first = VGroup(textF, textMuNu)

        self.play(Write(textF))
        self.play(Write(textLs))

        self.wait()

        self.play(ReplacementTransform(textLs, textMuNu))

        textArgF = Tex(
            r"\Delta arg ",
            r"F(j\omega)",
            r" = ",
            r"(m - n) \cdot \frac{\pi}{2}",
            r" - ",
            r"(m_i + m_r) \cdot \frac{\pi}{2}",
            r" + ",
            r"(n_i + 2 n_r) \cdot \frac{\pi}{2}"
        )

        self.play(
            first.shift, 1*DOWN,
            textLIs.shift, 1*DOWN
        )

        textArgF.next_to(first, TOP)
        self.play(Write(textArgF))


        ## -------------------------------------------------
        ## m = n
        textMuGENu = Tex(
            r"deg(", 
            r"\nu(s)", 
            r") \leq deg(", 
            r"\mu(s)", r")"
        )

        textMuGENu[1].set_color(COLOR_NU)
        textMuGENu[3].set_color(COLOR_MU)
        textMuGENu.next_to(textLIs.get_center())
        textMuGENu.shift(LEFT)

        self.play(ReplacementTransform(textLIs, textMuGENu))
        self.wait()

        textReplacmentNuPlusMu = Tex(r"deg(", r"\mu(s)", " + ")
        textReplacmentNuPlusMu[1].set_color(COLOR_MU)
        textReplacmentNuPlusMu.next_to(textMuGENu, LEFT)
        textReplacmentNuPlusMu.shift(RIGHT)

        self.play(ReplacementTransform(textMuGENu[0], textReplacmentNuPlusMu))

        textMEqualN = Tex(r"\rightarrow m = n")
        textMEqualN.next_to(textReplacmentNuPlusMu)

        self.wait()
        self.play(ReplacementTransform(
            VGroup(textMuGENu, textLIs, textReplacmentNuPlusMu), textMEqualN
        ))

        self.wait()
        self.play(
            textArgF[3].set_color, ORANGE,
            textMEqualN.set_color, ORANGE
        )

        textZero = Tex("0")
        textZero.set_color(ORANGE)
        textZero.next_to(textArgF[3])
        textZero.shift(2*LEFT)
        self.play(ReplacementTransform(textArgF[3], textZero))

        self.wait()
        self.play(
            textArgF[3].set_color, WHITE,
            textMEqualN.set_color, WHITE
        )

        self.wait()


        # -----------------------------------------------
        # Poles to the left
        textPolesToLeft = Tex(r"\text{for Hurwitz:}")
        textPolesToLeft.next_to(textF)

        textPolesToLeft2 = Tex(r"m_i = m_r \overset{!}{=} 0")
        textPolesToLeft2.next_to(textPolesToLeft, BOTTOM)

        self.play(
            VGroup(textF, textMuNu).shift, 12*LEFT,
            textMEqualN.shift, 12*RIGHT
        )

        self.play(Write(textPolesToLeft))
        self.play(Write(textPolesToLeft2))

        self.play(
            textArgF[5].set_color, ORANGE,
            textPolesToLeft2.set_color, ORANGE
        )

        textZero2 = Tex("0")
        textZero2.set_color(ORANGE)
        textZero2.next_to(textArgF[5])
        textZero2.shift(2*LEFT)
        self.play(ReplacementTransform(textArgF[5], textZero2))

        self.wait()
        self.play(
            textArgF[5].set_color, WHITE,
            textPolesToLeft2.set_color, WHITE
        )

        self.wait()
        self.play(
            VGroup(textPolesToLeft, textPolesToLeft2).shift, 5*DOWN
        )


        self.play(
            FadeOut(VGroup(
                textZero, textZero2, 
                textArgF[3], textArgF[4], textArgF[5], textArgF[6]
            )),
            textArgF[7].shift, 3*LEFT,
            VGroup(textArgF[0], textArgF[1], textArgF[2]).shift, 3.4*RIGHT
        )

        formula = VGroup(textArgF[0], textArgF[1], textArgF[2], textArgF[7])
        
        self.play(formula.scale, 1.25)

        textOnePlusL = Tex(r"\{1 + L(j\omega)\}") 
        textOnePlusL.next_to(textArgF[1])
        textOnePlusL.shift(3*LEFT)
        textOnePlusL.scale(1.25)
        self.play(
            ReplacementTransform(textArgF[1], textOnePlusL),
            textArgF[0].shift, 1.7*LEFT
        )

        self.play(
            VGroup(textOnePlusL, textArgF[0]).set_color, BLUE_A
        )

def getControlLoop():
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
    
    plantText = TexText("Plant", "$P(s)$")
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
    
    controllerText = TexText("Controller", "$C(s)$")
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
            

    return VGroup(plant, controller,
                loopLineDown, loopLineBottom, loopLineUp,
                connectionCircle, minusText, referenceLine, referenceText,
                referenceArrow, controllerArrow, plantArrow, loopArrow)

def getImagGrid(label, rangeX=[3], rangeY=[3], xOffset=1):
    ###########################################################
    # Hurwitz - Pole Zero Plor
    ###########################################################
    axes = Axes(
        x_range=(-abs(min(rangeX)), max(rangeX)), 
        y_range=(-abs(min(rangeY)), max(rangeY)),
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

    xLabel = Tex("\\Re\{" + label + "\}")
    xLabel.move_to(axes.c2p(max(rangeX)+xOffset, 0))
    yLabel = Tex("\\Im\{" + label + "}\}")
    yLabel.move_to(axes.c2p(xOffset, max(rangeY)))

    return VGroup(axes, xLabel, yLabel)

class nyquist3(Scene):
    def construct(self):

        texTitle = TexText("\\underline{The Nyquist Criterion:}")
        texTitle.set_color("#ffff00")
        texTitle.scale(1.2)
        
        self.play(Write(texTitle))
        self.wait()
        self.play(
            texTitle.scale, 0.8,
            texTitle.shift, 3.2*UP+3*LEFT
        )

        textForumla = Tex(
            r"\Delta arg \{1 + L(j\omega)}\}",
            r" = (n_i + 2n_r) \cdot \frac{\pi}{2}"
        )
        textForumla.scale(1.2)
        textForumla.shift(1*UP)
        self.play(Write(textForumla))

        ## Recap parts

        # ----------------------------------------------------
        # control loop / L(j\omega)
        textL = Tex(r"L(j\omega) = C(j\omega)P(j\omega)")
        textL[0][0:5].set_color(BLUE)

        controlLoop = getControlLoop()
        controlLoop.scale(.6)
        controlLoop.next_to(textL, BOTTOM)

        recapL = VGroup(textL, controlLoop)
        recapL.shift(0.5*DOWN+12*RIGHT)

        self.add(recapL)
        self.play(
            recapL.shift, 12*LEFT,
            textForumla[0][7:12].set_color, BLUE
        )

        self.play(
            textL[0][6:11].set_color, RED,
            controlLoop[1][3].set_color, RED
        )
        self.play(
            textL[0][11:16].set_color, GREEN,
            controlLoop[0][3].set_color, GREEN
        )

        self.wait()
        self.play(
            textL.set_color, WHITE,
            textL.set_color, WHITE,
            controlLoop.shift, 12*LEFT
        )

        # ----------------------------------------------------
        # Poles of L
        self.wait()

        textL2 = Tex(
            r"1 + L(j\omega) = ", 
            r"{\mu(j\omega) + \nu(j\omega) \over \nu(j\omega)}",
            r"\qquad | \quad L(j\omega) = {\mu(j\omega) \over \nu(j\omega)}"
        )
        textL2.scale(.85)
        textL2[0][0:7].set_color(BLUE)
        textL2.shift(.5*DOWN)

        self.play(
            ReplacementTransform(textL, VGroup(textL2[0], textL2[1])),
            textForumla[0][5:12].set_color, BLUE,
        )

        self.play(
            Write(textL2[2]),
            textL2[1][0:5].set_color, RED_A,
            textL2[2][7:12].set_color, RED_A,
            textL2[2][13:18].set_color, GREEN_A, 
            textL2[1][6:11].set_color, GREEN_A,
            textL2[1][12:17].set_color, GREEN_A
        )

        grid = getImagGrid("s_{\\nu}")
        grid.scale(.55)
        grid.next_to(textL2, BOTTOM)
        grid.shift(12*LEFT+1.7*UP)

        self.play(
            textL2[1][0:5].set_color, WHITE,
            textL2[2][7:12].set_color, WHITE,
            textL2[2][13:18].set_color, GREEN, 
            textL2[1][6:11].set_color, WHITE,
            textL2[1][12:17].set_color, GREEN,
            textForumla[1][2:8].set_color, GREEN,
        )

        self.wait()

        self.play(
            VGroup(textL2).shift, 12*RIGHT,
            grid.shift, 12*RIGHT,
            textForumla.set_color, WHITE
        )

        offset = -0.575
        dotsR = [Dot(), Dot(), Dot(), Dot()]
        for index, dot in enumerate(dotsR): 
            dot.set_color(GREEN)
            dot.scale(.75)
            dot.next_to(grid[0].c2p(offset + min(2, index)+.5, 0 if index < 2 else 3*(index-2.5)))

            self.play(Write(dot))

        self.play(textForumla[1][6:8].set_color, GREEN)

        dotsI = [Dot(), Dot(), Dot()]
        for index, dot in enumerate(dotsI): 
            dot.set_color(RED)
            dot.scale(.75)
            dot.next_to(grid[0].c2p(offset, 0 if index < 1 else 2*(index-1.5)))

            self.play(Write(dot))

        self.play(textForumla[1][2:4].set_color, RED)

        dots = VGroup(
            dotsI[0], dotsI[1], dotsI[2],
            dotsR[0], dotsR[1], dotsR[2], dotsR[3],
        )

        self.wait()
        self.play(
            textForumla.set_color, WHITE,
            VGroup(grid, dots).scale, 0
        )

class nyquist4(Scene):
    def construct(self):

        texTitle = TexText("\\underline{The Nyquist Criterion:}")
        texTitle.set_color("#ffff00")
        texTitle.scale(.8)
        texTitle.shift(3.2*UP+3*LEFT)
        self.add(texTitle)

        textForumla = Tex(
            r"\Delta arg \{1 + L(j\omega)}\}",
            r" = (n_i + 2n_r) \cdot \frac{\pi}{2}"
        )
        textForumla.scale(1.2)
        textForumla.shift(1*UP)
        self.add(textForumla)


        grid = getImagGrid("", [-2, 4], [-4, 1])
        axes = grid[0]

        grid.scale(.75)
        grid.shift(DOWN)

        self.play(textForumla[0].set_color, BLUE)
        self.play(
            Write(grid),
            textForumla.shift, 1.2*UP
        )

        graphLjwPlus1 = grid[0].get_graph(
            lambda x: -np.sqrt(1-(x-2)**2) if x >= 1 and x <= 3 else 0,
            discontinuities=[1, 3],
            stroke_width=10,
            color=GREEN,
            x_range=[1, 3, 0.001]
        )

        indicatorX = -8

        indicatorLjwPlus1 = grid[0].get_graph(
            lambda x: -3,
            discontinuities=[indicatorX, indicatorX+1],
            stroke_width=10,
            color=GREEN,
            x_range=[indicatorX, indicatorX+1]
        )

        indicatorArrow = Arrow(axes.c2p(indicatorX, -2), axes.c2p(indicatorX+1, -2), buff=0)
        textIndocatorArrow = Tex(r"F(j\omega) := 1 + L(j\omega)")
        textIndocatorArrow.next_to(indicatorArrow)

        textIndicatorLjwPlus1 = Tex(r"1 + L(j\omega)")
        textIndicatorLjwPlus1.next_to(indicatorLjwPlus1)

        self.play(
            ShowCreation(indicatorLjwPlus1),
            Write(textIndicatorLjwPlus1),
            ShowCreation(indicatorArrow),
            Write(textIndocatorArrow)
        )

        self.play(
            ShowCreation(graphLjwPlus1)
        )


        argDot = Dot()
        argDot.scale(0)
        argDot.move_to(axes.c2p(1, 0))
        argArrow = always_redraw(lambda: Arrow(axes.c2p(0, 0), axes.c2p(axes.p2c(argDot.get_x())[0], -np.sqrt(1-(axes.p2c(argDot.get_x())[0]-2)**2)), buff=0))


        self.play(ShowCreation(argArrow))
        self.play(argDot.animate.move_to(axes.c2p(2, 0)))
        self.play(argDot.animate.move_to(axes.c2p(2.99999999, 0)))
        self.wait()
        self.play(argDot.animate.move_to(axes.c2p(1.5, 0)))

        fixedArrow = Arrow(axes.c2p(0, 0), axes.c2p(axes.p2c(argDot.get_x())[0], -np.sqrt(1-(axes.p2c(argDot.get_x())[0]-2)**2)), buff=0)

        self.add(fixedArrow)
        self.play(FadeOut(argArrow))

        graphStuff = VGroup(fixedArrow, graphLjwPlus1)
        self.bring_to_front(fixedArrow)
        self.play(graphStuff.shift, 1*DOWN)
        self.play(graphStuff.shift, 1*UP)
        self.play(graphStuff.shift, 1*RIGHT)

        self.wait()

        graphLjw = grid[0].get_graph(
            lambda x: -np.sqrt(1-(x-1)**2) if x >= 0 and x <= 2 else 0,
            discontinuities=[0, 2],
            stroke_width=10,
            color=RED,
            x_range=[0, 2, 0.001]
        )


        indicatorLjw = grid[0].get_graph(
            lambda x: -4,
            discontinuities=[indicatorX, indicatorX+1],
            stroke_width=10,
            color=RED,
            x_range=[indicatorX, indicatorX+1]
        )

        textIndicatorLjw = Tex(r"L(j\omega)")
        textIndicatorLjw.next_to(indicatorLjw)

        self.play(
            ShowCreation(indicatorLjw),
            Write(textIndicatorLjw)
        )

        self.play(
            ShowCreation(graphLjw)
        )

        self.wait()

        self.play(graphStuff.shift, 1.75*LEFT)

        point = Dot()
        point.scale(.75)
        point.set_color(RED)
        point.move_to(axes.c2p(-1, 0))
        self.play(FadeIn(point))

        argArrow = always_redraw(lambda: Arrow(axes.c2p(-1, 0), axes.c2p(axes.p2c(argDot.get_x())[0], -np.sqrt(1-(axes.p2c(argDot.get_x())[0]-1)**2)), buff=0))
        argDot.move_to(axes.c2p(.5, 0))
        
        self.play(ShowCreation(argArrow)) 
        self.remove(fixedArrow)
        self.play(argDot.animate.move_to(axes.c2p(1.9999999, 0)))
        self.play(argDot.animate.move_to(axes.c2p(1, 0)))
        self.wait()
        self.play(argDot.animate.move_to(axes.c2p(1e-6, 0)))

        self.play(point.scale, 1.5)

        self.play(FadeOut(argArrow))

        self.play(
            VGroup(
                grid, graphStuff, point, graphLjw,
                indicatorLjw, textIndicatorLjw,
                indicatorLjwPlus1, textIndicatorLjwPlus1,
                indicatorArrow, textIndocatorArrow
            ).shift, 20*RIGHT,
            texTitle.shift, 5*UP,
            textForumla.shift, 12*LEFT
        )


class example(Scene):
    def construct(self):

        textExample = Tex(r"\underline{\text{Example}}")
        textExample.shift(3*UP+10*LEFT)

        self.add(textExample)
        self.play(textExample.shift, 5*RIGHT)

        equation_s = Tex(r"L_{(s)}", " = {", "K", "\over ", "(s + 1)}")

        self.play(Write(equation_s))


        poles = Tex(r"s_1 = -1")
        poles[0][0:2].set_color(BLUE)


        self.wait(2)

        polePoses = Tex(r"n_l = 1 \qquad ", r"n_i = 0 \qquad ", r"n_r = 0")
        polePoses[0][0:2].set_color(BLUE)
        polePoses[1][0:2].set_color(RED)
        polePoses[2][0:2].set_color(GREEN)

        poles.next_to(equation_s, BOTTOM)
        polePoses.next_to(poles, BOTTOM)

        self.play(
            Write(poles),
            equation_s[4].set_color, BLUE
        )
        self.wait()
        self.play(
            equation_s[4].set_color, WHITE,
            poles.set_color, WHITE
        )

        self.play(Write(polePoses[0]))
        self.play(Write(polePoses[1]))
        self.play(Write(polePoses[2]))

        argEquation = Tex("\\Delta ",
                          "arg \\left\\lbrace 1 + L(j\\omega) \\right\\rbrace = ",
                          "(n_i + 2n_r)\\frac{\\pi}{2}"
                        )

        argEquation.next_to(equation_s, BOTTOM)

        self.play(ReplacementTransform(poles, argEquation))
        self.play(
            argEquation[2][1:3].set_color, RED,
            argEquation[2][5:7].set_color, GREEN
        )
        self.wait()

        textResult = Tex("0")
        textResult.next_to(argEquation[1])
        self.play(ReplacementTransform(
            argEquation[2], textResult
        ))

        self.wait()

        argEquationAll = VGroup(argEquation, textResult)
        self.play(
            equation_s.shift, 4*RIGHT+2*UP,
            argEquationAll.shift, 5*RIGHT+2.6*UP,
            polePoses.shift, 5*DOWN
        )

        self.wait()

        equation_jw = Tex(r"L_{(j\omega)}", " = {", "K",  "\over ", "(j\omega + 1)}")
        equation_jw.move_to(equation_s)

        self.play(
            ReplacementTransform(equation_s, equation_jw)
        )

        # -------------------------------------------------
        w, k = 0, 2

        kText = Tex(r"K = ")
        kText.next_to(argEquationAll, BOTTOM)

        wText = Tex(r"\omega = ")
        wText.next_to(kText, BOTTOM)

        kDecimalNumber = DecimalNumber(k,**{"unit": r""})
        kDecimalNumber.scale(.7)
        kDecimalNumber.next_to(kText)

        wDecimalNumber = DecimalNumber(w,**{"unit": r""})
        wDecimalNumber.scale(.7)
        wDecimalNumber.next_to(wText)

        self.wait()

        self.play(
            Write(kText), 
            Write(kDecimalNumber)
        )

        self.wait()

        self.play(
            Write(wText), 
            Write(wDecimalNumber)
        )


        self.wait()


        # -------------------------------------------------
        # grid stuff
        grid = getImagGrid(r"L_{(j\omega)}", xOffset=1.2)
        axes = grid[0]

        grid.shift(4*LEFT+1*DOWN)
        grid.scale(.8)
        self.play(ShowCreation(grid))

        graphLjw = grid[0].get_graph(
            lambda x: -np.sqrt(1-(x-1)**2) if x >= 0 and x <= 2 else 0,
            discontinuities=[0, 2, 0],
            stroke_width=10,
            color=GREEN,
            x_range=[0, 2, 0.001]
        )

        indicatorX = 2

        indicatorLjw = grid[0].get_graph(
            lambda x: -3,
            discontinuities=[indicatorX, indicatorX+1],
            stroke_width=10,
            color=GREEN,
            x_range=[indicatorX, indicatorX+1]
        )

        indicatorArrow = Arrow(axes.c2p(indicatorX, -2), axes.c2p(indicatorX+1, -2), buff=0)
        textIndocatorArrow = Tex(r"F(j\omega) := 1 + L(j\omega)")
        textIndocatorArrow.scale(.7)
        textIndocatorArrow.next_to(indicatorArrow)

        textIndicatorLjw = Tex(r"L(j\omega)")
        textIndicatorLjw.scale(.7)
        textIndicatorLjw.next_to(indicatorLjw)

        #self.play(
        #    ShowCreation(indicatorLjw),
        #    Write(textIndicatorLjw)
        #)

        # ----------------------------------------
        #self.play(
        #    ShowCreation(graphLjw)
        #)

        # ----------------------------------------
        # Change omega
        
        L = lambda w, k: k / ((w*1.j + 1)) 

        tol = 1e-9
        LPoints = lambda t: np.array([np.real(L(min(t, wDecimalNumber.get_value()), kDecimalNumber.get_value())), \
                                      np.imag(L(min(t, wDecimalNumber.get_value()), kDecimalNumber.get_value())), \
                                      0])
        
        tRange_ = [2*tol, 30, .01]

        plane = axes
        locus = plane.get_parametric_curve(
            LPoints,
            t_range=tRange_,
            tolerance_for_point_equality=tol,
            epsilon=tol
        )
        

        locus.add_updater(
            lambda mob: mob.become(plane.get_parametric_curve(
                LPoints,
                t_range=tRange_,
                tolerance_for_point_equality=tol,
                epsilon=tol, 
                color=[RED,YELLOW,BLUE,RED])
            )
        )
        
        plane.add(locus)


        self.wait()
   
        self.play(
            wText[0][0].set_color, RED,
            equation_jw[0][3].set_color, RED,
            equation_jw[4][2].set_color, RED
        )


        self.wait()

        self.play(
            ChangeDecimalToValue(wDecimalNumber, 30),
            run_time=2
        )

        wInfValue = Tex(r"\infty")
        wInfValue.next_to(wText)


        self.wait()

        self.play(ReplacementTransform(wDecimalNumber, wInfValue))

        wDecimalNumber.set_value(1e6)

        self.wait()

        self.play(
            wText.set_color, WHITE,
            equation_jw.set_color, WHITE
        )

        dot = Dot()
        dot.scale(.75)
        dot.set_color(RED)
        dot.move_to(axes.c2p(-1, 0))
        self.play(FadeIn(dot))


        self.wait()

        self.play(
            Write(indicatorArrow),
            Write(textIndocatorArrow)
        )


        argDot = Dot()
        argDot.scale(0)
        argDot.move_to(axes.c2p(1.99999999999999999, 0))

        arrowR = lambda k_: k_ / 2
        argArrow = always_redraw(lambda: Arrow(axes.c2p(-1, 0), axes.c2p(axes.p2c(argDot.get_x())[0], -1*np.sign(kDecimalNumber.get_value())*np.sqrt(arrowR(kDecimalNumber.get_value())**2-(axes.p2c(argDot.get_x())[0]-arrowR(kDecimalNumber.get_value()))**2)), buff=0))



        self.wait()

        self.play(ShowCreation(argArrow))
        self.play(argDot.animate.move_to(axes.c2p(1, 0)))
        self.play(argDot.animate.move_to(axes.c2p(1e-6, 0)))

        self.wait(2)

        self.play(argEquation[2].set_color, GREEN)
        self.wait()


        ###################################################
        # Change K

        self.play(
            kText[0][0].set_color, BLUE,
            equation_jw[2].set_color, BLUE
        )


        self.wait()

        self.play(
            ChangeDecimalToValue(kDecimalNumber, 2.999999999),
            run_time=2
        )

        argDot.move_to(axes.c2p(2.999999999, 0))
        self.play(argDot.animate.move_to(axes.c2p(1e-6, 0)))


        self.wait()

        self.play(
            ChangeDecimalToValue(kDecimalNumber, -1),
            run_time=2
        )

        self.play(argEquation[2].set_color, RED)


        self.wait()

        self.play(
            ChangeDecimalToValue(kDecimalNumber, -2),
            run_time=2
        )

        argDot.move_to(axes.c2p(-1.999999999, 0))
        self.play(argDot.animate.move_to(axes.c2p(-1e-6, 0)))

        self.wait()

        self.play(
            kText.set_color, WHITE,
            equation_jw.set_color, WHITE
        )

        self.wait(2)


