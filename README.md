# ⚡ Quiz Harry Potter ⚡

Um quiz interativo desenvolvido em **Python** utilizando a biblioteca **Flet**, inspirado no universo de Harry Potter. 🪄

O jogador responde a uma sequência de perguntas sobre personagens, lugares, objetos, criaturas e elementos do mundo mágico. Ao final, recebe sua pontuação e pode jogar novamente.

## 🎮 Sobre o projeto

O projeto foi desenvolvido como uma aplicação gráfica utilizando **Flet**, colocando em prática conceitos como:

* Criação de interfaces gráficas;
* Organização de layouts;
* Botões e eventos;
* Listas e estruturas de dados;
* Gerenciamento de estado;
* Atualização dinâmica da interface;
* Sistema de pontuação;
* Navegação entre telas;
* Temporizador para avançar entre perguntas.

## 🧙 Funcionalidades

* ⚡ 10 perguntas sobre Harry Potter;
* 🪄 4 alternativas para cada pergunta;
* ✅ Indicação visual de resposta correta;
* ❌ Indicação visual de resposta incorreta;
* 🏆 Sistema de pontuação;
* 📊 Resultado final;
* 🔄 Botão para jogar novamente;
* ⏱️ Avanço automático para a próxima pergunta;
* 🎨 Interface temática inspirada no universo mágico.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Flet**
* **Threading / Timer**

## 📋 Como funciona

O jogo apresenta uma pergunta por vez acompanhada de quatro alternativas.

Quando o jogador seleciona uma resposta:

1. As alternativas são desativadas;
2. A resposta escolhida é verificada;
3. A alternativa correta fica destacada;
4. O jogador recebe uma mensagem indicando se acertou ou errou;
5. Após alguns segundos, a próxima pergunta é exibida;
6. Ao terminar todas as perguntas, a pontuação final é apresentada.

## 🏆 Sistema de pontuação

O resultado final depende da quantidade de respostas corretas:

| Pontuação | Resultado           |
| --------- | ------------------- |
| 10/10     | 🏆 PERFEITO!        |
| 7 a 9     | 👏 MUITO BEM!       |
| 4 a 6     | 💪 BEM LEGAL!       |
| 0 a 3     | 🌟 TENTE NOVAMENTE! |

## 🚀 Como executar o projeto

### 1. Instale o Python

Certifique-se de ter o Python instalado no computador.

### 2. Instale o Flet

No terminal, execute:

```bash
pip install flet
```

### 3. Clone o projeto

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd nome-do-projeto
```

### 4. Execute o programa

```bash
python main.py
```

O aplicativo será iniciado e o quiz poderá ser jogado.

## 📁 Estrutura do projeto

```text
quiz-harry-potter/
│
├── main.py
└── README.md
```

## ✨ Exemplos de perguntas

O quiz contém perguntas como:

* Qual é o nome da escola de magia onde Harry estuda?
* Qual é o animal de estimação de Harry?
* Qual é o nome da coruja de Harry?
* Qual é a casa de Harry em Hogwarts?
* Qual esporte é jogado em vassouras?
* Qual objeto escolhe a casa dos alunos?
* Quem é o melhor amigo ruivo de Harry?
* Qual feitiço é usado para desarmar um adversário?
* Qual criatura é Dobby?
* Qual é o nome do vilão principal da história?

## 🎯 Objetivo

O objetivo do projeto é desenvolver um aplicativo simples, interativo e divertido, utilizando os principais recursos aprendidos com a biblioteca **Flet** e a linguagem **Python**.

## 👩‍💻 Desenvolvido por

**Isabella Puzenato**

Projeto acadêmico desenvolvido para prática de programação e desenvolvimento de interfaces com Flet.

---

⚡ **Boa sorte e que o Chapéu Seletor escolha sua casa!** 🪄
