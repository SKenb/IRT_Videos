#!/usr/bin/env python

from manimlib import *

# To watch one of these scenes, run the following:
# python -m manim VideoIRT.py [scene]
# add -n [number] to skip first n animations

class stetige_winkel(Scene):
    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):
        eq0 = Tex(
            "F(s) = ",
            "K {\\prod\\limits_{i=1}^{m}",
            "(s-\\beta_i)",
            "\\over \\prod\\limits_{i=1}^{n}",
            "(s-\\alpha_i)",
            "}\\quad \\mathrm{mit} \quad K \in\mathbb{R}, \\alpha_i,\\beta_i\in\mathbb{C}"
        )

        eq0.shift(UP*2.5+LEFT)
        self.play(Write(eq0),
            run_time = 5
        )

        eq1 = Tex("m = m_l + m_a + m_r")
        eq1.shift(UP)
        eq1.align_to(eq0, LEFT)
        self.play(Write(eq1))

        eq2 = Tex(",\\quad n = n_l + n_a + n_r")
        eq2.shift(UP+RIGHT)
        eq2.next_to(eq1)
        self.play(Write(eq2))

        eq3 = Tex(
            "F(j\\omega) = ",
            "K {\\prod\\limits_{i=1}^{m}",
            "(j\\omega-\\beta_i)",
            "\\over \\prod\\limits_{i=1}^{n}",
            "(j\\omega-\\alpha_i)",
            "}\\quad \\mathrm{mit} \quad K \in\mathbb{R}, \\alpha_i,\\beta_i\in\mathbb{C}"
        )
        eq3.shift(UP*2.5+LEFT),
        self.play(
            ReplacementTransform(eq0[0],eq3[0]),
            ReplacementTransform(eq0[2],eq3[2]),
            ReplacementTransform(eq0[4],eq3[4]),
            run_time=1
            )

        eq4 = Tex(
            "arg F(j\\omega) = arg K +\\sum\\limits_{i=1}^{m}\!arg(j\\omega-\\beta_i)-",
            "\\sum\\limits_{i=1}^{n}\!arg(j\\omega-\\alpha_i)"
        )
        eq4.align_to(eq1, LEFT)
        self.play(Write(eq4))

        eq5 = Tex(
            "\\underset{-\\infty}{\\overset{+\\infty}{\\Delta}}arg F(j\\omega) = ",
            "\\underset{-\\infty}{\\overset{+\\infty}{\\Delta}}arg K",
            "+\\sum\\limits_{i=1}^m\\underset{-\\infty}{\\overset{+\\infty}{\\Delta}}arg(j\\omega-\\beta_i)\\\\-",
            "\\sum\\limits_{i=1}^n\\underset{-\\infty}{\\overset{+\\infty}{\\Delta}}arg(j\\omega-\\alpha_i)"
        )
        eq5.shift(2*DOWN)
        eq5.align_to(eq4, LEFT)
        self.play(Write(eq5))
        self.play(
            FadeOut(eq4),
            eq5.shift, UP,
            run_time = 1
            )

        eq6 = Tex(
            "\\underset{-\\infty}{\\overset{+\\infty}{\\Delta}}arg F(j\\omega) = 0 + m_a\\cdot 0 + m_l\\cdot\\pi-m_r\\pi - n_a\\cdot 0-n_l\\pi+n_r\\pi"
        )
        eq6.shift(3*DOWN)# + LEFT)
        # eq6.align_to(eq4, LEFT)
        self.play(Write(eq6))
        self.play(
            FadeOut(eq5),
            eq6.shift, 3*UP,
            run_time = 1
            )

        eq7 = Tex(
            "\\underset{-\\infty}{\\overset{+\\infty}{\\Delta}}arg F(j\\omega) = (m-n)\\pi + (m_a+2m_r)\\pi-(n_a+2n_r)\\pi"
        )
        eq7.shift(DOWN)
        eq7.align_to(eq4, LEFT)
        self.play(Write(eq7))
        self.play(
            FadeOut(eq6),
            FadeOut(eq1),
            FadeOut(eq2),
            eq7.shift, 2*UP,
            run_time = 1
            )

        eq8 = Tex(
            "\\underset{0}{\\overset{+\\infty}{\\Delta}}",
            "arg F(j\\omega) = (m-n)\\frac{\\pi}{2} + (m_a+2m_r)\\frac{\\pi}{2}-(n_a+2n_r)\\frac{\\pi}{2}"
        )
        eq8.align_to(eq4, LEFT)
        self.play(Write(eq8))
        self.play(
            FadeOut(eq7),
            eq8.shift, UP,
            # eq8.align_to, eq0, LEFT,
            run_time = 1
            )

        eq9 = Tex(
            "\\Delta ",
            "arg F(j\\omega) = (m-n)\\frac{\\pi}{2} + (m_a+2m_r)\\frac{\\pi}{2}-(n_a+2n_r)\\frac{\\pi}{2}"
        )
        eq9.shift(UP)
        eq9.align_to(eq4, LEFT)
        self.play(
            ReplacementTransform(eq8[0],eq9[0]),
            run_time=1
        )
        self.wait(3)
        self.play(
            FadeOut(eq8[1:]),
            FadeOut(eq9[0]),
            FadeOut(eq0[1]),
            FadeOut(eq0[3]),
            FadeOut(eq0[5:]),
            FadeOut(eq3[0]),
            FadeOut(eq3[2]),
            FadeOut(eq3[4]),
            run_time=1,
            )

        txt = TexText(
            "\\underline{Nyquist Kriterium}"
        ).shift(2.5*UP + 3*LEFT)
        txt.set_color("#ffff00")
        self.play(
            Write(txt)
        )

        eq10 = Tex(
            "\\Delta ",
            "arg \\left\\lbrace 1 + L(j\\omega) \\right\\rbrace = (n_a+2n_r)\\frac{\\pi}{2}"
        )
        eq10.shift(UP)
        eq10.align_to(txt, LEFT)
        self.play(
            Write(eq10),
            run_time=1
        )
        self.wait()
        ###################################################
        # Sachen löschen
        ###################################################

        # self.play(
        #     FadeOut(eq10),
        #     FadeOut(eq8[1:]),
        #     run_time=1,
        #     )
        self.wait()

class funktion1(Scene):
    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):
        eq0 = Tex(
            "L(s) = \\frac{K}{s(s+1)} \\quad \\mathrm{mit} \\quad K\in\mathbb{R}"
        )
        eq0.shift(UP*2.5+LEFT*2)
        self.play(Write(eq0))

        eq1 = Tex("n_a = 1, n_r = 0")
        eq1.shift(UP)
        eq1.align_to(eq0, LEFT)
        self.play(Write(eq1))

        eq2 = Tex("\\Delta arg\\left\\lbrace 1+L(j\\omega)\\right\\rbrace \\overset{!}{=}\\frac{\\pi}{2}")
        eq2.align_to(eq0, LEFT)
        self.play(Write(eq2))

        self.wait()
        ###################################################
        # Sachen löschen
        ###################################################

        self.play(
            FadeOut(eq0),
            FadeOut(eq1),
            FadeOut(eq2),
            run_time=1,
            )
        self.wait()

class genericExample(Scene):
    L = lambda s, w, k: k / (max(w, 1e-6)*1.j * (w*1.j + 1)) 
    equation_s = Tex(r"L_{(s)}", " = {", "K", "\over ", "(s)", "(s + 1)}")
    equation_jw = Tex(r"L_{(j\omega)}", " = {", "K",  "\over ", "(j\omega)", "(j\omega + 1)}")
    indexK = 2
    eqPoleIndices = [4, 5]
    reqArg = "\\frac{\\pi}{2}"
    nAValue = 1
    nRValue = 0
    poleTexts = [
                    [r"s", "\quad \\rightarrow \; s_1 = 0"],
                    [r"s + 1", "\quad \\rightarrow \; s_2 = -1"]
                ]

    def construct(self):

        ###################################################
        # Defines
        colorMap = [RED, GOLD, YELLOW, BLUE]
    
        plane = ThreeDAxes()
        
        poles = VGroup(*[Tex(*poleText) for poleText in self.poleTexts])

        nAnRValues = Tex("n_a = " + str(self.nAValue), \
                         " \\quad ", "n_r = " + str(self.nRValue))

        argEquation = Tex("\\Delta ",
                          "arg \\left\\lbrace 1 + L(j\\omega) \\right\\rbrace = ",
                          "(n_a + 2n_r)\\frac{\\pi}{2}"
                        )

        argResultEquation = Tex("\\Delta ",
                                "arg \\left\\lbrace 1 + L(j\\omega) \\right\\rbrace = ",
                                self.reqArg
                                )

        infText = Tex(r"\rightarrow \infty").scale(1.3)

        equations = VGroup(self.equation_s, poles)


        ###################################################
        # Positioning
        if len(poles) > 0:
            poles[0].next_to(self.equation_s,3*DOWN)
            print(len(poles))
        
            for index in range(1,len(poles)):
                poles[index].next_to(poles[index-1],DOWN)

        nAnRValues.next_to(self.equation_s,3*DOWN)
        argEquation.next_to(nAnRValues,DOWN)
        argResultEquation.next_to(nAnRValues,DOWN)

        ###################################################
        # Start animation / scene
        self.play(Write(self.equation_s))

        ###################################################
        # Poles
        for index in range(0,len(poles)):

            color = colorMap[index % len(colorMap)]
            self.play(ApplyMethod(self.equation_s[self.eqPoleIndices[index]].set_color, color))
            poles[index][0].set_color(color)
            self.play(Write(poles[index]))

        self.wait(1)

        ###################################################
        # n_a, n_r
        if len(poles) > 1:
            self.play(
                Transform(poles[0], nAnRValues),
                Transform(poles[1], argEquation)
            )

            self.wait(1)
            self.play(
                FadeOut(argEquation),
                Transform(poles[1],argResultEquation),
            )
        else:
            self.play(
                Transform(poles[0], nAnRValues),
                Write(argEquation)
            )

            equations = VGroup(equations, argEquation)

            self.wait(1)
            self.play(
                Transform(argEquation,argResultEquation),
            )


        self.wait(1)
        self.play(ApplyMethod(equations.to_corner, UR))
        self.play(ApplyMethod(equations.scale, .8))


        ###################################################
        # Omega, K
        paramText = VGroup(*[
            Tex(f"{t}=",tex_to_color_map={f"{t}":color}).scale(1.3)
            for t,color in zip(["\omega", "K"],[MAROON, GREEN])
        ])
        paramText.arrange(DOWN,aligned_edge=LEFT,buff=1.2)
        paramText.next_to(equations,DOWN,buff=1.4)
        paramText.align_to(equations,LEFT).shift(RIGHT*0.2)

        omega, k = 0, 1
        omegaDecimalNumber = DecimalNumber(omega,**{"unit": r""})
        kDecimalNumber = DecimalNumber(k,**{"unit": r""})

        groupDecimalNumbers = VGroup(omegaDecimalNumber, kDecimalNumber)

        for d,s in zip(groupDecimalNumbers, paramText):
            d.next_to(s,aligned_edge=DOWN)

        infText.next_to(paramText[0] ,aligned_edge=DOWN)


        ###################################################
        # Complex plane
        #plane = ExamplePlane3D()

        # 3D
        #frame = self.camera.frame
        #self.play(ApplyMethod(frame.reorient, 30, 45, 0))

        plane.add_coordinate_labels()
        plane.scale(.75)
        plane.to_edge(LEFT)

        self.play(ShowCreation(plane))


        # Back to 0 - no 3d
        #self.play(ApplyMethod(frame.reorient, 0, 0, 0))


        ###################################################
        # Change \omega
        self.play(
            Write(paramText[0]), 
            Write(groupDecimalNumbers[0])
        )

        self.equation_jw.move_to(self.equation_s)
        self.equation_jw.scale(.75)

        self.play(ReplacementTransform(self.equation_s[0],self.equation_jw[0]))
        for index in self.eqPoleIndices:
             self.play(ReplacementTransform( \
                 self.equation_s[index],self.equation_jw[index]))



        ###################################################
        # Locus
        tol = 1e-9
        LPoints = lambda t: np.array([np.real(self.L(min(t, omegaDecimalNumber.get_value()), kDecimalNumber.get_value())), \
                                      np.imag(self.L(min(t, omegaDecimalNumber.get_value()), kDecimalNumber.get_value())), \
                                      0])
        
        tRange_ = [2*tol, 30, .01]

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


        ###################################################
        # Animate
        self.play(
            ChangeDecimalToValue(omegaDecimalNumber, 30),
            run_time=3,
        )
        self.play(Transform(omegaDecimalNumber,infText))


        ###################################################
        # Change K

        self.play(
            Write(paramText[1]), 
            Write(groupDecimalNumbers[1]),
            ApplyMethod(self.equation_s[self.indexK].set_color, GREEN)
        )

        self.play(
            ChangeDecimalToValue(kDecimalNumber, 3),
            run_time=2
        )


        self.play(
            ChangeDecimalToValue(kDecimalNumber, -3),
            run_time=2
        )

        self.wait(2)

        ###################################################
        # L + 1
        


    def get_func_value(self, L, k, w=None):
        tol = 1e-9

        if w is None:
            pc = ParametricCurve(
                lambda t: np.array([
                    np.real(L(t, k)),
                    np.imag(L(t, k)),
                    0
                ]),
                t_range=[2*tol, 100, .1],
                tolerance_for_point_equality=tol,
                epsilon=tol,
            )
        else:
            pc = ParametricCurve(
                lambda t: np.array([
                    np.real(L(w, k)),
                    np.imag(L(w, k)),
                    w
                ]),
                t_range=[2*tol, 100,.1],
                tolerance_for_point_equality=tol,
                epsilon=tol,
            )

        pc.set_color(color=[RED,YELLOW,BLUE,RED])
        #pc.scale(2)
        return pc

class example1(genericExample):
    pass

class example2(genericExample):
    L = lambda s, w, k: k / ((w*1.j + 1)) 
    equation_s = Tex(r"L_{(s)}", " = {", "K", "\over ", "(s + 1)}")
    equation_jw = Tex(r"L_{(j\omega)}", " = {", "K",  "\over ", "(j\omega + 1)}")
    indexK = 2
    eqPoleIndices = [4]
    reqArg = "0"
    nAValue = 0
    nRValue = 0
    poleTexts = [
                    [r"s", "\quad \\rightarrow \; s_1 = 0"]
                ]
