from manim import *
from manim_slides import Slide
import math
import cmath
import re

class MySlide5(Slide, ThreeDScene):
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
        self.SectionNum = 4 # 0~4
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

        #########################
        ## １、線形補完の概要１
        #########################
        self.clear()
        text = MathTex(r"f(z)=z^2").to_edge(UL)
        self.add(text)

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )

        def homotopy(p):
            x, y, z = p
            c = complex(x, y)
            c2 = c**2
            return np.array([c2.real, c2.imag, 0])

        self.play(
            ApplyPointwiseFunction(
                homotopy,
                VGroup(plane)
            )
        )

        line = Line(LEFT*8, RIGHT*8)
        self.add(line)
        self.wait()
        self.next_slide()

        #########################
        ## ２、線形補完の概要２
        #########################
        self.clear()
        text = MathTex(r"f(z)=z^2").to_edge(UL)
        self.add(text)
        
        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )

        dot = Dot(plane.n2p(-1+1j), color=YELLOW)

        def homotopy(p):
            x, y, z = p
            c = complex(x, y)
            c2 = c**2
            return np.array([c2.real, c2.imag, 0])

        self.play(
            ApplyPointwiseFunction(
                homotopy,
                VGroup(plane, dot)
            )
        )

        line = Line(LEFT*8, RIGHT*8)
        self.add(line)
        self.wait()
        self.next_slide()

        #########################
        ## ３、線形補完の概要３
        #########################
        self.clear()
        text = MathTex(r"f(z)=z^2").to_edge(UL)
        self.add(text)

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )

        circle = ImplicitFunction(
            lambda x, y: x**2 + y**2 -1,
            color = YELLOW
        )

        def homotopy(p):
            x, y, z = p
            c = complex(x, y)
            c2 = c**2
            return np.array([c2.real, c2.imag, 0])

        self.play(
            ApplyPointwiseFunction(
                homotopy,
                VGroup(plane, circle)
            )
        )

        line = Line(LEFT*8, RIGHT*8)
        self.add(line)
        self.wait()
        self.next_slide()

        #########################
        ## ４、f(z) = 1/z
        #########################
        self.clear()
        text = MathTex(r"f(z)=\frac{1}{z}").to_edge(UL)
        self.add(text)

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.add(plane)

        t_tracker = ValueTracker(0)

        def homotopy(z, t):
            if abs(z) < 0.1:
                return z
            else:
                return t * (1 / z) + (1 - t) * z

        # t_tracker を明示的に使って、always_redraw に変更を伝える
        def make_dots():
            t = t_tracker.get_value()  # これが redraw のトリガーになる
            dots = VGroup()
            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(k, i/40)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)

            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(i/40, k)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)
            return dots

        dots = always_redraw(make_dots)
        self.add(dots)
        self.play(t_tracker.animate.set_value(1), run_time=5)
        self.next_slide()

        #########################
        ## ４、ジューコフスキー変換
        #########################
        self.clear()
        text = MathTex(r"f(z)=z+\frac{1}{z}").to_edge(UL)
        self.add(text)

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.add(plane)

        t_tracker = ValueTracker(0)

        def homotopy(z, t):
            if abs(z) < 0.1:
                return z
            else:
                return t * (1/z + z) + (1 - t) * z

        # t_tracker を明示的に使って、always_redraw に変更を伝える
        def make_dots():
            t = t_tracker.get_value()  # これが redraw のトリガーになる
            dots = VGroup()
            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(k, i/40)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)

            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(i/40, k)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)
            return dots

        dots = always_redraw(make_dots)
        self.add(dots)
        self.play(t_tracker.animate.set_value(1), run_time=5)
        self.next_slide()

        #########################
        ## ５、ジューコフスキー変換２
        #########################
        self.clear()
        text = MathTex(r"f(z)=z+\frac{1}{z}").to_edge(UL)
        self.add(text)

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.add(plane)

        circle = ImplicitFunction(
            lambda x, y: x**2 + y**2 -1,
            color = YELLOW
        )

        t_tracker = ValueTracker(0)

        def homotopy(z, t):
            if abs(z) < 0.1:
                return z
            else:
                return t * (1/z + z) + (1 - t) * z

        # t_tracker を明示的に使って、always_redraw に変更を伝える
        def make_dots():
            t = t_tracker.get_value()  # これが redraw のトリガーになる
            dots = VGroup()
            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(k, i/40)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)

            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(i/40, k)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)
            return dots

        dots = always_redraw(make_dots)
        self.add(dots)
        anim1 = t_tracker.animate.set_value(1)
        anim2 = ComplexHomotopy(homotopy, circle)
        self.play(anim1, anim2, run_time=5.0)
        self.next_slide()

        #########################
        ## ６、ジューコフスキー変換３
        #########################
        self.clear()
        text = MathTex(r"f(z)=z+\frac{1}{z}").to_edge(UL)
        self.add(text)

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.add(plane)

        circle = ImplicitFunction(
            lambda x, y: (x+0.2)**2 + (y-0.6)**2 -1,
            color = YELLOW
        )

        t_tracker = ValueTracker(0)

        def homotopy(z, t):
            if abs(z) < 0.1:
                return z
            else:
                return t * (1/z + z) + (1 - t) * z

        # t_tracker を明示的に使って、always_redraw に変更を伝える
        def make_dots():
            t = t_tracker.get_value()  # これが redraw のトリガーになる
            dots = VGroup()
            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(k, i/40)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)

            for k in range(-4, 5):
                for i in range(-160, 161):
                    from_pos = complex(i/40, k)
                    new_pos = homotopy(from_pos, t)
                    dot = Dot(plane.n2p(new_pos), radius=0.02)
                    if k == 0:
                        dot.set_color(WHITE)
                    else:
                        dot.set_color(BLUE)
                    dots.add(dot)
            return dots

        dots = always_redraw(make_dots)
        self.add(dots)
        anim1 = t_tracker.animate.set_value(1)
        anim2 = ComplexHomotopy(homotopy, circle)
        self.play(anim1, anim2, run_time=5.0)
        self.next_slide()