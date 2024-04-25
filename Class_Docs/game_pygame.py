import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 30)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

logic_gates = {
    "AND": [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)],
    "OR": [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)],
    "XOR": [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)],
    "NOT": [(0, 1), (1, 0)]
}

gate_names = list(logic_gates.keys())

def generate_random_gate():
    gate_name = random.choice(gate_names)
    truth_table = logic_gates[gate_name]
    return gate_name, truth_table

def display_truth_table(truth_table, screen):
    x_offset = 50
    y_offset = 100
    cell_width = 100
    cell_height = 30

    for i, row in enumerate(truth_table):
        for j, value in enumerate(row):
            rect = pygame.Rect(x_offset + j * cell_width, y_offset + i * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, WHITE, rect, 1)
            text = font.render(str(value), True, WHITE)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

def display_text(text, screen, x, y):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Logic Gate Identification Game")

    score = 0

    while True:
        screen.fill(BLACK)

        display_text("Welcome to the Logic Gate Identification Game!", screen, SCREEN_WIDTH // 2, 50)

        gate_name, truth_table = generate_random_gate()
        display_truth_table(truth_table, screen)

        display_text("Score: {}".format(score), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    guess = "AND"
                elif event.key == pygame.K_o:
                    guess = "OR"
                elif event.key == pygame.K_x:
                    guess = "XOR"
                elif event.key == pygame.K_n:
                    guess = "NOT"
                else:
                    continue  

                if guess == gate_name:
                    score += 1
                    print("Correct!")
                else:
                    score -= 1
                    print("Incorrect! Correct answer was: {}".format(gate_name))

if __name__ == "__main__":
    main()
