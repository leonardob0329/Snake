import pygame
import time
import random

pygame.init()

largura = 1000
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

tamanho_bloco = 10
velocidade = 15

fonte = pygame.font.SysFont("comicsansms", 35)

clock = pygame.time.Clock()


def mensagem(msg, cor):
    """Exibe mensagem centralizada."""
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])


def jogo():
    x1 = largura / 2
    y1 = altura / 2

    x1_mudanca = 0
    y1_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    fim_jogo = False

    while not fim_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x1_mudanca == 0:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x1_mudanca == 0:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP and y1_mudanca == 0:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN and y1_mudanca == 0:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim_jogo = True

        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(preto)

        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = [x1, y1]
        cobra.append(cabeca)
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for segmento in cobra[:-1]:
            if segmento == cabeca:
                fim_jogo = True

        for bloco in cobra:
            pygame.draw.rect(tela, azul, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1

        pygame.display.update()

        clock.tick(velocidade)

    tela.fill(preto)
    mensagem("Você perdeu! Pressione Q para sair ou C para jogar novamente", vermelho)
    pygame.display.update()
    time.sleep(2)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if evento.key == pygame.K_c:
                    jogo()

jogo()