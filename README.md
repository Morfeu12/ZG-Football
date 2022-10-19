# ZG Football
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Morfeu12/ZG-Football/blob/main/LICENSE) 

## Sobre o projeto

O "ZG Football" é um projeto utilizando a biblioteca Pygame para construção de um game. A temática utilizada foi Copa do Mundo devido 2022 ser ano de copa.

![Pygame](https://camo.githubusercontent.com/1971c0a4f776fb5351c765c37e59630c83cabd52/68747470733a2f2f7777772e707967616d652e6f72672f696d616765732f6c6f676f2e706e67)

### Apresentação ZG Football v1.0
![Apresentação](https://youtu.be/J2ycm3HALJo)

### Como jogar? 
Objetivo: Vence quem marcar 10 gols primeiro! 

Cada jogar controla um personagem (na v1.0 apenas Brasil e Argentina) que se movem para cima e para baixo.
No momento que a bola colide com o personagem acontece o evento de "chute" e assim ela retorna em direção ao campo do adversário.
Se o personagem não conseguir a colisão com a bola o adversário consegue marcar um gol.
A cada chute a bola ganha mais velocidade. 
A cada gol a bola fica mais lenta e reinicia no centro do campo em direção contrária ao gol.

Movimentação + placar

![Movimentação e placar](https://github.com/Morfeu12/assets/blob/main/ZGFootball/move-and-win.jpg)

Área de gols

![Área de gol](https://github.com/Morfeu12/assets/blob/main/ZGFootball/gol_area.jpg)

## Tecnologias utilizadas

Python 3.10.0.final.0
Pygame 2.1.2 (SDL 2.0.16, Python 3.10.6)

## Como executar o projeto

```bash
# Clonar repositório
$ git clone https://github.com/Morfeu12/ZG-Football
# Navegue até a pasta do projeto 
# Instale o Pygame. https://www.pygame.org/wiki/GettingStarted
$ pip install -U pygame
# Inicie o arquivo main.py
$ python main.py 
ou
$ python3.10 main.py
```

## Autor

Omar Costa

https://www.linkedin.com/in/omarcosta152/