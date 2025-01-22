import pygame
import random
from collections import namedtuple
from enum import Enum

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

ROBOT_ROOM_A_POS = (50,50)
ROBOT_ROOM_B_POS = (SCREEN_WIDTH//2 + 50,50)
DIRT_ROOM_A_POS = (125, 250)
DIRT_ROOM_B_POS = (SCREEN_WIDTH//2 + 125, 250)
COUNTER_POS = (20, 350)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load sprites
robot_image = pygame.image.load('robot_sprite.png')
dirt_image = pygame.image.load('dirt_sprite.png')

# Set label font
font = pygame.font.SysFont(None, 48)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CoIn - Vacuum World')
clock = pygame.time.Clock()

Observation = namedtuple('Observation', 'robot_position room_a_dirty room_b_dirty')
Position = Enum('Position', ['A', 'B'])
Action = Enum('Action', ['MOVE', 'VACUUM'])

def render(position:Position, room_a_dirty:bool, room_b_dirty:bool, counter:int=0):
    # Check for window closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    
    # Clear screen
    screen.fill(WHITE)

    # Draw Counter
    if counter > 0:
        label_cnt = font.render(str(counter), True, BLACK)
        screen.blit(label_cnt, COUNTER_POS)
    
    # Draw room A
    pygame.draw.rect(screen, BLACK, (10, 10, 380, 380), 5)
    label_A = font.render("A", True, BLACK)
    screen.blit(label_A, (50, 50))

    # Draw room B
    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2 + 10, 10, 380, 380), 5)
    label_B = font.render("B", True, BLACK)
    screen.blit(label_B, (SCREEN_WIDTH // 2 + 50, 50))

    # (Re-)Position Robot
    if position == Position.A:
        screen.blit(robot_image, ROBOT_ROOM_A_POS)
    elif position == Position.B:
        screen.blit(robot_image, ROBOT_ROOM_B_POS)
    else:
        print("unknown position")
        return False

    # (Re-)Draw Dirt
    if room_a_dirty:
        screen.blit(dirt_image,  DIRT_ROOM_A_POS)
    if room_b_dirty:
        screen.blit(dirt_image,  DIRT_ROOM_B_POS)
        
    # Update display
    pygame.display.flip()
    
    # Advance ingame time 
    timeout_in_ms = 1000
    clock.tick(1000/timeout_in_ms)
    return True

def random_robot_policy(observation:Observation) -> Action:
    if random.choice([0,1]):
        return Action.MOVE
    else:
        return Action.VACUUM

def target_robot_policy(observation:Observation) -> Action:
    if observation[0] == Position.A and observation[1]:
        return Action.VACUUM
    elif observation[0] == Position.B and observation[2]:
        return Action.VACUUM
    else:
        return Action.MOVE

def gets_dirty(p=0.5):
    return p <= random.random()


# Environment information
obs = Observation(Position.A, False, True)
running = True
cleaning_score = 0
transition_tuples = {"random":[], "targeted":[]}
# Game loop
while running:

    # Randomly dirty the rooms (if the aren't dirty already)
    if not obs.room_a_dirty and gets_dirty():
        obs = Observation(obs.robot_position, True, obs.room_b_dirty)
    if not obs.room_b_dirty and gets_dirty():
        obs = Observation(obs.robot_position, obs.room_a_dirty, True)
    
    running = render(*obs, cleaning_score)
        
    # Let the robot 'decide' on its action ...
    action = random_robot_policy(obs)
    transition_tuples["random"].append((action, obs))
    # or
    action = target_robot_policy(obs)
    transition_tuples["targeted"].append((action, obs))

    # ... then realize MOVE action ...
    if action == action.MOVE and obs.robot_position == Position.A:
        obs = Observation(Position.B, obs.room_a_dirty, obs.room_b_dirty)
    elif action == action.MOVE and obs.robot_position == Position.B:
        obs = Observation(Position.A, obs.room_a_dirty, obs.room_b_dirty)

    # or realize VACUUM action and clean the room if possible.
    if action == action.VACUUM and obs.room_a_dirty and obs.robot_position == Position.A:
        obs = Observation(obs.robot_position, False, obs.room_b_dirty)
        cleaning_score += 1
    elif action == action.VACUUM and obs.room_b_dirty and obs.robot_position == Position.B:
        obs = Observation(obs.robot_position, obs.room_a_dirty, False)
        cleaning_score += 1
    
    running = render(*obs, cleaning_score)

# Quit pygame
pygame.quit()

def gamma_1(transition_tuples):
    return len({action for action, _ in transition_tuples}) > 1

print(f"collected {len(transition_tuples['random'])} transition tuples, with gamma_1 = {gamma_1(transition_tuples['random'])}")

def tau(transition_tuples):
    cleaning_score = 0
    for action, obs in transition_tuples:
        if action == action.VACUUM and obs.room_a_dirty and obs.robot_position == Position.A:
            cleaning_score += 1
        elif action == action.VACUUM and obs.room_b_dirty and obs.robot_position == Position.B:
            cleaning_score += 1
    return cleaning_score

print(f"cleaning scores at t={len(transition_tuples['random'])}: Random policy: {tau(transition_tuples['random'])} | Targeted policy: {tau(transition_tuples['targeted'])}")