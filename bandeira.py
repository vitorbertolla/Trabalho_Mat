from manim import *

# ─── Paleta de cores da bandeira ───────────────────────────────────────────────
VERDE   = "#009C3B"
AMARELO = "#FFDF00"
AZUL    = "#002776"
BRANCO  = "#FFFFFF"
FUNDO   = "#1a1a2e"

# ─── Dados do problema ────────────────────────────────────────────────────────
COMP  = 2.00   # comprimento do retangulo (m)
LARG  = 1.40   # largura do retangulo (m)
DIST  = 0.17   # distancia dos vertices do losango as bordas (m)
RAIO  = 0.35   # raio do circulo (m)

SCALE = 3.0    # 1 metro -> SCALE unidades Manim


def metros(v):
    return v * SCALE


class BandeiraBrasilCompleta(Scene):
    """Resolucao completa do exercicio sobre areas da Bandeira do Brasil."""

    # ── helpers ─────────────────────────────────────────────────────────────────
    def titulo(self, txt, cor=YELLOW):
        return Text(txt, font_size=36, color=cor, weight=BOLD)

    def subtitulo(self, txt, cor=WHITE):
        return Text(txt, font_size=26, color=cor)

    def formula(self, txt, cor=WHITE, size=30):
        return MathTex(txt, color=cor, font_size=size)

    def caixa(self, mob, cor=YELLOW, pad=0.2):
        return SurroundingRectangle(mob, color=cor, buff=pad, corner_radius=0.08)

    # ── construtor da bandeira ──────────────────────────────────────────────────
    def bandeira(self, escala=1.0,
                 destacar_verde=False,
                 destacar_amarelo=False,
                 destacar_circulo=False):
        s = escala
        W = metros(COMP) * s
        H = metros(LARG) * s
        d = metros(DIST) * s
        r = metros(RAIO) * s

        op_ret  = 1.0
        op_los  = 1.0
        op_circ = 1.0
        if destacar_verde:
            op_los  = 0.15
            op_circ = 0.15
        if destacar_amarelo:
            op_ret  = 0.15
            op_circ = 0.15
        if destacar_circulo:
            op_ret  = 0.15
            op_los  = 0.15

        ret = Rectangle(width=W, height=H,
                        fill_color=VERDE, fill_opacity=op_ret,
                        stroke_color=WHITE, stroke_width=2)

        verts = [
            np.array([0,           H/2 - d, 0]),
            np.array([W/2 - d,     0,       0]),
            np.array([0,          -H/2 + d, 0]),
            np.array([-W/2 + d,   0,        0]),
        ]
        losango = Polygon(*verts,
                          fill_color=AMARELO, fill_opacity=op_los,
                          stroke_color=WHITE, stroke_width=2)

        circulo = Circle(radius=r,
                         fill_color=AZUL, fill_opacity=op_circ,
                         stroke_color=WHITE, stroke_width=2)

        faixa = Line([-r * 0.9, -r * 0.12, 0], [r * 0.9, -r * 0.12, 0],
                     stroke_color=BRANCO, stroke_width=max(2, r * 3.5))

        return VGroup(ret, losango, circulo, faixa)

    # ══════════════════════════════════════════════════════════════════════════
    def construct(self):
        self.camera.background_color = FUNDO

        self.cena_introducao()
        self.cena_dados_problema()
        self.cena_area_retangulo()
        self.cena_area_losango()
        self.cena_resposta_a()
        self.cena_area_circulo()
        self.cena_resposta_b()
        self.cena_resumo_final()

    # ══════════════════════════════════════════════════════════════════════════
    def cena_introducao(self):
        titulo = self.titulo("Bandeira do Brasil", cor=AMARELO)
        sub    = self.subtitulo("Calculo de Areas")
        sub.next_to(titulo, DOWN, buff=0.3)
        grupo = VGroup(titulo, sub).center()

        self.play(FadeIn(grupo, shift=UP))
        self.wait(1.5)
        self.play(FadeOut(grupo))

        flag = self.bandeira(escala=0.85)
        flag.center()
        self.play(FadeIn(flag, shift=UP, run_time=1.2))
        self.wait(0.5)

        W = metros(COMP) * 0.85
        H = metros(LARG) * 0.85

        brace_w = BraceBetweenPoints(
            [-W/2, -H/2 - 0.15, 0], [W/2, -H/2 - 0.15, 0], direction=DOWN)
        brace_h = BraceBetweenPoints(
            [W/2 + 0.15, -H/2, 0], [W/2 + 0.15, H/2, 0], direction=RIGHT)
        txt_w = self.formula("2{,}00\\,m").next_to(brace_w, DOWN,  buff=0.1)
        txt_h = self.formula("1{,}40\\,m").next_to(brace_h, RIGHT, buff=0.1)

        self.play(
            GrowFromCenter(brace_w), Write(txt_w),
            GrowFromCenter(brace_h), Write(txt_h),
        )
        self.wait(2)
        self.play(FadeOut(VGroup(flag, brace_w, brace_h, txt_w, txt_h)))

    # ══════════════════════════════════════════════════════════════════════════
    def cena_dados_problema(self):
        titulo = self.titulo("Dados do Problema")
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo))

        dados = [
            ("Comprimento do retangulo:", "2{,}00\\,m"),
            ("Largura do retangulo:",     "1{,}40\\,m"),
            ("Distancia vertice-borda:",  "17\\,cm = 0{,}17\\,m"),
            ("Raio do circulo:",          "35\\,cm = 0{,}35\\,m"),
            ("Aproximacao de \\pi:",      "\\dfrac{22}{7}"),
        ]

        linhas = VGroup()
        for label, valor in dados:
            txt = Text(label, font_size=24, color=WHITE)
            mat = MathTex(valor, font_size=28, color=AMARELO)
            mat.next_to(txt, RIGHT, buff=0.3)
            linhas.add(VGroup(txt, mat))

        linhas.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        linhas.next_to(titulo, DOWN, buff=0.5)
        linhas.center()

        for ln in linhas:
            self.play(FadeIn(ln, shift=RIGHT, run_time=0.5))
        self.wait(2.5)
        self.play(FadeOut(titulo), FadeOut(linhas))

    # ══════════════════════════════════════════════════════════════════════════
    def cena_area_retangulo(self):
        titulo = self.titulo("Area do Retangulo", cor=VERDE)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo))

        flag = self.bandeira(escala=0.68)
        flag.to_edge(LEFT, buff=0.5)
        flag.shift(DOWN * 0.3)
        self.play(FadeIn(flag, run_time=0.8))


        self.wait(0.5)

        passos = VGroup(
            MathTex(r"A_{\text{ret}} = \text{comp} \times \text{larg}", font_size=30),
            MathTex(r"A_{\text{ret}} = 2{,}00 \times 1{,}40",           font_size=30, color=YELLOW),
            MathTex(r"A_{\text{ret}} = 2{,}80\,m^2",                    font_size=34, color=VERDE),
        )
        passos.arrange(DOWN, buff=0.45)
        passos.next_to(titulo, DOWN, buff=0.5)
        passos.shift(RIGHT * 1.5)

        for p in passos:
            self.play(Write(p, run_time=0.8))
            self.wait(0.6)

        caixa = self.caixa(passos[-1], cor=VERDE)
        self.play(Create(caixa))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, flag, passos, caixa)))

    # ══════════════════════════════════════════════════════════════════════════
    def cena_area_losango(self):
        titulo = self.titulo("Area do Losango", cor=AMARELO)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo))

        flag = self.bandeira(escala=0.60, destacar_amarelo=True)
        flag.to_edge(LEFT, buff=0.5)
        flag.shift(DOWN * 0.2)
        self.play(FadeIn(flag, run_time=0.8))

        s   = 0.60
        W   = metros(COMP) * s
        H   = metros(LARG) * s
        d_m = metros(DIST) * s
        cx  = flag.get_center()[0]
        cy  = flag.get_center()[1]

        pt_top = np.array([cx,            cy + H/2 - d_m, 0])
        pt_bot = np.array([cx,            cy - H/2 + d_m, 0])
        pt_dir = np.array([cx + W/2 - d_m, cy,            0])
        pt_esq = np.array([cx - W/2 + d_m, cy,            0])

        diag_v = DashedLine(pt_top, pt_bot, color=RED,    stroke_width=2.5)
        diag_h = DashedLine(pt_esq, pt_dir, color=PURPLE, stroke_width=2.5)
        lbl_D  = self.formula("D", cor=RED,    size=22).next_to(diag_v, RIGHT, buff=0.06)
        lbl_d  = self.formula("d", cor=PURPLE, size=22).next_to(diag_h, DOWN,  buff=0.06)

        self.play(Create(diag_v), Create(diag_h))
        self.play(Write(lbl_D), Write(lbl_d))
        self.wait(0.5)

        calc = VGroup(
            MathTex(r"D = 2{,}00 - 2 \times 0{,}17",                        font_size=27, color=RED),
            MathTex(r"D = 2{,}00 - 0{,}34 = 1{,}66\,m",                     font_size=27, color=RED),
            MathTex(r"d = 1{,}40 - 2 \times 0{,}17",                        font_size=27, color=PURPLE),
            MathTex(r"d = 1{,}40 - 0{,}34 = 1{,}06\,m",                     font_size=27, color=PURPLE),
            MathTex(r"A_{\text{los}} = \frac{D \times d}{2}",               font_size=27),
            MathTex(r"A_{\text{los}} = \frac{1{,}66 \times 1{,}06}{2}",     font_size=27, color=AMARELO),
            MathTex(r"A_{\text{los}} = \frac{1{,}7596}{2} = 0{,}8798\,m^2", font_size=29, color=AMARELO),
        )
        calc.arrange(DOWN, buff=0.25)
        calc.next_to(titulo, DOWN, buff=0.4)
        calc.shift(RIGHT * 1.6)

        for c in calc:
            self.play(Write(c, run_time=0.55))
            self.wait(0.3)

        caixa = self.caixa(calc[-1], cor=AMARELO)
        self.play(Create(caixa))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, flag, diag_v, diag_h,
                                  lbl_D, lbl_d, calc, caixa)))

    # ══════════════════════════════════════════════════════════════════════════
    def cena_resposta_a(self):
        titulo = self.titulo("a)  Area Verde", cor=VERDE)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo))

        flag = self.bandeira(escala=0.65, destacar_verde=True)
        flag.to_edge(LEFT, buff=0.6)
        flag.shift(DOWN * 0.3)
        self.play(FadeIn(flag, run_time=0.8))

        conceito = Text("Area verde = Retangulo - Losango",
                         font_size=26, color=WHITE)
        conceito.next_to(titulo, DOWN, buff=0.45).shift(RIGHT * 1.5)
        self.play(Write(conceito))
        self.wait(0.8)

        calc = VGroup(
            MathTex(r"A_{\text{verde}} = A_{\text{ret}} - A_{\text{los}}",  font_size=32),
            MathTex(r"A_{\text{verde}} = 2{,}80 - 0{,}8798",                font_size=32, color=VERDE),
            MathTex(r"A_{\text{verde}} = 1{,}9202\,m^2",                    font_size=36, color=VERDE),
        )
        calc.arrange(DOWN, buff=0.45)
        calc.next_to(conceito, DOWN, buff=0.5)

        for c in calc:
            self.play(Write(c, run_time=0.7))
            self.wait(0.5)

        caixa = self.caixa(calc[-1], cor=VERDE, pad=0.3)
        self.play(Create(caixa))
        self.wait(2.5)
        self.play(FadeOut(VGroup(titulo, flag, conceito, calc, caixa)))

    # ══════════════════════════════════════════════════════════════════════════
    def cena_area_circulo(self):
        titulo = self.titulo("Area do Circulo", cor=BLUE)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo))

        r_vis = metros(RAIO) * 0.75
        circ  = Circle(radius=r_vis, fill_color=AZUL, fill_opacity=1,
                        stroke_color=WHITE, stroke_width=2)
        circ.to_edge(LEFT, buff=1.2)
        circ.shift(DOWN * 0.3)

        raio_line = Line(circ.get_center(), circ.get_right(),
                          color=WHITE, stroke_width=2)
        raio_lbl  = self.formula("r = 0{,}35\\,m", size=24)
        raio_lbl.next_to(raio_line, UP, buff=0.12)

        self.play(Create(circ), Create(raio_line), Write(raio_lbl))
        self.wait(0.5)

        calc = VGroup(
            MathTex(r"A_{\text{circ}} = \pi r^2",                          font_size=32),
            MathTex(r"A_{\text{circ}} = \frac{22}{7} \times (0{,}35)^2",  font_size=32, color=BLUE_B),
            MathTex(r"(0{,}35)^2 = 0{,}1225",                              font_size=28, color=GRAY_C),
            MathTex(r"A_{\text{circ}} = \frac{22}{7} \times 0{,}1225",    font_size=32, color=BLUE_B),
            MathTex(r"A_{\text{circ}} = \frac{2{,}695}{7}",                font_size=30, color=BLUE_B),
            MathTex(r"A_{\text{circ}} = 0{,}385\,m^2",                     font_size=32, color=BLUE_B),
        )
        calc.arrange(DOWN, buff=0.28)
        calc.next_to(titulo, DOWN, buff=0.4)
        calc.shift(RIGHT * 1.4)

        for c in calc:
            self.play(Write(c, run_time=0.6))
            self.wait(0.35)

        caixa = self.caixa(calc[-1], cor=BLUE)
        self.play(Create(caixa))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, circ, raio_line, raio_lbl, calc, caixa)))

    # ══════════════════════════════════════════════════════════════════════════
    def cena_resposta_b(self):
        titulo = self.titulo("b)  Porcentagem Amarela", cor=AMARELO)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo))

        flag = self.bandeira(escala=0.65, destacar_amarelo=True)
        flag.to_edge(LEFT, buff=0.6)
        flag.shift(DOWN * 0.3)
        self.play(FadeIn(flag, run_time=0.8))

        conceito = Text("Amarelo = Losango - Circulo",
                         font_size=26, color=WHITE)
        conceito.next_to(titulo, DOWN, buff=0.45).shift(RIGHT * 1.5)
        self.play(Write(conceito))
        self.wait(0.6)

        calc = VGroup(
            MathTex(r"A_{\text{am}} = A_{\text{los}} - A_{\text{circ}}",      font_size=30),
            MathTex(r"A_{\text{am}} = 0{,}8798 - 0{,}385",                    font_size=30, color=AMARELO),
            MathTex(r"A_{\text{am}} = 0{,}4948\,m^2",                         font_size=30, color=AMARELO),
            MathTex(r"\% = \frac{A_{\text{am}}}{A_{\text{ret}}} \times 100",  font_size=30),
            MathTex(r"\% = \frac{0{,}4948}{2{,}80} \times 100",              font_size=30, color=AMARELO),
            MathTex(r"\% \approx 17{,}67\%",                                  font_size=36, color=AMARELO),
        )
        calc.arrange(DOWN, buff=0.28)
        calc.next_to(conceito, DOWN, buff=0.4)

        for c in calc:
            self.play(Write(c, run_time=0.6))
            self.wait(0.35)

        caixa = self.caixa(calc[-1], cor=AMARELO, pad=0.3)
        self.play(Create(caixa))
        self.wait(2.5)
        self.play(FadeOut(VGroup(titulo, flag, conceito, calc, caixa)))

    # ══════════════════════════════════════════════════════════════════════════
    def cena_resumo_final(self):
        titulo = self.titulo("Respostas Finais", cor=WHITE)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo))

        painel_a = VGroup(
            Text("a) Area Verde", font_size=28, color=VERDE, weight=BOLD),
            MathTex(r"A_{\text{verde}} = 1{,}9202\,m^2", font_size=32, color=VERDE),
        ).arrange(DOWN, buff=0.3)
        box_a = SurroundingRectangle(
            painel_a, color=VERDE, buff=0.3,
            corner_radius=0.12, fill_color=VERDE, fill_opacity=0.08)
        grupo_a = VGroup(box_a, painel_a)

        painel_b = VGroup(
            Text("b) % Amarela", font_size=28, color=AMARELO, weight=BOLD),
            MathTex(r"\approx 17{,}67\%", font_size=32, color=AMARELO),
        ).arrange(DOWN, buff=0.3)
        box_b = SurroundingRectangle(
            painel_b, color=AMARELO, buff=0.3,
            corner_radius=0.12, fill_color=AMARELO, fill_opacity=0.08)
        grupo_b = VGroup(box_b, painel_b)

        paineis = VGroup(grupo_a, grupo_b)
        paineis.arrange(RIGHT, buff=0.8)
        paineis.next_to(titulo, DOWN, buff=0.6)

        self.play(
            FadeIn(grupo_a, shift=LEFT,  run_time=0.9),
            FadeIn(grupo_b, shift=RIGHT, run_time=0.9),
        )
        self.wait(1)

        flag = self.bandeira(escala=0.45)
        flag.next_to(paineis, DOWN, buff=0.5)
        self.play(FadeIn(flag, shift=UP, run_time=0.8))

        self.wait(3.5)
        self.play(FadeOut(VGroup(titulo, paineis, flag)))