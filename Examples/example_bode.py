#!/usr/bin/env python

from manimlib import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.

class Bode_title_scene(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):
        t0 = TexText("Grundlagen der Elektrotechnik")
        t0.set_color_by_gradient("#8ad7be")
        t1 = TexText("\\large{Einheit 9}")
        t1.set_color_by_gradient("#eedc98")
        t2 = TexText("\\Large{Bode Diagramme}")
        t2.set_color_by_gradient("#eaaf7d")
        t0.move_to(UP*2)

        t0.scale(1.5)
        t1.scale(1.5)
        t2.scale(1.5)

        self.play(Write(t0,runtime = 1))
        self.play(Write(t1,runtime = 2))
        self.wait(0.5)
        self.play(Transform(t1, t2))
        self.play(t1.scale,1.3)
        self.play(ShrinkToCenter(t0,runtime=1),ShrinkToCenter(t1,runtime=3))
        self.wait()


class bode_einleitung(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        ###########################################################
        ###########################################################
        # Schaltbild Parameter

        length_box = 5
        length_line = 2
        y_diff = 2
        y_shift = -1
        x_shift = 4.5
        text_abstand=1

        ###########################################################
        ###########################################################

        klemme_l_o = Circle(radius = 0.1,color=WHITE)
        klemme_l_o.shift(UP*y_diff+UP*y_shift+LEFT*x_shift)

        klemme_l_u = Circle(radius = 0.1,color=WHITE)
        klemme_l_u.shift(UP*y_shift+LEFT*x_shift)

        line_klemme_l_o_box = Line(LEFT*0,RIGHT*length_line)
        line_klemme_l_o_box.next_to(klemme_l_o.get_corner(RIGHT), RIGHT,buff=0)

        line_klemme_r_o_box = Line(LEFT*0,RIGHT*length_line)
        line_klemme_r_o_box.next_to(klemme_l_o.get_corner(RIGHT), RIGHT,buff=0)
        line_klemme_r_o_box.shift(RIGHT*(length_box+length_line))

        line_klemme_l_u_box = Line(LEFT*0,RIGHT*length_line)
        line_klemme_l_u_box.next_to(klemme_l_u.get_corner(RIGHT), RIGHT,buff=0)

        line_klemme_r_u_box = Line(LEFT*0,RIGHT*length_line)
        line_klemme_r_u_box.next_to(klemme_l_u.get_corner(RIGHT), RIGHT,buff=0)
        line_klemme_r_u_box.shift(RIGHT*(length_box+length_line))

        klemme_r_o = Circle(radius = 0.1,color=WHITE)
        klemme_r_o.next_to(line_klemme_r_o_box.get_corner(RIGHT), RIGHT,buff=0)

        klemme_r_u = Circle(radius = 0.1,color=WHITE)
        klemme_r_u.next_to(line_klemme_r_u_box.get_corner(RIGHT), RIGHT,buff=0)

        box = Rectangle(height=y_diff*1.5, width=length_box)
        box.next_to(((line_klemme_l_o_box.get_corner(RIGHT)+line_klemme_l_u_box.get_corner(RIGHT))/2), RIGHT,buff=0)
        text = TexText("passives","lineares","Netzwerk")

        text[0].next_to(box.get_center(), LEFT*0)
        text[0].shift(UP*text_abstand)
        text[1].next_to(box.get_center(), LEFT*0)
        text[1].shift(DOWN*0)
        text[2].next_to(box.get_center(), LEFT*0)
        text[2].shift(DOWN*text_abstand)

        U_e = CurvedArrow(DOWN*0, UP*(y_diff-0.2), angle=-TAU/4, color=BLUE)
        U_e.next_to(klemme_l_o.get_corner(LEFT),DOWN+LEFT,buff=0.1)

        UE_text = TexText('$\\underline{U}_e$',color=BLUE)
        UE_text.next_to(U_e.get_center(), RIGHT*0.5)

        U_a = CurvedArrow(DOWN*0, UP*(y_diff-0.2), angle=-TAU/4, color=BLUE)
        U_a.flip(UP)
        U_a.next_to(klemme_r_o.get_corner(RIGHT),DOWN+RIGHT,buff=0.1)

        UA_text = TexText('$\\underline{U}_a$',color=BLUE)
        UA_text.next_to(U_a.get_center(), LEFT*0.5)

        #----------------------------------------------------------

        NetzwerkGROUP = VGroup(klemme_l_o,klemme_l_u,klemme_r_o,klemme_r_u,line_klemme_l_u_box,
            line_klemme_l_o_box,line_klemme_r_u_box,line_klemme_r_o_box,box,text,U_e,U_a,UA_text,UE_text)

        ###########################################################
        # EQUATIONS
        ###########################################################

        F_jw = Tex(
            "\\underline{F}(j\\omega)",
            "=",
            "{\\underline{U}_a",
            "\\over",
            "\\underline{U}_e}",
            )
        F_jw_rest = Tex(
            "=",
            "K",
            "\\cdot",
            "{ \\left( { {j\\omega} \\over \\omega_0 } \\right)^{m_1}",
            "\\left( { 1 \\pm { {j\\omega} \\over \\omega_1 }} \\right)",
            "\\left( { 1 \\pm { {j\\omega} \\over \\omega_2 }} \\right)",
            "\\cdots",
            "\\left( { 1 \\pm { {j\\omega} \\over \\omega_{m-m_1} }} \\right)",
            # BRUCHSTRICH
            "\\over",
            # BRUCHSTRICH
            "\\left( { {j\\omega} \\over \\Omega_0 } \\right)^{n_1}",
            "\\left( { 1 \\pm { {j\\omega} \\over \\Omega_1 }} \\right)",
            "\\left( { 1 \\pm { {j\\omega} \\over \\Omega_2 }} \\right)",
            "\\cdots",
            "\\left( { 1 \\pm { {j\\omega} \\over \\Omega_{n-n_1} }} \\right)}",
            )

        F_jw_el_R = Tex(
            "\\omega_0, \\omega_1, \\omega_2, \\dots, \\omega_{m-m_1} \\in \\mathbb{R}^+",
            "\\hspace{0.5cm}",
            "\\Omega_0, \\Omega_1, \\Omega_2, \\dots, \\Omega_{n-n_1} \\in \\mathbb{R}^+",
            )

        F_jw_DB = Tex(
            "\\underline{F}(j\\omega)",
            "=",
            "|\\underline{F}(j\\omega)|",
            "e^{",
            "j",
            "arg\\{\\underline{F}(j\\omega)\\} }",
            ).set_color(TEAL_B)

        F_DEZIBEL = Tex(
            "\\left.\\underline{F}(j\\omega)\\right|_{dB}",
            "=",
            "{20 \\cdot}",
            "\\log_{10}",
            "\\left|  \\underline{F}(j\\omega) \\right|",
            )

        eq_shift = 5*LEFT

        F_jw.scale(0.9)
        F_jw_rest.scale(0.9)
        F_jw_el_R.scale(0.8)

        F_jw.shift(DOWN*1.5)
        F_jw_rest.next_to(F_jw.get_corner(RIGHT), RIGHT)
        F_jw_rest.shift(eq_shift)
        F_jw_el_R.shift(DOWN*3.3)
        F_jw_DB.shift(DOWN*0.9)
        F_DEZIBEL.shift(2.5*DOWN)

        F_jwGROUP = VGroup(F_jw,F_jw_rest,F_jw_el_R)

        ######
        # BOXXXX
        #####

        framebox_FdB = SurroundingRectangle(F_jw_DB, buff = .3).set_color(TEAL_B)

        ###########################################################
        ###########################################################
        # PLAY
        ###########################################################
        ###########################################################

        # BOX
        self.play(Write(klemme_l_o),Write(klemme_l_u))
        self.play(Write(line_klemme_l_o_box),Write(line_klemme_l_u_box))
        self.play(Write(box))
        self.play(Write(text))
        self.play(Write(line_klemme_r_o_box),Write(line_klemme_r_u_box))
        self.play(Write(klemme_r_o),Write(klemme_r_u))
        self.play(Write(U_e))
        self.play(Write(UE_text))
        self.play(Write(U_a))
        self.play(Write(UA_text))
        self.wait(2)

        self.play(NetzwerkGROUP.shift,UP*2, runtime = 2)

        # EQUATION
        self.play(Write(F_jw))
        self.play(F_jw.shift,eq_shift,runtime=2)
        self.wait()

        self.play(Write(F_jw_rest[0]))
        for i in [1,2,8,3,4,5,6,7,9,10,11,12,13]:
            self.play(Write(F_jw_rest[i].set_color(ORANGE)))
            self.wait(0.3)
            F_jw_rest[i].set_color(WHITE)

        self.wait(2)
        self.play(Write(F_jw_el_R[0:2]))
        self.wait(0.5)
        self.play(Write(F_jw_el_R[2]))
        self.wait(3)

        ###########################################################
        # DELETE LTI
        ###########################################################

        self.play(FadeOut(NetzwerkGROUP))
        self.play(F_jwGROUP.shift, UP*4)
        self.wait(2)

        ##########################################################
        # PLAY DEZIBEL SHIT
        ##########################################################
        self.play( Write(F_jw_DB))
        self.play( ShowCreation(framebox_FdB) )
        self.wait(2)

        for i in range(5):
            self.play(Write(F_DEZIBEL[i].set_color(YELLOW_B)))
            self.wait(0.3)
            F_DEZIBEL[i].set_color(WHITE)

        self.wait(4)

class bode_einleitung2(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        ###########################################################
        ###########################################################
        # TEXT
        ###########################################################

        text1 = TexText("Ist die",
        r"\textbf{{\"U}bertragungsfunktion}",
        "$\\underline{F}(j\\omega)$ des Netzwerkes bekannt,",
        "so kann die Antwort auf eine beliebige Erregung bestimmt werden.")
        text1.scale(0.7)
        text1[1].set_color(MAROON_B)

        ###########################################################
        # EQUATIONS
        ###########################################################

        ue_t = Tex(
            "u_e(t)",
            "=",
            "\\sqrt{2}",
            "U_{e_{eff}}",
            "\\cos ( \\tilde{\\omega} t + \\phi_{u_e} ) "
            )

        UE = Tex(
            "\\underline{U}_e",
            "=",
            "U_{e_{eff}}",
            "e^{",
            "j \\phi_{u_e} }"
            )

        ua_t = Tex(
            "u_a(t)",
            "=",
            "\\sqrt{2}",
            "U_{a_{eff}}",
            "\\cos ( \\tilde{\\omega} t + \\phi_{u_a} ) "
            )

        UA = Tex(
            "\\underline{U}_a",
            "=",
            "\\underline{F}(j\\tilde{\\omega})",
            "\\underline{U}_e",
            "=",
            "U_{a_{eff}}",
            "e^{",
            "j \\phi_{u_a} }"
            )
        UA2 = Tex(
            "U_{a_{eff}}",
            "=",
            "|\\underline{F}(j\\tilde{\\omega})|",
            "U_{e_{eff}}",
            "\\hspace{0.7cm}",
            "\\phi_{u_a}",
            "=",
            "\\phi_{u_e}",
            "+",
            "arg\\{ \\underline{F}(j\\tilde{\\omega}) \\}"
            )

        UE.shift(DOWN)
        UA.shift(DOWN*0.7)
        UA2.shift(DOWN*1.6)
        ua_t.shift(DOWN*3)

        ue_GROUP = VGroup(ue_t,UE)

        framebox_ua_t = SurroundingRectangle(ua_t, buff = .3).set_color(MAROON_B)

        ###########################################################
        # PLAY ANIMATIONS
        ###########################################################
        self.play(Write(text1, run_time=5.0))
        self.play(text1.shift,UP*2)
        self.wait(2)
        #--------------
        # UE
        #--------------
        for i in range(len(ue_t)):
            self.play(Write(ue_t[i].set_color(YELLOW_B)))
            self.wait(0.3)
            ue_t[i].set_color(WHITE)
        self.wait()
        for i in range(len(UE)):
            self.play(Write(UE[i].set_color(YELLOW_B)))
            self.wait(0.3)
            UE[i].set_color(WHITE)
        self.wait()
        self.play(ue_GROUP.shift,UP*1.5, text1.shift,UP*1)
        #--------------
        # UA
        #--------------
        for i in range(len(UA)):
            self.play(Write(UA[i].set_color(YELLOW_B)))
            self.wait(0.3)
            UA[i].set_color(WHITE)
        self.wait()
        #--------------
        for i in range(len(UA2)):
            self.play(Write(UA2[i].set_color(YELLOW_B)))
            self.wait(0.3)
            UA2[i].set_color(WHITE)
        #--------------
        for i in range(len(ua_t)):
            self.play(Write(ua_t[i].set_color(MAROON_B)))
            self.wait(0.3)
            # ua_t[i].set_color(WHITE)

        self.play( ShowCreation(framebox_ua_t) )
        self.wait()

        self.wait(4)


class bsp1_einleitung(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        ###########################################################
        ###########################################################
        # TEXT
        ###########################################################

        text_BSP1 = TexText("Beispiel 1")
        text_BSP1.scale(1.2)
        text_BSP1.set_color(MAROON_B)

        #---------------------------------------------------

        text_geg = TexText(
            r"Gegeben sei folgende {\"U}bertragungsfunktion:").scale(0.8)
        text_geg.next_to(text_BSP1.get_corner(LEFT),LEFT*0)
        text_geg.shift(UP*2)

        #---------------------------------------------------

        F1 = Tex(
                "\\underline{F}_1(j \\omega)",
                "=",
                "10^{-3} \\frac{j\\omega+0.1}{j\\omega \\cdot (j\\omega + 10)}}"
            ).scale(0.8)

        F1.next_to(text_geg.get_corner(RIGHT),LEFT*0.3)
        F1.shift(DOWN)

        framebox_F = SurroundingRectangle(F1, buff = .1).set_color(MAROON_B)
        #---------------------------------------------------
        # Unterpunkt 1
        #---------------------------------------------------

        text_1 = TexText("1").scale(0.8)
        circle_1 = Circle(radius =0.35,color=WHITE).set_fill(MAROON_B,opacity=0.5)
        circle_1_GROUP = VGroup(circle_1,text_1)
        circle_1_GROUP.shift(6.5*LEFT+DOWN*0.5)

        text_ges_1 = TexText(
            r"\textit{ Faktorisieren der {\"U}bertragungsfunktion in die 5 charakteristischen Terme}.",
            "\\textit{Zeichnen des Bode-Diagramms (Amplituden- und Phasengang). }"
            ).scale(0.7)

        text_ges_1.next_to(circle_1_GROUP.get_corner(RIGHT),RIGHT*2)
        text_ges_1.shift(DOWN*0.2)
        #---------------------------------------------------

        #---------------------------------------------------
        # Unterpunkt 2
        #---------------------------------------------------

        text_2 = TexText("2").scale(0.8)
        circle_2 = Circle(radius =0.35,color=WHITE).set_fill(MAROON_B,opacity=0.5)
        circle_2_GROUP = VGroup(circle_2,text_2)
        circle_2_GROUP.shift(6.5*LEFT+DOWN*2)

        text_ges_2 = TexText(
            r"\textit{Berechnung des Ausgangssignals $u_a(t)$ f{\"u}r das folgende Eingangssignal:}"
            ).scale(0.7)

        text_ges_2.next_to(circle_2_GROUP.get_corner(RIGHT),RIGHT*2)
        text_ges_2.shift(UP*0)

        u_a_t = Tex(
            "u_e(t)",
            "=",
            "\\sqrt{2}\\cdot",
            "4\\mathrm{V}",
            "\\cos ( 1\\mathrm{\\frac{1}{s}} t + 15 \\degree) "
            ).scale(0.7)
        u_a_t[4][5:8].scale(0.8)
        u_a_t.next_to(text_geg.get_corner(RIGHT),LEFT*0.3)
        u_a_t.shift(DOWN*4.8)

        #---------------------------------------------------



        ##########################
        # PLAY
        #########################ä

        # überschrift
        self.play(Write(text_BSP1))
        self.play(text_BSP1.shift,UP*3+LEFT*4)
        self.wait()
        # angabe
        self.play(Write(text_geg))
        self.wait()
        self.play(Write(F1),ShowCreation(framebox_F))
        self.wait(2)
        #-------
        # kreis1
        self.play(Write(circle_1_GROUP))
        # gesucht 1
        self.play(Write(text_ges_1[0]),runtime=6)
        self.wait()
        self.play(Write(text_ges_1[1]),runtime=6)
        self.wait(3)
        #-------
        # kreis2
        self.play(Write(circle_2_GROUP))
        # gesucht 2
        self.play(Write(text_ges_2),runtime=6)
        self.play(Write(u_a_t),runtime=3)

        self.wait(3)



class bsp1_rechnung(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):
        eq0 = Tex(
            "\\underline{F}_1(j \\omega)"+"="+
            "\\left. 10^{-3} \\frac{j\\omega+0.1}{j\\omega \\cdot (j\\omega + 10)}\\right|_{j\\omega = s}"
        )

        self.play(Write(eq0))
        self.play(
                eq0.shift, UP*2.5+LEFT*2,
                eq0.scale, 1,
                eq0.set_color, WHITE,
                run_time=2,
            )

        eq1 = Tex("=\\left. 10^{-3} \\frac{s+0.1}{s\\cdot (s + 10)}")
        eq1.shift(UP)
        eq1.align_to(eq0[7:], LEFT)

        eq2 = Tex("=\\left. 10^{-3} \\frac{s+0.1}{s\\cdot (s + 10)}")
        eq2.next_to(eq1, RIGHT)
        eq2_2 = Tex("=\\left. 10^{-3} \\frac{\\frac{0.1}{0.1}(s+0.1) }{\\frac{10}{10}s\\cdot (s + 10) }")
        eq2_2.next_to(eq1, RIGHT)

        eq3_2 = Tex("=\\left. 10^{-3} \\frac{0.1}{10} \\frac{(\\frac{s}{0.1}+1)}{s\\cdot (\\frac{s}{10} + 1)}")
        eq3_2.shift(DOWN*0.5)
        eq3_2.align_to(eq1, LEFT)


        eq4 = Tex("= 10^{-5} \\frac{(\\frac{s}{0.1}+1)}{s\\cdot (\\frac{s}{10} + 1)}")
        eq4.shift(DOWN*2)
        eq4.align_to(eq3_2, LEFT)
        # s ... 6,15,18

        eq4[1:5].set_color(YELLOW_B)

        eq4_1 = Tex("=\\left. 10^{-5} \\frac{(\\frac{s}{0.1}+1)}{s\\cdot (\\frac{s}{10} + 1)}")
        eq4_1.next_to(eq4, RIGHT)
        eq4_1[1:5].set_color(YELLOW_B)

        eq4_2 = Tex("=\\left. 10^{-5} \\frac{(\\frac{j\\omega}{0.1}+1)}{j\\omega\\cdot (\\frac{j\\omega}{10} + 1)}")
        eq4_2.next_to(eq4, RIGHT)
        eq4_2[1:5].set_color(YELLOW_B)
        # jw ... 6,7 , 16,17  , 20,21

        framebox1 = SurroundingRectangle(eq1[7:10], buff = .1)
        framebox2 = SurroundingRectangle(eq1[16:18], buff = .1)

        self.play(Write(eq1))
        self.play(ShowCreation(framebox1.set_color(YELLOW_B)))
        self.wait()
        self.play(ShowCreation(framebox2.set_color(YELLOW_B)))
        self.wait()

        self.play(
            ReplacementTransform(eq1.copy(),eq2),
            run_time=1
            )

        self.wait()
        self.play(ReplacementTransform(eq2[5:10],eq2_2[5:19]),ReplacementTransform(eq2[11:19],eq2_2[20:33]))
        self.wait()

        self.play(
            ReplacementTransform(eq2.copy(),eq3_2),
            run_time=1
            )

        for letter in eq3_2[1:11]:
            self.play(LaggedStart(
                ApplyMethod, letter,
                lambda m : (m.set_color, YELLOW_B),
                run_time = 0.12
            ))

        self.wait()
        self.play(
            ReplacementTransform(eq3_2[0].copy(),eq4[0]),
            ReplacementTransform(eq3_2[1:11].copy(),eq4[1:5]),
            ReplacementTransform(eq3_2[12:].copy(),eq4[5:]),
            run_time=1
            )

        self.wait()

        for i in [6,15,18]:
            eq4[i].set_color(RED)
            eq4_1[i].set_color(RED)

        self.wait()

        for i in [6,7,16,17,20,21]:
            eq4_2[i].set_color(RED)

        self.wait()

        self.play(
            ReplacementTransform(eq4.copy(),eq4_1),
            run_time=1
            )
        self.play(ReplacementTransform(eq4_1[5:14],eq4_2[5:15]),ReplacementTransform(eq4_1[15:25],eq4_2[16:28]))
        self.wait(3)

        eq_group_sol = VGroup(eq4_1[1:],eq4_2[5:15],eq4_2[16:28])

        ###################################################
        # Sachen löschen
        ###################################################

        self.play(
            FadeOut(eq0[8:]),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq2_2[5:19]),
            FadeOut(eq2_2[20:33]),
            FadeOut(eq3_2),
            FadeOut(eq4[0:6]),
            FadeOut(eq4[6:]),
            FadeOut(eq4_1[0]),
            # FadeOut(eq4_2[6:15]),
            # FadeOut(eq4_2[16:28]),
            FadeOut(framebox1),
            FadeOut(framebox2),
            eq_group_sol.shift, UP*4.5+LEFT*4.3,
            run_time=1,
            )
        eq_group_sol.set_color(WHITE)
        self.wait()

class bsp1_rechnung2(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):
        F1 = Tex(
            "\\underline{F}_1(j \\omega) =",
            "\\left. 10^{-3} \\frac{j\\omega+0.1}{j\\omega \\cdot (j\\omega + 10)}\\right|_{j\\omega = s}",
        )
        F1_1 = Tex(
            "10^{-5} \\frac{(\\frac{j\\omega}{0.1}+1)}{j\\omega\\cdot (\\frac{j\\omega}{10} + 1)}"
            )

        F_2 = Tex(
            "=",
            "10^{-5}",
            "~~\\cdot~~",
            "\\left(\\frac{j\\omega}{0.1}+1\\right)",
            "~~\\cdot~~",
            "\\frac{1}{(\\frac{j\\omega}{10} + 1)}",
            "~~\\cdot~~",
            "\\frac{1}{j\\omega"
            )

        F1.shift(UP*2.5+LEFT*2)
        F1_1.align_to(F1[0][7].get_corner(RIGHT), LEFT)
        F1_1.shift(UP*2.5+RIGHT*0.27)

        F_2.align_to(F1[0][7].get_corner(LEFT), LEFT)
        F_2.shift(RIGHT*0)

        ########################
        # DEFINE FOUR BOXES!!!
        framebox_F11 = SurroundingRectangle(F_2[1], buff = .1)
        framebox_F11.set_color(YELLOW)
        t_F11 = Tex("F_1^{(1)} (j\\omega)")
        t_F11.next_to(framebox_F11, DOWN, buff=0.55)
        t_F11.set_color(YELLOW)
        #----------------------------
        framebox_F12 = SurroundingRectangle(F_2[3], buff = .1)
        framebox_F12.set_color(ORANGE)
        t_F12 = Tex("F_1^{(2)} (j\\omega)")
        t_F12.next_to(framebox_F12, DOWN, buff=0.1)
        t_F12.set_color(ORANGE)
        #----------------------------
        framebox_F13 = SurroundingRectangle(F_2[5], buff = .1)
        framebox_F13.set_color(GREEN)
        t_F13 = Tex("F_1^{(3)} (j\\omega)")
        t_F13.next_to(framebox_F13, DOWN, buff=0.1)
        t_F13.set_color(GREEN)
        #----------------------------
        framebox_F14 = SurroundingRectangle(F_2[7], buff = .1)
        framebox_F14.set_color(RED)
        t_F14 = Tex("F_1^{(4)} (j\\omega)")
        t_F14.next_to(framebox_F14, DOWN, buff=0.2)
        t_F14.set_color(RED)
        frameboxGROUP = VGroup(framebox_F11,framebox_F12,framebox_F13,framebox_F14)
        frametextGROUP = VGroup(t_F11,t_F12,t_F13,t_F14)
        #----------------------------


        #######################
        # TEXT - ANGABE BLABLA
        #######################

        text_ges = TexText("$\\rightarrow~~~$ graphische Darstellung:")
        text_ges.shift(LEFT*3+UP*1)

        text_amp = TexText("$\\bullet~~~$ \\textit{Amplitudengang}:",)
        tex_amp = Tex(
            "\\left.\\underline{F}_1(j\\omega)\\right|_{dB}",
            "= ",
            "\\left.\\underline{F}_1^{(1)}(j\\omega)\\right|_{dB}",
            "+ ",
            "\\left.\\underline{F}_2^{(2)}(j\\omega)\\right|_{dB}",
            "+ ",
            "\\left.\\underline{F}_2^{(3)}(j\\omega)\\right|_{dB}",
            "+ ",
            "\\left.\\underline{F}_2^{(4)}(j\\omega)\\right|_{dB}",)

        text_amp.next_to(text_ges[0].get_corner(LEFT), RIGHT)
        text_amp.shift(DOWN*1+LEFT*0.3)
        text_amp.scale(0.8)

        tex_amp.next_to(text_amp[0].get_corner(LEFT), RIGHT)
        tex_amp.shift(DOWN*0.8+LEFT*2)
        tex_amp.scale(0.8)

        tex_amp[2].set_color(YELLOW)
        tex_amp[4].set_color(ORANGE)
        tex_amp[6].set_color(GREEN)
        tex_amp[8].set_color(RED)

        text_phase = TexText("$\\bullet~~~$ \\textit{Phasengang}:",)
        tex_phase = Tex(
            "arg\\{\\underline{F}_1(j\\omega)\\}",
            "= ",
            "arg\\{\\underline{F}_1^{(1)}(j\\omega)\\}",
            "+",
            "arg\\{\\underline{F}_1^{(2)}(j\\omega)\\}",
            "+",
            "arg\\{\\underline{F}_1^{(3)}(j\\omega)\\}",
            "+",
            "arg\\{\\underline{F}_1^{(4)}(j\\omega)\\}",
            )


        text_phase.next_to(text_ges[0].get_corner(LEFT), RIGHT)
        text_phase.shift(DOWN*3+LEFT*0.3)
        text_phase.scale(0.8)

        tex_phase.next_to(text_phase[0].get_corner(LEFT), RIGHT)
        tex_phase.shift(DOWN*0.8+LEFT*2.3)
        tex_phase.scale(0.8)

        tex_phase[2].set_color(YELLOW)
        tex_phase[4].set_color(ORANGE)
        tex_phase[6].set_color(GREEN)
        tex_phase[8].set_color(RED)

        #################################################
        # ANIMATIONS
        #################################################
        self.add(F1[0])
        self.add(F1_1)
        self.wait()

        for i in range(8):
            self.play(Write(F_2[i]))
            self.wait()

        for i in range(4):
            self.play(
                ShowCreation(frameboxGROUP[i]),
                FadeIn(frametextGROUP[i]),
                )
            self.wait(.5)

        self.wait(3)

        ###################################################
        # Sachen löschen
        ###################################################

        self.play(
            FadeOut(F1_1),
            FadeOut(F_2[0:2]),
            FadeOut(F_2[3]),
            FadeOut(F_2[5]),
            FadeOut(F_2[7]),
            FadeOut(frameboxGROUP),
            run_time=1,
            )
        ###################################################
        # MOVE BITCH
        ###################################################
        self.play(
            t_F11.shift, UP*3.7+RIGHT*0.5,
            F_2[2].shift, UP*2.5+RIGHT*0.8,
            t_F12.shift, UP*3.7+RIGHT*0.4,
            F_2[4].shift, UP*2.5,
            t_F13.shift, UP*3.7+LEFT*0.2,
            F_2[6].shift, UP*2.5+LEFT*0.4,
            t_F14.shift, UP*3.7+RIGHT*0,
            run_time = 1
            )
        self.wait()

        ###################################################
        # Gesucht Text
        ###################################################
        self.play(Write(text_ges))
        self.wait()
        self.play(Write(text_amp))
        self.wait()
        self.play(Write(tex_amp))
        self.wait()
        self.play(Write(text_phase))
        self.wait()
        self.play(Write(tex_phase[0:6].copy()),)
        tex_phase[5:].shift(DOWN*0.7+LEFT*3)
        self.play(Write(tex_phase[5:]))
        self.wait(3)

class bsp1_rechnung3(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        #----------------------------
        # ue(t)
        #----------------------------

        u_e_t = Tex(
            "u_e(t)",
            "=",
            "\\sqrt{2}\\cdot",
            "4\\mathrm{V}",
            "\\cos ( 1\\mathrm{\\frac{1}{s}} t + 15 \\degree) "
            ).shift(UP*0.6)
        u_e_t[4][5:8].scale(0.8)

        framebox_w = SurroundingRectangle(u_e_t[4][4:8], buff = .1).set_color(PURPLE)
        tw = Tex("\\tilde{\\omega}")
        tw.next_to(framebox_w, UP, buff=0.3)
        tw.set_color(PURPLE)

        UE = Tex(
            "\\underline{U}_e",
            "=",
            "4\\mathrm{V}",
            "e^{",
            "j 15 \\degree }"
            ).shift(DOWN*0.6)

        ue_GROUP = VGroup(u_e_t,UE,framebox_w,tw)

        #----------------------------
        # F
        #----------------------------

        text_bode = TexText("$\\Rightarrow$\\textit{aus Bode-Diagramm ablesen:}").scale(0.8).set_color(TEAL_A)
        text_bode.shift(LEFT*3.5)

        F_abs = Tex(
            "|\\underline{F}_1(j\\tilde{\\omega})|",
            "= -80~\\mathrm{dB}",
            "= 10^{{-80\\mathrm{dB}} \\over {20}}",
            "= 10^{-4}"
            ).shift(DOWN)

        F_arg = Tex(
            "arg\\{ \\underline{F}_1(j\\tilde{\\omega})\\}",
            "=",
            "-11.421\\degree"
            ).shift(DOWN*2)


        UA = Tex(
            "\\underline{U}_a",
            "=",
            "\\underline{F}(j\\tilde{\\omega})",
            "\\underline{U}_e",
            "=",
            "|\\underline{F}(j\\tilde{\\omega})|",
            "4\\mathrm{V}",
            "e^{",
            "j \\left( arg\\{ \\underline{F}(j\\tilde{\\omega}) \\}+ 15\\degree \\right) }"
            ).shift(DOWN*3.5)

        UA_repl = Tex(
            "\\underline{U}_a",
            "=",
            "\\underline{F}(j\\tilde{\\omega})",
            "\\underline{U}_e",
            "=",
            "10^{-4}",
            "4\\mathrm{V}",
            "e^{",
            "j \\left( -11.421 \\degree + 15\\degree \\right) }"
            ).shift(DOWN*3.5)

        ua_t = Tex(
            "\\Rightarrow",
            "u_a(t)",
            "=",
            "\\sqrt{2} \\cdot ",
            "400\\mathrm{\\mu V}",
            "\\cos ( 1\\mathrm{\\frac{1}{s}} t + 3.579 \\degree) "
            ).shift(DOWN*2.5)

        framebox_ua = SurroundingRectangle(ua_t, buff = .3).set_color(GOLD)

        rest_GROUP = VGroup(text_bode,F_abs,F_arg,UA[0:5])


        #####################
        # PLAYPLAYPLAY
        #####################

        #----------------------------
        # ue(t)
        #----------------------------
        for i in range(len(u_e_t)):
            self.play(Write(u_e_t[i].set_color(TEAL_A)))
            self.wait(0.1)
            u_e_t[i].set_color(WHITE)
        self.play(ShowCreation(framebox_w),FadeIn(tw))


        self.wait()

        for i in range(len(UE)):
            self.play(Write(UE[i].set_color(TEAL_A)))
            self.wait(0.1)
            UE[i].set_color(WHITE)
        self.wait()

        self.play(ue_GROUP.shift,UP*2)

        #----------------------------
        # F
        #----------------------------
        self.play(Write(text_bode))
        self.wait()
        self.play(Write(F_abs))
        self.wait()
        self.play(Write(F_arg))

        self.wait()
        self.play(Write(UA))
        self.play(ReplacementTransform(UA[5:],UA_repl[5:]))
        # self.play(FadeOut(UA_repl))
        self.play(UA_repl[5:].shift,LEFT*0.6)

        self.wait(2)
        self.remove(UA[5:])
        self.play(FadeOut(ue_GROUP),)
        self.play(rest_GROUP.shift,UP*2.5,UA_repl[5:].shift,UP*2.5)

        self.wait()

        for i in range(len(ua_t)):
            self.play(Write(ua_t[i].set_color(GOLD_A)))
            self.wait(0.1)
        self.play(ShowCreation(framebox_ua))

        self.wait(3)





# class ConfigFormula1(CheckFormulaByTXT):


#     CONFIG={
#     "show_elements":[],
#     "remove": [], #2
#     #"text": Tex("=\\left. 10^{-3} \\frac{s+0.1}{s\\cdot (s + 10)}"),
#     # "text":Tex("=\\left. 10^{-3} \\frac{\\frac{0.1}{0.1}(s+0.1) }{\\frac{10}{10}s\\cdot (s + 10) }")

#     "text": Tex(" R_1 L_1 C_1\\cdot (s^2 + s \\frac{1}{R_1 C_1} + \\frac{1}{L_1 C_1} )}")
#     }


class bsp2_einleitung(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        ###########################################################
        ###########################################################
        # TEXT
        ###########################################################

        text_BSP2 = TexText("Beispiel 2")
        text_BSP2.scale(1.2)
        text_BSP2.set_color(MAROON_B)

        #---------------------------------------------------
        # Unterpunkt 1
        #---------------------------------------------------

        text_1 = TexText("1").scale(0.8)
        circle_1 = Circle(radius =0.35,color=WHITE).set_fill(MAROON_B,opacity=0.5)
        circle_1_GROUP = VGroup(circle_1,text_1)
        circle_1_GROUP.shift(6.5*LEFT+DOWN*0.5)

        text_ges_1 = TexText(
            r"\textit{ Ermittlung der {\"U}bertragungsfunktion der folgenden Schaltung}.",
            ).scale(0.7)

        text_ges_2 = TexText(
            "\\textit{Zeichnen des Bode-Diagramms (Amplituden- und Phasengang). }"
            ).scale(0.7)

        text_ges_1.next_to(circle_1_GROUP.get_corner(RIGHT),RIGHT*2)
        text_ges_1.shift(UP*0.3)
        text_ges_2.next_to(circle_1_GROUP.get_corner(RIGHT),RIGHT*2)
        text_ges_2.shift(DOWN*0.3)
        #---------------------------------------------------

        ##########################
        # PLAY
        #########################ä

        # überschrift
        self.play(Write(text_BSP2))
        self.play(text_BSP2.shift,UP*1.5+LEFT*4)
        self.wait()
        #-------
        # kreis1
        self.play(Write(circle_1_GROUP))
        # gesucht 1
        self.play(Write(text_ges_1),runtime=6)
        self.wait()
        self.play(Write(text_ges_2),runtime=6)
        self.wait(3)




class bsp2_circuit(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        factor_L1 = 0.4
        factor_R1 = 0.4

        klemme_l_o = Circle(radius = 0.1,color=WHITE)
        klemme_l_o.shift(LEFT*5+UP*2)

        line_klemme_l_o_L1 = Line(LEFT,RIGHT*(1-factor_L1))
        line_klemme_l_o_L1.next_to(klemme_l_o.get_corner(RIGHT), RIGHT,buff=0)

        L1 = Rectangle(height=0.5, width=1+2*factor_L1)
        L1.set_fill(WHITE,opacity=1)
        L1.next_to(line_klemme_l_o_L1.get_corner(RIGHT), RIGHT,buff=0)
        L1_text = TexText('$L_1$')
        L1_text.next_to(L1, UP)

        line_L1_short_R1 = Line(LEFT,RIGHT*(1-factor_L1))
        line_L1_short_R1.next_to(L1.get_corner(RIGHT), RIGHT,buff=0)

        line_L1_short_R1_dot = Dot(radius = 0.1)
        line_L1_short_R1_dot.next_to(line_L1_short_R1.get_corner(RIGHT), RIGHT,buff=0)

        line_short_to_R1 = Line(LEFT,LEFT+DOWN*(1.5-factor_R1))
        line_short_to_R1.next_to(line_L1_short_R1_dot, DOWN,buff=0)

        R1 = Rectangle(height=1+2*factor_R1, width=0.5)
        R1.next_to(line_short_to_R1.get_corner(DOWN), DOWN,buff=0)
        R1_text = TexText('$R_1$')
        R1_text.next_to(R1, LEFT)

        line_R1_to_short = Line(LEFT,LEFT+DOWN*(1.5-factor_R1))
        line_R1_to_short.next_to(R1.get_corner(DOWN), DOWN,buff=0)

        line_R1_to_short_dot = Dot(radius = 0.1)
        line_R1_to_short_dot.next_to(line_R1_to_short.get_corner(DOWN), DOWN,buff=0)

        line_klemme_lu_R1_short = Line(LEFT,RIGHT*4)
        line_klemme_lu_R1_short.next_to(line_R1_to_short_dot, LEFT,buff=0)

        klemme_l_u = Circle(radius = 0.1,color=WHITE)
        klemme_l_u.next_to(line_klemme_lu_R1_short.get_corner(LEFT), LEFT,buff=0)

        line_L1_to_klemme_r_o = Line(LEFT,RIGHT*3)
        line_L1_to_klemme_r_o.next_to(line_L1_short_R1_dot, RIGHT,buff=0)

        klemme_r_o = Circle(radius = 0.1,color=WHITE)
        klemme_r_o.next_to(line_L1_to_klemme_r_o.get_corner(RIGHT), RIGHT,buff=0)

        line_L1_to_klemme_r_o_dot = Dot(radius = 0.1)
        line_L1_to_klemme_r_o_dot.next_to(line_L1_to_klemme_r_o.get_center(), LEFT ,buff=0)


        line_R1_to_klemme_r_u = Line(LEFT,RIGHT*3)
        line_R1_to_klemme_r_u.next_to(line_R1_to_short_dot, RIGHT,buff=0)

        klemme_r_u = Circle(radius = 0.1,color=WHITE)
        klemme_r_u.next_to(line_R1_to_klemme_r_u.get_corner(RIGHT), RIGHT,buff=0)

        line_R1_to_klemme_r_u_dot = Dot(radius = 0.1)
        line_R1_to_klemme_r_u_dot.next_to(line_R1_to_klemme_r_u.get_center(), LEFT ,buff=0)

        line_short_to_C1 = Line(LEFT,LEFT+DOWN*(4/2-0.25))
        line_short_to_C1.next_to(line_L1_to_klemme_r_o_dot,DOWN,buff=0)

        line_short_to_C1_up = Line(LEFT,LEFT+UP*(4/2-0.25))
        line_short_to_C1_up.next_to(line_R1_to_klemme_r_u_dot,UP,buff=0)

        line_C1_plus = Line(LEFT,RIGHT)
        line_C1_plus.next_to(line_short_to_C1.get_corner(DOWN),DOWN,buff=0)

        line_C1_minus = Line(LEFT,RIGHT)
        line_C1_minus.next_to(line_short_to_C1_up.get_corner(UP),UP,buff=0)

        C1_text = TexText('$C_1$')
        C1_text.next_to(line_C1_plus.get_corner(RIGHT)+DOWN*0.25, RIGHT)

        U_e = CurvedArrow(2*DOWN, 2*UP, angle=-TAU/4, color=BLUE)
        U_e.next_to(klemme_l_o.get_corner(LEFT),DOWN+LEFT,buff=0.1)

        UE_text = TexText('$\\underline{U}_e$',color=BLUE)
        UE_text.next_to(U_e.get_center(), RIGHT*0.5)

        U_a = CurvedArrow(2*DOWN, 2*UP, angle=-TAU/4, color=BLUE)
        U_a.flip(UP)
        U_a.next_to(klemme_r_o.get_corner(RIGHT),DOWN+RIGHT,buff=0.1)

        UA_text = TexText('$\\underline{U}_a$',color=BLUE)
        UA_text.next_to(U_a.get_center(), RIGHT*3)


        self.play(Write(klemme_l_o))
        self.play(Write(line_klemme_l_o_L1))
        self.play(Write(L1))
        self.play(Write(L1_text))
        self.play(Write(line_L1_short_R1))
        self.play(Write(line_L1_short_R1_dot))
        self.play(Write(line_short_to_R1))
        self.play(Write(R1))
        self.play(Write(R1_text))
        self.play(Write(line_R1_to_short))
        self.play(Write(line_R1_to_short_dot))
        self.play(Write(line_klemme_lu_R1_short))
        self.play(Write(klemme_l_u))

        self.play(Write(line_L1_to_klemme_r_o),Write(line_R1_to_klemme_r_u))
        self.play(Write(klemme_r_o),Write(klemme_r_u))
        self.play(Write(line_L1_to_klemme_r_o_dot),Write(line_R1_to_klemme_r_u_dot))

        self.play(Write(line_short_to_C1),Write(line_short_to_C1_up))

        self.play(Write(line_C1_plus),Write(line_C1_minus))
        self.play(Write(C1_text))

        self.play(Write(U_e))
        self.play(Write(UE_text))
        self.play(Write(U_a))
        self.play(Write(UA_text))

        self.wait()


class bsp2_circuit2(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        #############################################################
        #############################################################
        # ALL OBJECTS FOR THE PLOT
        #############################################################
        #############################################################

        factor_L1 = 0.4
        factor_R1 = 0.4

        klemme_l_o = Circle(radius = 0.1,color=WHITE)
        klemme_l_o.shift(LEFT*5+UP*2)

        line_klemme_l_o_L1 = Line(LEFT,RIGHT*(1-factor_L1))
        line_klemme_l_o_L1.next_to(klemme_l_o.get_corner(RIGHT), RIGHT,buff=0)

        L1 = Rectangle(height=0.5, width=1+2*factor_L1)
        L1.set_fill(WHITE,opacity=1)
        L1.next_to(line_klemme_l_o_L1.get_corner(RIGHT), RIGHT,buff=0)
        L1_text = TexText('$L_1$')
        L1_text.next_to(L1, UP)

        line_L1_short_R1 = Line(LEFT,RIGHT*(1-factor_L1))
        line_L1_short_R1.next_to(L1.get_corner(RIGHT), RIGHT,buff=0)

        line_L1_short_R1_dot = Dot(radius = 0.1)
        line_L1_short_R1_dot.next_to(line_L1_short_R1.get_corner(RIGHT), RIGHT,buff=0)

        line_short_to_R1 = Line(LEFT,LEFT+DOWN*(1.5-factor_R1))
        line_short_to_R1.next_to(line_L1_short_R1_dot, DOWN,buff=0)

        R1 = Rectangle(height=1+2*factor_R1, width=0.5)
        R1.next_to(line_short_to_R1.get_corner(DOWN), DOWN,buff=0)
        R1_text = TexText('$R_1$')
        R1_text.next_to(R1, LEFT)

        line_R1_to_short = Line(LEFT,LEFT+DOWN*(1.5-factor_R1))
        line_R1_to_short.next_to(R1.get_corner(DOWN), DOWN,buff=0)

        line_R1_to_short_dot = Dot(radius = 0.1)
        line_R1_to_short_dot.next_to(line_R1_to_short.get_corner(DOWN), DOWN,buff=0)

        line_klemme_lu_R1_short = Line(LEFT,RIGHT*4)
        line_klemme_lu_R1_short.next_to(line_R1_to_short_dot, LEFT,buff=0)

        klemme_l_u = Circle(radius = 0.1,color=WHITE)
        klemme_l_u.next_to(line_klemme_lu_R1_short.get_corner(LEFT), LEFT,buff=0)

        line_L1_to_klemme_r_o = Line(LEFT,RIGHT*3)
        line_L1_to_klemme_r_o.next_to(line_L1_short_R1_dot, RIGHT,buff=0)

        klemme_r_o = Circle(radius = 0.1,color=WHITE)
        klemme_r_o.next_to(line_L1_to_klemme_r_o.get_corner(RIGHT), RIGHT,buff=0)

        line_L1_to_klemme_r_o_dot = Dot(radius = 0.1)
        line_L1_to_klemme_r_o_dot.next_to(line_L1_to_klemme_r_o.get_center(), LEFT ,buff=0)


        line_R1_to_klemme_r_u = Line(LEFT,RIGHT*3)
        line_R1_to_klemme_r_u.next_to(line_R1_to_short_dot, RIGHT,buff=0)

        klemme_r_u = Circle(radius = 0.1,color=WHITE)
        klemme_r_u.next_to(line_R1_to_klemme_r_u.get_corner(RIGHT), RIGHT,buff=0)

        line_R1_to_klemme_r_u_dot = Dot(radius = 0.1)
        line_R1_to_klemme_r_u_dot.next_to(line_R1_to_klemme_r_u.get_center(), LEFT ,buff=0)

        line_short_to_C1 = Line(LEFT,LEFT+DOWN*(4/2-0.25))
        line_short_to_C1.next_to(line_L1_to_klemme_r_o_dot,DOWN,buff=0)

        line_short_to_C1_up = Line(LEFT,LEFT+UP*(4/2-0.25))
        line_short_to_C1_up.next_to(line_R1_to_klemme_r_u_dot,UP,buff=0)

        line_C1_plus = Line(LEFT,RIGHT)
        line_C1_plus.next_to(line_short_to_C1.get_corner(DOWN),DOWN,buff=0)

        line_C1_minus = Line(LEFT,RIGHT)
        line_C1_minus.next_to(line_short_to_C1_up.get_corner(UP),UP,buff=0)

        C1_text = TexText('$C_1$')
        C1_text.next_to(line_C1_plus.get_corner(RIGHT)+DOWN*0.25, RIGHT)

        U_e = CurvedArrow(2*DOWN, 2*UP, angle=-TAU/4, color=BLUE)
        U_e.next_to(klemme_l_o.get_corner(LEFT),DOWN+LEFT,buff=0.1)

        UE_text = TexText('$\\underline{U}_e$',color=BLUE)
        UE_text.next_to(U_e.get_center(), RIGHT*0.5)

        U_a = CurvedArrow(2*DOWN, 2*UP, angle=-TAU/4, color=BLUE)
        U_a.flip(UP)
        U_a.next_to(klemme_r_o.get_corner(RIGHT),DOWN+RIGHT,buff=0.1)

        UA_text = TexText('$\\underline{U}_a$',color=BLUE)
        UA_text.next_to(U_a.get_center(), RIGHT*3)

        #############################################################

        GROUP = VGroup(klemme_l_o, line_klemme_l_o_L1, L1, L1_text,line_L1_short_R1,line_L1_short_R1_dot,
            line_short_to_R1,R1,R1_text,line_R1_to_short,line_R1_to_short_dot,line_klemme_lu_R1_short,
            klemme_l_u,line_L1_to_klemme_r_o,line_R1_to_klemme_r_u,klemme_r_o,klemme_r_u,
            line_L1_to_klemme_r_o_dot,line_R1_to_klemme_r_u_dot,line_short_to_C1,line_short_to_C1_up,
            line_C1_plus,line_C1_minus,C1_text,U_e,UE_text,U_a,UA_text)

        self.add(GROUP)

        self.play(
            GROUP.shift, UP*2+LEFT*3.5,
            GROUP.scale, 0.5,
            run_time=3,
            )

        #############################################################
        #############################################################
        #############################################################
        # EQUATIONS
        #############################################################
        #############################################################

        #############################################################
        # Angabe und gesucht
        #############################################################

        angabe_text = TexText('Gegeben:',color=ORANGE)
        angabe_text.shift(3*LEFT)
        gesucht_text = TexText('Gesucht:',color=ORANGE)
        gesucht_text.shift(3*LEFT)

        gesucht = Tex("\\underline{H}(j\\omega) = \\frac{\\underline{U}_a}{\\underline{U}_e}")
        gesucht.scale(0.8)
        angabe = Tex("C_1 = 100~\\mathrm{nF} "," L_1 = 100~\\mathrm{mH} "," R_1 = 500~\\Omega")
        angabe.scale(0.8)

        gesucht.shift(DOWN)
        gesucht.align_to(gesucht_text.get_corner(LEFT), LEFT)
        angabe.shift(DOWN)
        angabe[0].align_to(angabe_text.get_corner(LEFT), LEFT)

        for i in range(1,3):
            angabe[i:].shift(DOWN)
            angabe[i].align_to(angabe[i-1].get_corner(LEFT), LEFT)

        #############################################################
        # Rechnung
        #############################################################

        H_jw = Tex("\\left.\\underline{H}(j\\omega)\\right|_{j\\omega = s} = \\frac{\\underline{U}_a}{\\underline{U}_e} = ",
            "{\\frac{ \\frac{ 1 }{ sC_1 } \\cdot R_1 }{ \\frac{ 1 }{ sC_1 } + R_1 } ",
            "\\over",
            "\\frac{ \\frac{ 1 }{ sC_1 } \\cdot R_1 }{ \\frac{ 1 }{ sC_1 } + R_1 }  + sL_1}")
        H_jw.shift(DOWN+LEFT*2)


        ################################################################
        ################################################################
        ################################################################
        # PLOT ANIMATIONS
        ################################################################
        ################################################################
        ################################################################

        ################################
        # ANGABE
        ################################

        angabe_group = VGroup(angabe_text,angabe)

        self.play(Write(angabe_text),run_time=0.7)
        self.play(Write(angabe),run_time=0.7)

        self.play(
                    angabe_text.shift, UP*(3)+RIGHT*(4),
                    angabe_text.scale, 0.8,
                    run_time=1,
                )
        for i in range(0,3):
            self.play(
                    angabe[i].shift, UP*(i+3.5)+RIGHT*(i*2.3+4),
                    angabe[i].scale, 0.8,
                    run_time=1,
                )

        ################################
        # GESUCHT
        ################################

        self.play(Write(gesucht_text),run_time=0.7)
        self.play(Write(gesucht),run_time=0.7)

        self.play(
                    gesucht_text.shift, UP*(2)+RIGHT*(4),
                    gesucht_text.scale, 0.8,
                    run_time=1,
                )
        self.play(
                    gesucht.shift, UP*(2.4)+RIGHT*(4),
                    gesucht.scale, 0.8,
                    run_time=1,
                )

        self.wait(2)

        self.play(Write(H_jw[0]))
        self.wait()
        self.play(Write(H_jw[2]))
        self.wait()

        R1.set_color(GREEN)
        R1_text.set_color(GREEN)
        line_C1_plus.set_color(GREEN)
        line_C1_minus.set_color(GREEN)
        C1_text.set_color(GREEN)
        H_jw[1].set_color(GREEN)
        H_jw[3][0:17].set_color(GREEN)


        H_jw[3][18:21].set_color(PURPLE)

        self.play(Write(H_jw[1]))
        self.wait()
        self.play(Write(H_jw[3][0:17]))
        self.wait()
        self.play(Write(H_jw[3][17]))
        self.wait()
        L1.set_color(PURPLE)
        L1_text.set_color(PURPLE)
        self.play(Write(H_jw[3][18:21]))
        self.wait(3)

        self.play(
            FadeOut(GROUP),
            FadeOut(angabe),
            FadeOut(angabe_text),
            FadeOut(gesucht),
            FadeOut(gesucht_text),
            H_jw.shift, UP*3.5+LEFT*0,
                    run_time=1,
            )

        self.wait()



class bsp2_rechnung2(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        #################################
        # RECHNUNGEN
        #################################

        H_jw = Tex(
            "\\left.\\underline{H}(j\\omega)\\right|_{j\\omega = s} = \\frac{\\underline{U}_a}{\\underline{U}_e} = ",
            "{\\frac{ \\frac{ 1 }{ sC_1 } \\cdot R_1 }{ \\frac{ 1 }{ sC_1 } + R_1 } ",
            "\\over",
            "\\frac{ \\frac{ 1 }{ sC_1 } \\cdot R_1 }{ \\frac{ 1 }{ sC_1 } + R_1 }  + sL_1}",
            "=",
            "{  { \\frac{R_1}{sC_1} ",
            " \\over ",
            " {1+sR_1 C_1 ",
            "\\over" ,
            "s C_1} } ",
            "\\over",
            " \\frac{ \\frac{R_1}{s C_1} }{ \\frac{1+sR_1 C_1}{s C_1}  } ",
            "+sL_1")

        H_jw.shift(UP*2.5)
        H_jw[1].set_color(GREEN)
        H_jw[3][0:17].set_color(GREEN)
        H_jw[3][18:21].set_color(PURPLE)


        self.add(H_jw[0:4])
        self.wait()

        # = & großer Bruch
        self.play( Write(H_jw[4]) )
        self.play( Write(H_jw[10]) )
        self.wait()

        # oben Bruch
        self.play( Write(H_jw[6]) )
        self.wait()
        # Werte oben Bruch
        self.play( Write(H_jw[5]) )
        self.wait()

        # unten Bruch
        self.play( Write(H_jw[8]) )
        self.wait()
        # Werte unten Bruch
        self.play( Write(H_jw[9]) )
        self.wait()
        self.play( Write(H_jw[7]) )
        self.wait()

        # Werte unter großem Bruch
        self.play( Write(H_jw[11]) )
        self.wait()
        self.play( Write(H_jw[12]) )
        self.wait()

        ###################################################
        # Zweite Zeile
        ###################################################

        H_jw2 = Tex(
            "=",
            "{{ R_1 ",
            " \\over ",
            " 1+sR_1 C_1 }",
            "\\over",
            "{ \\frac{ R_1 }{ 1+sR_1 C_1 } ",
            "+sL_1 }}",
            "=",
            "{{ R_1 ",
            " \\over ",
            " 1+sR_1 C_1 }",
            "\\over",
            "{ R_1+sL_1+s^2 R_1 L_1 C_1 ",
            "\\over",
            " 1+sR_1 C_1}}")

        H_jw2.shift(UP*0)
        H_jw2.align_to(H_jw[0][11].get_corner(LEFT), LEFT)

        # = & großer Bruch
        self.play(Write(H_jw2[0]))
        self.play(Write(H_jw2[4]))
        self.wait()
        # oberer Bruch
        self.play(Write(H_jw2[2]))
        self.wait()
        # Werte oberer Bruch
        self.play(Write(H_jw2[1]))
        self.wait()
        self.play(Write(H_jw2[3]))
        self.wait()
        # unten
        self.play(Write(H_jw2[5]))
        self.wait()
        self.play(Write(H_jw2[6]))
        self.wait()

        ###################################################
        # = & Bruch
        self.play(Write(H_jw2[7]))
        self.play(Write(H_jw2[11]))
        self.wait()
        # oberer Bruch
        self.play(Write(H_jw2[8:11]))
        self.wait()
        # unterer Bruch
        self.play(Write(H_jw2[13]))
        self.wait()
        # Werte unten
        self.play(Write(H_jw2[14]))
        self.wait()
        # Werte oben
        self.play(Write(H_jw2[12][0:3]))
        self.wait()
        self.play(Write(H_jw2[12][3:7]))
        self.wait()
        self.play(Write(H_jw2[12][7:9]))
        self.wait()
        self.play(Write(H_jw2[12][9:]))
        self.wait()


        ###################################################
        # Dritte Zeile
        ###################################################

        H_jw3 = Tex(
            "=",
            "{ R_1",
            "\\over",
            " s^2 R_1 L_1 C_1 + s L_1 + R_1 }"
            )

        H_jw3.shift(DOWN*1.5)
        H_jw3.align_to(H_jw2[0][0].get_corner(LEFT), LEFT)

        # = & großer Bruch
        self.play(Write(H_jw3[0]))
        self.play(Write(H_jw3[2]))
        self.wait()
        # oben
        self.play(Write(H_jw3[1]))
        self.wait()
        # unten
        self.play(Write(H_jw3[3]))
        self.wait()


        ###################################################
        # Vierte Zeile
        ###################################################

        H_jw4 = Tex(
            "=",
            "{ R_1 ",
            "\\over",
            " R_1 L_1 C_1\\cdot (s^2 + s \\frac{1}{R_1 C_1} + \\frac{1}{L_1 C_1} )}"
            )

        H_jw5 = Tex(
            "=",
            "{ R_1 ",
            "\\over",
            " R_1 L_1 C_1\\cdot (s^2 + s \\frac{1}{R_1 C_1} + \\frac{1}{L_1 C_1} )}"
            )


        H_jw4.align_to(H_jw3[0][0].get_corner(LEFT), LEFT)
        H_jw4.shift(DOWN*3)

        H_jw3[3][2:8].set_color(GREEN)
        H_jw4[3][0:6].set_color(GREEN)

        self.wait()
        # = & großer Bruch
        self.play(Write(H_jw4[0]))
        self.play(Write(H_jw4[2]))
        self.wait()
        # oben
        self.play(Write(H_jw4[1]))
        self.wait()
        # unten
        self.play(Write(H_jw4[3][0:7]))
        self.wait()
        # Klammern
        self.play(Write(H_jw4[3][7]),Write(H_jw4[3][25]))
        self.wait()
        # Inhalt
        self.play(Write(H_jw4[3][8:11]))
        self.wait()
        self.play(Write(H_jw4[3][11]))
        self.wait()
        self.play(Write(H_jw4[3][12:19]))
        self.wait()
        self.play(Write(H_jw4[3][19:25]))
        self.wait()


        ###################################################
        # Sachen löschen
        ###################################################


        self.play(
            FadeOut(H_jw[1:]),
            FadeOut(H_jw[0][11:]),
            FadeOut(H_jw2),
            FadeOut(H_jw3),
            H_jw[0][0:11].shift,RIGHT,
            H_jw4.shift, UP*5.5+RIGHT,
            run_time=1,
            )

        self.wait()

class bsp2_rechnung3(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        #################################
        # RECHNUNGEN
        #################################

        #################################
        # ERSTE ZEILE
        #################################

        H_jw = Tex(
            "\\left.\\underline{H}(j\\omega)\\right|_{j\\omega = s} = { R_1 \\over ",
            "R_1 L_1 C_1\\cdot (s^2 + s \\frac{1}{R_1 C_1} + \\frac{1}{L_1 C_1} )}"
            )

        H_jw1 = Tex(
            "\\left.\\underline{H}(j\\omega)\\right|_{j\\omega = s} = { 1 \\over ",
            "~~~~~L_1 C_1\\cdot (s^2 + s \\frac{1}{R_1 C_1} + \\frac{1}{L_1 C_1} )}"
            )

        H_jw.shift(UP*2.5)
        H_jw[1][0:7].set_color(GREEN)

        H_jw1.shift(UP*2.5)
        H_jw1.align_to(H_jw[0][0].get_corner(LEFT), LEFT)
        H_jw1[1][0:5].set_color(GREEN)

        brace1 = Brace(H_jw1[1][5:], DOWN, buff = SMALL_BUFF,color = YELLOW_B)
        t1 = brace1.get_text("$= \\mu(s) $")
        t1.set_color(YELLOW_B)

        self.add(H_jw)
        self.wait()

        self.play(
            ReplacementTransform(H_jw[0][12:14],H_jw1[0][12]),
            ReplacementTransform(H_jw[1][0:7],H_jw1[1][0:5]),
            )

        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()


        #################################
        # ERSTE ZEILE
        #################################

        H_jw2 = Tex(
            "\\mu(s) \\overset{!}{=} 0",
            "\\hspace{0.3cm}\\Rightarrow s_{0,1} = - {1 \\over {2 R_1 C_1}} ",
            "\\pm ",
            " \\sqrt{  \\left({1 \\over {2 R_1 C_1}} \\right)^2 - {1 \\over {L_1 C_1}}}",
            "= -10^4 \\mathrm{s}^{-1} \\pm 0"
            )

        H_jw3 = Tex(
            "\\left.\\underline{H}(j\\omega)\\right|_{j\\omega = s} = ",
            "{1 \\over L_1 C_1 (s+\\Omega_1)^2}",
            "= {1 \\over L_1 C_1 \\Omega_1^2 ({s \\over \\Omega_1}+1)^2}"
            )

        H_jw4 = Tex(
            "{1 \\over \\left({s \\over \\Omega_1}+1\\right)^2}"
            )


        H_jw2.scale(0.8)
        H_jw2.align_to(H_jw[0][0].get_corner(LEFT), LEFT)
        H_jw2.shift(DOWN*0.25+LEFT*1.5)
        H_jw2[0].set_color(YELLOW_B)

        H_jw3.shift(DOWN*2)
        H_jw3.align_to(H_jw[0][0].get_corner(LEFT), LEFT)


        H_jw4.align_to(H_jw[0][11].get_corner(RIGHT), LEFT)
        H_jw4.shift(UP*2.3+RIGHT*0.3)

        framebox_mu = SurroundingRectangle(H_jw2[0], buff = .1)
        framebox_mu.set_color(YELLOW_B)


        framebox_SEK = SurroundingRectangle(H_jw2[4][5:8], buff = .1)
        framebox_SEK.set_color(RED)
        t_SEK = TexText("\\textbf{Achtung:}\\ $s^{-1}$ hier \\text{1/Sekunde}")
        t_SEK.scale(0.8)
        t_SEK.next_to(framebox_SEK, DOWN+LEFT, buff=0.4)
        t_SEK.set_color(RED).shift(RIGHT*2)


        framebox_Omega_0 = SurroundingRectangle(H_jw2[4][2:10], buff = .1)
        framebox_Omega_0.set_color(PURPLE)
        t3 = Tex("\\Omega_1")
        t3.next_to(framebox_Omega_0, DOWN, buff=0.1)
        t3.set_color(PURPLE)

        #########################################################
        # PLOTS
        #########################################################
        # mu = 0
        self.play(Write(H_jw2[0]))
        self.play(ShowCreation(framebox_mu))
        self.wait()

        # Quadratische Gleichung
        self.play(Write(H_jw2[1][0:6]))
        self.wait()
        self.play(Write(H_jw2[1][6:]))
        self.wait()
        self.play(Write(H_jw2[2]))
        self.wait()
        self.play(Write(H_jw2[3][0:2]))
        self.wait()
        self.play(Write(H_jw2[3][2:]))
        self.wait()
        # Lösung Zahlenwerte
        self.play(Write(H_jw2[4]))
        self.wait()

        self.play(ShowCreation(framebox_SEK),
            FadeIn(t_SEK),)
        self.wait(3)
        self.play(FadeOut(framebox_SEK),
            FadeOut(t_SEK),)

        self.play(ShowCreation(framebox_Omega_0),
            FadeIn(t3),)

        self.wait(3)

        # H_jw kopieren und umschreiben
        self.play(
            ReplacementTransform(H_jw.copy(),H_jw3[0:2])
            )
        self.wait()

        # H_jw nach links verschieben und umschreiben
        self.play(
            H_jw3[0:2].shift,LEFT,
            )

        H_jw3[2:].shift(LEFT)
        self.play( Write(
            H_jw3[2])
            )
        self.wait()

        # LC Omega löschen
        self.play(
            FadeOut(H_jw3[2][3:10]),
            )

        self.wait(0.2)
        # Rest nach links verschieben
        self.play(
            H_jw3[2][10:].shift,LEFT
            )

        self.wait(3)


        ###################################################
        # Sachen löschen
        ###################################################


        self.play(
            FadeOut(H_jw[0][12:]),
            # ReplacementTransform(H_jw[0][12:14],H_jw1[0][12]),
            # ReplacementTransform(H_jw[1][0:7],H_jw1[1][0:5]),
            FadeOut(H_jw[1]),
            FadeOut(H_jw1[0][12]),
            FadeOut(H_jw1[1][0:5]),
            FadeOut(H_jw2),
            FadeOut(H_jw3[0:2]),
            FadeOut(H_jw3[2][0:3]),
            FadeOut(H_jw3[2][10:]),
            FadeOut(brace1),
            FadeOut(framebox_Omega_0),
            FadeOut(framebox_mu),
            FadeOut(t1),
            FadeOut(t3),
            # H_jw[0][0:12].shift,LEFT,
            run_time=1,
            )
        # H_jw4.shift(LEFT)
        self.play(Write(H_jw4),)

        self.wait()

class bsp2_rechnung4(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        #################################
        # RECHNUNGEN
        #################################

        # H(jw) anfang
        H_jw = Tex(
            "\\left.\\underline{H}(j\\omega)\\right|_{j\\omega = s} =",
            " { R_1 \\over  R_1 L_1 C_1\\cdot (s^2 + s \\frac{1}{R_1 C_1} + \\frac{1}{L_1 C_1} )}",
            )

        # normierte Form
        H_jw1 = Tex(
            "{1 \\over \\left({s \\over \\Omega_1}+1\\right)^2}",
            " = ",
            "{{1 \\over \\left({s \\over \\Omega_1}+1\\right)} ",
            "\\cdot ",
            " {1 \\over \\left({s \\over \\Omega_1}+1\\right)}}"
            )

        # Text erste Zeile verschieben
        H_jw.shift(UP*2.5)
        H_jw1.align_to(H_jw[0][11].get_corner(RIGHT), LEFT)
        H_jw1.shift(UP*2.3+RIGHT*0.3)

        # Boxen
        framebox_H1 = SurroundingRectangle(H_jw1[2], buff = .1)
        framebox_H1.shift(LEFT)
        framebox_H1.set_color(PURPLE)
        t1 = Tex("H^{(1)} (j\\omega)")
        t1.next_to(framebox_H1, DOWN, buff=0.1)
        t1.set_color(PURPLE)

        framebox_H2 = SurroundingRectangle(H_jw1[4], buff = .1)
        framebox_H2.shift(LEFT)
        framebox_H2.set_color(GREEN)
        t2 = Tex("H^{(2)} (j\\omega)")
        t2.next_to(framebox_H2, DOWN, buff=0.1)
        t2.set_color(GREEN)

        #######################
        # TEXT
        #######################

        text_ges = TexText("$\\rightarrow~~~$ graphische Darstellung:")
        text_ges.shift(LEFT*3+DOWN*0.5)

        text_amp = TexText("$\\bullet~~~$ \\textit{Amplitudengang}:",
            " $\\left.\\underline{H}(j\\omega)\\right|_{dB}$",
            "$= $ ",
            "$\\left.\\underline{H}^{(1)}(j\\omega)\\right|_{dB}$",
            "$+$ ",
            "$\\left.\\underline{H}^{(2)}(j\\omega)\\right|_{dB}$")

        text_amp.align_to(text_ges[0].get_corner(RIGHT), UP)
        text_amp.shift(DOWN*0.5)
        text_amp.scale(0.8)
        text_amp[3].set_color(PURPLE)
        text_amp[5].set_color(GREEN)

        text_phase = TexText("$\\bullet~~~$ \\textit{Phasengang}:",
            "$arg\\{\\underline{H}(j\\omega)\\}$",
            "$= $ ",
            "$arg\\{\\underline{H}^{(1)}(j\\omega)\\}$",
            "$+$ ",
            "$arg\\{\\underline{H}^{(2)}(j\\omega)\\}$")

        text_phase.align_to(text_amp[0].get_corner(LEFT), UP)
        text_phase.shift(DOWN*0.5+RIGHT*0.25)
        text_phase.scale(0.8)
        text_phase[3].set_color(PURPLE)
        text_phase[5].set_color(GREEN)

        #################################################
        # ANIMTATIONEN
        #################################################

        # Text von vorheriger Szene
        self.add(H_jw[0],H_jw1[0])

        # Nach links verschieben für mehr Platz
        self.wait()
        self.play(H_jw[0].shift,LEFT,
                 H_jw1[0].shift,LEFT)

        # ^2 -> ().()
        H_jw1[1:].shift(LEFT)
        self.play(Write(H_jw1[1]))
        self.play(Write(H_jw1[2:]))
        self.wait()

        # Boxen
        self.play(ShowCreation(framebox_H1),
            FadeIn(t1),)
        self.wait()
        self.play(ShowCreation(framebox_H2),
            FadeIn(t2),)
        self.wait()

        # Gesucht Text
        self.play(Write(text_ges))
        self.wait()
        self.play(Write(text_amp))
        self.wait(2)
        self.play(Write(text_phase))



        self.wait(3)


class bsp1_image(Scene):

    CONFIG={
        "camera_config":{"background_color":"#102331"}
    }

    def construct(self):

        bode= ImageMobject(r"C:\Manim\manim_3_feb\media\designs\raster_images\BSP1.png")
        bode.scale(3.5)
        self.add(bode)

        circle_abs = Circle(radius = 0.1,color=BLUE_D).shift(RIGHT*0.25+UP*0.58)
        t_abs = Tex("-80 \\mathrm{dB}").scale(0.6)
        t_abs.next_to(circle_abs, UP, buff=0.1)
        t_abs.set_color(BLUE_C)

        circle_arg = Circle(radius = 0.1,color=BLUE_D).shift(RIGHT*0.25+DOWN*1.9)
        t_arg = Tex("-11.421\\degree").scale(0.6)
        t_arg.next_to(circle_arg, UP, buff=0.2)
        t_arg.set_color(BLUE_C)

        self.play(ShowCreation(circle_abs))
        self.play(Write(t_abs))

        self.wait(1)

        self.play(ShowCreation(circle_arg))
        self.play(Write(t_arg))


        self.wait(3)
