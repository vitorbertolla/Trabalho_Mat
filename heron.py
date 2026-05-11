from manim import *

class DeducaoHeron(Scene):
    def construct(self):

        # -----------------------------
        # TÍTULO
        # -----------------------------
        titulo = Text(
            "Dedução da Fórmula de Heron",
            font_size=38,
            color=MAROON
        ).to_edge(UP)

        self.play(Write(titulo))
        self.wait(1)

        # -----------------------------
        # TRIÂNGULO — posicionado à esquerda para deixar espaço para equações
        # -----------------------------
        escala = 0.75
        A = UP * 2   * escala
        B = LEFT * 3 * escala + DOWN * 1.5 * escala
        C = RIGHT * 3 * escala + DOWN * 1.5 * escala
        H = np.array([0, -1.5 * escala, 0])

        # Grupo do triângulo deslocado para a esquerda
        offset = LEFT * 2.5

        A += offset
        B += offset
        C += offset
        H += offset

        triangulo = Polygon(B, A, C, color=RED)
        altura = DashedLine(A, H, color=YELLOW)

        labelA = MathTex("A", font_size=28).next_to(A, UP, buff=0.1)
        labelB = MathTex("B", font_size=28).next_to(B, LEFT, buff=0.1)
        labelC = MathTex("C", font_size=28).next_to(C, RIGHT, buff=0.1)
        labelH = MathTex("H", font_size=28).next_to(H, DOWN, buff=0.1)

        labela = MathTex("a", font_size=26).next_to(Line(B, C).get_center(), DOWN)
        labelb = MathTex("b", font_size=26).next_to(Line(A, C).get_center(), RIGHT, buff=0.1)
        labelc = MathTex("c", font_size=26).next_to(Line(A, B).get_center(), LEFT, buff=0.1)

        labelx  = MathTex("x",   font_size=24).next_to(Line(B, H).get_center(), DOWN)
        labelax = MathTex("a{-}x", font_size=24).next_to(Line(H, C).get_center(), DOWN)
        labelh  = MathTex("h",   font_size=24).next_to(altura.get_center(), RIGHT, buff=0.1)

        grupo_triangulo = VGroup(
            triangulo, altura,
            labelA, labelB, labelC, labelH,
            labela, labelb, labelc,
            labelx, labelax, labelh,
        )

        self.play(Create(triangulo))
        self.play(Create(altura))
        self.play(
            Write(labelA), Write(labelB), Write(labelC), Write(labelH),
            Write(labela), Write(labelb), Write(labelc),
            Write(labelx),  Write(labelax),  Write(labelh),
        )
        self.wait(2)

        # -----------------------------
        # PITÁGORAS — coluna da direita
        # -----------------------------
        eq1 = MathTex(r"(I)\quad c^2 = h^2 + x^2", font_size=30)
        eq2 = MathTex(r"(II)\quad b^2 = h^2 + (a-x)^2", font_size=30)

        grupo_pit = VGroup(eq1, eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        grupo_pit.to_corner(RIGHT + DOWN).shift(UP * 0.3)

        self.play(Write(grupo_pit))
        self.wait(2)

        # -----------------------------
        # SUBSTITUIÇÃO — coluna da direita, acima de Pitágoras
        # -----------------------------
        sub1 = MathTex(r"h^2 = c^2 - x^2", font_size=28)
        sub2 = MathTex(r"b^2 = c^2 - x^2 + (a-x)^2", font_size=28)
        sub3 = MathTex(r"b^2 = c^2 - x^2 + a^2 - 2ax + x^2", font_size=28)
        sub4 = MathTex(r"2ax = a^2 - b^2 + c^2", font_size=28)
        sub5 = MathTex(r"x = \dfrac{a^2 - b^2 + c^2}{2a}", font_size=30)

        grupo_sub = VGroup(sub1, sub2, sub3, sub4, sub5).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        )
        # Posiciona acima das equações de Pitágoras, alinhado à direita
        grupo_sub.next_to(grupo_pit, UP, buff=0.4, aligned_edge=LEFT)
        # Garante que não saia da tela pelo topo
        if grupo_sub.get_top()[1] > titulo.get_bottom()[1] - 0.15:
            grupo_sub.shift(DOWN * (grupo_sub.get_top()[1] - titulo.get_bottom()[1] + 0.15))

        self.play(Write(sub1))
        self.wait(0.8)
        self.play(Write(sub2))
        self.wait(0.8)
        self.play(Write(sub3))
        self.wait(0.8)
        self.play(Write(sub4))
        self.wait(0.8)
        self.play(Write(sub5))
        self.wait(2)

        # -----------------------------
        # EXPRESSÃO DE h² — limpa a direita, mantém triângulo
        # -----------------------------
        self.play(FadeOut(grupo_pit), FadeOut(grupo_sub))

        h_eq = MathTex(
            r"h^2 = c^2 - \left(\dfrac{a^2 - b^2 + c^2}{2a}\right)^2",
            font_size=32,
        )
        h_eq2 = MathTex(
            r"h^2 = \dfrac{4a^2c^2 - (a^2 - b^2 + c^2)^2}{4a^2}",
            font_size=32,
        )

        grupo_h = VGroup(h_eq, h_eq2).arrange(DOWN, buff=0.5)
        # Posiciona na metade direita da tela, abaixo do título
        grupo_h.move_to(RIGHT * 2.2 + DOWN * 0.5)
        # Ajusta se necessário para não colidir com o triângulo
        grupo_h.shift(UP * 0.2)

        self.play(Write(h_eq))
        self.wait(2)
        self.play(Write(h_eq2))
        self.wait(2)

        # -----------------------------
        # ÁREA — limpa tudo, começa nova seção centralizada
        # -----------------------------
        self.play(
            FadeOut(grupo_triangulo),
            FadeOut(h_eq),
        )

        area1 = MathTex(r"A = \dfrac{a \cdot h}{2}", font_size=38)
        area2 = MathTex(r"A^2 = \dfrac{a^2 h^2}{4}", font_size=38)
        area3 = MathTex(
            r"A^2 = \dfrac{4a^2c^2 - (a^2 - b^2 + c^2)^2}{16}",
            font_size=34,
        )

        grupo_area = VGroup(area1, area2, area3).arrange(DOWN, buff=0.55)
        grupo_area.move_to(DOWN * 0.3)

        self.play(Write(area1))
        self.wait(1)
        self.play(Write(area2))
        self.wait(1)
        self.play(Write(area3))
        self.wait(2)

        # -----------------------------
        # FATORAÇÃO
        # -----------------------------
        fator1 = MathTex(
            r"A^2 = \dfrac{(2ac)^2 - (a^2 - b^2 + c^2)^2}{16}",
            font_size=34,
        )
        fator2 = MathTex(
            r"A^2 = \dfrac{[2ac + (a^2-b^2+c^2)]\,[2ac - (a^2-b^2+c^2)]}{16}",
            font_size=28,
        )
        fator3 = MathTex(
            r"A^2 = \dfrac{[(a+c)^2 - b^2]\,[b^2 - (a-c)^2]}{16}",
            font_size=32,
        )

        grupo_fator = VGroup(fator1, fator2, fator3).arrange(DOWN, buff=0.5)
        grupo_fator.move_to(DOWN * 0.3)

        self.play(FadeOut(grupo_area), FadeOut(h_eq2))
        self.play(Write(fator1))
        self.wait(2)
        self.play(Write(fator2))
        self.wait(2)
        self.play(Write(fator3))
        self.wait(2)

        # -----------------------------
        # EXPRESSÃO FINAL — limpa tudo, exibe em duas linhas
        # -----------------------------
        self.play(FadeOut(grupo_fator))

        final1 = MathTex(
            r"A^2 = \frac{(a+c-b)}{2}"
            r"\cdot \frac{(a-c+b)}{2}"
            r"\cdot \frac{(-a+c+b)}{2}"
            r"\cdot \frac{(a+b+c)}{2}",
            font_size=30,
        )
        final1.move_to(UP * 0.5)

        self.play(Write(final1))
        self.wait(3)

        # -----------------------------
        # DEFINIÇÃO DE p e FÓRMULA DE HERON
        # -----------------------------
        definicao = MathTex(r"p = \dfrac{a+b+c}{2}", font_size=36)

        heron = MathTex(
            r"\boxed{A = \sqrt{p(p-a)(p-b)(p-c)}}",
            font_size=38,
        ).set_color(YELLOW)

        grupo_final = VGroup(definicao, heron).arrange(DOWN, buff=0.7)
        grupo_final.next_to(final1, DOWN, buff=0.6)

        # Empurra para baixo se sair da tela
        if grupo_final.get_bottom()[1] < -3.6:
            grupo_final.shift(UP * (abs(grupo_final.get_bottom()[1]) - 3.6))

        self.play(Write(definicao))
        self.wait(1)
        self.play(Write(heron))
        self.wait(3)

        self.play(Circumscribe(heron, color=YELLOW, run_time=2))
        self.wait(3)