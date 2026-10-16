import pygame
from random import *

# Inicjalizacja Pygame
pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unmatched Team Balancer")

clock = pygame.time.Clock()

# Czcionki dopasowane do 1920x1080
font_title = pygame.font.SysFont("Arial", 54, bold=True)
font_main = pygame.font.SysFont("Arial", 36, bold=True)
font_small = pygame.font.SysFont("Arial", 28)

# Kolory
BG_COLOR = (30, 30, 40)
TEAM1_COLOR = (50, 110, 160)
TEAM2_COLOR = (180, 70, 70)
TEXT_COLOR = (240, 240, 240)
ACCENT_COLOR = (255, 215, 0)
PANEL_BG = (45, 45, 60)

players = [
    'Jonatan',
    'Łucja',
    'Piotrek',
    'Jacek'
]

players_strength = {
    'Łucja': 10,
    'Piotrek': 5,
    'Jonatan': 15,
    'Jacek': 15
}

units_strenght = {
    "Sherlock Holmes": 15,
    "Geralt z Rivii": 14,
    "Meduza": 14,
    "Nikola Tesla": 13,
    "Czerwony Kapturek": 13,
    "Wielka Stopa": 13,
    "Yennefer z Vengerbergu": 12,
    "Achilles": 11,
    "Niewidzialny Człowiek": 10,
    "Leszy": 10,
    "Dracula": 9,
    "Annie Christmas": 9,
    "Król Artur": 7,
    "Doktor Jekyll i Pan Hyde": 6,
    "Ciri": 6,
    "Dr Jill Trent": 6,
    "Sinbad": 5,
    "Jaskier": 4,
    "Alicja": 3
}

teem, teem_ = ('', ''), ('', '')
u1, u2, u3, u4 = '', '', '', ''
team1_power, team2_power = 0, 0
team1_chance, team2_chance = 50.0, 50.0


def generate_match():
    global teem, teem_, u1, u2, u3, u4, team1_power, team2_power, team1_chance, team2_chance

    # Losowanie drużyn
    p1 = choice(players)
    while True:
        p2 = choice(players)
        if p2 != p1:
            break
    teem = (p1, p2)

    while True:
        p3 = choice(players)
        if p3 not in teem:
            break

    while True:
        p4 = choice(players)
        if p4 not in teem and p4 != p3:
            break
    teem_ = (p3, p4)

    # Losowanie jednostek i balansowanie
    unit_names = list(units_strenght.keys())
    best_diff = float('inf')
    best_units = None

    for _ in range(100):
        drawn = sample(unit_names, 4)
        p1_pow = players_strength[teem[0]] * units_strenght[drawn[0]]
        p2_pow = players_strength[teem[1]] * units_strenght[drawn[1]]
        p3_pow = players_strength[teem_[0]] * units_strenght[drawn[2]]
        p4_pow = players_strength[teem_[1]] * units_strenght[drawn[3]]

        t1_total = p1_pow + p2_pow
        t2_total = p3_pow + p4_pow

        diff = abs(t1_total - t2_total)

        if diff < best_diff:
            best_diff = diff
            best_units = drawn
            if diff == 0:
                break

    u1, u2, u3, u4 = best_units
    team1_power = (players_strength[teem[0]] * units_strenght[u1]) + (players_strength[teem[1]] * units_strenght[u2])
    team2_power = (players_strength[teem_[0]] * units_strenght[u3]) + (players_strength[teem_[1]] * units_strenght[u4])

    # Obliczanie procentowych szans na wygraną
    total_power = team1_power + team2_power
    if total_power > 0:
        team1_chance = (team1_power / total_power) * 100
        team2_chance = (team2_power / total_power) * 100
    else:
        team1_chance = 50.0
        team2_chance = 50.0


# Pierwsze losowanie przy starcie
generate_match()

# Główna pętla gry
running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                generate_match()  # Ponowne losowanie po naciśnięciu Spacji
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Nagłówek (wyśrodkowany dla 1920px)
    title_surface = font_title.render("UNMATCHED - BALANSER DRUŻYN", True, ACCENT_COLOR)
    screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 40))

    instruction = font_small.render("Naciśnij [SPACE] aby wylosować ponownie | [ESC] aby wyjść", True, (170, 170, 170))
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, 110))

    # --- PANEL DRUŻYNY 1 ---
    panel_w, panel_h = 840, 780
    x1 = 100
    y1 = 180

    pygame.draw.rect(screen, PANEL_BG, (x1, y1, panel_w, panel_h), border_radius=16)
    pygame.draw.rect(screen, TEAM1_COLOR, (x1, y1, panel_w, 80), border_top_left_radius=16, border_top_right_radius=16)

    t1_title = font_main.render("DRUŻYNA 1", True, (255, 255, 255))
    screen.blit(t1_title, (x1 + 40, y1 + 22))

    # Gracze i postacie w Drużynie 1
    p1_str = f"• {teem[0]} (Siła gracza: {players_strength[teem[0]]})"
    u1_str = f"   Postać: {u1} (Siła: {units_strenght[u1]})"
    p2_str = f"• {teem[1]} (Siła gracza: {players_strength[teem[1]]})"
    u2_str = f"   Postać: {u2} (Siła: {units_strenght[u2]})"

    screen.blit(font_main.render(p1_str, True, TEXT_COLOR), (x1 + 50, y1 + 130))
    screen.blit(font_small.render(u1_str, True, (200, 200, 200)), (x1 + 50, y1 + 185))

    screen.blit(font_main.render(p2_str, True, TEXT_COLOR), (x1 + 50, y1 + 280))
    screen.blit(font_small.render(u2_str, True, (200, 200, 200)), (x1 + 50, y1 + 335))

    t1_pow = font_small.render(f"Wynik łączny: {team1_power}", True, TEXT_COLOR)
    screen.blit(t1_pow, (x1 + 50, y1 + 570))

    t1_ch = font_title.render(f"Szanse: {team1_chance:.1f}%", True, ACCENT_COLOR)
    screen.blit(t1_ch, (x1 + 50, y1 + 630))


    # --- PANEL DRUŻYNY 2 ---
    x2 = 980

    pygame.draw.rect(screen, PANEL_BG, (x2, y1, panel_w, panel_h), border_radius=16)
    pygame.draw.rect(screen, TEAM2_COLOR, (x2, y1, panel_w, 80), border_top_left_radius=16, border_top_right_radius=16)

    t2_title = font_main.render("DRUŻYNA 2", True, (255, 255, 255))
    screen.blit(t2_title, (x2 + 40, y1 + 22))

    # Gracze i postacie w Drużynie 2
    p3_str = f"• {teem_[0]} (Siła gracza: {players_strength[teem_[0]]})"
    u3_str = f"   Postać: {u3} (Siła: {units_strenght[u3]})"
    p4_str = f"• {teem_[1]} (Siła gracza: {players_strength[teem_[1]]})"
    u4_str = f"   Postać: {u4} (Siła: {units_strenght[u4]})"

    screen.blit(font_main.render(p3_str, True, TEXT_COLOR), (x2 + 50, y1 + 130))
    screen.blit(font_small.render(u3_str, True, (200, 200, 200)), (x2 + 50, y1 + 185))

    screen.blit(font_main.render(p4_str, True, TEXT_COLOR), (x2 + 50, y1 + 280))
    screen.blit(font_small.render(u4_str, True, (200, 200, 200)), (x2 + 50, y1 + 335))

    t2_pow = font_small.render(f"Wynik łączny: {team2_power}", True, TEXT_COLOR)
    screen.blit(t2_pow, (x2 + 50, y1 + 570))

    t2_ch = font_title.render(f"Szanse: {team2_chance:.1f}%", True, ACCENT_COLOR)
    screen.blit(t2_ch, (x2 + 50, y1 + 630))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()