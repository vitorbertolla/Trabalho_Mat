from manim import *
import numpy as np

class DeducaoHeron(Scene):
    def construct(self):

        # ---------------------------------------------------
        # TÍTULO
        # ---------------------------------------------------

        titulo = Text(
            "Dedução da Fórmula de Heron",
            font_size=40
        )

        self.play(Write(titulo))
        self.wait(1)

        # CORREÇÃO DO ERRO
        self.play(titulo.animate.to_edge(UP))

        # ---------------------------------------------------
        # TRIÂNGULO
        # ---------------------------------------------------

        A = np.array([-3, 2, 0])
        B = np.array([-5, -2, 0])
        C = np.array([3, -2, 0])
        H = np.array([-3, -2, 0])

        triangulo = Polygon(
            A, B, C,
            color=WHITE
        )

        altura = DashedLine(
            A, H,
            color=YELLOW
        )

        # Labels dos pontos
        labelA = MathTex("A").next_to(A, UP)
        labelB = MathTex("B").next_to(B, DOWN)
        labelC = MathTex("C").next_to(C, DOWN)
        labelH = MathTex("H").next_to(H, DOWN)

        # Labels dos lados
        h_label = MathTex("h").next_to(altura, LEFT)

        x_label = MathTex("x").next_to(
            (B + H) / 2,
            DOWN
        )

        ax_label = MathTex("a-x").next_to(
            (H + C) / 2,
            DOWN
        )

        a_label = MathTex("a").next_to(
            Line(B, C),
            DOWN
        )

        b_label = MathTex("b").next_to(
            Line(A, C).get_center(),
            RIGHT
        )

        c_label = MathTex("c").next_to(
            Line(A, B).get_center(),
            LEFT
        )

        self.play(Create(triangulo))
        self.play(Create(altura))

        self.play(
            Write(labelA),
            Write(labelB),
            Write(labelC),
            Write(labelH),
        )

        self.play(
            Write(h_label),
            Write(x_label),
            Write(ax_label),
            Write(a_label),
            Write(b_label),
            Write(c_label),
        )

        self.wait(2)

        # ---------------------------------------------------
        # EQUAÇÃO I
        # ---------------------------------------------------

        eq1 = MathTex(
            r"(I)\quad c^2 = h^2 + x^2",
            r"\Rightarrow",
            r"h^2 = c^2 - x^2"
        ).scale(0.8)

        eq1.to_corner(UR)

        self.play(Write(eq1))
        self.wait(2)

        # ---------------------------------------------------
        # EQUAÇÃO II
        # ---------------------------------------------------

        eq2 = MathTex(
            r"(II)\quad b^2 = h^2 + (a-x)^2"
        ).scale(0.8)

        eq2.next_to(eq1, DOWN, aligned_edge=LEFT)

        self.play(Write(eq2))
        self.wait(2)

        # Substituição
        substituicao = MathTex(
            r"b^2 = c^2 - x^2 + (a-x)^2"
        ).scale(0.8)

        substituicao.next_to(
            eq2,
            DOWN,
            aligned_edge=LEFT
        )

        self.play(Write(substituicao))
        self.wait(1)

        # Expansão
        expansao1 = MathTex(
            r"= c^2 - x^2 + a^2 - 2ax + x^2"
        ).scale(0.8)

        expansao1.next_to(
            substituicao,
            DOWN,
            aligned_edge=LEFT
        )

        self.play(Write(expansao1))
        self.wait(1)

        # Resultado x
        resultado_x = MathTex(
            r"\Rightarrow x = \frac{a^2 - b^2 + c^2}{2a}"
        ).scale(0.8)

        resultado_x.next_to(
            expansao1,
            DOWN,
            aligned_edge=LEFT
        )

        self.play(Write(resultado_x))
        self.wait(3)

        # ---------------------------------------------------
        # SUBSTITUIÇÃO EM h²
        # ---------------------------------------------------

        self.play(
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(substituicao),
            FadeOut(expansao1),
            FadeOut(resultado_x),
        )

        substitui_h = MathTex(
            r"h^2 = c^2 - \left(",
            r"\frac{a^2 - b^2 + c^2}{2a}",
            r"\right)^2"
        ).scale(0.75)

        substitui_h.to_edge(LEFT)

        self.play(Write(substitui_h))
        self.wait(2)

        eq_h2 = MathTex(
            r"\Rightarrow h^2 =",
            r"\frac{4a^2c^2 - (a^2 - b^2 + c^2)^2}{4a^2}"
        ).scale(0.75)

        eq_h2.next_to(substitui_h, DOWN)

        self.play(Write(eq_h2))
        self.wait(3)

        # ---------------------------------------------------
        # ÁREA
        # ---------------------------------------------------

        area1 = MathTex(
            r"A = \frac{a \cdot h}{2}"
        ).scale(0.8)

        area1.to_edge(RIGHT)

        self.play(Write(area1))
        self.wait(1)

        area2 = MathTex(
            r"A^2 = \frac{a^2 h^2}{4}"
        ).scale(0.8)

        area2.next_to(area1, DOWN)

        self.play(Write(area2))
        self.wait(2)

        # ---------------------------------------------------
        # SUBSTITUIÇÃO FINAL
        # ---------------------------------------------------

        final1 = MathTex(
            r"A^2 =",
            r"\frac{(2ac)^2 - (a^2 - b^2 + c^2)^2}{16}"
        ).scale(0.7)

        final1.to_edge(DOWN)

        self.play(Write(final1))
        self.wait(3)

        # Fatoração
        fatoracao = MathTex(
            r"A^2 =",
            r"\frac{[2ac+(a^2-b^2+c^2)]",
            r"[2ac-(a^2-b^2+c^2)]}{16}"
        ).scale(0.65)

        fatoracao.next_to(final1, UP)

        self.play(Write(fatoracao))
        self.wait(3)

        # ---------------------------------------------------
        # FÓRMULA DE HERON
        # ---------------------------------------------------

        self.play(
            FadeOut(final1),
            FadeOut(fatoracao),
        )

        heron = MathTex(
            r"A^2 = p(p-a)(p-b)(p-c)"
        ).scale(1.1)

        heron.set_color(YELLOW)

        definicao_p = MathTex(
            r"p = \frac{a+b+c}{2}"
        ).scale(0.9)

        definicao_p.next_to(
            heron,
            DOWN
        )

        self.play(Write(heron))
        self.play(Write(definicao_p))

        self.wait(5)