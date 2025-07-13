from manim import *
from manim_slides import Slide
import math
import cmath
import re

class MySlide4(Slide, ThreeDScene):
    def NextSection(self):
        if self.SectionNum >= len(self.section_items):
            return

        # 前回の強調を戻す（左端を基準に縮小）
        if self.SectionNum !=0 :
            self.play(
                self.last_highlighted.animate.scale(1 / 1.2, about_edge=LEFT)
            )

        # 今回の対象（左端を基準に拡大）
        current = self.section_items[self.SectionNum]

        self.play(current.animate.scale(1.2, about_edge=LEFT))
        self.play(Circumscribe(current, color=YELLOW))

    def construct(self):

        self.next_slide()
        self.clear()
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.SectionNum = 3 # 0~4
        self.section_items = []

        colors = [RED_E, GOLD_E, GREEN_E, BLUE_E, PURPLE_E]
        contents = [
            "複素数・複素関数とは何か",
            "一つの軸を犠牲にした可視化",
            "色を用いた可視化",
            "ベクトルを用いた可視化",
            "線形補完を用いた可視化"
        ]

        rows = VGroup()

        for i in range(5):
            number = Integer(i + 1, color=WHITE)
            circle = Circle()
            circle.set_fill(colors[i], opacity=1.0)
            circle.set_stroke(WHITE, width=3)
            circle.scale(0.3)
            number.move_to(circle.get_center())
            number_group = VGroup(circle, number)

            text = Text(contents[i]).scale(0.8)

            row = VGroup(number_group, text)
            row.arrange(RIGHT, buff=0.5)

            rows.add(row)
            self.section_items.append(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.7).to_edge(LEFT)

        self.last_highlighted = self.section_items[self.SectionNum-1]

        if self.SectionNum != 0:
            self.section_items[self.SectionNum-1].scale(1.2, about_edge=LEFT)
        
        self.add(rows)
        self.wait()

        self.NextSection()
        self.wait(0.5)
        self.next_slide()

        self.clear()

        starttext = Text("Vector Field").to_edge(UP*2)
        func = MathTex("w = f(z)", color = YELLOW)

        self.play(
            Write(starttext)
        )
        self.wait()
        self.next_slide()

        self.play(
            Write(func)
        )

        stress_arrow1 = Vector(UP * 0.5).next_to(func.get_part_by_tex("z"), DOWN + RIGHT * 1.5, buff=SMALL_BUFF).rotate(PI / 6)
        stress_arrow2 = Vector(UP * 0.5).next_to(func.get_part_by_tex("w"), DOWN + LEFT * 1.5, buff=SMALL_BUFF).rotate(-PI / 6)

        stress_text1 = Text("入力").scale(0.5).next_to(stress_arrow1, DOWN)
        stress_text2 = Text("出力").scale(0.5).next_to(stress_arrow2, DOWN)
        
        self.play(
            AnimationGroup(
                FadeIn(stress_arrow1, stress_text1),
                FadeIn(stress_arrow2, stress_text2),
                lag_ratio = 1.0
            )
        )
        self.wait()
        self.next_slide()

        func.generate_target()
        func.target.shift(RIGHT*3 + UP*3).scale(1.2)
        plane = ComplexPlane(
            x_range = [-4, 5],
            y_range = [-3, 4],
        ).add_coordinates()

        self.play(
            AnimationGroup(
                FadeOut(starttext, stress_arrow1, stress_arrow2, stress_text1, stress_text2),
                MoveToTarget(func),
                Write(plane)
            )
        )
        self.wait()
        self.next_slide()

        z1 = -1 + 2j
        z2 = 2 - 1j

        dot1 = Dot(plane.n2p(z1), color = YELLOW)
        dot2 = Dot(plane.n2p(z2), color = BLUE)

        complex_value1 = plane.p2n(dot1.get_center())
        complex_value2 = plane.p2n(dot2.get_center())

        real1 = complex_value1.real
        imag1 = complex_value1.imag
        real2 = complex_value2.real
        imag2 = complex_value2.imag

        label_text1 = f"{real1:.0f} {'+' if imag1 >= 0 else '-'} {abs(imag1):.0f}i"
        label1 = MathTex(label_text1).next_to(dot1, UP, buff=0.1)
        label_text2 = f"{real2:.0f} {'+' if imag2 >= 0 else '-'} i"
        label2 = MathTex(label_text2).next_to(dot2, DOWN, buff=0.1)

        self.play(LaggedStart(
            FadeIn(dot1, label1),
            FadeIn(dot2, label2),
            lag_ratio = 1.5
            )
        )
        self.wait()
        self.next_slide()

        def written_arrows(startpoint, endpoint):
            return Arrow(startpoint, endpoint, buff = 0, color = YELLOW)
        
        vector1 = written_arrows(dot1, dot2)

        self.play(GrowArrow(vector1), run_time = 1.5)
        self.wait()
        self.next_slide()
        
        dot3 = Dot(plane.n2p(-2 - 1j), color = YELLOW)
        dot4 = Dot(plane.n2p(-1.4 + 2.2j), color = BLUE)
        vector2 = written_arrows(dot3, dot4)
       
        vector_group = VGroup(dot1, label1, dot2, label2, dot3, dot4, vector1, vector2)

        self.play(LaggedStart(
            FadeIn(dot3),
            FadeIn(dot4),
            GrowArrow(vector2, 
            run_time = 1.5)
            )
        )
        self.wait() 
        self.next_slide()
            
        self.play(FadeOut(VGroup(plane, func, vector_group)))

        plane2 = ComplexPlane()
        plane2.add(plane2.get_axis_labels(x_label = "Re", y_label="Im"))

        self.play(Create(plane2))
            
        def vector_func(pos):
            z = complex(pos[0], pos[1])
            m = (z**2 + 1) * (z + 1 - 3j)
            n = (z**2) + 1 + 4j
            fz = m / n
            vects = np.array([z.real, z.imag, 0])
            vecte = np.array([fz.real, fz.imag, 0])
            vect = vecte - vects
            return vect
        
        vector_field1 = ArrowVectorField(
                        vector_func,
                        color = YELLOW,
                        length_func = lambda x : x
                        )

        self.play(
            AnimationGroup(
                ShowIncreasingSubsets(
                    vector_field1,
                    run_time = 3.5
                )
            )
        )    
        self.wait()
        self.next_slide()
        
        vector_field2 = ArrowVectorField(
                        vector_func,
                        color = YELLOW,
                        )

        self.play(
            Transform(
                vector_field1,
                vector_field2,
                run_time = 2.0
            )
        )
        self.wait()
        self.next_slide()

        vector_field3 = ArrowVectorField(
                        vector_func,
                        colors=[RED, ORANGE, GREEN, BLUE]
                        )
        grad = Rectangle(height = 1.0,width = 2.5).move_to(RIGHT * 3 + UP * 2)
        grad.set_fill(color = [RED, ORANGE, GREEN, BLUE], opacity=1)
        gradtex1 = Text("長", font_size = 30).next_to(grad, LEFT)
        gradtex2 = Text("短", font_size = 30).next_to(grad, RIGHT)
        gradtex = VGroup(gradtex1, gradtex2)

        self.play(AnimationGroup(
            Transform(
                vector_field2,
                vector_field3,
                run_time = 2.0
                ),
            FadeIn(VGroup(grad, gradtex)),
            lag_ratio = 1.0
            )
        )
        self.wait()
        self.next_slide()
       
        self.play(FadeOut(grad, gradtex))

        stream1 = StreamLines(vector_func, 
                    stroke_width = 3, 
                    colors = [RED, ORANGE, GREEN, BLUE])
        stream1.start_animation(warm_up = False, flow_speed = 1.0, always_continue=True)
        
        self.play(Create(stream1))
        self.add(stream1)
        self.wait(30)
        self.next_slide()
        
        p1 = Dot(plane2.n2p(-(0.5 + 0.5j)))
        qcircle = Circle(radius = 0.6, color = YELLOW).move_to(p1)

        self.play(Create(qcircle))
        self.wait(30)
        self.next_slide()

        self.play(FadeOut(VGroup(stream1, vector_field1, vector_field2, vector_field3, qcircle)))

        def func2(pos):
            z = complex(pos[0], pos[1])
            fz = z ** 2
            vects = np.array([z.real, z.imag, 0])
            vecte= np.array([fz.real, fz.imag, 0])
            vect = vecte - vects
            return vect

        vector_field4 = ArrowVectorField(
            func2, 
            colors=[RED, ORANGE, GREEN, BLUE]
            )
        
        stream2 = StreamLines(func2, 
                    stroke_width = 3,
                    colors = [RED, ORANGE, GREEN, BLUE]
        )
        stream2.start_animation(warm_up = False, flow_speed = 1.0, always_continue=True)

        label_func2 = MathTex(r'f(z) = z^2', font_size=50).to_corner(UR).add_background_rectangle(BLACK)

        self.play(FadeIn(VGroup(vector_field4, label_func2)))
        self.wait()
        self.next_slide()

        self.play(Create(stream2))
        self.add(stream2)
        self.wait(40)
        self.next_slide()
        
        self.play(FadeOut(*[stream2, label_func2, vector_field4]))

        def func3(pos):
            z = complex(pos[0], pos[1])
            if z == 0:
                return np.array([0, 0, 0])  # ゼロベクトルを返す
            fz = 1 / z
            vects = np.array([z.real, z.imag, 0])
            vecte= np.array([fz.real, fz.imag, 0])
            vect = vecte - vects
            return vect

        vector_field5 = ArrowVectorField(
            func3, 
            colors = [RED, ORANGE, GREEN, BLUE]
            )
        
        stream3 = StreamLines(func3, 
                    stroke_width = 3,
                    colors = [RED, ORANGE, GREEN, BLUE]
        )
        stream3.start_animation(warm_up = False, flow_speed = 1.0, always_continue=True)

        label_func3 = MathTex(r"f(z) = \frac{1}{z}", font_size=50).to_corner(UR).add_background_rectangle(BLACK)

        self.play(FadeIn(VGroup(vector_field5, label_func3)))
        self.wait()
        self.next_slide()

        self.play(Create(stream3))
        self.add(stream3)
        self.wait(40)
        self.next_slide()
        
        self.play(FadeOut(VGroup(stream3, vector_field5, label_func3, plane2)))
        self.next_slide()