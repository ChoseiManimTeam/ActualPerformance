from manim import *
from manim_slides import Slide
import math
import cmath
import re

class MySlide2(Slide, ThreeDScene):
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

        self.SectionNum = 1 # 0~4
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
        ## １、複素関数の概要
        #########################
        self.clear()
        eq1 = MathTex("z", r"\quad\longrightarrow\quad", "z^2").scale(2.0).shift(UP)
        self.play(Write(eq1))

        arrow_a = Arrow(start=0.6 * DOWN, end=0.6 * UP, buff=0.1).next_to(eq1[0], DOWN, buff=0.3)
        label_a = Text("（実部, 虚部）", font_size=40).next_to(arrow_a, DOWN, buff=0.3)
        arrow_b = Arrow(start=0.6 * DOWN, end=0.6 * UP, buff=0.1).next_to(eq1[2], DOWN, buff=0.3)
        label_b = Text("（実部, 虚部）", font_size=40).next_to(arrow_b, DOWN, buff=0.3)

        self.play(
            GrowArrow(arrow_a), FadeIn(label_a),
            GrowArrow(arrow_b), FadeIn(label_b)
        )
        self.next_slide()
        self.play(LaggedStart(
                Circumscribe(label_a[1:3]),
                Circumscribe(label_a[4:6]),
                Circumscribe(label_b[1:3]),
                Circumscribe(label_b[4:6]),
                lag_ratio = 1.0
            )
        )
        self.wait()
        self.next_slide()

        #########################
        ## ２、一つの軸を犠牲にした可視化の概要１
        #########################
        self.clear()
        head1 = Text("１つ目の可視化").to_edge(UP)

        self.add(head1)
        
        label_a = Text("（実部, 虚部）", font_size=40)
        arrow = MathTex(r"\longrightarrow")
        label_b = Text("（実部, 虚部）", font_size=40)

        group1 = VGroup(label_a, arrow, label_b).arrange(RIGHT, buff = LARGE_BUFF).next_to(head1, DOWN)

        arrow_1 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_a[1:3], DOWN)
        arrow_2 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_a[4:6], DOWN)
        arrow_3 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_b[1:3], DOWN)
        arrow_4 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_b[4:6], DOWN)

        group2 = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        tex1 = Text("x軸", font_size=40).next_to(arrow_1, DOWN)
        tex2 = Text("y軸", font_size=40).next_to(arrow_2, DOWN)
        tex3 = Text("z軸", font_size=40).next_to(arrow_3, DOWN)
        tex4 = Text("なし", font_size=40).next_to(arrow_4, DOWN)

        group3 = VGroup(tex1, tex2, tex3, tex4)

        self.play(FadeIn(group1))
        self.play(FadeIn(group2, group3))

        blabel_a = Text("（実部, 虚部）", font_size=40)
        barrow = MathTex(r"\longrightarrow")
        blabel_b = Text("（実部, 虚部）", font_size=40)

        bgroup1 = VGroup(blabel_a, barrow, blabel_b).arrange(RIGHT, buff = LARGE_BUFF).next_to(group3, DOWN, buff=LARGE_BUFF)

        barrow_1 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_a[1:3], DOWN)
        barrow_2 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_a[4:6], DOWN)
        barrow_3 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_b[1:3], DOWN)
        barrow_4 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.1, stroke_width=4).next_to(blabel_b[4:6], DOWN)

        bgroup2 = VGroup(barrow_1, barrow_2, barrow_3, barrow_4)

        btex1 = Text("x軸", font_size=40).next_to(barrow_1, DOWN)
        btex2 = Text("y軸", font_size=40).next_to(barrow_2, DOWN)
        btex3 = Text("なし", font_size=40).next_to(barrow_3, DOWN)
        btex4 = Text("z軸", font_size=40).next_to(barrow_4, DOWN)

        bgroup3 = VGroup(btex1, btex2, btex3, btex4)

        self.play(FadeIn(bgroup1))
        self.play(FadeIn(bgroup2, bgroup3))
        self.wait()
        self.next_slide()

        #########################
        ## ２、一つの軸を犠牲にした可視化の概要２
        #########################
        self.clear()
        head1 = Text("２つ目の可視化").to_edge(UP)

        self.add(head1)
        
        label_a = Text("（実部, 虚部）", font_size=40)
        arrow = MathTex(r"\longrightarrow")
        label_b = Text("（実部, 虚部）", font_size=40)

        group1 = VGroup(label_a, arrow, label_b).arrange(RIGHT, buff = LARGE_BUFF)

        arrow_1 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_a[1:3], DOWN)
        arrow_2 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_a[4:6], DOWN)
        arrow_3 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_b[1:3], DOWN)
        arrow_4 = Arrow(start=0.4 * UP, end=0.4 * DOWN, buff=0.0, stroke_width=4).next_to(label_b[4:6], DOWN)

        group2 = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        tex1 = Text("x軸", font_size=40).next_to(arrow_1, DOWN)
        tex2 = Text("なし", font_size=40).next_to(arrow_2, DOWN)
        tex3 = Text("z軸", font_size=40).next_to(arrow_3, DOWN)
        tex4 = Text("y軸", font_size=40).next_to(arrow_4, DOWN)

        group3 = VGroup(tex1, tex2, tex3, tex4)

        VGroup(group1, group2, group3).move_to(ORIGIN)

        self.play(FadeIn(group1))
        self.play(FadeIn(group2, group3))
        self.wait()
        self.next_slide()

        #########################
        ## ２、出力の実部のみの描画
        #########################
        self.clear()
        self.set_camera_orientation(phi=65 * DEGREES, theta=-135 * DEGREES)

        fixed_text = MathTex("f(z)=z^2", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes1 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface1 = Surface(
            lambda u, v: axes1.c2p(u, v, (complex(u, v)**2).real),
            resolution = 16,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        labels1 = axes1.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Re}(f(z))")
        )

        graph1 = VGroup(axes1, surface1, labels1)

        self.add(graph1)

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.next_slide()

        self.begin_ambient_camera_rotation(rate=0.15)

        intersection_curve = ParametricFunction(
            lambda t: axes1.c2p(t, 0, t**2),
            t_range=[-3, 3],
            color=YELLOW,
            stroke_width=4
        )
        self.play(Create(intersection_curve))

        self.wait(2)
        self.play(FadeOut(intersection_curve))
        self.wait()
        self.stop_ambient_camera_rotation()
        self.next_slide()

        #########################
        ## ３、出力の虚部も横に並べた表示
        #########################
        self.play(graph1.animate.scale(0.9).shift(LEFT*3))

        axes2 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface2 = Surface(
            lambda u, v: axes2.c2p(u, v, (complex(u, v)**2).imag),
            resolution = 16,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[RED_D, RED_E],
        )

        labels2 = axes2.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Im}(f(z))")
        )

        graph2 = VGroup(axes2, surface2, labels2)
        graph2.scale(0.9).shift(RIGHT*3)

        self.play(TransformFromCopy(graph1, graph2))
        self.wait()

        self.play(graph1.animate.rotate(-PI/2), graph2.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()
        

        # graph1 の交線（z = 0 ⇔ y = ±x）
        intersection_curve1_a = ParametricFunction(
            lambda t: axes1.c2p(t, t, 0),
            t_range=[-3, 3],
            color=YELLOW
        )
        intersection_curve1_b = ParametricFunction(
            lambda t: axes1.c2p(t, -t, 0),
            t_range=[-3, 3],
            color=YELLOW
        )
        self.play(Create(intersection_curve1_a), Create(intersection_curve1_b))

        # graph2 の交線（z = 0 ⇔ x = 0 または y = 0）
        intersection_curve2_a = ParametricFunction(
            lambda t: axes2.c2p(t, 0, 0),
            t_range=[-3, 3],
            color=ORANGE
        )
        intersection_curve2_b = ParametricFunction(
            lambda t: axes2.c2p(0, t, 0),
            t_range=[-3, 3],
            color=ORANGE
        )
        self.play(Create(intersection_curve2_a), Create(intersection_curve2_b))
        self.wait()

        graph1plus = VGroup(graph1, intersection_curve1_a, intersection_curve1_b)
        graph2plus = VGroup(graph2, intersection_curve2_a, intersection_curve2_b)

        self.play(graph1plus.animate.rotate(-PI/2), graph2plus.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()

        
        self.play(graph1plus.animate.move_to(ORIGIN))
        self.play(graph2plus.animate.move_to(ORIGIN))
        self.wait()

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.next_slide()

        #########################
        ## ３、上下に平行移動させたとき１
        #########################
        self.clear()
        self.set_camera_orientation(phi=65 * DEGREES, theta=-90 * DEGREES)

        fixed_text = MathTex("f(z)=z^2-1", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes1 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface1 = Surface(
            lambda u, v: axes1.c2p(u, v, (complex(u, v)**2-1).real),
            resolution = 16,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        labels1 = axes1.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Re}(f(z))")
        )

        graph1 = VGroup(axes1, surface1, labels1)
        graph1.scale(0.9).shift(LEFT*3.5)

        axes2 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface2 = Surface(
            lambda u, v: axes2.c2p(u, v, (complex(u, v)**2-1).imag),
            resolution = 16,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[RED_D, RED_E],
        )

        labels2 = axes2.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Im}(f(z))")
        )

        graph2 = VGroup(axes2, surface2, labels2)
        graph2.scale(0.9).shift(RIGHT*3.5)

        self.play(FadeIn(graph1, graph2))
        self.wait()
        self.play(graph1.animate.rotate(-PI/2), graph2.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()

        # graph1の交線：x^2 - y^2 - 1 = 0 → y = ±sqrt(x^2 - 1), |x| ≥ 1
        curve1_pos = ParametricFunction(
            lambda t: axes1.c2p(t, np.sqrt(t**2 - 1), 0),
            t_range=[-3, -1],
            color=YELLOW
        )
        curve1_neg = ParametricFunction(
            lambda t: axes1.c2p(t, -np.sqrt(t**2 - 1), 0),
            t_range=[-3, -1],
            color=YELLOW
        )
        curve1_pos2 = ParametricFunction(
            lambda t: axes1.c2p(t, np.sqrt(t**2 - 1), 0),
            t_range=[1, 3],
            color=YELLOW
        )
        curve1_neg2 = ParametricFunction(
            lambda t: axes1.c2p(t, -np.sqrt(t**2 - 1), 0),
            t_range=[1, 3],
            color=YELLOW
        )
        self.play(
            Create(curve1_pos), Create(curve1_neg),
            Create(curve1_pos2), Create(curve1_neg2)
        )

        # graph2の交線：2xy = 0 → x=0 または y=0
        curve2_xaxis = ParametricFunction(
            lambda t: axes2.c2p(t, 0, 0),
            t_range=[-3, 3],
            color=ORANGE
        )
        curve2_yaxis = ParametricFunction(
            lambda t: axes2.c2p(0, t, 0),
            t_range=[-3, 3],
            color=ORANGE
        )
        self.play(Create(curve2_xaxis), Create(curve2_yaxis))
        self.wait()

        graph1plus = VGroup(graph1, curve1_pos, curve1_neg, curve1_pos2, curve1_neg2)
        graph2plus = VGroup(graph2, curve2_xaxis, curve2_yaxis)

        self.play(graph1plus.animate.rotate(-PI/2), graph2plus.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()

        # 各座標軸の原点（3D空間上の位置）を取得
        origin1 = axes1.c2p(0, 0, 0)
        origin2 = axes2.c2p(0, 0, 0)

        # 原点の差をベクトルとして計算
        shift_vector1 = ORIGIN - origin1
        shift_vector2 = ORIGIN - origin2

        # 各グラフをその原点が絶対原点に一致するように移動
        self.play(graph1plus.animate.shift(shift_vector1))
        self.play(graph2plus.animate.shift(shift_vector2))
        self.wait()

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.next_slide()

        curve1_y_eq_0 = ParametricFunction(
            lambda t: axes1.c2p(t, 0, t**2 - 1),
            t_range=[-3, 3],
            color=PURPLE,
            stroke_width=4
        )
        self.play(Create(curve1_y_eq_0))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait()
        self.next_slide()

        #########################
        ## ４、上下に平行移動させたとき２
        #########################
        self.clear()
        self.set_camera_orientation(phi=65 * DEGREES, theta=-90 * DEGREES)

        fixed_text = MathTex("f(z)=z^2+1", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes1 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface1 = Surface(
            lambda u, v: axes1.c2p(u, v, (complex(u, v)**2+1).real),
            resolution = 16,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        labels1 = axes1.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Re}(f(z))")
        )

        graph1 = VGroup(axes1, surface1, labels1)
        graph1.scale(0.9).shift(LEFT*3.5)

        axes2 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface2 = Surface(
            lambda u, v: axes2.c2p(u, v, (complex(u, v)**2+1).imag),
            resolution = 16,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[RED_D, RED_E],
        )

        labels2 = axes2.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Im}(f(z))")
        )

        graph2 = VGroup(axes2, surface2, labels2)
        graph2.scale(0.9).shift(RIGHT*3.5)

        self.play(FadeIn(graph1, graph2))
        self.wait()
        self.play(graph1.animate.rotate(-PI/2), graph2.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()

        # graph1の交線：x^2 - y^2 - 1 = 0 → y = ±sqrt(x^2 - 1), |x| ≥ 1
        curve1_pos = ParametricFunction(
            lambda t: axes1.c2p(t, np.sqrt(t**2 + 1), 0),
            t_range=[-3, 3],
            color=YELLOW
        )
        curve1_neg = ParametricFunction(
            lambda t: axes1.c2p(t, -np.sqrt(t**2 + 1), 0),
            t_range=[-3, 3],
            color=YELLOW
        )
        self.play(
            Create(curve1_pos), Create(curve1_neg),
        )

        # graph2の交線：2xy = 0 → x=0 または y=0
        curve2_xaxis = ParametricFunction(
            lambda t: axes2.c2p(t, 0, 0),
            t_range=[-3, 3],
            color=ORANGE
        )
        curve2_yaxis = ParametricFunction(
            lambda t: axes2.c2p(0, t, 0),
            t_range=[-3, 3],
            color=ORANGE
        )
        self.play(Create(curve2_xaxis), Create(curve2_yaxis))
        self.wait()

        graph1plus = VGroup(graph1, curve1_pos, curve1_neg)
        graph2plus = VGroup(graph2, curve2_xaxis, curve2_yaxis)

        self.play(graph1plus.animate.rotate(-PI/2), graph2plus.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()

        # 各座標軸の原点（3D空間上の位置）を取得
        origin1 = axes1.c2p(0, 0, 0)
        origin2 = axes2.c2p(0, 0, 0)

        # 原点の差をベクトルとして計算
        shift_vector1 = ORIGIN - origin1
        shift_vector2 = ORIGIN - origin2

        # 各グラフをその原点が絶対原点に一致するように移動
        self.play(graph1plus.animate.shift(shift_vector1))
        self.play(graph2plus.animate.shift(shift_vector2))
        self.wait()

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.next_slide()

        curve1_y_eq_0 = ParametricFunction(
            lambda t: axes1.c2p(t, 0, t**2 + 1),
            t_range=[-3, 3],
            color=PURPLE_D,
            stroke_width=4
        )
        self.play(Create(curve1_y_eq_0))
        self.wait()

        curve1_x_eq_0 = ParametricFunction(
            lambda t: axes1.c2p(0, t, -t**2 + 1),
            t_range=[-3, 3],
            color=PURPLE_E,
            stroke_width=4
        )
        self.play(Create(curve1_x_eq_0))
        self.wait()

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait()
        self.next_slide()

        #########################
        ## ５、極をもつようなグラフ１
        #########################
        self.clear()
        def exclude_points(rng, excluded_points, distance):
            start, end = rng
            excluded_points = sorted(excluded_points)

            # 除外点ごとに除外区間を作る（前後に distance 分）
            split_points = [start]
            for p in excluded_points:
                low = max(start, p - distance)
                high = min(end, p + distance)
                split_points.extend([low, high])
            split_points.append(end)

            # 昇順にソートして隣接点で区間を作成
            split_points = sorted(set(split_points))  # 重複を避けてソート
            intervals = [[split_points[i], split_points[i+1]] for i in range(len(split_points) - 1)]

            return intervals
        
        def is_exclude_area(hole, x_range, y_range):
            check = True
            for (x, y) in hole:
                if(x_range[0] < x < x_range[1] and y_range[0] < y < y_range[1]):
                    check = False
            return check

        def holed_surface(
                func,
                hole = [(0,0)],
                distance = 0.1,
                u_range = [-1, 1],
                v_range = [-1, 1],
                resolution_const = 0.1,
                fill_opacity = 1,
                checkerboard_colors = [BLUE_D, BLUE_E]
        ):
            x_hole, y_hole = zip(*hole)
            x_ranges = exclude_points(u_range, x_hole, distance)
            y_ranges = exclude_points(v_range, y_hole, distance)
            surface = VGroup()

            for x_range in x_ranges:
                for y_range in y_ranges:
                    if is_exclude_area(hole, x_range, y_range):
                        x_re = int((x_range[1] - x_range[0]) / resolution_const)
                        y_re = int((y_range[1] - y_range[0]) / resolution_const)
                        surface.add(
                            Surface(
                                func=func,
                                u_range=x_range,
                                v_range=y_range,
                                resolution=[x_re, y_re],
                                fill_opacity=fill_opacity,
                                checkerboard_colors=checkerboard_colors,
                            )
                    )
                        
            return surface
        


        # ここから
        self.set_camera_orientation(phi=65 * DEGREES, theta=-135 * DEGREES)

        fixed_text = MathTex(r"f(z)=\frac{1}{z}", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes1 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface1 = holed_surface(
            lambda u, v: axes1.c2p(u, v, (1/complex(u, v)).real),
            distance = 0.1,
            hole = [(0, 0)],
            resolution_const = 0.1,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],  # 単色にして継ぎ目を目立たなく
        )

        labels1 = axes1.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Re}(f(z))")
        )

        graph1 = VGroup(axes1, surface1, labels1)

        self.add(graph1)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        self.play(graph1.animate.scale(0.9).shift(LEFT*3))

        axes2 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface2 = holed_surface(
            lambda u, v: axes2.c2p(u, v, (1/complex(u, v)).imag),
            distance = 0.1,
            hole = [(0, 0)],
            resolution_const = 0.1,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[RED_D, RED_E],  # 単色にして継ぎ目を目立たなく
        )

        labels2 = axes2.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Im}(f(z))")
        )

        graph2 = VGroup(axes2, surface2, labels2)
        graph2.scale(0.9).shift(RIGHT*3)

        self.play(TransformFromCopy(graph1, graph2))
        self.wait()

        self.play(graph1.animate.rotate(-PI/2), graph2.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()

        #########################
        ## ６、極をもつようなグラフ２
        #########################
        self.clear()
        self.set_camera_orientation(phi=65 * DEGREES, theta=-135 * DEGREES)

        fixed_text = MathTex(r"f(z)=\frac{1}{(z-1-i)(z+1+i)}", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes1 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface1 = holed_surface(
            lambda u, v: axes1.c2p(u, v, (1/((complex(u, v)-(1+1j))*(complex(u, v)-(-1-1j)))).real),
            distance = 0.1,
            hole = [(1, 1), (-1, -1)],
            resolution_const = 0.1,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],  # 単色にして継ぎ目を目立たなく
        )

        labels1 = axes1.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Re}(f(z))")
        )

        graph1 = VGroup(axes1, surface1, labels1)

        self.add(graph1)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        self.play(graph1.animate.scale(0.9).shift(LEFT*3))

        axes2 = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=4,
            y_length=4,
            z_length=4,
        )

        surface2 = holed_surface(
            lambda u, v: axes2.c2p(u, v, (1/((complex(u, v)-(1+1j))*(complex(u, v)-(-1-1j)))).imag),
            distance = 0.1,
            hole = [(1, 1), (-1, -1)],
            resolution_const = 0.1,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.75,
            checkerboard_colors=[RED_D, RED_E],  # 単色にして継ぎ目を目立たなく
        )

        labels2 = axes2.get_axis_labels(
            x_label=MathTex(r"\mathrm{Re}(z)"),
            y_label=MathTex(r"\mathrm{Im}(z)"),
            z_label=MathTex(r"\mathrm{Im}(f(z))")
        )

        graph2 = VGroup(axes2, surface2, labels2)
        graph2.scale(0.9).shift(RIGHT*3)

        self.play(TransformFromCopy(graph1, graph2))
        self.wait()

        self.play(graph1.animate.rotate(-PI/2), graph2.animate.rotate(-PI/2), run_time = 6.0, rate_func=linear)
        self.wait()
        self.next_slide()

        #########################
        ## ７、ルート２の実平面上のグラフ
        #########################
        self.clear()
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        ).add_coordinates()

        curve = plane.plot(lambda x: np.sqrt(x), color=YELLOW, x_range=[0, 4])

        text = MathTex(r"f(x)=\sqrt{x}").scale(1.2).to_edge(UL)

        self.add(text)
        self.play(Create(plane, run_time=2.0))
        self.play(Create(curve))
        self.wait()
        self.next_slide()

        #########################
        ## ８、ルート２の複素平面上のグラフ
        #########################
        self.clear()
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        fixed_text = MathTex(r"f(x)=\sqrt{x}", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes = ThreeDAxes()
        
        labels = axes.get_axis_labels(
            x_label=MathTex("Re(z)"),
            y_label=MathTex("Im(f(z))"),
            z_label=MathTex("Re(f(z))")
        )
        self.add(axes, labels)

        t_tracker = ValueTracker(4)
        u_tracker = ValueTracker(4)

        def create_plane():
            # スケール合わせ
            x_range = axes.z_range
            y_range = axes.y_range
            x_unit_size = axes.z_axis.get_length() / (x_range[1] - x_range[0])
            y_unit_size = axes.y_axis.get_length() / (y_range[1] - y_range[0])

            plane = ComplexPlane(
                x_range=x_range,
                y_range=y_range,
                x_length=x_unit_size * (x_range[1] - x_range[0]),
                y_length=y_unit_size * (y_range[1] - y_range[0]),
                axis_config={"include_ticks": True, "include_numbers": False},
            )

            plane.apply_matrix(rotation_matrix(PI / 2, axis=DOWN))

            # 原点一致のため、原点位置を補正して移動
            shift_vector = axes.c2p(t_tracker.get_value(), 0, 0) - plane.n2p(0)
            plane.shift(shift_vector)

            return plane


        plane = always_redraw(create_plane)

        # (-1)^n = e^(i*pi*n) の複素数を描画
        def complex_dot():
            # n に基づいて複素数を計算
            n_value = t_tracker.get_value()
            complex_number = cmath.sqrt(n_value)
            dot = Dot().apply_matrix(rotation_matrix(PI / 2, axis=DOWN))
            dot.move_to(plane.n2p(complex_number))
            return dot

        dot = always_redraw(complex_dot)

        def parametric_curve():
            return ParametricFunction(
                    lambda t: axes.c2p(
                        t,
                        cmath.sqrt(t).imag,
                        cmath.sqrt(t).real
                    ),
                    t_range=[t_tracker.get_value(), u_tracker.get_value()],
                    color=YELLOW,
                    stroke_width=4
                )
        
        curve = always_redraw(parametric_curve)

        self.add(plane, dot, curve)

        self.play(t_tracker.animate.set_value(-4), run_time=12, rate_func=linear)

        self.play(FadeOut(plane, dot))

        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=4.0, rate_func=linear)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=2.0, rate_func=linear)
        self.play(t_tracker.animate.set_value(0), run_time=0.07)
        self.wait(2)
        self.play(t_tracker.animate.set_value(-4), run_time=0.07)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=4.0, rate_func=linear)
        self.play(u_tracker.animate.set_value(0), run_time=0.07)
        self.wait(2)
        self.play(u_tracker.animate.set_value(4), run_time=0.07)
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=4.0, rate_func=linear)
        self.wait()
        self.next_slide()

        #########################
        ## ９、半円の実平面上のグラフ
        #########################
        self.clear()
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        ).add_coordinates()

        curve = plane.plot(lambda x: np.sqrt(1-x**2), color=YELLOW, x_range=[-1, 1])

        text = MathTex(r"f(x)=\sqrt{1-x^2}").scale(1.2).to_edge(UL)

        self.add(text)
        self.play(Create(plane, run_time=2.0))
        self.play(Create(curve))
        self.wait()
        self.next_slide()

        #########################
        ## １０、半円の複素平面上のグラフ
        #########################
        self.clear()
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        fixed_text = MathTex(r"f(x)=\sqrt{1-x^2}", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes = ThreeDAxes()
        
        labels = axes.get_axis_labels(
            x_label=MathTex("Re(z)"),
            y_label=MathTex("Im(f(z))"),
            z_label=MathTex("Re(f(z))")
        )
        self.add(axes, labels)

        t_tracker = ValueTracker(4)
        u_tracker = ValueTracker(4)

        def create_plane():
            # スケール合わせ
            x_range = axes.z_range
            y_range = axes.y_range
            x_unit_size = axes.z_axis.get_length() / (x_range[1] - x_range[0])
            y_unit_size = axes.y_axis.get_length() / (y_range[1] - y_range[0])

            plane = ComplexPlane(
                x_range=x_range,
                y_range=y_range,
                x_length=x_unit_size * (x_range[1] - x_range[0]),
                y_length=y_unit_size * (y_range[1] - y_range[0]),
                axis_config={"include_ticks": True, "include_numbers": False},
            )

            plane.apply_matrix(rotation_matrix(PI / 2, axis=DOWN))

            # 原点一致のため、原点位置を補正して移動
            shift_vector = axes.c2p(t_tracker.get_value(), 0, 0) - plane.n2p(0)
            plane.shift(shift_vector)

            return plane


        plane = always_redraw(create_plane)

        # (-1)^n = e^(i*pi*n) の複素数を描画
        def complex_dot():
            # n に基づいて複素数を計算
            n_value = t_tracker.get_value()
            complex_number = cmath.sqrt(1-n_value**2)
            dot = Dot().apply_matrix(rotation_matrix(PI / 2, axis=DOWN))
            dot.move_to(plane.n2p(complex_number))
            return dot

        dot = always_redraw(complex_dot)

        def parametric_curve():
            return ParametricFunction(
                    lambda t: axes.c2p(
                        t,
                        cmath.sqrt(1-t**2).imag,
                        cmath.sqrt(1-t**2).real
                    ),
                    t_range=[t_tracker.get_value(), u_tracker.get_value()],
                    color=YELLOW,
                    stroke_width=4
                )
        
        curve = always_redraw(parametric_curve)

        self.add(plane, dot, curve)

        self.play(t_tracker.animate.set_value(-4), run_time=12, rate_func=linear)

        self.play(FadeOut(plane, dot))

        def curve_range(a, b):
            return ParametricFunction(
                    lambda t: axes.c2p(
                        t,
                        cmath.sqrt(1-t**2).imag,
                        cmath.sqrt(1-t**2).real
                    ),
                    t_range=[a, b],
                    color=YELLOW,
                    stroke_width=4
                )

        curvei = VGroup(curve_range(-4, -1), curve_range(1, 4))

        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=4.0, rate_func=linear)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=2.0, rate_func=linear)
        self.play(t_tracker.animate.set_value(-1), run_time=0.07)
        self.play(u_tracker.animate.set_value(1), run_time=0.07)
        self.wait(2)
        self.play(t_tracker.animate.set_value(-4), run_time=0.07)
        self.play(u_tracker.animate.set_value(4), run_time=0.07)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=4.0, rate_func=linear)
        self.remove(curve)
        self.add(curvei)
        self.wait(2)
        self.remove(curvei)
        self.add(curve)
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=4.0, rate_func=linear)
        self.wait()
        self.next_slide()

        #########################
        ## １１、(-2)^xの実平面上の点
        #########################
        self.clear()
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
        ).add_coordinates()

        text = MathTex(r"f(x)=(-2)^x").scale(1.2).to_edge(UL)

        self.add(text)
        self.play(Create(plane, run_time=2.0))

        dots = VGroup()
        for i in range(-4, 5):
            dots.add(Dot(plane.c2p(i, (-2)**i), color=YELLOW))
            
        self.play(FadeIn(dots))
        self.wait()
        self.next_slide()

        #########################
        ## １２、(-2)^xの複素平面上の点
        #########################
        self.clear()
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        fixed_text = MathTex(r"f(x)=(-2)^x", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes = ThreeDAxes()
        
        labels = axes.get_axis_labels(
            x_label=MathTex("Re(z)"),
            y_label=MathTex("Im(f(z))"),
            z_label=MathTex("Re(f(z))")
        )
        self.add(axes, labels)

        t_tracker = ValueTracker(4)

        def create_plane():
            # スケール合わせ
            x_range = axes.z_range
            y_range = axes.y_range
            x_unit_size = axes.z_axis.get_length() / (x_range[1] - x_range[0])
            y_unit_size = axes.y_axis.get_length() / (y_range[1] - y_range[0])

            plane = ComplexPlane(
                x_range=x_range,
                y_range=y_range,
                x_length=x_unit_size * (x_range[1] - x_range[0]),
                y_length=y_unit_size * (y_range[1] - y_range[0]),
                axis_config={"include_ticks": True, "include_numbers": False},
            )

            plane.apply_matrix(rotation_matrix(PI / 2, axis=DOWN))

            # 原点一致のため、原点位置を補正して移動
            shift_vector = axes.c2p(t_tracker.get_value(), 0, 0) - plane.n2p(0)
            plane.shift(shift_vector)

            return plane


        plane = always_redraw(create_plane)

        # (-1)^n = e^(i*pi*n) の複素数を描画
        def complex_dot():
            # n に基づいて複素数を計算
            n_value = t_tracker.get_value()
            complex_number = cmath.exp(n_value * cmath.log(-2))
            dot = Dot().apply_matrix(rotation_matrix(PI / 2, axis=DOWN))
            dot.move_to(plane.n2p(complex_number))
            return dot

        dot = always_redraw(complex_dot)

        def parametric_curve():
            return ParametricFunction(
                    lambda t: axes.c2p(
                        t,
                        cmath.exp(t * cmath.log(-2)).imag,
                        cmath.exp(t * cmath.log(-2)).real
                    ),
                    t_range=[t_tracker.get_value(), 4],
                    color=YELLOW,
                    stroke_width=4
                )
        
        curve = always_redraw(parametric_curve)

        self.add(plane, dot, curve)

        self.play(t_tracker.animate.set_value(-4), run_time=12, rate_func=linear)

        self.play(FadeOut(plane, dot))

        dots = VGroup()
        for i in range(-4, 5):
            dot = Dot().apply_matrix(rotation_matrix(PI / 2, axis=RIGHT))
            dot.move_to(axes.c2p(i, 0, (-2)**i)).set_color(PURPLE)
            dots.add(dot)

        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=4.0, rate_func=linear)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=2.0, rate_func=linear)
        self.add(dots)
        self.wait(2)
        self.remove(dots)
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=2.0, rate_func=linear)
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=4.0, rate_func=linear)
        self.wait()
        self.next_slide()

        #########################
        ## １３、(-1)^xの複素平面上の点
        #########################
        self.clear()
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES)

        fixed_text = MathTex(r"f(x)=(-1)^x", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes = ThreeDAxes()
        
        labels = axes.get_axis_labels(
            x_label=MathTex("Re(z)"),
            y_label=MathTex("Im(f(z))"),
            z_label=MathTex("Re(f(z))")
        )
        self.add(axes, labels)

        def parametric_curve():
            return ParametricFunction(
                    lambda t: axes.c2p(
                        t,
                        cmath.exp(t * cmath.log(-1)).imag,
                        cmath.exp(t * cmath.log(-1)).real
                    ),
                    t_range=[-4, 4],
                    color=YELLOW,
                    stroke_width=4
                )
        
        curve = always_redraw(parametric_curve)

        self.add(curve)

        dots = VGroup()
        for i in range(-4, 5):
            dot = Dot().apply_matrix(rotation_matrix(PI / 2, axis=RIGHT))
            dot.move_to(axes.c2p(i, 0, (-1)**i)).set_color(PURPLE)
            dots.add(dot)

        self.add(dots)
        self.wait(2)
        self.remove(dots)
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=2.0, rate_func=linear)
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=4.0, rate_func=linear)
        self.wait()
        self.next_slide()

        #########################
        ## １４、(-1/2)^xの複素平面上の点
        #########################
        self.clear()
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES)

        fixed_text = MathTex(r"f(x)=(-\frac{1}{2})^x", font_size=36)
        fixed_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(fixed_text)

        axes = ThreeDAxes()
        
        labels = axes.get_axis_labels(
            x_label=MathTex("Re(z)"),
            y_label=MathTex("Im(f(z))"),
            z_label=MathTex("Re(f(z))")
        )
        self.add(axes, labels)

        def parametric_curve():
            return ParametricFunction(
                    lambda t: axes.c2p(
                        t,
                        cmath.exp(t * cmath.log(-1/2)).imag,
                        cmath.exp(t * cmath.log(-1/2)).real
                    ),
                    t_range=[-4, 4],
                    color=YELLOW,
                    stroke_width=4
                )
        
        curve = always_redraw(parametric_curve)

        self.add(curve)

        dots = VGroup()
        for i in range(-4, 5):
            dot = Dot().apply_matrix(rotation_matrix(PI / 2, axis=RIGHT))
            dot.move_to(axes.c2p(i, 0, (-1/2)**i)).set_color(PURPLE)
            dots.add(dot)

        self.add(dots)
        self.wait(2)
        self.remove(dots)
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=2.0, rate_func=linear)
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=4.0, rate_func=linear)
        self.wait()
        self.next_slide()

        #########################
        ## １５、a^xの複素平面上の点
        #########################
        self.clear()
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes()

        a_tracker = ValueTracker(-1/2)

        def create_formula():
            a_val = DecimalNumber(
                a_tracker.get_value(),
                num_decimal_places=2,
                include_sign=True,
                group_with_commas=False,
                font_size=36,
            )

            prefix = MathTex("f(x) = ").scale(0.8)
            x_exp = MathTex("x").scale(0.6)
            x_exp.next_to(a_val, UR, buff=0.05)

            group = VGroup(prefix, a_val, x_exp)
            group.arrange(RIGHT, buff=0.05)
            group.to_corner(UL)
            x_exp.shift(UP * 1/6)
            return group

        formula_label = always_redraw(create_formula)
        self.add_fixed_in_frame_mobjects(formula_label)
        
        labels = axes.get_axis_labels(
            x_label=MathTex("Re(z)"),
            y_label=MathTex("Im(f(z))"),
            z_label=MathTex("Re(f(z))")
        )
        self.add(axes, labels)

        def parametric_curve():
            return ParametricFunction(
                    lambda t: axes.c2p(
                        t,
                        cmath.exp(t * cmath.log(a_tracker.get_value())).imag,
                        cmath.exp(t * cmath.log(a_tracker.get_value())).real
                    ),
                    t_range=[-4, 4],
                    color=YELLOW,
                    stroke_width=4
                )
        
        curve = always_redraw(parametric_curve)

        self.add(curve)

        self.play(a_tracker.animate.set_value(-1), run_time=4.0, rate_func=linear)
        self.wait(4)
        self.play(a_tracker.animate.set_value(-2), run_time=4.0, rate_func=linear)
        self.wait(4)
        self.next_slide()

        #########################
        ## １６、x^aの複素平面上の点
        #########################
        self.clear()
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes()
        self.add(axes)

        a_tracker = ValueTracker(3)

        def create_formula():
            a_val = DecimalNumber(
                a_tracker.get_value(),
                num_decimal_places=2,
                include_sign=True,
                group_with_commas=False,
                font_size=20,
            )

            prefix = MathTex("f(x) = x").scale(0.8)
            group = VGroup(prefix, a_val)
            group.to_corner(UL)
            a_val.shift([1, 0.2, 0])
            return group
        
        formula_label = always_redraw(create_formula)
        self.add_fixed_in_frame_mobjects(formula_label)

        def f(t):
            try:
                return cmath.exp(a_tracker.get_value() * cmath.log(complex(t)))
            except:
                return complex(float('nan'), float('nan'))

        def graph():
            group1 = VGroup()
            group2 = VGroup()

            t_values1 = [i * 0.01 for i in range(-500, -1) if i != 0]
            points1 = [
                axes.c2p(t, f(t).imag, f(t).real)
                for t in t_values1
                if not math.isnan(f(t).real) and not math.isnan(f(t).imag)
            ]
            for p1, p2 in zip(points1[:-1], points1[1:]):
                group1.add(Line(p1, p2, color=YELLOW, stroke_width=5))

            t_values2 = [i * 0.01 for i in range(1, 500) if i != 0]
            points2 = [
                axes.c2p(t, f(t).imag, f(t).real)
                for t in t_values2
                if not math.isnan(f(t).real) and not math.isnan(f(t).imag)
            ]
            for p1, p2 in zip(points2[:-1], points2[1:]):
                group1.add(Line(p1, p2, color=YELLOW, stroke_width=5))

            return VGroup(group1, group2)
        
        expgraph = always_redraw(graph)

        self.add(expgraph)

        for i in range(13):
            set_value = i * -0.5 + 3.0
            self.play(a_tracker.animate.set_value(set_value), run_time=2, rate_func=linear)
            self.wait(0.5)
        
        self.next_slide()