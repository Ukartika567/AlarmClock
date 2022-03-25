
# \a to generate sound & we can set it as  alarm 
# print('\a')
import datetime
import time
import pygame
pygame.init()

alHour = int(input('Enter hour which You want to set as ur alarm hour : '))
alMinute = int(input('Enter minute which You want to set as ur alarm minute : '))
alamPm = str(input('set am or pm : '))
if alamPm == 'pm':
    alHour = alHour +12

while True:
    if alHour == datetime.datetime.now().hour and alMinute == datetime.datetime.now().minute:
        print('Usha Mam, wake Up')
        count = 0
        while count<2:
            pygame.mixer.music.load('Alarm.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(int(3000))
            count += 1

            inp =input('Enter s to stop : ')            
            if inp == 's' or 'S':
                pygame.mixer.music.stop()
                exit()

    
           

                    
                
  


                
        

