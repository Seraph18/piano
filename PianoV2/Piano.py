import pygame #imports the pygame system
import time
pygame.init() #initializes pygame
events = pygame.event.get() #sets an event varaible equal to whatever event is going on
done = False #creates a done variable and sets it to false, telling the program the user is not done

img = pygame.image.load('PianoPic.bmp') #creates the image of the Piano keys and stores it in the img variable
w = 640 #width of the screen
h = 480 #height of the screen
WHITE = (255,255,255) #creates a variable for the color white, stored in hexedecimal or somthing like that, not really sure
screen = pygame.display.set_mode((w, h)) #sets the dimensions of the screen to what we set before
myfont = pygame.font.SysFont('Times New Roman', 14) #This makes a font we can use in the next line, makes it cleaner
textsurface = myfont.render("Press Escape to Exit Piano Simulator, Press O to record and stop recording, Press P to play recording.", False, WHITE) #This creates a serface on which we can put the text
textsurface2 = myfont.render("WARNING: Recording when somthing is already recorded will record over it, deleting the previous one.", False, WHITE) #This is to create a second line because Pygame only allows one line
screen.blit(img, (100, 100)) #This updates the sceen to show the image we gave it
screen.blit(textsurface, (0, 0)) #This updates the screen to show the text we gave it
screen.blit(textsurface2, (0, 15)) #This updates the screen to show the text we gave it

recording = []
rec = False

while not done: #This loop keeps the program running until the user chooses to exit by pressing the ESC key, making done = true

    pygame.display.flip() #This makes the program put the screen we build onto the actual physical screen, it is in the while loop because if we want to put more stuff in that updates with key presses it is easier


    for event in pygame.event.get(): #This checks for if an event happened
        if event.type == pygame.KEYDOWN: #This checks if that event was a key being pressed down
            if event.key == pygame.K_a: #This checks if the key that was pressed down was the "a" key
                effect = pygame.mixer.Sound('C - Piano.wav') #This makes an 'effect' variable that is set to the sound that we want, in the case the 'C' sound
                effect.play() #This plays the effect variable
                if rec:
                    recording.append('C - Piano.wav')
                #All the other elif statments except for the last one do the same thing
            elif event.key == pygame.K_w:
                effect = pygame.mixer.Sound('C# - Piano.wav')
                effect.play()
                if rec:
                    recording.append('C# - Piano.wav')
            elif event.key == pygame.K_s:
                effect = pygame.mixer.Sound('D - Piano.wav')
                effect.play()
                if rec:
                    recording.append('D - Piano.wav')
            elif event.key == pygame.K_e:
                effect = pygame.mixer.Sound('D# - Piano.wav')
                effect.play()
                if rec:
                    recording.append('D# - Piano.wav')
            elif event.key == pygame.K_d:
                effect = pygame.mixer.Sound('E - Piano.wav')
                effect.play()
                if rec:
                    recording.append('E - Piano.wav')
            elif event.key == pygame.K_f:
                effect = pygame.mixer.Sound('F - Piano.wav')
                effect.play()
                if rec:
                    recording.append('F - Piano.wav')
            elif event.key == pygame.K_t:
                effect = pygame.mixer.Sound('F# - Piano.wav')
                effect.play()
                if rec:
                    recording.append('G - Piano.wav')
            elif event.key == pygame.K_g:
                effect = pygame.mixer.Sound('G - Piano.wav')
                effect.play()
                if rec:
                    recording.append('G - Piano.wav')
            elif event.key == pygame.K_y:
                effect = pygame.mixer.Sound('G# - Piano.wav')
                effect.play()
                if rec:
                    recording.append('G# - Piano.wav')
            elif event.key == pygame.K_h:
                effect = pygame.mixer.Sound('A - Piano.wav')
                effect.play()
                if rec:
                    recording.append('A - Piano.wav')
            elif event.key == pygame.K_u:
                effect = pygame.mixer.Sound('A# - Piano.wav')
                effect.play()
                if rec:
                    recording.append('A# - Piano.wav')
            elif event.key == pygame.K_j:
                effect = pygame.mixer.Sound('B - Piano.wav')
                effect.play()
                if rec:
                    recording.append('B - Piano.wav')

            elif event.key == pygame.K_o:
                if rec:
                    rec = False
                    print("Not Recording")
                else:
                    recording = []
                    rec = True
                    print("Recording Now")

            elif event.key == pygame.K_p:
                for x in recording:
                    effect = pygame.mixer.Sound(x)
                    effect.play()
                    time.sleep(1)

            elif event.key == pygame.K_ESCAPE: #This checks if the 'ESC' button was pressed
                done = True #This sets our 'done' variable equal to True, letting the program know the user is done and to break the while loop
