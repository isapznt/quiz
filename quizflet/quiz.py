import flet as ft
from threading import Timer


def main(page: ft.Page):
    page.title = "Quiz da Pzilda 🎮"
    page.bgcolor = "#f9dfe8"
    page.padding = 30
    page.window_width = 900
    page.window_height = 700

    perguntas = [
        {
            "pergunta": "Qual é o maior planeta do Sistema Solar?",
            "opcoes": ["Terra", "Marte", "Júpiter", "Vênus"],
            "resposta": "Júpiter",
        },
        {
            "pergunta": "Quantos dias tem uma semana?",
            "opcoes": ["5", "6", "7", "8"],
            "resposta": "7",
        },
        {
            "pergunta": "Qual linguagem estamos usando neste aplicativo?",
            "opcoes": ["Python", "Java", "HTML", "C++"],
            "resposta": "Python",
        },
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": ["São Paulo", "Brasília", "Rio de Janeiro", "Salvador"],
            "resposta": "Brasília",
        },
        {
            "pergunta": "Quanto é 10 + 5?",
            "opcoes": ["12", "15", "20", "25"],
            "resposta": "15",
        },
        {
            "pergunta": "Qual é o maior oceano do planeta?",
            "opcoes": ["Atlântico", "Índico", "Pacífico", "Ártico"],
            "resposta": "Pacífico",
        },
        {
            "pergunta": "Qual é o animal mais rápido do mundo?",
            "opcoes": ["Gavião", "Tigre", "Guepardo", "Leão"],
            "resposta": "Guepardo",
        },
        {
            "pergunta": "Qual é a cor da grama em um dia ensolarado?",
            "opcoes": ["Azul", "Verde", "Roxo", "Amarelo"],
            "resposta": "Verde",
        },
        {
            "pergunta": "Quantos lados tem um hexágono?",
            "opcoes": ["5", "6", "7", "8"],
            "resposta": "6",
        },
        {
            "pergunta": "Qual desses é um continente?",
            "opcoes": ["Amazonas", "Nilo", "Europa", "Médio Oriente"],
            "resposta": "Europa",
        },
    ]

    pergunta_atual = 0
    pontos = 0
    botoes_opcoes = {}

    titulo = ft.Text(
        "🎮 QUIZ DA PZILDA",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#8a3d66",
    )

    contador = ft.Text("", size=18, color="#704c5d")

    pergunta = ft.Text(
        "",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#4b2340",
        text_align=ft.TextAlign.CENTER,
    )

    alternativas = ft.Column(
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    mensagem = ft.Text(
        "",
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    pontuacao = ft.Text(
        "",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="#704c5d",
    )

    def mostrar_pergunta():
        nonlocal pergunta_atual

        pergunta.value = perguntas[pergunta_atual]["pergunta"]
        contador.value = f"Pergunta {pergunta_atual + 1} de {len(perguntas)}"
        mensagem.value = ""
        alternativas.controls.clear()
        botoes_opcoes.clear()

        for opcao in perguntas[pergunta_atual]["opcoes"]:
            botao = ft.Button(
                content=ft.Text(opcao, size=16, color="white", weight=ft.FontWeight.W_500),
                width=430,
                height=60,
                bgcolor="#e59ab9",
                color="white",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=14),
                    padding=ft.Padding(0, 0, 0, 0),
                ),
                on_click=lambda e, resposta=opcao: verificar_resposta(resposta),
            )
            botoes_opcoes[id(botao)] = opcao
            alternativas.controls.append(botao)

        page.update()

    def verificar_resposta(resposta):
        nonlocal pergunta_atual, pontos

        resposta_correta = perguntas[pergunta_atual]["resposta"]

        for botao in alternativas.controls:
            botao.disabled = True
            opcao = botoes_opcoes.get(id(botao))

            if opcao == resposta:
                if resposta == resposta_correta:
                    botao.bgcolor = "#2ecc71"
                    botao.color = "white"
                else:
                    botao.bgcolor = "#e74c3c"
                    botao.color = "white"

            if opcao == resposta_correta:
                botao.bgcolor = "#2ecc71"
                botao.color = "white"

        if resposta == resposta_correta:
            pontos += 1
            mensagem.value = "✅ ACERTOU!"
            mensagem.color = "#1f9d4f"
        else:
            mensagem.value = f"❌ ERROU! A resposta correta era {resposta_correta}."
            mensagem.color = "#c0392b"

        page.update()
        Timer(5, avancar_pergunta).start()

    def avancar_pergunta():
        nonlocal pergunta_atual

        pergunta_atual += 1

        if pergunta_atual < len(perguntas):
            mostrar_pergunta()
        else:
            mostrar_resultado()

    def mostrar_resultado():
        page.clean()

        if pontos == len(perguntas):
            resultado = "🏆 PERFEITO!"
        elif pontos >= 7:
            resultado = "👏 MUITO BEM!"
        elif pontos >= 4:
            resultado = "💪 BEM LEGAL!"
        else:
            resultado = "🌟 TENTE NOVAMENTE!"

        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("🎮 FIM DO QUIZ", size=32, weight=ft.FontWeight.BOLD, color="#4b2340"),
                        ft.Text(resultado, size=26, weight=ft.FontWeight.BOLD, color="#8a3d66"),
                        ft.Text(
                            f"Você acertou {pontos} de {len(perguntas)} perguntas!",
                            size=22,
                            color="#4b2340",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Button(
                            content="🔄 Jogar novamente",
                            bgcolor="#8a3d66",
                            color="white",
                            width=250,
                            height=55,
                            on_click=reiniciar,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=25,
                ),
                padding=30,
                bgcolor="#fbeaf2",
                border_radius=24,
                alignment=ft.Alignment(0, 0),
                expand=True,
            )
        )
        page.update()

    def reiniciar(e):
        nonlocal pergunta_atual, pontos

        pergunta_atual = 0
        pontos = 0
        page.clean()
        construir_tela()
        mostrar_pergunta()

    def construir_tela():
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        titulo,
                        contador,
                        ft.Container(
                            content=pergunta,
                            padding=20,
                            bgcolor="#f6d8e7",
                            border_radius=18,
                            width=520,
                        ),
                        alternativas,
                        mensagem,
                        pontuacao,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=ft.Padding(top=80, left=20, right=20, bottom=20),
                expand=True,
            )
        )

    construir_tela()
    mostrar_pergunta()


ft.run(main)