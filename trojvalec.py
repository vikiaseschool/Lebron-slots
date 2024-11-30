import pygame
import random
pygame.init()
import os




# Načítání obrázků
base_path = os.path.dirname(__file__)  # Získá aktuální adresář
images = {
    'cherry': pygame.image.load(os.path.join(base_path, 'cherry.jpg')),
    'lemon': pygame.image.load(os.path.join(base_path, 'lemon.jpg')),
    'orange': pygame.image.load(os.path.join(base_path, 'orange.jpg')),
    'lebron': pygame.image.load(os.path.join(base_path, 'LeBron_James.jpg'))
}
pygame.mixer.init()
lebron_win_sound = pygame.mixer.Sound(os.path.join(base_path, 'lebron_win.mp3'))
win_sound = pygame.mixer.Sound(os.path.join(base_path, 'win.wav'))

for key in images:
    images[key] = pygame.transform.scale(images[key], (60, 60))

password = 'x5E84sLoT5'

for _ in range(100):
    if input('heslo?') == password:
        balance = int(input('kredity?'))
        puvodni_balance = balance

        bet = 10
        min_bet = 10
        max_bet = 100

        symbols = ['cherry', 'lemon', 'orange', 'lebron']
        weights = [3, 9, 2, 8]

        WIDTH, HEIGHT = 400, 400
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Lebron Slots")

        # Barvy
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        YELLOW = (255, 255, 0)
        PURPLE = (160, 32, 240)

        font = pygame.font.Font(None, 36)

        def spin():
            return random.choices(symbols, weights)[0], random.choices(symbols, weights)[0], \
            random.choices(symbols, weights)[0]

        # Funkce pro kontrolu výhry
        def check_win(reel1, reel2, reel3):
            return reel1 == reel2 == reel3

        button_rect = pygame.Rect(50, HEIGHT - 80, 150, 50)
        button_increase_bet = pygame.Rect(140, 290, 25, 25)  # Tlačítko Zvýšení sázky
        button_decrease_bet = pygame.Rect(165, 290, 25, 25)  # Tlačítko Snížení sázky
        button_cashout = pygame.Rect(WIDTH - 150 - 25, HEIGHT - 80, 150, 50)  # Tlačítko Cashout

        reel1, reel2, reel3 = spin()
        message = ""

        # Hlavní herní smyčka
        running = True
        game_active = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Když hráč klikne na tlačítko "Roztočit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if balance >= min_bet:
                        if balance * 3 == puvodni_balance:
                            weights = [11, 9, 8, 4]
                        if balance * 2 == puvodni_balance:
                            weights = [11, 9, 8, 4]
                        if balance / 2 == puvodni_balance:
                            weights = [10, 5, 3, 2]
                        if game_active:
                            if button_rect.collidepoint(event.pos):
                                reel1, reel2, reel3 = spin()
                                balance -= bet
                                if check_win(reel1, reel2, reel3) and reel1 == 'lebron':
                                    balance += bet * 50
                                    message = f'LeBron JACKPOT!!! {bet * 50}'
                                    pygame.mixer.Sound.play(pygame.mixer.Sound(lebron_win_sound))
                                elif check_win(reel1, reel2, reel3):
                                    pygame.mixer.Sound.play(pygame.mixer.Sound(win_sound))
                                    if reel1 == 'cherry':
                                        message = f'Won: {bet * 3}'
                                        balance += bet * 3
                                    if reel1 == 'lemon':
                                        message = f'Won: {bet * 6}'
                                        balance += bet * 6
                                    if reel1 == 'orange':
                                        message = f'Won: {bet * 8}'
                                        balance += bet * 8
                                else:
                                    int = random.randint(0, 1)
                                    if int == 1:
                                        message = "Good luck."
                                    else:
                                        message = 'LeBron - 100x'

                        # Tlačítko zvýšení sázky
                        if button_increase_bet.collidepoint(event.pos):
                            if bet < max_bet:
                                bet += 10

                        # Tlačítko snížení sázky
                        if button_decrease_bet.collidepoint(event.pos):
                            if bet > min_bet:
                                bet -= 10
                    else:
                        message = 'Not enough credit!'
                        # Tlačítko Cashout

                    if button_cashout.collidepoint(event.pos):
                        # Zobrazení konečné zprávy po Cashoutu
                        message = f"Cashout! Final balance is {balance} $."
                        game_active = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if balance >= bet:
                            if balance * 3 == puvodni_balance:
                                weights = [11, 9, 8, 4]
                            if balance * 2 == puvodni_balance:
                                weights = [11, 9, 8, 4]
                            if balance / 2 == puvodni_balance:
                                weights = [10, 5, 3, 2]
                            if game_active:
                                reel1, reel2, reel3 = spin()
                                balance -= bet
                                if check_win(reel1, reel2, reel3) and reel1 == 'lebron':
                                    balance += bet * 100
                                    message = f'LeBron JACKPOT!!! {bet * 100}'
                                    pygame.mixer.Sound.play(pygame.mixer.Sound('lebron_win.mp3'))
                                elif check_win(reel1, reel2, reel3):
                                    pygame.mixer.Sound.play(pygame.mixer.Sound('win.wav'))
                                    if reel1 == 'cherry':
                                        message = f'Won: {bet * 3}'
                                        balance += bet * 3
                                    if reel1 == 'lemon':
                                        message = f'Won: {bet * 6}'
                                        balance += bet * 6
                                    if reel1 == 'orange':
                                        message = f'Won: {bet * 8}'
                                        balance += bet * 8
                                else:
                                    int = random.randint(0, 1)

                                    if int == 1:
                                        message = "Good luck."
                                    else:
                                        message = 'LeBron - 100x'

                screen.fill(PURPLE)
            if game_active:
                screen.blit(images[reel1], (80, 100))  # Obrázek 1. válce
                screen.blit(images[reel2], (160, 100))  # Obrázek 2. válce
                screen.blit(images[reel3], (240, 100))  # Obrázek 3. válce

                # Zobrazíme zprávu (výhra nebo prohra)
                message_text = font.render(message, True, BLACK)
                screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 50))

                balance_text = font.render(f"Credit: {balance}", True, BLACK)
                screen.blit(balance_text, (10, 270))

                # Zobrazíme sázku
                bet_text = font.render(f"Bet: {bet}", True, BLACK)
                screen.blit(bet_text, (10, 290))

                pygame.draw.rect(screen, YELLOW, button_rect)
                button_text = font.render("SPIN", True, BLACK)
                screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))

                # Vykreslíme tlačítka pro zvýšení a snížení sázky
                pygame.draw.rect(screen, YELLOW, button_increase_bet)
                increase_text = font.render("+", True, BLACK)
                screen.blit(increase_text, (button_increase_bet.x + 7, button_increase_bet.y))

                pygame.draw.rect(screen, YELLOW, button_decrease_bet)
                decrease_text = font.render("-", True, BLACK)
                screen.blit(decrease_text, (button_decrease_bet.x + 7, button_decrease_bet.y))

                # Vykreslíme tlačítko Cashout
                pygame.draw.rect(screen, YELLOW, button_cashout)
                cashout_text = font.render("End", True, BLACK)
                screen.blit(cashout_text, (button_cashout.x + 40, button_cashout.y + 12))


            else:
                # Zobrazení konečné zprávy po Cashoutu
                final_m = font.render(f"Game Over.", True, BLACK)
                screen.blit(final_m, (WIDTH // 2 - final_m.get_width() // 2, HEIGHT // 2 - final_m.get_height() // 2))
                final_m2 = font.render(f"Final Balance: {balance} ", True, BLACK)
                screen.blit(final_m2, (WIDTH // 2 - final_m2.get_width() // 2, HEIGHT // 2 + 20))
            pygame.display.flip()
            # Ukončení Pygame
        pygame.quit()

    else:
        print('spatne heslo. zkus znova')
