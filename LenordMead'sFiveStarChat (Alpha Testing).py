#***************************#
#  Made By: Rico Alexander  #
#  Version: Alpha Testing   #
#  (Requires an internet    #
#        connection)        #
#***************************#


import gspread, pygame
from oauth2client.service_account import ServiceAccountCredentials

scope  = ['https://www.googleapis.com/auth/drive']
creds  = ServiceAccountCredentials.from_json_keyfile_name('ActCreds.json', scope)
client = gspread.authorize(creds)

pygame.init()  
gameDisplay = pygame.display.set_mode()
pygame.display.set_caption('LMFSC (Alpha Testing)')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

sheet = client.open('MMP Data').sheet1
cell = sheet.cell(3,1).value
sheet.update_cell(3,2,"test")


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text(msg, x, y, size=100):
    largeText = pygame.font.Font("Raleway-Medium.ttf", size)
    TextSurf, TextRect = text_objects((msg), largeText)
    TextRect.center = ((x),(y))
    gameDisplay.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,ic,ac,action=None,params=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h >mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if params != None:
                (params1, params2) = params
                action(params1,params2)
            else:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("Raleway-Medium.ttf",45)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def read_file(filename):
    f = open(filename,'r')
    line = f.readline()
    f.close()
    return line

def write_file(filename,text):
    f = open(filename,'w')
    f.write(text)
    f.close()

def main():
    while True:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text_input = str(read_file("Input.txt"))
        cell = sheet.cell(3,1).value
        sheet.update_cell(3,1,text_input)
        text(cell,640,200)
        

        pygame.display.update()
        clock.tick(1)


print (cell)

main()
pygame.quit()
quit()
