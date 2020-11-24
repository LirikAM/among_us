##Import
from crewmate import Crewmate
from tasker import Tasker
from use import UseButton       
from task_weapons import TaskWeapons
from begin_of_game import ButtonToStartGame
from exit_game import ExitGame
from character_selection import CharacterSelection
from the_impostor import Impostor
from experimental_for_impostor import ExperimentalForImpostor
from button_for_kill import ButtonForKill
from button_to_report import ButtonToReport
from beautiful_appearance_of_letters import FiltrOfWords
from bot_crewmate import BotCrewmate
from online_game import OnlineGame
from enter_name import EnterName
from bot_impostor import BotImpostor
from press_to_go_out import PressGoOut
##Import
            
#class TaskElectric():
    #(I will do it in a future!)

player_crewmate              = None
impostor                     = None
experimental_for_impostor    = None
place_task                   = None
use                          = None
button_for_kill              = None
button_to_report             = None
filtrofwords                 = None
bot_crewmate                 = None
online_game                  = None
enter_name                   = None
bot_impostor                 = None
press_to_go_out              = None

player_creemate_black        = None
the_sofa                     = None
experimental_red             = None
experimental_red_isnot_alive = None
use_button                   = None
kill_button                  = None
start_button                 = None
report                       = None
dead_body                    = None

meteorits = []

quantity_meteorits = 0

start_game                   = None
exit_game                    = None
character_selection          = None

minim                        = None
play_music_report            = None

file_for_name                = None
t                            = None

#music
add_library("minim")
#music

def setup():
    size(1024,600)
    
    global player_crewmate, place_task, use, meteorits, player_crewmate_black, the_sofa, start_game, report, button_to_report, filtrofwords, bot_crewmate, dead_body, minim, play_music_report, enter_name, t, bot_impostor
    global exit_game, character_selection, impostor, experimental_red, experimental_red_isnot_alive, experimental_for_impostor, button_for_kill, use_button, kill_button, start_button, online_game, file_for_name
    global press_to_go_out
    
    rectMode(CENTER)
    textAlign(CENTER)
    textSize(34)
    imageMode(CENTER)
    
    #music
    minim = Minim(this)
    play_music_report = minim.loadFile("among_us_report.wav")
    #music
    
    ## loadImage()
    player_crewmate_black        = loadImage('black_crewmate.png')
    experimental_red             = loadImage('crewmatered.png')
    experimental_red_isnot_alive = loadImage('crewmateisnotalive.png')
    the_sofa                     = loadImage('the_sofa.png')
    use_button                   = loadImage('use_button.png')
    kill_button                  = loadImage('kill.png')
    start_button                 = loadImage('start.png')
    report                       = loadImage('report.png')
    dead_body                    = loadImage('dead_body.png')
    ## loadImage()
    
    start_game                = ButtonToStartGame(width/2, height/2)
    exit_game                 = ExitGame(width/2, height/2+200, 100, 45)
    place_task                = Tasker(width/2-200,height/2-200, the_sofa, 200, 200, width/2, height/2)
    use                       = UseButton(width-100, height/2+150, 150, 150)
    player_crewmate           = Crewmate(player_crewmate_black, width-200, height/2-200, 300, 200, width/2, height/2+250, 500, 25, place_task.x, place_task.y, width/2, height/2)
    experimental_for_impostor = ExperimentalForImpostor(int(random(width/2-250,width/2+250)), 500)
    bot_crewmate              = BotCrewmate(width, height/2-100, player_crewmate.rx, player_crewmate.ry, player_crewmate_black, player_crewmate.speed, dead_body)
    impostor                  = Impostor(width/2, height/2, player_crewmate.xt, player_crewmate.yt, player_crewmate.wt, player_crewmate.ht)
                                         
    character_selection       = CharacterSelection(width/2-200, height/2, 250, 300, width/2+200)
    button_for_kill           = ButtonForKill(use.x, use.y, use.r_x, use.r_y)
    button_to_report          = ButtonToReport(use.x, use.y-200, use.r_x, use.r_y)
    filtrofwords              = FiltrOfWords()
    online_game               = OnlineGame(width/2, height-200, use.r_x, use.r_y)
    enter_name                = EnterName(width/2, height/2+200, 300, 50)
    press_to_go_out           = PressGoOut(place_task.x2+place_task.r2/2, place_task.y2-place_task.r2/2, 50, 50)
    bot_impostor              = BotImpostor(width, height/2, player_crewmate.rx, player_crewmate.ry, experimental_red, width/2-425, height/2, use.r_x, use.r_y)

    file_for_name = open("file_save_name.txt", "r")
    t = file_for_name.readline()
    file_for_name.close()

    for i in range(0,2):
        meteorits.append(TaskWeapons(width, int(random(place_task.y2 - place_task.r2/2, place_task.y2 + place_task.r2/2)), int(random(2,7)), place_task.x2, place_task.y2, place_task.r2))

def draw():
    global player_crewmate, place_task, use, meteorits, quantity_meteorits, start_game, character_selection, impostor, use_button, kill_button, button_for_kill, start_button, button_to_report, report, filtrofwords
    global online_game, experimental_for_impostor, bot_crewmate, enter_name, file_for_name, t, bot_impostor, press_to_go_out
    
    background(255,255,255)
    
    strokeWeight(1)

    if not start_game.select_game:
        start_game.show(start_button)
        online_game.show()
        exit_game.show()

    ## start game
    if start_game.select_game:
    ## start game

        if character_selection.select_to_choose == 0:
            character_selection.show(player_crewmate.rx, player_crewmate.rx, player_crewmate_black)
            enter_name.show(t)
            bot_impostor.show_to_hide_impostor()
            player_crewmate.name = enter_name.text_
            if t == '':
                file_for_name = open("file_save_name.txt", "w")
                file_for_name.write(player_crewmate.name)
                file_for_name.close()
            else:
                enter_name.text_ = t

        else:

            ##show()
            place_task.show()
            button_to_report.show_report(report)
            ##show()

            if character_selection.select_to_choose == 1:
                
                player_crewmate.show()
                use.show(use_button)
                #player_crewmate.him_tasks()
                player_crewmate.scale_()

                if not bot_impostor.select_impostor:
                    bot_impostor.show()

                    if bot_impostor.kill_player(player_crewmate.list_of_ghost_rect):
                        pass
                    else:
                        bot_impostor.move()

                bot_impostor.distance(player_crewmate.x, player_crewmate.y, player_crewmate.rx, player_crewmate.ry)
                if bot_impostor.select:
                    bot_impostor.kill_you()
                ###return xtask and ytask
                place_task.x, place_task.y = player_crewmate.return_task()
                ###return xtask and ytask

                if use.select:

                    place_task.show_background()
                    place_task.show_line()
                    press_to_go_out.show()

                    numb = 20
                    fill(0,0,0)
                    text(str(quantity_meteorits) + '/' + str(numb), width/2, height/2+200)
                    fill(255,255,255)

                    if press_to_go_out.select:
                        use.select = False

                    else:

                        if quantity_meteorits < numb:

                            i = 0
                            while i < len(meteorits):
                                meteorits[i].move()

                                if meteorits[i].show_on_background():
                                    meteorits[i].show()

                                if meteorits[i].select:
                                    quantity_meteorits = quantity_meteorits + 1   

                                if meteorits[i].select or meteorits[i].delite():
                                    del meteorits[i]
                                else:
                                    i = i+1

                            if len(meteorits) < 2:
                                meteorits.append(TaskWeapons(width, int(random(place_task.y2 - place_task.r2/2, place_task.y2 + place_task.r2/2)), int(random(2,7)), place_task.x2, place_task.y2, place_task.r2))
                        else:
                            player_crewmate.scale_fill()

            elif character_selection.select_to_choose == 2:
                impostor.show(player_crewmate_black)
                use.select_button = not True
                impostor.him_tasks()
                button_for_kill.show(kill_button)
                bot_crewmate.show()

                impostor.name = enter_name.text_

                if abs(impostor.dx) != 0:
                    #impostor.x = impostor.x - dx
                    #dx = 0
                    if impostor.dx <= 0:
                        impostor.x = impostor.x + abs(impostor.dx)
                        impostor.dx = 0
                    elif impostor.dx >= 0:
                        impostor.x = impostor.x - abs(impostor.dx)
                        impostor.dx = 0
                    if impostor.dy <= 0:
                        impostor.y = impostor.y + abs(impostor.dy)
                        impostor.dy = 0
                    elif impostor.dy >= 0:
                        impostor.y = impostor.y - abs(impostor.dy)
                        impostor.dy = 0
                        #while dx != 0:
                         #   impostor.x = impostor.x + 1
                         #   print(str(dx))
                         #   dx = dx + 1
                        #while dx != 0:
                         #   impostor.x = impostor.x - 1
                         #   print(str(dx))
                         #   dx = dx - 1

                if button_to_report.select_to_show_back == True:
                    filtrofwords.show()
                experimental_for_impostor.show_alive(experimental_red, player_crewmate.rx, player_crewmate.ry)
                experimental_for_impostor.show_not_alive(experimental_red_isnot_alive, 100, 100)
                if bot_crewmate.distance():
                    if not experimental_for_impostor.select:
                        bot_crewmate.report()
                        bot_crewmate.speed = 0
                        play_music_report.play()
    ###keyPressed
    if keyPressed:
        if start_game.select_game:

            if character_selection.select_to_choose == 1:
                if not bot_impostor.after_kill_u:
                    if key == 'a':
                        bot_impostor.x,bot_impostor.y = player_crewmate.move(LEFT,bot_impostor.x,bot_impostor.y,bot_impostor.speed)
                    elif key == 'd':
                        bot_impostor.x,bot_impostor.y = player_crewmate.move(RIGHT,bot_impostor.x,bot_impostor.y,bot_impostor.speed)
                    elif key == 'w':
                        bot_impostor.x,bot_impostor.y = player_crewmate.move(UP,bot_impostor.x,bot_impostor.y,bot_impostor.speed)
                    elif key == 's':
                        bot_impostor.x,bot_impostor.y = player_crewmate.move(DOWN,bot_impostor.x,bot_impostor.y,bot_impostor.speed)

            elif character_selection.select_to_choose == 2:
                if key == 'a':
                    bot_crewmate.x, bot_crewmate.y, experimental_for_impostor.x, experimental_for_impostor.y, place_task.x, place_task.y = impostor.move(LEFT,bot_crewmate.x,bot_crewmate.y,bot_crewmate.speed,experimental_for_impostor.x,experimental_for_impostor.y,place_task.x,place_task.y)
                elif key == 'd':
                    bot_crewmate.x, bot_crewmate.y, experimental_for_impostor.x, experimental_for_impostor.y, place_task.x, place_task.y = impostor.move(RIGHT,bot_crewmate.x,bot_crewmate.y,bot_crewmate.speed,experimental_for_impostor.x,experimental_for_impostor.y,place_task.x,place_task.y)
                elif key == 'w':
                    bot_crewmate.x, bot_crewmate.y, experimental_for_impostor.x, experimental_for_impostor.y, place_task.x, place_task.y = impostor.move(UP,bot_crewmate.x,bot_crewmate.y,bot_crewmate.speed,experimental_for_impostor.x,experimental_for_impostor.y,place_task.x,place_task.y)
                elif key == 's':
                    bot_crewmate.x, bot_crewmate.y, experimental_for_impostor.x, experimental_for_impostor.y, place_task.x, place_task.y = impostor.move(DOWN,bot_crewmate.x,bot_crewmate.y,bot_crewmate.speed,experimental_for_impostor.x,experimental_for_impostor.y,place_task.x,place_task.y)
                    
                    

def keyPressed():
    global file_for_name, character_selection, t, enter_name
    if character_selection.select_to_choose == 0:
        if enter_name.select:
            if enter_name.numb < 10:
                enter_name.text_ = enter_name.text_ + key
                enter_name.numb  = enter_name.numb  + 1
        #if ord(str(key)) == 8:
        #    enter_name.text_ = enter_name.text_[:-1]


def mousePressed():
    global use, meteorits, player_crewmate, start_game, exit_game, impostor, experimental_for_impostor, button_to_report, bot_crewmate, bot_impostor, press_to_go_out

    if not start_game.select_game:
        start_game.push_button()
        exit_game.push_button()

    if start_game.select_game:

        character_selection.choose_button()
        if character_selection.select_to_choose == 1:
            if place_task.distance(player_crewmate.x, player_crewmate.y, player_crewmate.rx, player_crewmate.ry):
                use.pressing()# give to us True or False
            if use.select:
                for i in range(0,len(meteorits)):
                    meteorits[i].boom()# give to us True or False
                press_to_go_out.pressing()

        elif character_selection.select_to_choose == 2:
            if experimental_for_impostor.select:
                if impostor.distance(experimental_for_impostor.x, experimental_for_impostor.y, player_crewmate.rx+100, player_crewmate.ry+50):
                    if button_for_kill.pressing():
                        impostor.x = experimental_for_impostor.x
                        impostor.y = experimental_for_impostor.y
                        impostor.dx = impostor.x - width/2
                        impostor.dy = impostor.y - height/2
                        experimental_for_impostor.select = not True
                    if not experimental_for_impostor.select:
                        button_to_report.pressing()

        elif character_selection.select_to_choose == 0:
            enter_name.pressing()
            bot_impostor.press_to_hide_impostor()
