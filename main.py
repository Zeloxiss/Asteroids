import pygame, sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroidfield import *
from shot import *

def print_scoreboard(screen, stage, score):
    font = pygame.font.Font(None, 64)
    stage_text = font.render(f"Stage: {stage}", False, (210, 210, 210))
    score_text = font.render(f"Score: {score}", False, (210, 210, 210))
    screen.blit(stage_text, [15,15])
    screen.blit(score_text, [15,85])

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    clock = pygame.time.Clock()
    dt = 0
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    spaceship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    # GAME LOOP
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)

        #stages (score dependant)
        stage = 1 + int(score / STAGE_SIZE) 
        asteroid_speed_modifier = 1 + (stage * STAGE_ASTEROID_SPEED_MULTIPLIER)


        for asteroid in asteroids:
            if spaceship.collide_with(asteroid):
                log_event("player_hit")
                print(f"\n========= Game over! ==========\n || You scored {score} points ! || \n===============================\n")
                sys.exit()
            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    score += asteroid.split()
            asteroid.speed_mod = asteroid_speed_modifier

        for x in drawable:
            x.draw(screen)

        print_scoreboard(screen, stage, score)
        


    #SCREEN UPDATE
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        

       



 







if __name__ == "__main__":
    main()
