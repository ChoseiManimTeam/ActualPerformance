from manim import *
from manim_slides import Slide
import math
import cmath
import re

class MySlide3(Slide, ThreeDScene):
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
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.SectionNum = 2 # 0~4
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
        ## １、色を用いた可視化の概要１
        #########################
        self.clear()
        te1 = Text("RGB :")
        te2 = Text("HEX :")
        te3 = Text("HSL :")
        text1 = Text("赤（RED）、緑（GREEN）、青（BLUE）")
        text2 = Text("16進数カラーコード")
        text3 = Text("色相 (Hue)、彩度 (Saturation)、明度 (Lightness)")

        group1 = VGroup(te1, text1).arrange(DOWN).scale(0.8)
        group2 = VGroup(te2, text2).arrange(DOWN).scale(0.8)
        group3 = VGroup(te3, text3).arrange(DOWN).scale(0.8)

        group = VGroup(group1, group2, group3).arrange(DOWN, buff = LARGE_BUFF)
        self.play(FadeIn(group1))
        self.play(FadeIn(group2))
        self.play(FadeIn(group3))
        self.play(Circumscribe(group3))
        self.wait()
        self.next_slide()

        #########################
        ## ２、色を用いた可視化の概要２
        #########################
        self.clear()
        head1 = Text("平面上での可視化").to_edge(UP).scale(0.9)

        self.add(head1)
        
        label_a = Text("（実部, 虚部）", font_size=40)
        arrow = MathTex(r"\longrightarrow")
        label_b = Text("（絶対値, 偏角）", font_size=40)

        group1 = VGroup(label_a, arrow, label_b).arrange(RIGHT, buff = LARGE_BUFF).next_to(head1, DOWN)

        arrow_1 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_a[1:3], DOWN)
        arrow_2 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_a[4:6], DOWN)
        arrow_3 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_b[1:4], DOWN)
        arrow_4 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_b[5:7], DOWN)

        group2 = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        tex1 = Text("x軸", font_size=40).next_to(arrow_1, DOWN)
        tex2 = Text("y軸", font_size=40).next_to(arrow_2, DOWN)
        tex3 = Text("彩度", font_size=40).next_to(arrow_3, DOWN)
        tex4 = Text("色相", font_size=40).next_to(arrow_4, DOWN)

        group3 = VGroup(tex1, tex2, tex3, tex4)

        self.play(FadeIn(group1))
        self.play(FadeIn(group2, group3))
        self.wait(2)

        head2 = Text("空間上での可視化").next_to(group3, DOWN, buff=LARGE_BUFF).scale(0.9)

        self.add(head2)
        
        blabel_a = Text("（実部, 虚部）", font_size=40)
        barrow = MathTex(r"\longrightarrow")
        blabel_b = Text("（絶対値, 偏角）", font_size=40)

        bgroup1 = VGroup(blabel_a, barrow, blabel_b).arrange(RIGHT, buff = LARGE_BUFF).next_to(head2, DOWN)

        barrow_1 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_a[1:3], DOWN)
        barrow_2 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_a[4:6], DOWN)
        barrow_3 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_b[1:4], DOWN)
        barrow_4 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_b[5:7], DOWN)

        bgroup2 = VGroup(barrow_1, barrow_2, barrow_3, barrow_4)

        btex1 = Text("x軸", font_size=40).next_to(barrow_1, DOWN)
        btex2 = Text("y軸", font_size=40).next_to(barrow_2, DOWN)
        btex3 = Text("z軸", font_size=40).next_to(barrow_3, DOWN)
        btex4 = Text("色相", font_size=40).next_to(barrow_4, DOWN)

        bgroup3 = VGroup(btex1, btex2, btex3, btex4)

        self.play(FadeIn(bgroup1))
        self.play(FadeIn(bgroup2, bgroup3))
        self.wait()
        self.next_slide()

        #########################
        ## ３、f(z)=z^2 を用いた具体的な説明
        #########################
        self.clear()

        text = MathTex(r"f(z)=z^2").to_edge(UL)
        self.add(text)

        infield = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4]
            ).scale(0.65).add_coordinates()
        outfield = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
            background_line_style={
                "stroke_color": BLACK,
            }
            ).scale(0.65).add_coordinates()
        VGroup(infield, outfield).arrange(RIGHT, buff=MED_LARGE_BUFF)
        self.play(Create(infield), Create(outfield))
        self.wait()
        self.next_slide()

        size = 4
        x, y = -size, -size
        dots = VGroup()
        fineness = 0.1

        for i in range(int(size*2/fineness + 1)):
            y = -size
            for i in range(int(size*2/fineness + 1)):
                num = complex(x, y)
                hue = (cmath.phase(num)+PI) / (2*PI)
                saturation = (1 / (abs(num) ** 1/3))-1/5
                if saturation > 1:
                    saturation = 1
                color = HSV((hue, saturation, 1.0))
                dots.add(Dot(outfield.n2p(num), color = color, radius=0.1))
                y = y + fineness
            x = x + fineness

        outfield2 = outfield.copy()
        outfield2.x_axis.set_color(BLACK)
        outfield2.y_axis.set_color(BLACK)
        outfield2.coordinate_labels.set_color(BLACK)

        self.add(dots)
        self.add(outfield2)
        self.wait()
        self.next_slide()

        pos = [-1+1j, 1j, 1+1j, -1, 1, -1-1j, -1j, 1-1j]
        indots = VGroup()
        for i in pos:
            indots.add(Dot(infield.n2p(i), color=YELLOW))
        outdots = VGroup()
        for i in pos:
            outdots.add(Dot(outfield2.n2p(i**2), color=YELLOW))
        anims = [
            TransformFromCopy(indots[i], outdots[i]) for i in range(8)
        ]

        self.play(LaggedStart(*anims, lag_ratio=0.2), run_time=2.0)
        self.wait()
        self.next_slide()

        for i in outdots:
            pos = i.get_center()
            num = outfield.p2n(pos)
            hue = (cmath.phase(num)+PI) / (2*PI)
            saturation = (1 / (abs(num) ** 1/3))-1/5
            if saturation > 1:
                saturation = 1
            color = HSV((hue, saturation, 1.0))
            i.set_color(color)
        self.wait()
        self.next_slide()

        anims2 = [
            outdots[i].animate.move_to(indots[i].get_center()) for i in range(8)
        ]
        self.play(LaggedStart(*anims2, lag_ratio=0.2), run_time=2.0)
        self.wait()
        self.next_slide()

        size = 4
        x, y = -size, -size
        dots2 = VGroup()
        fineness = 0.1

        for i in range(int(size*2/fineness + 1)):
            y = -size
            for i in range(int(size*2/fineness + 1)):
                num = complex(x, y)
                num2 = num**2
                hue = (cmath.phase(num2)+PI) / (2*PI)
                saturation = (1 / (abs(num2) ** 1/3))-1/5
                if saturation > 1:
                    saturation = 1
                color = HSV((hue, saturation, 1.0))
                dots2.add(Dot(infield.n2p(num), color = color, radius=0.1))
                y = y + fineness
            x = x + fineness

        infield2 = infield.copy()
        infield2.x_axis.set_color(BLACK)
        infield2.y_axis.set_color(BLACK)
        infield2.coordinate_labels.set_color(BLACK)

        self.add(dots2)
        self.add(infield2)
        self.wait()
        self.next_slide()

        #########################
        ## ４、パターン１
        #########################
        self.clear()

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4]
            ).add_coordinates()
        
        plane.x_axis.set_color(BLACK)
        plane.y_axis.set_color(BLACK)
        plane.coordinate_labels.set_color(BLACK)
        
        size = 4
        x, y = -size, -size
        dots = VGroup()
        fineness = 0.1

        for i in range(int(size*2/fineness + 1)):
            y = -size
            for i in range(int(size*2/fineness + 1)):
                num = complex(x, y)
                num2 = 1/((num-1)*(num+1))
                hue = (cmath.phase(num2)+PI) / (2*PI)
                saturation = (1 / (abs(num2) ** 1/3))-1/5
                if saturation > 1:
                    saturation = 1
                color = HSV((hue, saturation, 1.0))
                dots.add(Dot(plane.n2p(num), color = color, radius=0.1))
                y = y + fineness
            x = x + fineness

        self.add(dots)
        self.add(plane)

        text = MathTex(r"f(z)=\frac{1}{(z-1)(z+1)}").to_edge(UL)
        self.add(text)

        self.wait()
        self.next_slide()

        #########################
        ## ５、パターン２
        #########################
        self.clear()

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4]
            ).add_coordinates()
        
        plane.x_axis.set_color(BLACK)
        plane.y_axis.set_color(BLACK)
        plane.coordinate_labels.set_color(BLACK)
        
        size = 4
        x, y = -size, -size
        dots = VGroup()
        fineness = 0.1

        for i in range(int(size*2/fineness + 1)):
            y = -size
            for i in range(int(size*2/fineness + 1)):
                num = complex(x, y)
                num2 = ((num-(2+2j))*(num-(-2-2j)))/((num-(2-2j))*(num-(-2+2j)))
                hue = (cmath.phase(num2)+PI) / (2*PI)
                saturation = (1 / (abs(num2) ** 1/3))-1/5
                if saturation > 1:
                    saturation = 1
                color = HSV((hue, saturation, 1.0))
                dots.add(Dot(plane.n2p(num), color = color, radius=0.1))
                y = y + fineness
            x = x + fineness

        self.add(dots)
        self.add(plane)

        text = MathTex(r"f(z)=\frac{\{z-(2+2i)\}\{z-(-2-2i)\}}{\{z-(2-2i)\}\{z-(-2+2i)\}}").to_edge(UL)
        self.add(text)

        self.wait()
        self.next_slide()

        #########################
        ## ６、パターン３
        #########################
        self.clear()

        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4]
            ).add_coordinates()
        
        plane.x_axis.set_color(BLACK)
        plane.y_axis.set_color(BLACK)
        plane.coordinate_labels.set_color(BLACK)
        
        size = 4
        x, y = -size, -size
        dots = VGroup()
        fineness = 0.1

        for i in range(int(size*2/fineness + 1)):
            y = -size
            for i in range(int(size*2/fineness + 1)):
                num = complex(x, y)
                num2 = ((num-(2+2j))*(num-(-2+2j)))/((num-(2-2j))*(num-(-2-2j)))
                hue = (cmath.phase(num2)+PI) / (2*PI)
                saturation = (1 / (abs(num2) ** 1/3))-1/5
                if saturation > 1:
                    saturation = 1
                color = HSV((hue, saturation, 1.0))
                dots.add(Dot(plane.n2p(num), color = color, radius=0.1))
                y = y + fineness
            x = x + fineness

        self.add(dots)
        self.add(plane)

        text = MathTex(r"f(z)=\frac{\{z-(2+2i)\}\{z-(-2+2i)\}}{\{z-(2-2i)\}\{z-(-2-2i)\}}").to_edge(UL)
        self.add(text)

        self.wait()
        self.next_slide()

        #########################
        ## ７、空間上の可視化 f(z)=z^2
        #########################
        self.clear()

        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[0, 10, 2],
        )
        self.add(axes)

        def f(z):
            return z**2

        # 曲面を構成する三角形のリスト
        triangles = []

        u_min, u_max = -3, 3
        v_min, v_max = -3, 3
        u_steps = v_steps = 16
        du = (u_max - u_min) / u_steps
        dv = (v_max - v_min) / v_steps

        for i in range(u_steps):
            for j in range(v_steps):
                u = u_min + i * du
                v = v_min + j * dv

                # 4点を取得
                def p(u, v):
                    z = f(complex(u, v))
                    return axes.c2p(u, v, abs(z))

                p1 = p(u, v)
                p2 = p(u + du, v)
                p3 = p(u, v + dv)
                p4 = p(u + du, v + dv)

                # 三角形2枚（p1-p2-p4, p1-p4-p3）
                for a, b, c in [(p1, p2, p4), (p1, p4, p3)]:
                    center = (a + b + c) / 3
                    x, y, _ = axes.p2c(center)
                    hue = (cmath.phase(f(complex(x, y))) + PI) / (2 * PI)
                    color = HSV((hue, 0.8, 1.0))
                    tri = Polygon(a, b, c, fill_color=color, fill_opacity=1, stroke_width=0)
                    triangles.append(tri)

        # カメラ位置を取得する
        def get_camera_position():
            phi = self.camera.get_phi()
            theta = self.camera.get_theta()
            r = self.camera.focal_distance
            return r * np.array([
                np.sin(phi) * np.cos(theta),
                np.sin(phi) * np.sin(theta),
                np.cos(phi)
            ])

        # 描画順制御（毎フレーム remove → add し直す）
        def update_draw_order():
            for tri in triangles:
                self.remove(tri)
            cam_pos = get_camera_position()
            sorted_tris = sorted(
                triangles,
                key=lambda m: -np.linalg.norm(m.get_center() - cam_pos)
            )
            for tri in sorted_tris:
                self.add(tri)

        self.add_updater(lambda dt: update_draw_order())
        update_draw_order()

        fixed_text = MathTex(r"f(z)=z^2", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(7)
        self.stop_ambient_camera_rotation()

        self.next_slide()

        #########################
        ## ８、パターン１
        #########################
        self.clear()
        self.remove_updater(lambda dt: update_draw_order())

        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[0, 10, 2],
        )
        self.add(axes)

        def f(z):
            if abs(z-1) < 0.1 or abs(z+1) < 0.1:
                return 10
            else:
                return 1/((z-1)*(z+1))

        # 曲面を構成する三角形のリスト
        triangles = VGroup()

        u_min, u_max = -3, 3
        v_min, v_max = -3, 3
        u_steps = v_steps = 32
        du = (u_max - u_min) / u_steps
        dv = (v_max - v_min) / v_steps

        for i in range(u_steps):
            for j in range(v_steps):
                u = u_min + i * du
                v = v_min + j * dv

                # 4点を取得
                def p(u, v):
                    z = f(complex(u, v))
                    return axes.c2p(u, v, abs(z))

                p1 = p(u, v)
                p2 = p(u + du, v)
                p3 = p(u, v + dv)
                p4 = p(u + du, v + dv)

                # 三角形2枚（p1-p2-p4, p1-p4-p3）
                for a, b, c in [(p1, p2, p4), (p1, p4, p3)]:
                    center = (a + b + c) / 3
                    x, y, _ = axes.p2c(center)
                    hue = (cmath.phase(f(complex(x, y))) + PI) / (2 * PI)
                    color = HSV((hue, 0.8, 1.0))
                    tri = Polygon(a, b, c, fill_color=color, fill_opacity=1, stroke_width=0)
                    triangles.add(tri)

        self.add(triangles)

        fixed_text = MathTex(r"f(z)=\frac{1}{(z-1)(z+1)}", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)
        self.wait()
        
        self.next_slide()

        #########################
        ## ９、パターン２
        #########################
        self.clear()
        self.set_camera_orientation(phi=55 * DEGREES, theta=45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[0, 10, 2],
        )
        self.add(axes)

        def f(z):
            if abs(z-(1-1j)) < 0.1 or abs(z-(-1+1j)) < 0.1:
                return 10
            else:
                return ((z-(1+1j))*(z-(-1-1j)))/((z-(1-1j))*(z-(-1+1j)))

        # 曲面を構成する三角形のリスト
        triangles = VGroup()

        u_min, u_max = -3, 3
        v_min, v_max = -3, 3
        u_steps = v_steps = 32
        du = (u_max - u_min) / u_steps
        dv = (v_max - v_min) / v_steps

        for i in range(u_steps):
            for j in range(v_steps):
                u = u_min + i * du
                v = v_min + j * dv

                # 4点を取得
                def p(u, v):
                    z = f(complex(u, v))
                    return axes.c2p(u, v, abs(z))

                p1 = p(u, v)
                p2 = p(u + du, v)
                p3 = p(u, v + dv)
                p4 = p(u + du, v + dv)

                # 三角形2枚（p1-p2-p4, p1-p4-p3）
                for a, b, c in [(p1, p2, p4), (p1, p4, p3)]:
                    center = (a + b + c) / 3
                    x, y, _ = axes.p2c(center)
                    hue = (cmath.phase(f(complex(x, y))) + PI) / (2 * PI)
                    color = HSV((hue, 0.8, 1.0))
                    tri = Polygon(a, b, c, fill_color=color, fill_opacity=1, stroke_width=0)
                    triangles.add(tri)

        self.add(triangles)

        fixed_text = MathTex(r"f(z)=\frac{\{z-(1+i)\}\{z-(-1-i)\}}{\{z-(1-i)\}\{z-(-1+i)\}}", font_size=36)
        fixed_text.to_corner(DL)
        self.add_fixed_in_frame_mobjects(fixed_text)
        self.wait()

        self.next_slide()

        #########################
        ## １０、パターン３
        #########################
        self.clear()

        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[0, 15, 2],
        )
        self.add(axes)

        def f(z):
            if abs(z-(1-1j)) < 0.1 or abs(z-(-1-1j)) < 0.1:
                return 10
            else:
                return ((z-(1+1j))*(z-(-1+1j)))/((z-(1-1j))*(z-(-1-1j)))

        # 曲面を構成する三角形のリスト
        triangles = VGroup()

        u_min, u_max = -3, 3
        v_min, v_max = -3, 3
        u_steps = v_steps = 32
        du = (u_max - u_min) / u_steps
        dv = (v_max - v_min) / v_steps

        for i in range(u_steps):
            for j in range(v_steps):
                u = u_min + i * du
                v = v_min + j * dv

                # 4点を取得
                def p(u, v):
                    z = f(complex(u, v))
                    return axes.c2p(u, v, abs(z))

                p1 = p(u, v)
                p2 = p(u + du, v)
                p3 = p(u, v + dv)
                p4 = p(u + du, v + dv)

                # 三角形2枚（p1-p2-p4, p1-p4-p3）
                for a, b, c in [(p1, p2, p4), (p1, p4, p3)]:
                    center = (a + b + c) / 3
                    x, y, _ = axes.p2c(center)
                    hue = (cmath.phase(f(complex(x, y))) + PI) / (2 * PI)
                    color = HSV((hue, 0.8, 1.0))
                    tri = Polygon(a, b, c, fill_color=color, fill_opacity=1, stroke_width=0)
                    triangles.add(tri)

        self.add(triangles)

        fixed_text = MathTex(r"f(z)=\frac{\{z-(1+i)\}\{z-(-1+i)\}}{\{z-(1-i)\}\{z-(-1-i)\}}", font_size=36)
        fixed_text.to_corner(DL)
        self.add_fixed_in_frame_mobjects(fixed_text)
        self.wait()

        self.next_slide()