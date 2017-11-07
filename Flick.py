import pickle,random,time,os,winsound
def title():
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print "                  H======         @         []     "
    print "                  H       W            __   [] //   "
    print "                  H===    W       I  []     []//   "
    print "                  H       W       I  []     []\\\  "
    print "                  H       DDDDD   I  []__   [] \\\  "
    print ""
    print "                                                 -A Football Simulator"
    print ""
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print ""
print ""
print "                  H======         @         []     "
winsound.Beep(500,600)
print "                  H       W            __   [] //   "
winsound.Beep(550,700)
print "                  H===    W       I  []     []//   "
winsound.Beep(600,800)
print "                  H       W       I  []     []\\\  "
winsound.Beep(700,900)
print "                  H       DDDDD   I  []__   [] \\\  "
print "                                                 "
winsound.Beep(750,920)
print "                                                 -A Football Simulator"
time.sleep(2)
os.system('cls')
class team:
    def __init__(self):
        #Team name
        self.name=''
        #Formation Variables
        self.d=0
        self.m=0
        self.a=0
        #Defense positioned players
        self.dfnse=''
        self.defense=[]
        #Mid positioned players
        self.md=''
        self.mid=[]
        #Attack positioned players
        self.atck=''
        self.attack=[]
        #Goalie
        self.goalie=''
        #Menu Option
        self.choice=''
        self.option=''

    def read(self):
        self.name=raw_input("ENTER TEAM NAME: ")
        self.name=self.name.upper()
        print ''
        print 'FORMATION-       (For example: 4-4-2  ;Should add up to 10)'
        self.d=input('Enter no. of DEFENSE           :')
        self.m=input('Enter no. of MIDFIELD(min 1)   :')
        self.a=input('Enter no. of attack  (min 1)   :')
        print 'DEFENSE'
        for i in range(self.d):
            self.dfnse=raw_input('ENTER DEFENCE PLAYER NAME - ')
            self.defense.append(self.dfnse.upper())

        print "MID FIELD"
        for i in range(self.m):
            self.md=raw_input('ENTER MIDFIELD PLAYER NAME - ')
            self.mid.append(self.md.upper())

        print "ATTACK"
        for i in range(self.a):
            self.atck=raw_input('ENTER ATTACK PLAYER NAME - ')
            self.attack.append(self.atck.upper())

        print "GOALIE"
        for i in range(1):
            self.goalie=raw_input('ENTER GOALIE NAME - ')
            self.goalie=self.goalie.upper()
        print "YOUR TEAM SUCCESSFULLY CREATED!"
        print ''
        

    def show_team(self):
        print '_______________________________________________________________'
        print '             ',self.name
        print '---------------------------------------------------------------'
        print '                                     FORMATION'
        print '                                     1-',self.d,'-',self.m,'-',self.a
        print self.goalie
        for i in range(len(self.defense)):
            print self.defense[i]
        for i in range(len(self.mid)):
            print self.mid[i]
        for i in range(len(self.attack)):
            print self.attack[i]
        print '_______________________________________________________________'
def showteams():
    allteams=[]
    f=open('D:\TEAM LIST.dat','rb+')
    try:
        stnum=1
        while True:
            p=pickle.load(f)
            print stnum,')',p.name
            stnum=stnum+1
            allteams.append(p)
    except EOFError:
                pass
    f.close()
    return allteams
    
def play(teamA,teamB):
    winner=teamA
    scoreA=0
    scoreB=0
    timedisplay=''
    ball=teamA
    ballchance=[0,0,0,0,0,0,0,0,0,1]
    inDchance=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    shoot=['cross','freekick','indee']
    goalchance=[0,0,0,0,1]
    timer=1
    everyone=[]
    print '                               KICKOFF!'
    time.sleep(2.5)
    os.system('cls')
    while timer<91:
        title()
        print '========================================================================='
        print '                                 ',timer
        print timedisplay
        print '-------------------------------------------------------------------------'
        print '                     ',teamA.name,'           ',teamB.name,'         ',scoreA,'-',scoreB
        print ''
        if ball==teamA:
            print '                     @'
        else:
            print '                                             @'
        print ''
        print ''
        if random.choice(inDchance)==1:
            shoo=random.choice(shoot)
            if shoo=='cross':
                wing=random.choice(ball.mid)
                print '                     ',wing,'CROSSES THE BALL!!'
                time.sleep(3)
                if random.choice(goalchance)==1:
                    
                    shooter=random.choice(ball.attack)
                    print '                 ',shooter,' PROVIDES A MARVELOUS FINISH'
                    time.sleep(3)
                    if ball==teamA:
                        scoreA+=1
                        ball=teamB
                    else:
                        scoreB+=1
                        ball=teamA
                else:
                    print '                     ','CLOSE!!!!'
                    time.sleep(3)
                    if ball!=teamA:
                        ball=teamA
                    else:
                        ball=teamB
                    
            if shoo=='freekick':
                print '                     FOUL!!',ball.name,'GETS A FREEKICK.'
                everyone=ball.attack+ball.mid+ball.defense
                e=random.choice(everyone)
                time.sleep(2.5)
                print '                     ',e,'TAKES THE FREEKICK!!!'
                time.sleep(2.5)
                if random.choice(goalchance)==1:
                    print ''
                    print '                     ',e,' MAKES IT THROUGH TO THE NET!!'
                    time.sleep(3)

                    if ball==teamA:
                        scoreA+=1
                        ball=teamB
                    else:
                        scoreB+=1
                        ball=teamA
                else:
                    print '                     ',e, 'MISSES!!!!'
                    time.sleep(2.5)

                    if ball!=teamA:
                        ball=teamA
                    else:
                        ball=teamB
            if shoo=='indee':
                striker=random.choice(ball.attack)
                print '                     ',striker,'GETS THE BALL IN THE DEE'
                time.sleep(3)
                if random.choice(goalchance)==1:
                    print '                         ',striker ,'SCORES!!'
                    time.sleep(2.5)
                    if ball==teamA:
                        scoreA+=1
                        ball=teamB
                    else:
                        scoreB+=1
                        ball=teamA
                    
                else :
                    dee=['corner','miss']
                    if random.choice(dee)=='miss':
                        print '                         ',striker,' FUMBLES!!'
                        time.sleep(2.5)
                    else:
                        print '                     GONE FOR A CORNER!!!'
                        time.sleep(3)
                        print '                 ',random.choice(ball.mid),'TAKES THE CORNER.'
                        time.sleep(3)
                        print '                 ',random.choice(ball.attack),'HEADS IT INSIDE!'
                        time.sleep(3)
                        if ball==teamA:
                            scoreA+=1
                            ball=teamB
                        else:
                            scoreB+=1
                            ball=teamA
        if random.choice(ballchance)==1:
            if ball!=teamA:
                ball=teamA
            else:
                ball=teamB
        time.sleep(.05)
        timer=timer+1
        if timer<75:
            timedisplay+='|'
        os.system('cls')

    if scoreA>scoreB:
        
        print '                      ',teamA.name
        print ''
        print ''
        print '                       W',
        time.sleep(1)
        print 'I',
        time.sleep(1)
        print 'N',
        time.sleep(1)
        print 'S'
        time.sleep(.5)
        print ''
        print '                        ',scoreA,'-',scoreB
    elif scoreA<scoreB:
        print '                      ',teamB.name
        print ''
        print '                       W',
        time.sleep(1)
        print 'I',
        time.sleep(1)
        print 'N',
        time.sleep(1)
        print 'S'
        time.sleep(.5)
        print '                        ',scoreA,'-',scoreB
        winner=teamB
        
    else:
        print '             WHATA MATCH!!', ' THE SCORES ARE TIED '
        print ''
        time.sleep(2)
        print '                 PENALTIES STAND IN THE WAY OF THE WINNERS !'
        print ''
        time.sleep(1.5)
        print ''
        print '                      REFREE CALLS IT IN !'
        print ''
        time.sleep(2)
        penscoreA=0
        penscoreB=0
        penalty=['goal','blocked']
        PENA=teamA.mid+teamA.attack
        PENB=teamB.mid+teamB.attack
        print '============================================================='
        os.system('cls')
        for i in range(5):
            for j in range(2):
                print '---------- SCORE ------------------------------------------------'
                print teamA.name,' :',penscoreA
                print teamB.name,' :',penscoreB
                print '================================================================='
                if j==0:
                    print   teamA.name
                
                    pen=random.choice(penalty)
                    print '                         ',PENA[i],'TAKES THE PENALTY.'
                    print ''
                    time.sleep(3)
                    if pen=='goal':
                        print '                     ',PENA[i],' SCORES!!'
                        penscoreA+=1
                    if pen=='blocked':
                        print '                     ',teamB.goalie,'DOES A MIRACULOUS SAVE!!'
                    time.sleep(3)
                if j==1:
                    print teamB.name
                    pen=random.choice(penalty)
                    print '                         ',PENB[i],'TAKES THE PENALTY.'
                    print ''
                    time.sleep(3)
                    if pen=='goal':
                        print '                     ',PENB[i],' SCORES!!'
                        penscoreB+=1
                    if pen=='blocked':
                        print '                     ',teamA.goalie,'DOES A MIRACULOUS SAVE!!'
                    time.sleep(3)
        
        
        
        
        if penscoreA==penscoreB:
            os.system('cls')
            print '                                     MATCH GOES TO SUDDEN DEATH!!'
            time.sleep(3)
            while penscoreA==penscoreB:
                for j in range(2):
                    print '-----------------------------------------------------'
                    if j==0:
                        print teamA.name
                        pen=random.choice(penalty)
                        print '                         ',PENA[i],'TAKES THE PENALTY.'
                        print ''
                        time.sleep(3)
                        if pen=='goal':
                            print '                     ',PENA[i],' SCORES!!'
                            penscoreA+=1
                        if pen=='blocked':
                            print '                     ',teamB.goalie,'DOES A MIRACULOUS SAVE!!'
                        time.sleep(3)
                    if j==1:
                        print teamB.name
                        pen=random.choice(penalty)
                        print '                         ',PENB[i],'TAKES THE PENALTY.'
                        print ''
                        time.sleep(3)
                        if pen=='goal':
                            print '                     ',PENB[i],' SCORES!!'
                            penscoreB+=1
                        if pen=='blocked':
                            print '                     ',teamA.goalie,'DOES A MIRACULOUS SAVE!!'
                            time.sleep(3)
                if penscoreA>penscoreB:
        
                    print '                     ',teamA.name
                    print ''
                    print '                         W',
                    time.sleep(1)
                    print 'I',
                    time.sleep(1)
                    print 'N',
                    time.sleep(1)
                    print 'S'
                    time.sleep(.5)
                    print '                     ',scoreA,'-',scoreB
                    print '                     ','By Penalities.'
                if penscoreA<penscoreB:
                    print '                    ',teamB.name
                    print ''
                    print '                          W',
                    time.sleep(1)
                    print 'I',
                    time.sleep(1)
                    print 'N',
                    time.sleep(1)
                    print 'S'
                    time.sleep(.5)
                    print '                     ',scoreA,'-',scoreB
                    print '                     ','By Penalities.'
                    winner=teamB

        if penscoreA>penscoreB:
        
            print '                 ',teamA.name
            print ''
            print '                     W',
            time.sleep(1)
            print 'I',
            time.sleep(1)
            print 'N',
            time.sleep(1)
            print 'S'
            time.sleep(.5)
            print '                     ',scoreA,'-',scoreB
            print '                     ',penscoreA,'-',penscoreB
        if penscoreA<penscoreB:
            print '                 ',teamB.name
            print ''
            print '                            W',
            time.sleep(1)
            print 'I',
            time.sleep(1)
            print 'N',
            time.sleep(1)
            print 'S'
            time.sleep(.5)
            print '                          TEAM RESULTS!                                '
            print '                     ',scoreA,'-',scoreB
            print '                     ',penscoreA,'-',penscoreB
            winner=teamB
    print ""
    print ""
    raw_input('PRESS ENTER TO CONTINUE...')
    os.system('cls')
    return winner                            
choice='A'
while choice!='D':
    
    a=team()
    option=''
    title()
    print 'QUICK PLAY--------A'
    print 'TOURNAMENT--------B'
    print 'EDIT TEAMS--------C'
    print 'QUIT      --------D'
    print ''
    choice=raw_input('ENTER OPTION:')
    choice=choice.upper()
    os.system('cls')
    if choice=='D':
        break

    elif choice=='B':
        print "                             TOURNAMENT BEGINS!"
        print '----------------------------------------------------------------'
        users=4
        allteams=showteams()
        tourteams=[]
        print '----------------------------------------------------------------'
        print ''
        print 'CHOSE THE 4 TEAMS PARTICIPATING IN THE TOURNAMENT'
        
        for i in range(users):
            print ''
            print 'TEAM',i+1
            sname=raw_input('ENTER TEAM : ')
            sname=sname.upper()
            f=open('D:\TEAM LIST.dat','rb+')
            found=False
            
            try:
                while True:
                        
                    p=pickle.load(f)
                    if p.name==sname:
                        tourteams.append(p)
                        found=True
                    
            except EOFError:
                if found==False:
                    print 'TEAM NOT FOUND'
                    print 'PLEASE CLOSE TAB AND RE-ENTER TEAMS.'
                    raw_input()
            f.close()
        os.system('cls')    
        groupA=random.sample(tourteams,2)           #this gets 2 random items from tourteams
        groupB=list(set(tourteams)-set(groupA))
        print '----------------------------------------------'
        print groupA[0].name
        print '     VS'
        print groupA[1].name
        print ''
        print groupB[0].name
        print '     VS'
        print groupB[1].name
        print '-----------------------------------------------'
        raw_input('PRESS ENTER TO CONTINUE...')
        groupAwinner=play(groupA[0],groupA[1])
        groupBwinner=play(groupB[0],groupB[1])
        print '                         Two teams remain...'
        time.sleep(2)
        print '                     But only one will attain '
        time.sleep(2)
        print '                             GLORY!'
        time.sleep(1.5)
        print '                             '
        print '*****FINALS**************************************************'
        print ''
        print '             ',groupAwinner.name,' VS',groupBwinner.name
        
        print '.............................................................'
        print ''
        raw_input('PRESS ENTER TO CONTINUE...')
        os.system('cls')
        tourwin=play(groupAwinner,groupBwinner)
        print ''
        print '                         CONGRATULATIONS!!'
        print '                             '
        print '                  YOU HAVE WON THE TOURNEMENT !!!'
        print ''
        winsound.Beep(500,300)
        winsound.Beep(500,300)
        winsound.Beep(600,100)
        winsound.Beep(500,400)
        winsound.Beep(400,100)
        winsound.Beep(600,450)
            
            
    elif choice=='C':
        while option!='D':
            print 'SEARCH TEAM-----------A'
            print 'CREATE TEAM-----------B'
            print 'SHOW TEAMS -----------C'
            print 'RETURN TO MAIN MENU---D'
            option=raw_input('ENTER OPTION:')
            option=option.upper()
            if option=='A':
                print 'SEARCH TEAM'
                sname=raw_input('ENTER TEAM TO BE SEARCHED : ')
                sname=sname.upper()
                f=open('D:\TEAM LIST.dat','ab+')
                found=False
                try:
                    while True:
                        
                        p=pickle.load(f)
                        if p.name==sname:
                            p.show_team()
                            found=True
                except EOFError:
                    if found==False:
                        print 'TEAM NOT FOUND'
                f.close()
            elif option=='B':
                a.read()
                a.show_team()
                f=open('D:\TEAM LIST.dat','ab+')
                pickle.dump(a,f)
                f.close()
            elif option=='C':
                showteams()
            else:
                option=='D'
                break         
                
    else:
        print ''
        print 'QUICK PLAY'
        print ''
        teamlist=[]
        f=open('D:\TEAM LIST.dat','ab+')
        try:
            while True:
                p=pickle.load(f)
                teamlist.append(p)
        except EOFError:
            pass
        f.close()
        A=random.choice(teamlist)
        B=random.choice(teamlist)
        while A==B:
            A=random.choice(teamlist)
            B=random.choice(teamlist)
        play(A,B)
