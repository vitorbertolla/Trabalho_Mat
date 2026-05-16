from manim import *

# ── Paleta ────────────────────────────────────────────────────────────────────
COR_TITULO    = MAROON
COR_TRIANGULO = RED
COR_ALTURA    = YELLOW
COR_DEST      = GOLD
COR_FINAL     = GREEN_B
FUNDO         = "#0f0f1a"


class DeducaoHeron(Scene):

    # ── helpers ───────────────────────────────────────────────────────────────
    def tit(self, txt, size=34, cor=COR_TITULO):
        return Text(txt, font_size=size, color=cor, weight=BOLD)

    def eq(self, latex, size=30, cor=WHITE):
        return MathTex(latex, font_size=size, color=cor)

    def caixa(self, mob, cor=COR_DEST, pad=0.22):
        return SurroundingRectangle(mob, color=cor, buff=pad, corner_radius=0.07)

    # ── construtor do triangulo ───────────────────────────────────────────────
    def _build_triangle(self, escala=0.78, offset=LEFT * 2.8):
        A = UP * 2   * escala + offset
        B = LEFT * 3 * escala + DOWN * 1.5 * escala + offset
        C = RIGHT * 3 * escala + DOWN * 1.5 * escala + offset
        H = np.array([offset[0], -1.5 * escala, 0])

        tri   = Polygon(B, A, C, color=COR_TRIANGULO, stroke_width=2.5)
        alt   = DashedLine(A, H, color=COR_ALTURA, stroke_width=2)
        ang_r = RightAngle(Line(B, H), Line(H, A), length=0.18, color=WHITE)

        lA = MathTex("A", font_size=26).next_to(A, UP,    buff=0.12)
        lB = MathTex("B", font_size=26).next_to(B, LEFT,  buff=0.12)
        lC = MathTex("C", font_size=26).next_to(C, RIGHT, buff=0.12)

        la  = MathTex("a",     font_size=24).next_to(Line(B, C).get_center(), DOWN,  buff=0.22)
        lb  = MathTex("b",     font_size=24).next_to(Line(A, C).get_center(), RIGHT, buff=0.12)
        lc  = MathTex("c",     font_size=24).next_to(Line(A, B).get_center(), LEFT,  buff=0.12)
        lx  = MathTex("x",     font_size=22).next_to(Line(B, H).get_center(), DOWN,  buff=0.14)
        lax = MathTex("a{-}x", font_size=20).next_to(Line(H, C).get_center(), DOWN,  buff=0.14)
        lh  = MathTex("h",     font_size=22).next_to(alt.get_center(),        RIGHT, buff=0.10)

        grupo = VGroup(tri, alt, ang_r, lA, lB, lC, la, lb, lc, lx, lax, lh)
        return grupo

    # ══════════════════════════════════════════════════════════════════════════
    def construct(self):
        self.camera.background_color = FUNDO
        self._cena_titulo()
        self._cena_triangulo()
        self._cena_pitagoras()
        self._cena_isola_x()
        self._cena_h2()
        self._cena_area()
        self._cena_fatoracao()
        self._cena_heron()

    # ══════════════════════════════════════════════════════════════════════════
    # 1. TITULO
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_titulo(self):
        t1 = self.tit("Formula de Heron", size=40, cor=COR_DEST)
        t2 = self.tit("Deducao Completa", size=28, cor=WHITE)
        t2.next_to(t1, DOWN, buff=0.3)
        grupo = VGroup(t1, t2).center()

        self.play(FadeIn(grupo, shift=UP, run_time=1.2))
        self.wait(2)
        self.play(FadeOut(grupo))

    # ══════════════════════════════════════════════════════════════════════════
    # 2. TRIANGULO
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_triangulo(self):
        titulo = self.tit("Triangulo com altura h", cor=COR_TITULO)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo))

        self._tri = self._build_triangle()

        self.play(Create(self._tri[0]))                              # triangulo
        self.play(
            Write(self._tri[3]), Write(self._tri[4]), Write(self._tri[5]),   # A B C
            Write(self._tri[6]), Write(self._tri[7]), Write(self._tri[8]),   # a b c
        )
        self.play(Create(self._tri[1]), Create(self._tri[2]))        # altura + angulo reto
        self.play(
            Write(self._tri[9]),    # x
            Write(self._tri[10]),   # a-x
            Write(self._tri[11]),   # h
        )
        self.wait(2)
        self.play(FadeOut(titulo))

    # ══════════════════════════════════════════════════════════════════════════
    # 3. PITAGORAS
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_pitagoras(self):
        titulo = self.tit("Teorema de Pitagoras", cor=COR_TITULO)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo))

        self._eq1 = self.eq(r"(I)\quad c^2 = h^2 + x^2",      size=28)
        self._eq2 = self.eq(r"(II)\quad b^2 = h^2 + (a-x)^2", size=28)
        grupo = VGroup(self._eq1, self._eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        grupo.to_edge(RIGHT, buff=0.6).shift(DOWN * 0.5)

        self.play(Write(self._eq1))
        self.wait(1)
        self.play(Write(self._eq2))
        self.wait(2.5)

        # FadeOut apenas do titulo — as equacoes ficam para a proxima cena
        self.play(FadeOut(titulo))

    # ══════════════════════════════════════════════════════════════════════════
    # 4. ISOLA x
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_isola_x(self):
        titulo = self.tit("Isolando x", cor=COR_TITULO)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo))

        # Move eq I e II para cima como referencia, e apaga o triangulo
        self.play(
            FadeOut(self._tri),
            self._eq1.animate.scale(0.85).to_corner(UL).shift(DOWN * 0.8 + RIGHT * 0.1),
            self._eq2.animate.scale(0.85).to_corner(UL).shift(DOWN * 1.5 + RIGHT * 0.1),
        )
        self.wait(0.3)

        passos = VGroup(
            self.eq(r"h^2 = c^2 - x^2",                   size=28, cor=BLUE_B),
            self.eq(r"b^2 = (c^2 - x^2) + (a-x)^2",       size=28),
            self.eq(r"b^2 = c^2 - x^2 + a^2 - 2ax + x^2", size=28),
            self.eq(r"b^2 = c^2 + a^2 - 2ax",              size=28),
            self.eq(r"2ax = a^2 + c^2 - b^2",              size=28),
            self.eq(r"x = \frac{a^2 + c^2 - b^2}{2a}",    size=32, cor=COR_DEST),
        )
        passos.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        passos.to_edge(RIGHT, buff=0.6)
        # Garante que nao ultrapassa o titulo
        if passos.get_top()[1] > titulo.get_bottom()[1] - 0.1:
            passos.shift(DOWN * (passos.get_top()[1] - titulo.get_bottom()[1] + 0.12))

        for p in passos:
            self.play(Write(p, run_time=0.65))
            self.wait(0.5)

        cx = self.caixa(passos[-1], cor=COR_DEST)
        self.play(Create(cx))
        self.wait(2)

        # Limpa TUDO: titulo, referencias I e II, passos intermediarios, caixa
        self.play(
            FadeOut(titulo),
            FadeOut(self._eq1),
            FadeOut(self._eq2),
            FadeOut(cx),
            FadeOut(passos[0]),
            FadeOut(passos[1]),
            FadeOut(passos[2]),
            FadeOut(passos[3]),
            FadeOut(passos[4]),
        )
        # Guarda apenas o resultado final de x
        self._x_expr = passos[5]

    # ══════════════════════════════════════════════════════════════════════════
    # 5. CALCULO DE h²
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_h2(self):
        titulo = self.tit("Calculando h^2", cor=COR_TITULO)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo))

        # Move x para o canto superior esquerdo como referencia
        self.play(
            self._x_expr.animate.scale(0.82).to_corner(UL).shift(DOWN * 0.8 + RIGHT * 0.1)
        )

        ref_h = self.eq(r"h^2 = c^2 - x^2", size=24, cor=BLUE_B)
        ref_h.next_to(self._x_expr, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(ref_h))
        self.wait(0.4)

        passos = VGroup(
            self.eq(r"h^2 = c^2 - \left(\frac{a^2+c^2-b^2}{2a}\right)^2",  size=28),
            self.eq(r"h^2 = \frac{4a^2c^2 - (a^2+c^2-b^2)^2}{4a^2}",       size=28),
        )
        passos.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        passos.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.2)

        self.play(Write(passos[0]))
        self.wait(1.5)
        self.play(Write(passos[1]))
        self.wait(2)

        cx = self.caixa(passos[1], cor=BLUE_B)
        self.play(Create(cx))
        self.wait(1.5)

        # Limpa tudo exceto o resultado h^2
        self.play(
            FadeOut(titulo),
            FadeOut(self._x_expr),
            FadeOut(ref_h),
            FadeOut(passos[0]),
            FadeOut(cx),
        )
        self._h2_expr = passos[1]

    # ══════════════════════════════════════════════════════════════════════════
    # 6. AREA
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_area(self):
        titulo = self.tit("Area em funcao de a, b, c", cor=COR_TITULO)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo))

        # h^2 vai para o canto como referencia
        self.play(
            self._h2_expr.animate.scale(0.78).to_corner(UL).shift(DOWN * 0.8 + RIGHT * 0.1)
        )

        passos = VGroup(
            self.eq(r"A = \frac{a \cdot h}{2}",                                       size=34),
            self.eq(r"A^2 = \frac{a^2 h^2}{4}",                                       size=34),
            self.eq(r"A^2 = \frac{a^2}{4}\cdot\frac{4a^2c^2-(a^2+c^2-b^2)^2}{4a^2}", size=26),
            self.eq(r"A^2 = \frac{4a^2c^2 - (a^2+c^2-b^2)^2}{16}",                   size=30),
        )
        passos.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        passos.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.1)

        for p in passos:
            self.play(Write(p, run_time=0.8))
            self.wait(0.8)

        cx = self.caixa(passos[-1], cor=COR_DEST)
        self.play(Create(cx))
        self.wait(2)

        # Limpa tudo exceto o A^2 final
        self.play(
            FadeOut(titulo),
            FadeOut(self._h2_expr),
            FadeOut(passos[0]),
            FadeOut(passos[1]),
            FadeOut(passos[2]),
            FadeOut(cx),
        )
        self._a2_expr = passos[3]

    # ══════════════════════════════════════════════════════════════════════════
    # 7. FATORACAO
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_fatoracao(self):
        titulo = self.tit("Fatoracao por diferenca de quadrados", cor=COR_TITULO)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo))

        # A^2 sobe para topo como ponto de partida
        self.play(
            self._a2_expr.animate.scale(0.82).next_to(titulo, DOWN, buff=0.3)
        )
        self.wait(0.5)

        fat1 = self.eq(r"A^2 = \frac{(2ac)^2 - (a^2+c^2-b^2)^2}{16}", size=30)
        fat1.next_to(self._a2_expr, DOWN, buff=0.4)
        self.play(Write(fat1))
        self.wait(1.5)

        fat2 = self.eq(
            r"A^2 = \frac{[2ac+(a^2+c^2-b^2)]\,[2ac-(a^2+c^2-b^2)]}{16}",
            size=26,
        )
        fat2.next_to(fat1, DOWN, buff=0.4)
        self.play(Write(fat2))
        self.wait(1.5)

        fat3 = self.eq(
            r"A^2 = \frac{[(a+c)^2-b^2]\,[b^2-(a-c)^2]}{16}",
            size=30,
        )
        fat3.next_to(fat2, DOWN, buff=0.4)
        self.play(Write(fat3))
        self.wait(2)

        cx = self.caixa(fat3, cor=COR_DEST)
        self.play(Create(cx))
        self.wait(1.5)

        # Limpa tudo exceto fat3
        self.play(
            FadeOut(titulo),
            FadeOut(self._a2_expr),
            FadeOut(fat1),
            FadeOut(fat2),
            FadeOut(cx),
        )
        self._fat3 = fat3

    # ══════════════════════════════════════════════════════════════════════════
    # 8. FORMULA DE HERON
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_heron(self):
        titulo = self.tit("Formula de Heron", cor=COR_TITULO)
        titulo.to_edge(UP, buff=0.35)
        self.play(Write(titulo))

        # fat3 sobe como referencia
        self.play(self._fat3.animate.next_to(titulo, DOWN, buff=0.35))
        self.wait(0.5)

        # Segunda fatoracao: 4 fatores lineares
        prod4 = self.eq(
            r"A^2 = \frac{(a+b+c)(-a+b+c)(a-b+c)(a+b-c)}{16}",
            size=28,
        )
        prod4.next_to(self._fat3, DOWN, buff=0.4)
        self.play(Write(prod4))
        self.wait(2)

        # Cada fator dividido por 2
        final_a2 = self.eq(
            r"A^2 = \frac{a+b+c}{2}"
            r"\cdot\frac{-a+b+c}{2}"
            r"\cdot\frac{a-b+c}{2}"
            r"\cdot\frac{a+b-c}{2}",
            size=26,
        )
        final_a2.next_to(prod4, DOWN, buff=0.4)
        self.play(Write(final_a2))
        self.wait(2)

        # Limpa para a parte do semiperim.
        self.play(
            FadeOut(titulo),
            FadeOut(self._fat3),
            FadeOut(prod4),
            FadeOut(final_a2),
        )

        # ── Definicao de p e formula final ────────────────────────────────────
        titulo2 = self.tit("Semiperim. p e formula final", cor=COR_TITULO)
        titulo2.to_edge(UP, buff=0.35)
        self.play(Write(titulo2))

        def_p  = self.eq(r"p = \frac{a+b+c}{2}",    size=32, cor=COR_DEST)
        def_pa = self.eq(r"p-a = \frac{-a+b+c}{2}", size=28)
        def_pb = self.eq(r"p-b = \frac{a-b+c}{2}",  size=28)
        def_pc = self.eq(r"p-c = \frac{a+b-c}{2}",  size=28)

        grupo_p = VGroup(def_p, def_pa, def_pb, def_pc)
        grupo_p.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        grupo_p.to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)

        self.play(Write(def_p))
        self.wait(0.8)
        self.play(Write(def_pa), Write(def_pb), Write(def_pc))
        self.wait(1.5)

        # A^2 = p(p-a)(p-b)(p-c)
        a2_heron = self.eq(r"A^2 = p\,(p-a)\,(p-b)\,(p-c)", size=34)
        a2_heron.to_edge(RIGHT, buff=0.8).shift(UP * 0.6)
        self.play(Write(a2_heron))
        self.wait(1.5)

        # Seta para raiz
        seta = Arrow(
            a2_heron.get_bottom() + DOWN * 0.05,
            a2_heron.get_bottom() + DOWN * 0.85,
            color=COR_DEST, buff=0.05,
        )
        self.play(GrowArrow(seta))

        heron = self.eq(
            r"\boxed{A = \sqrt{p\,(p-a)\,(p-b)\,(p-c)}}",
            size=36, cor=COR_FINAL,
        )
        heron.next_to(seta, DOWN, buff=0.1)
        self.play(FadeIn(heron, shift=DOWN, run_time=1.2))
        self.wait(1)

        self.play(
            Circumscribe(heron, color=COR_FINAL, run_time=2, buff=0.15),
            Flash(heron.get_center(), color=COR_FINAL,
                  line_length=0.4, num_lines=16, run_time=1.5),
        )
        self.wait(3)

        self.play(FadeOut(VGroup(titulo2, grupo_p, a2_heron, seta, heron)))