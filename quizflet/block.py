import random

import flet as ft


def main(page: ft.Page):
    page.title = "Ilha dos Ventos"
    page.bgcolor = "#102a43"
    page.padding = 0
    page.window_width = 980
    page.window_height = 720
    page.window_min_width = 700
    page.window_min_height = 600

    total_rodadas = 6
    jogador = ""
    rodada = 0
    pontos = 0
    energia = 3
    escolhas_usadas = []
    eventos = [
        {"titulo": "A praia das conchas azuis", "texto": "O vento sopra forte e revela um brilho entre a areia.", "ganho": 30, "perda": 0, "premio": "Você encontrou uma concha-lua! +30 pontos."},
        {"titulo": "O farol abandonado", "texto": "Uma escada em espiral leva até uma sala cheia de mapas.", "ganho": 45, "perda": 1, "premio": "O mapa secreto vale muitos pontos, mas a subida cansou você."},
        {"titulo": "A gruta do eco", "texto": "Três ecos respondem ao seu chamado. Um deles parece diferente.", "ganho": 20, "perda": 0, "premio": "Você seguiu o eco certo e achou cristais. +20 pontos."},
        {"titulo": "O jardim suspenso", "texto": "Frutas luminosas crescem no alto de uma árvore impossível.", "ganho": 35, "perda": 1, "premio": "A fruta dourada recupera sua coragem. +35 pontos."},
        {"titulo": "A ponte de cordas", "texto": "Do outro lado há uma bússola antiga, mas a travessia balança.", "ganho": 25, "perda": 1, "premio": "Você atravessou com cuidado e ganhou a bússola. +25 pontos."},
        {"titulo": "O mirante das estrelas", "texto": "O céu abre uma passagem de luz sobre a ilha inteira.", "ganho": 50, "perda": 0, "premio": "Você fez a descoberta da noite! +50 pontos."},
    ]

    nome = ft.TextField(
        label="Como podemos chamar você?",
        hint_text="Digite seu nome de explorador",
        width=360,
        autofocus=True,
        border_color="#8ecae6",
        focused_border_color="#ffb703",
        color="#f7fbff",
        label_color="#bde0fe",
    )
    mensagem = ft.Text("", size=16, color="#ffcf70", text_align=ft.TextAlign.CENTER)
    titulo_evento = ft.Text("", size=26, weight=ft.FontWeight.BOLD, color="#f7fbff")
    texto_evento = ft.Text("", size=16, color="#c7dff0", text_align=ft.TextAlign.CENTER)
    placar = ft.Text("", size=17, weight=ft.FontWeight.BOLD, color="#ffcf70")
    progresso = ft.ProgressBar(value=0, width=520, color="#ffb703", bgcolor="#254d68")
    opcoes = ft.Column(spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def painel(conteudo, largura=620):
        return ft.Container(
            content=conteudo,
            width=largura,
            padding=30,
            bgcolor="#173f5f",
            border=ft.Border.all(1, "#2d6687"),
            border_radius=18,
        )

    def atualizar_placar():
        placar.value = f"{jogador}   |   Pontos: {pontos}   |   Energia: {'★' * energia}{'☆' * (3 - energia)}"
        progresso.value = rodada / total_rodadas

    def fim_de_jogo(e=None):
        page.clean()
        if pontos >= 190:
            titulo, detalhe = "Lenda dos Ventos", "A ilha agora conhece o seu nome."
        elif pontos >= 120:
            titulo, detalhe = "Explorador de respeito", "Você encontrou tesouros que ninguém tinha visto."
        else:
            titulo, detalhe = "A aventura continua", "Toda grande descoberta começa com um primeiro passo."
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("FIM DA EXPEDIÇÃO", size=16, color="#8ecae6", weight=ft.FontWeight.BOLD),
                        ft.Text(titulo, size=32, color="#ffb703", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Text(f"{jogador}, sua pontuação foi {pontos} pontos.", size=20, color="#f7fbff", text_align=ft.TextAlign.CENTER),
                        ft.Text(detalhe, size=16, color="#c7dff0", text_align=ft.TextAlign.CENTER),
                        ft.Button(content="↻  Nova expedição", on_click=mostrar_inicio, width=250, height=48, bgcolor="#fb8500", color="white"),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=18,
                ),
                alignment=ft.Alignment(0, 0),
                expand=True,
            )
        )
        page.update()

    def resolver_evento(evento):
        nonlocal rodada, pontos, energia
        pontos += evento["ganho"]
        energia = max(0, energia - evento["perda"])
        rodada += 1
        mensagem.value = evento["premio"]
        atualizar_placar()
        if rodada >= total_rodadas or energia == 0:
            opcoes.controls = [ft.Button(content="Ver resultado", on_click=fim_de_jogo, width=220, bgcolor="#fb8500", color="white")]
        else:
            opcoes.controls = [ft.Button(content="Continuar explorando", on_click=mostrar_evento, width=240, bgcolor="#219ebc", color="white")]
        page.update()

    def mostrar_evento(e=None):
        nonlocal escolhas_usadas
        mensagem.value = "Escolha um destino para a próxima descoberta."
        opcoes.controls.clear()
        disponiveis = [evento for evento in eventos if evento["titulo"] not in escolhas_usadas]
        random.shuffle(disponiveis)
        escolhas_usadas = []
        for evento in disponiveis[:3]:
            escolhas_usadas.append(evento["titulo"])
            opcoes.controls.append(
                ft.Button(
                    content=ft.Column(
                        [
                            ft.Text(evento["titulo"], weight=ft.FontWeight.BOLD),
                            ft.Text(evento["texto"], size=12),
                        ],
                        spacing=3,
                    ),
                    width=520,
                    height=68,
                    bgcolor="#206a85",
                    color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=10),
                    on_click=lambda _, escolha=evento: resolver_evento(escolha),
                )
            )
        titulo_evento.value = f"Rodada {rodada + 1}: escolha seu caminho"
        texto_evento.value = "Cada destino esconde uma recompensa diferente."
        atualizar_placar()
        page.update()

    def iniciar(e):
        nonlocal jogador, rodada, pontos, energia, escolhas_usadas
        jogador = nome.value.strip() or "Explorador"
        rodada, pontos, energia, escolhas_usadas = 0, 0, 3, []
        page.clean()
        page.add(construir_jogo())
        mostrar_evento()

    def construir_jogo():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("ILHA DOS VENTOS", size=24, weight=ft.FontWeight.BOLD, color="#f7fbff"),
                            placar,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    progresso,
                    painel(ft.Column([titulo_evento, texto_evento, opcoes, mensagem], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=16)),
                ],
                spacing=18,
            ),
            padding=35,
            expand=True,
        )

    def mostrar_inicio(e=None):
        page.clean()
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("ILHA DOS VENTOS", size=38, weight=ft.FontWeight.BOLD, color="#ffb703", text_align=ft.TextAlign.CENTER),
                        ft.Text("Uma expedição de escolhas rápidas", size=20, color="#c7dff0", text_align=ft.TextAlign.CENTER),
                        ft.Text("Visite lugares misteriosos, acumule pontos e cuide da sua energia para chegar ao mirante final.", size=15, color="#8ecae6", text_align=ft.TextAlign.CENTER),
                        nome,
                        ft.Button(content="▶  Começar expedição", on_click=iniciar, width=250, height=50, bgcolor="#fb8500", color="white"),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                alignment=ft.Alignment(0, 0),
                padding=30,
                expand=True,
            )
        )
        page.update()

    mostrar_inicio()


ft.run(main)
