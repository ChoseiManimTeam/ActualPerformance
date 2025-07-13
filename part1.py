from manim import *
from manim_slides import Slide
import math
import cmath
import re

class MySlide1(Slide, ThreeDScene):
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
        self.SectionNum = 0 # 0~4
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
        ## １、虚数の説明
        #########################
        self.clear()
        eq1 = MathTex(r"i^2=-1").scale(2)
        self.play(Write(eq1))
        self.wait(1)
        eq2 = MathTex(r"\sqrt{-1}=i").scale(2).shift(DOWN)
        self.play(eq1.animate.shift(UP))
        self.play(Write(eq2))
        self.wait()
        self.next_slide()

        #########################
        ## ２、複素数の説明
        #########################
        self.play(FadeOut(eq1, eq2))
        # 数式表示（z = a + bi）
        eq3 = MathTex("z", "=", "a", "+", "b", "i").shift(UP)
        eq3.scale(2)
        self.play(Write(eq3))
        self.wait(1)
        # "a" と "b" のインデックスを取得
        a = eq3[2]
        b = eq3[4]
        arrow_a = Arrow(start=0.6 * DOWN, end=0.6 * UP, buff=0.1).next_to(a, DOWN, buff=0.1)
        label_a = Text("実部", font_size=30).next_to(arrow_a, DOWN, buff=0.1)
        arrow_b = Arrow(start=0.6 * DOWN, end=0.6 * UP, buff=0.1).next_to(b, DOWN, buff=0.1)
        label_b = Text("虚部", font_size=30).next_to(arrow_b, DOWN, buff=0.1)
        # 一斉に表示
        self.play(
            GrowArrow(arrow_a), FadeIn(label_a),
            GrowArrow(arrow_b), FadeIn(label_b)
        )
        self.wait()
        self.next_slide()

        #########################
        ## ３、足し算の説明
        #########################
        self.play(FadeOut(eq3, arrow_a, label_a, arrow_b, label_b))
        eq1 = MathTex(r"(2 - 3i) + (4 + i)").scale(1.5)
        eq2 = MathTex(r"= (2 + 4) + (-3 + 1)i").scale(1.5)
        eq3 = MathTex(r"= 6 - 2i").scale(1.5)
        # 行ごとに縦に並べる
        eq_group = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        # 1行ずつ順番に表示
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Write(eq2))
        self.wait(0.5)
        self.play(Write(eq3))
        self.wait()
        self.next_slide()

        #########################
        ## ４、掛け算の説明
        #########################
        self.play(FadeOut(eq1, eq2, eq3))
        eq1 = MathTex(r"(3+i)(2-3i)").scale(1.5)
        eq2 = MathTex(r"= 6-9i+2i-3{i}^2").scale(1.5)
        eq3 = MathTex(r"= 6-9i+2i+3").scale(1.5)
        eq4 = MathTex(r"= 9-7i").scale(1.5)
        # 行ごとに縦に並べる
        eq_group = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        # 1行ずつ順番に表示
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Write(eq2))
        self.wait(0.5)
        self.play(Write(eq3))
        self.wait(0.5)
        self.play(Write(eq4))
        self.wait()
        self.next_slide()

        #########################
        ## ５、複素数平面の説明
        #########################
        self.play(FadeOut(eq1, eq2, eq3, eq4))
        # 複素数平面の用意
        plane = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
            axis_config={"include_numbers": True}
        )
        plane.add_coordinates()
        self.play(Create(plane), run_time=2)
        self.wait(0.5)
        # 複素数 z = 3 + 2i
        z = complex(3, 2)
        point_pos = plane.c2p(z.real, z.imag)
        point = Dot(point_pos, color=YELLOW)
        label = MathTex("3 + 2i").next_to(point, UR, buff=0.2)
        self.play(FadeIn(point), Write(label))
        self.wait(0.5)
        # 複素数 z = -1 - 3i
        z = complex(-1, -3)
        point_pos = plane.c2p(z.real, z.imag)
        point = Dot(point_pos, color=YELLOW)
        label = MathTex("-1 - 3i").next_to(point, DL, buff=0.2)
        self.play(FadeIn(point), Write(label))
        self.wait()
        self.next_slide()

        #########################
        ## ６、極形式の説明
        #########################
        self.clear()
        # 複素数平面
        plane = ComplexPlane(
            x_range=[-1, 5],
            y_range=[-1, 5],
        )
        self.play(Create(plane), run_time=2)
        self.wait(0.5)
        # 複素数 z = sqrt(3) + 3i
        z = complex(np.sqrt(3), 3)
        point_pos = plane.c2p(z.real, z.imag)
        point = Dot(point_pos, color=YELLOW)
        # === 一般式ラベル ===
        label_gen = MathTex("(x, y)").next_to(point, UR, buff=0.2)
        line_h = plane.get_horizontal_line(point_pos)
        line_v = plane.get_vertical_line(point_pos)
        text_h_gen = MathTex("x").next_to(line_h, LEFT)
        text_v_gen = MathTex("y").next_to(line_v, DOWN)
        line_r = Line(plane.get_origin(), point_pos, color=GREEN_C)
        text_r_gen = MathTex("r", color=GREEN_C).scale(0.9)
        text_r_gen.move_to(line_r.get_center() + LEFT * 0.3 + UP * 0.5)
        angle = Angle(plane.get_x_axis(), line_r, color=RED_C)
        text_angle_gen = MathTex(r"\theta", color=RED_C).scale(0.9)
        text_angle_gen.move_to(angle.get_center() + RIGHT * 0.6 + UP * 0.35)
        self.play(FadeIn(point), Write(label_gen))
        self.play(Create(line_h), Create(line_v), Write(text_h_gen), Write(text_v_gen))
        self.play(Create(line_r), Create(angle))
        self.play(Write(text_r_gen), Write(text_angle_gen))
        self.wait(0.5)
        # すべてのグラフ構成要素を1つのグループにまとめる
        diagram_group = VGroup(
            plane, point, label_gen, line_h, line_v,
            text_h_gen, text_v_gen, line_r, text_r_gen,
            angle, text_angle_gen
        )
        # グラフ全体を少し小さくして画面下に移動
        self.play(diagram_group.animate.scale(0.96).to_edge(DOWN), run_time=1.5)
        self.wait(0.3)
        # === 数式（一般式）===
        eq1 = MathTex("x", "+", "y", "i", "=", "r", "(", "\\cos", "\\theta", "+", "i", "\\sin", "\\theta", ")")
        eq1.to_edge(UP)
        self.play(Write(eq1))
        self.wait()
        self.next_slide()

        #########################
        ## ７、極形式の具体例
        #########################
        # === 具体的なラベル ===
        label_val = MathTex(r"\left(\sqrt{3}, 3\right)").move_to(label_gen)
        text_h_val = MathTex("3").move_to(text_h_gen)
        text_v_val = MathTex(r"\sqrt{3}").move_to(text_v_gen)
        text_r_val = MathTex(r"2\sqrt{3}", color=GREEN_C).scale(0.9).move_to(text_r_gen)
        text_angle_val = MathTex(r"\frac{\pi}{3}", color=RED_C).scale(0.9).move_to(text_angle_gen)
        # 数式（具体式）
        eq2 = MathTex(
            r"\sqrt{3}", "+", "3", "i", "=",
            "2\sqrt{3}", "(", r"\cos", r"\frac{\pi}{3}",
            "+", "i", r"\sin", r"\frac{\pi}{3}", ")"
        )
        eq2.to_edge(UP)
        # === 一斉に変形 ===
        self.play(
            TransformMatchingTex(eq1, eq2),
            Transform(label_gen, label_val),
            Transform(text_h_gen, text_h_val),
            Transform(text_v_gen, text_v_val),
            Transform(text_r_gen, text_r_val),
            Transform(text_angle_gen, text_angle_val),
        )
        self.wait()
        self.next_slide()

        #########################
        ## ８、極座標の説明
        #########################
        self.clear()
        labels = {
            2: MathTex(r"\sqrt{3}"),
            4: MathTex(r"2\sqrt{3}")
        }
        polar = PolarPlane(
            azimuth_units="PI radians",
            size=9.5,
            azimuth_step=12,
            radius_step=2,
            azimuth_label_font_size=45,
            azimuth_label_buff=0.11,
            radius_config={"font_size": 33}
        ).add_coordinates([0]).move_to([0, -3.2, 0])
        polar.get_x_axis().add_labels(labels)
        self.play(Create(polar))
        self.wait(1)

        point = polar.polar_to_point(4, PI/3)

        dot = Dot(point, color=YELLOW)
        eq = MathTex(
            r"\sqrt{3}", "+", "3", "i", "=",
            "2\sqrt{3}", "(", r"\cos", r"\frac{\pi}{3}",
            "+", "i", r"\sin", r"\frac{\pi}{3}", ")"
        ).to_edge(UP)
        line_r = Line(polar.get_origin(), point, color=GREEN_C)
        text_r = MathTex(r"2\sqrt{3}", color=GREEN_C)
        text_r.move_to(line_r.get_center() + LEFT * 0.3 + UP * 0.5)
        angle = Angle(polar.get_x_axis(), line_r, color=RED_C)
        text_angle = MathTex(r"\frac{\pi}{3}", color=RED_C)
        text_angle.move_to(angle.get_center() + RIGHT * 0.6 + UP * 0.35)
        self.play(Create(line_r), Write(text_r), FadeIn(dot))
        self.play(Write(eq), Create(angle), Write(text_angle))
        self.next_slide()

        #########################
        ## ９、積・商の図形的意味
        #########################
        self.clear()
        polar = PolarPlane(
            azimuth_units="PI radians",
            size=9.5,
            azimuth_step=16,
            radius_step=1,
            azimuth_label_font_size=45,
            azimuth_label_buff=0.11,
            radius_config={"font_size": 33},
            azimuth_compact_fraction=False
        ).add_coordinates().move_to([0, -3.2, 0])
        self.play(Create(polar))
        self.wait(1)

        point_1 = polar.polar_to_point(2, 3*PI/8)
        dot_1 = Dot(point_1, color=YELLOW)
        label_1 = MathTex("z").next_to(dot_1, RIGHT)
        line_1 = Line(polar.get_origin(), point_1, color=GREEN_C)
        self.play(Create(line_1), Write(label_1), FadeIn(dot_1))
        self.wait(1)

        eq = MathTex(
            r"a=2(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4})"
        ).to_edge(UP)
        self.play(Write(eq))
        self.wait(1)

        self.next_slide()
        line_2 = line_1.copy()
        line_2.generate_target()
        start = line_2.get_start()
        end = line_2.get_end()
        direction = end - start
        new_end = start + 2 * direction
        line_2.target.put_start_and_end_on(start, new_end)
        line_2.target.rotate(PI/4, about_point=line_2.start)
        self.play(MoveToTarget(line_2))

        point_2 = polar.polar_to_point(4, 5*PI/8)
        dot_2 = Dot(point_2, color=YELLOW)
        label_2 = MathTex("za").next_to(dot_2, DR)
        self.play(FadeIn(dot_2), Write(label_2))

        angle_12 = Angle(line_1, line_2, color=RED_C, radius=0.6)
        label_angle12 = MathTex(r"\frac{\pi}{4}").next_to(angle_12, UP, SMALL_BUFF).scale(0.6)
        label_angle12.shift([0.2, 0, 0])
        self.play(Create(angle_12), Write(label_angle12))
        self.wait(1)
        
        self.next_slide()
        line_3 = line_1.copy()
        line_3.generate_target()
        start = line_3.get_start()
        end = line_3.get_end()
        direction = end - start
        new_end = start + 0.5 * direction
        line_3.target.put_start_and_end_on(start, new_end)
        line_3.target.rotate(-PI/4, about_point=line_3.start)
        self.play(MoveToTarget(line_3))

        point_3 = polar.polar_to_point(1, PI/8)
        dot_3 = Dot(point_3, color=YELLOW)
        label_3 = MathTex(r"\frac{z}{a}").next_to(dot_3, RIGHT).scale(0.9)
        label_3.shift([0, 0.1, 0])
        self.play(FadeIn(dot_3), Write(label_3))
        
        angle_13 = Angle(line_1, line_3, color=RED_C, other_angle=True)
        label_angle13 = MathTex(r"\frac{\pi}{4}").next_to(angle_13, UR, SMALL_BUFF).scale(0.6)
        label_angle13.shift([0, -0.2, 0])
        self.play(Create(angle_13), Write(label_angle13))
        self.wait(1)
        self.next_slide()

        #########################
        ## １０、ベクトルとの類似点１
        #########################
        self.clear()
        plane = NumberPlane(
            x_range=[-1, 5],
            y_range=[-1, 5],
        ).scale(0.96).to_edge(DOWN)
        plane.add_coordinates()

        eq1 = MathTex("z=1+2i")
        text = Text("のとき").scale(0.65)
        eq2 = MathTex("2z=2+4i")
        equation = VGroup(eq1, text, eq2).arrange(RIGHT, buff=0.4).to_edge(UP).scale(0.9)

        point1 = plane.c2p(1, 2)
        dot1 = Dot(point1, color=YELLOW)
        label1 = MathTex("z").next_to(dot1, UR, buff=0.1)

        point2 = plane.c2p(2, 4)
        dot2 = Dot(point2, color=YELLOW)
        label2 = MathTex("2z").next_to(dot2, UR, buff=0.1)

        self.play(Create(plane), Write(equation))
        self.play(FadeIn(dot1, label1))
        self.play(FadeIn(dot2, label2))
        self.wait()

        group1 = VGroup(plane, equation, dot1, label1, dot2, label2)

        self.play(group1.animate.scale(0.95).to_edge(LEFT, buff=0.8))

        group2 = group1.copy()
        group2.remove(*group2[2:6])  # ← この行で group2 から点とラベルを削除

        # 新しい数式を作成
        new_eq1 = MathTex(r"\vec{a}=(1, 2)").move_to(group2[1][0]).scale(0.9)
        new_eq2 = MathTex(r"2\vec{a}=(2, 4)").move_to(group2[1][2]).scale(0.9)

        self.wait(1)

        group2.generate_target()
        group2.target[1][0] = new_eq1
        group2.target[1][2] = new_eq2
        group2.target.to_edge(RIGHT, buff=0.8)

        # グループ全体を右端へ移動
        self.play(MoveToTarget(group2))
        self.wait()

        # group2[0] が plane（右側の座標平面）
        plane2 = group2[0]

        # ベクトルの始点と終点（座標をplaneに合わせて変換）
        start = plane2.c2p(0, 0)
        end = plane2.c2p(1, 2)

        # 矢印としてベクトルを描画（色や太さは自由に設定）
        vec_arrow = Arrow(start=start, end=end, buff=0, color=RED)
        vec_arrow.shift([-0.03, 0, 0])

        # ラベルも付ける（任意）
        vec_label = MathTex(r"\vec{a}").next_to(end, RIGHT, buff=0.2)

        # 描画
        self.play(GrowArrow(vec_arrow), FadeIn(vec_label))
        self.wait()

        # ベクトルの始点と終点（座標をplaneに合わせて変換）
        start = plane2.c2p(0, 0)
        end = plane2.c2p(2, 4)

        # 矢印としてベクトルを描画（色や太さは自由に設定）
        vec_arrow2 = Arrow(start=start, end=end, buff=0, color=GREEN)
        vec_arrow2.shift([0.03, 0, 0])

        # ラベルも付ける（任意）
        vec_label2 = MathTex(r"2\vec{a}").next_to(end, RIGHT, buff=0.2)

        # 描画
        self.play(GrowArrow(vec_arrow2), FadeIn(vec_label2))
        self.wait()
        self.next_slide()

        #########################
        ## １１、ベクトルとの類似点２
        #########################
        self.clear()
        plane = NumberPlane(
            x_range=[-1, 5],
            y_range=[-1, 5],
        ).scale(0.96).to_edge(DOWN)
        plane.add_coordinates()

        eq1 = MathTex(r"\alpha=1+2i,")
        eq2 = MathTex(r"\beta=2+i")
        text = Text("のとき").scale(0.65)
        eq3 = MathTex(r"\alpha+\beta=3+3i")
        eqUP = VGroup(eq1, eq2).arrange(RIGHT, buff=0.4).to_edge(UP, buff=0.4).scale(0.8)
        eqDW = VGroup(text, eq3).arrange(RIGHT, buff=0.4).next_to(eqUP, DOWN).scale(0.8)

        point1 = plane.c2p(1, 2)
        dot1 = Dot(point1, color=YELLOW)
        label1 = MathTex(r"\alpha").next_to(dot1, UR, buff=0.1)

        point2 = plane.c2p(2, 1)
        dot2 = Dot(point2, color=YELLOW)
        label2 = MathTex(r"\beta").next_to(dot2, UR, buff=0.1)

        point3 = plane.c2p(3, 3)
        dot3 = Dot(point3, color=YELLOW)
        label3 = MathTex(r"\alpha+\beta").next_to(dot3, UR, buff=0.1)

        self.play(Create(plane), Write(eqUP), Write(eqDW))
        self.play(FadeIn(dot1, label1, dot2, label2))
        self.play(FadeIn(dot3, label3))
        self.wait()

        group1 = VGroup(plane, eqUP, eqDW, dot1, label1, dot2, label2, dot3, label3)

        self.play(group1.animate.scale(0.95).to_edge(LEFT, buff=0.8))

        group2 = group1.copy()
        group2.remove(*group2[3:9])  # ← この行で group2 から点とラベルを削除

        # 新しい数式を作成
        new_eq1 = MathTex(r"\vec{a}=(1, 2),").move_to(group2[1][0]).scale(0.8)
        new_eq2 = MathTex(r"\vec{b}=(2, 1)").move_to(group2[1][1]).scale(0.8)
        new_eq3 = MathTex(r"\vec{a}+\vec{b}=(3, 3)").move_to(group2[2][1]).scale(0.8)

        # グループをシーンに追加（まだ表示していない場合）
        self.wait(1)

        group2.generate_target()
        group2.target[1][0] = new_eq1
        group2.target[1][1] = new_eq2
        group2.target[2][1] = new_eq3
        group2.target.to_edge(RIGHT, buff=0.8)

        # アニメーション：数式だけを滑らかに変化させる
        self.play(MoveToTarget(group2))
        self.wait()

        # group2[0] が plane（右側の座標平面）
        plane2 = group2[0]

        # ベクトルの始点と終点（座標をplaneに合わせて変換）
        start = plane2.c2p(0, 0)
        end1 = plane2.c2p(1, 2)
        end2 = plane2.c2p(2, 1)
        end3 = plane2.c2p(3, 3)

        # 矢印としてベクトルを描画（色や太さは自由に設定）
        vec_arrow1 = Arrow(start=start, end=end1, buff=0, color=RED)
        vec_arrow2 = Arrow(start=start, end=end2, buff=0, color=GREEN)
        vec_arrow3 = Arrow(start=start, end=end3, buff=0, color=YELLOW)

        vec_label1 = MathTex(r"\vec{a}").next_to(end1, UL, buff=0.1)
        vec_label2 = MathTex(r"\vec{b}").next_to(end2, UL, buff=0.1)
        vec_label3 = MathTex(r"\vec{a}+\vec{b}").next_to(end3, RIGHT, buff=0.2)

        # 描画
        self.play(GrowArrow(vec_arrow1), FadeIn(vec_label1))
        self.play(GrowArrow(vec_arrow2), FadeIn(vec_label2))

        dy = plane2.y_axis.get_unit_size()
        dx = plane2.x_axis.get_unit_size()
        self.play(VGroup(vec_arrow2, vec_label2).animate.shift(UP * dy * 2 + RIGHT * dx * 1))

        self.play(GrowArrow(vec_arrow3), FadeIn(vec_label3))
        self.wait()

        # 描画
        self.wait()
        self.next_slide()

        #########################
        ## １２、ベクトルとの相違点
        #########################
        self.clear()
        title = Text("複素数とベクトルの相違点").to_edge(UP)
        self.play(FadeIn(title))

        text1 = Text("１．複素数には掛け算と割り算がある")
        text2 = Text("２．複素数は代数方程式の解となる")
        text3 = Text("３．ベクトルは簡単に次元を増やせる")
        VGroup(text1, text2, text3).arrange(DOWN, buff=1.0, aligned_edge=LEFT)

        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.play(FadeIn(text3))
        self.wait()
        self.next_slide()

        #########################
        ## １３、複素関数の概要
        #########################
        self.clear()
        eq1 = MathTex(r"f(x)=x^2").scale(1.2)
        eq2 = MathTex(r"f(z)=z^2").scale(1.2)
        text1 = Text("実関数")
        text2 = Text("複素関数")
        symbol1 = MathTex(r"\dots")
        symbol2 = MathTex(r"\dots")

        VGroup(eq1, eq2).arrange(DOWN, buff=2.0, aligned_edge=LEFT).shift(LEFT * 2)
        VGroup(text1, text2).arrange(DOWN, buff=2.0, aligned_edge=LEFT).shift(RIGHT * 2)
        VGroup(symbol1, symbol2).arrange(DOWN, buff=2.6)

        self.play(FadeIn(eq1))
        self.play(FadeIn(eq2))
        self.play(FadeIn(text1, symbol1))
        self.play(FadeIn(text2, symbol2))
        self.wait()
        self.next_slide()

        #########################
        ## １４、複素関数 f(z)=z^2 の表
        #########################
        self.clear()
        func = MathTex(r"f(z)=z^2").to_edge(UP).scale(1.5)
        self.play(FadeIn(func))

        table = MathTable(
            [["2", "-i", "2-i", "1+i", "-1+2i"],
            ["4", "-1", "3-4i", "2i", "-3-4i"]],
            row_labels=[MathTex("z"), MathTex("f(z)")],)
        self.play(FadeIn(table))
        self.wait()
        self.next_slide()

        #########################
        ## １５、点のプロット
        #########################
        tablec = table.copy().scale(0.6)
        funcc = func.copy().scale(0.7)
        VGroup(funcc, tablec).arrange(RIGHT, buff=1.5).to_edge(UP, buff=0.5)

        self.play(Transform(table, tablec), Transform(func, funcc))
        infield = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4]
            ).scale(0.65).add_coordinates()
        outfield = ComplexPlane(
            x_range=[-4, 4],
            y_range=[-4, 4]
            ).scale(0.65).add_coordinates()
        VGroup(infield, outfield).arrange(RIGHT).to_edge(DOWN, buff=0.5)
        self.play(Create(infield), Create(outfield))
        self.wait()

        def plotdot(invalue, outvalue, color):
            indot = Dot(infield.n2p(invalue), color=color)
            outdot = Dot(outfield.n2p(outvalue), color=color)
            self.play(FadeIn(indot))
            self.play(FadeIn(outdot))
            self.wait()

        def parce_complex(s: str) -> str:
            s = s.strip().replace(" ", "").replace("−", "-").replace("＋", "+")
            s = s.replace("i", "j")

            # 補完：+j → +1j、-j → -1j、^ jの前に数字がない場合
            s = re.sub(r'(?<=[^\d])([+-])j', r'\g<1>1j', s)  # "+j" → "+1j", "-j" → "-1j"
            s = re.sub(r'^([+-]?)j', r'\g<1>1j', s)          # "j" or "-j" at the start

            # 「jだけ」の場合（例："j", "-j", "+j"）を "0+1j" にする
            if re.fullmatch(r'[+-]?1j', s):
                s = "0+" + s if not s.startswith("-") else "0" + s

            return complex(s)
        
        colorlist = [YELLOW, GREEN, RED, BLUE, PURPLE]
        dots = VGroup()
        
        def plotdot(inobj, outobj, color):
            intex = inobj.get_tex_string()
            outtex = outobj.get_tex_string()
            indot = Dot(infield.n2p(parce_complex(intex)), color=color)
            outdot = Dot(outfield.n2p(parce_complex(outtex)), color=color)
            dots.add(indot, outdot)
            anim1 = TransformFromCopy(inobj, indot)
            anim2 = TransformFromCopy(outobj, outdot)
            self.play(LaggedStart(anim1, anim2, lag_ratio=0.3))
            self.wait(0.1)

        for i in range(1, 6):
            group = table.get_columns()[i]
            plotdot(group[0], group[1], colorlist[i-1])

        self.wait()
        self.next_slide()

        #########################
        ## １６、規則的な点のプロット
        #########################
        self.play(FadeOut(dots))
        dots = VGroup()
        
        table2 = MathTable(
            [["-2+i", "-1+i", "i", "1+i", "2+i"],
            ["3-4i", "-2i", "-1", "2i", "3+4i"]],
            row_labels=[MathTex("z"), MathTex("f(z)")],)
        table2.scale(0.6).move_to(table).shift([-0.5, 0, 0])
        self.play(Transform(table, table2))
        self.wait()

        for i in range(1, 6):
            group = table2.get_columns()[i]
            plotdot(group[0], group[1], colorlist[i-1])
        
        self.wait()
        self.next_slide()

        self.play(FadeOut(table, dots))

        def infunc(t):
            real = t
            imag = 1
            return infield.n2p(complex(real, imag))
        
        def outfunc(t):
            real = t**2-1
            imag = 2*t
            return outfield.n2p(complex(real, imag))

        incurve = ParametricFunction(
            infunc,
            t_range=[-4, 4],
            color=YELLOW
        )

        outcurve = ParametricFunction(
            outfunc,
            t_range=[-2, 2],
            color=YELLOW
        )

        self.play(Create(incurve), Create(outcurve))
        self.wait()
        self.next_slide()

        self.play(FadeOut(incurve, outcurve))

        def infunc(t):
            real = 1
            imag = t
            return infield.n2p(complex(real, imag))
        
        def outfunc(t):
            real = 1-t**2
            imag = 2*t
            return outfield.n2p(complex(real, imag))

        incurve = ParametricFunction(
            infunc,
            t_range=[-4, 4],
            color=YELLOW
        )

        outcurve = ParametricFunction(
            outfunc,
            t_range=[-2, 2],
            color=YELLOW
        )

        self.play(Create(incurve), Create(outcurve))
        self.wait()
        self.next_slide()