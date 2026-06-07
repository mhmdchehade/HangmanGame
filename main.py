import pygame
import random

pygame.init()



WIDTH, HEIGHT = 830, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hang In There")

#colors
BG_TOP = (253, 245, 230)      #cream
BG_BOTTOM = (255, 235, 200)   #soft peach
BUTTON_COLORS = [
    (242,196,149),   #pastel orange
    (255, 218, 185), #pastel peach
    (255, 205, 210), #pastel pink
    (200, 230, 201), #pastel mint
    (197, 202, 233), #pastel lavender
]
BUTTON_HOVER = (255, 230, 180)  #brighter hover
TEXT_COLOR = (102,51,0)         #dark brown
WORD_COLOR = (153,76,0)         #medium brown
HANGMAN_COLOR = (120,80,40)     #soft brown
SHADOW_COLOR = (200,180,150)    #light shadow for title
UNDERSCORE_COLOR = (210,180,140)#light beige for missing letters
HINT_COLOR = (210,180,140)      #light beige for hint

#font
LETTER_FONT = pygame.font.SysFont("arial", 36, bold=True)
WORD_FONT = pygame.font.SysFont("arial", 50, bold=True)
TITLE_FONT = pygame.font.SysFont("arial", 70, bold=True)

#words
word_categories = {
    "Animals": [
        "ELEPHANT", "GIRAFFE", "KANGAROO", "DOLPHIN", "ALLIGATOR", "PENGUIN",
        "RHINOCEROS", "CHIMPANZEE", "CROCODILE", "OSTRICH", "HIPPOPOTAMUS",
        "SQUIRREL", "PORCUPINE", "FLAMINGO", "BUFFALO", "ARMADILLO", "MOOSE",
        "CHEETAH", "HEDGEHOG", "OTTER", "RABBIT", "TURTLE", "WHALE", "FOX", "BEAR"
    ],
    "Food": [
        "APPLE", "BANANA", "WATERMELON", "STRAWBERRY", "PINEAPPLE", "BLUEBERRY",
        "CUCUMBER", "CARROT", "BROCCOLI", "PUMPKIN", "AVOCADO", "GRAPEFRUIT",
        "POMEGRANATE", "RASPBERRY", "CAULIFLOWER", "KIWI", "MANGO", "TOMATO"
    ],
    "Countries": [
        "LEBANON", "BRAZIL", "AUSTRALIA", "CANADA", "GERMANY", "FRANCE", "JAPAN",
        "ARGENTINA", "ITALY", "PORTUGAL", "DENMARK", "SWEDEN",
        "NIGERIA", "RUSSIA", "EGYPT", "MEXICO", "SPAIN", "CHINA", "INDIA"
    ],
    "Objects": [
        "KEYBOARD", "NOTEBOOK", "MICROWAVE", "HEADPHONES", "BACKPACK",
        "TELEVISION", "REFRIGERATOR", "BICYCLE", "CALCULATOR", "SUNGLASSES",
        "UMBRELLA", "LAPTOP", "CAMERA", "FLASHLIGHT", "CLOCK", "LAMP"
    ],
    "Others": [
        "COMPUTER", "PROGRAMMING", "SCIENCE", "FRIENDSHIP", "HAPPINESS",
        "MYSTERY", "FANTASY", "LANGUAGE", "HISTORY", "MUSIC",
        "DREAM", "JOURNEY", "COURAGE"
    ]
}

MAX_ATTEMPTS = 10
RADIUS = 22
GAP = 10

# game state
def reset_game():
    global chosen_word, guessed, hangman_status, chosen_category
    chosen_category = random.choice(list(word_categories.keys()))
    chosen_word = random.choice(word_categories[chosen_category])
    guessed = []
    hangman_status = 0

#letters buttons
def create_letters():
    letters = []
    row_width = 13 * (RADIUS * 2) + 12 * GAP
    start_x = (WIDTH - row_width) // 2 + RADIUS
    start_y = 450
    for i in range(26):
        row = i // 13
        col = i % 13
        x = start_x + col * (RADIUS * 2 + GAP)
        y = start_y + row * (RADIUS * 2 + GAP + 10)
        color = BUTTON_COLORS[i % len(BUTTON_COLORS)]
        letters.append([x, y, chr(65+i), True, color])
    return letters

letters = create_letters()

#drawing functions
def draw_gradient():
    for i in range(HEIGHT):
        ratio = i / HEIGHT
        r = int(BG_TOP[0]*(1-ratio) + BG_BOTTOM[0]*ratio)
        g = int(BG_TOP[1]*(1-ratio) + BG_BOTTOM[1]*ratio)
        b = int(BG_TOP[2]*(1-ratio) + BG_BOTTOM[2]*ratio)
        pygame.draw.line(screen, (r,g,b), (0,i), (WIDTH,i))

def draw_hangman(status):
    x = 120
    y = 420
    thickness = 6
    head_radius = 22

    #stand
    if status >= 1: pygame.draw.line(screen,HANGMAN_COLOR,(x-50,y),(x+50,y),thickness)
    if status >= 2: pygame.draw.line(screen,HANGMAN_COLOR,(x,y),(x,y-220),thickness)
    if status >= 3: pygame.draw.line(screen,HANGMAN_COLOR,(x,y-220),(x+90,y-220),thickness)
    if status >= 4: pygame.draw.line(screen,HANGMAN_COLOR,(x+90,y-220),(x+90,y-180),thickness)
    #head
    if status >= 5:
        head_x = x+90
        head_y = y-155
        pygame.draw.circle(screen,HANGMAN_COLOR,(head_x,head_y),head_radius,thickness)
        pygame.draw.circle(screen,HANGMAN_COLOR,(head_x-7,head_y-4),2)
        pygame.draw.circle(screen,HANGMAN_COLOR,(head_x+7,head_y-4),2)
    #body
    if status >= 6: pygame.draw.line(screen,HANGMAN_COLOR,(x+90,y-133),(x+90,y-90),thickness)
    #arms
    if status >= 7: pygame.draw.line(screen,HANGMAN_COLOR,(x+90,y-128),(x+65,y-112),thickness)
    if status >= 8: pygame.draw.line(screen,HANGMAN_COLOR,(x+90,y-128),(x+115,y-112),thickness)
    #legs
    if status >= 9: pygame.draw.line(screen,HANGMAN_COLOR,(x+90,y-90),(x+70,y-60),thickness)
    if status >= 10: pygame.draw.line(screen,HANGMAN_COLOR,(x+90,y-90),(x+110,y-60),thickness)

def draw():
    draw_gradient()
    #title shadow
    title_shadow = TITLE_FONT.render("Hangman", True, SHADOW_COLOR)
    screen.blit(title_shadow, (WIDTH//2 - title_shadow.get_width()//2 + 3, 23))
    title_text = TITLE_FONT.render("Hangman", True, TEXT_COLOR)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 20))

    #word display
    display_word = "".join([l+" " if l in guessed else "_ " for l in chosen_word])
    underscore_render = WORD_FONT.render("_ "*len(chosen_word), True, UNDERSCORE_COLOR)
    screen.blit(underscore_render, (WIDTH//2 - underscore_render.get_width()//2, 150))
    word_text = WORD_FONT.render(display_word, True, WORD_COLOR)
    screen.blit(word_text, (WIDTH//2 - word_text.get_width()//2, 150))

    #hint (category)
    if chosen_category == "Others":
        extra_hint = "General / Abstract"
        hint_text = LETTER_FONT.render(f"Hint: ( {extra_hint} )", True, HINT_COLOR)
    else:
        hint_text = LETTER_FONT.render(f"Hint: ( {chosen_category} )", True, HINT_COLOR)

    screen.blit(
        hint_text,
        (WIDTH//2 - hint_text.get_width()//2, 300)
    )

    #letters button
    mx,my = pygame.mouse.get_pos()
    for letter in letters:
        x,y,ltr,visible,color = letter
        if visible:
            draw_color = BUTTON_HOVER if ((mx-x)**2 + (my-y)**2)**0.5 < RADIUS else color
            pygame.draw.circle(screen, draw_color, (x,y), RADIUS)
            pygame.draw.circle(screen, TEXT_COLOR, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True, TEXT_COLOR)
            screen.blit(text, (x - text.get_width()//2, y - text.get_height()//2))

    draw_hangman(hangman_status)
    pygame.display.update()

def display_message(text, second_text=""):
    draw_gradient()
    render1 = WORD_FONT.render(text, True, TEXT_COLOR)
    screen.blit(render1, (WIDTH//2-render1.get_width()//2, HEIGHT//2-50))
    if second_text:
        smaller_font = pygame.font.SysFont("arial",32,bold=True)
        render2 = smaller_font.render(second_text, True, WORD_COLOR)
        screen.blit(render2, (WIDTH//2-render2.get_width()//2, HEIGHT//2+20))
    pygame.display.update()
    pygame.time.delay(3500)

#instructions
def show_instructions():
    running = True
    small_font = pygame.font.SysFont("arial",28,bold=True)
    lines = [
        "Guess the word by clicking letters.",
        "Each wrong guess adds a part to the hangman.",
        "You win by guessing all letters before the hangman is complete.",
        "Click anywhere to return to menu."
    ]
    while running:
        draw_gradient()
        y_offset = 150
        for line in lines:
            render = small_font.render(line, True, TEXT_COLOR)
            screen.blit(render, (WIDTH//2 - render.get_width()//2, y_offset))
            y_offset += 50
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False

#main menu
def main_menu():
    menu_running = True
    MENU_FONT = pygame.font.SysFont("arial",50,bold=True)
    SMALL_FONT = pygame.font.SysFont("arial",24,bold=True)

    while menu_running:
        draw_gradient()
        #title
        shadow = TITLE_FONT.render("Hangman", True, SHADOW_COLOR)
        screen.blit(shadow, (WIDTH//2 - shadow.get_width()//2 +3, 50+3))
        title = TITLE_FONT.render("Hangman", True, TEXT_COLOR)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))

        #buttons
        buttons = []
        names = ["Start Game", "Instructions", "Quit"]
        for i,name in enumerate(names):
            rect = pygame.Rect(WIDTH//2-170, 220+i*90, 340, 65)
            buttons.append((rect,name))

            mx,my = pygame.mouse.get_pos()
            color = (230,200,180)
            if rect.collidepoint(mx,my):
                color = BUTTON_HOVER

            pygame.draw.rect(screen, color, rect, border_radius=20)
            pygame.draw.rect(screen, TEXT_COLOR, rect, 3, border_radius=20)
            text = MENU_FONT.render(name, True, TEXT_COLOR)
            screen.blit(text, (rect.centerx-text.get_width()/2, rect.centery-text.get_height()/2))

        #footer
        credit_text = SMALL_FONT.render("Created by Mhmd Ch for CIP2026 Final Project", True, TEXT_COLOR)
        screen.blit(credit_text, (WIDTH//2 - credit_text.get_width()//2, HEIGHT-40))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                for rect,name in buttons:
                    if rect.collidepoint(mx,my):
                        if name == "Start Game":
                            return
                        elif name == "Instructions":
                            show_instructions()
                        elif name == "Quit":
                            pygame.quit()
                            quit()

#start game
main_menu()
reset_game()
letters = create_letters()

#game loop
running = True
while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible,color = letter
                if visible:
                    distance = ((mx-x)**2 + (my-y)**2)**0.5
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in chosen_word:
                            hangman_status += 1

    #check win
    won = all(letter in guessed for letter in chosen_word)
    if won:
        display_message("YOU WON! :)", f"The word was: {chosen_word}")
        running = False

    #check lose
    if hangman_status >= MAX_ATTEMPTS:
        display_message("GAME OVER", f"The word was: {chosen_word}")
        running = False

pygame.quit()
