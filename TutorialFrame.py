from xmlReader import *
from wxPython.wx import *
import wx
import config

import pygame, sys, time, random
from pygame.locals import *

ID_FILE_RUN = wxNewId()
ID_FILE_EXIT = wxNewId()
ID_HELP_ABOUT = wxNewId()
ID_LANGUAGE_ENGLISH = wxNewId()
ID_LANGUAGE_POLISH = wxNewId()
ID_LANGUAGE_TANGALOK = wxNewId()
userAnswers = ["","","","",""]

class TutorialFrame(wxFrame):
    def __init__(self,parent,id,title):
            #create frame
            wxFrame.__init__(self, parent, id, title="Pyoneer",size=(1000,800))
            # create status bar
            status = self.CreateStatusBar()
            reader = Readerr()
            choice = wxSingleChoiceDialog(self, "What language would you like to learn Python in?",'Choose Your Langugage',['English','Polish','Filipino'],wx.CHOICEDLG_STYLE)
            if choice.ShowModal() == wx.ID_OK:
                if choice.GetStringSelection() == 'English':
                    reader.reader1(0)
                elif choice.GetStringSelection() == 'Polish':
                    reader.reader1(1)
                elif choice.GetStringSelection() == 'Filipino':
                    reader.reader1(2)
            self.initialize()
            
            
    def initialize(self):
            icon = wx.Icon('pyoneer.ico',wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon)
            #create first menu file
            config.file_menu = wxMenu()
            config.file_menu.Append(ID_FILE_RUN, wordBank[13], wordBank[13])
            config.file_menu.AppendSeparator()
            config.file_menu.Append(ID_FILE_EXIT, wordBank[14],wordBank[14])
            #create help menu
            help_menu = wxMenu()
            help_menu.Append(ID_HELP_ABOUT, wordBank[15], wordBank[16])
            #create language menu
            language_menu = wxMenu()
            language_menu.Append(ID_LANGUAGE_ENGLISH,'English', wordBank[17] + ' English')
            language_menu.Append(ID_LANGUAGE_POLISH,'Polish', wordBank[17] + ' Polish')
            language_menu.Append(ID_LANGUAGE_TANGALOK,'Filipino', wordBank[17] + ' Filipino')
            menu_bar = wxMenuBar()
            menu_bar.Append(config.file_menu, wordBank[0])
            menu_bar.Append(language_menu, wordBank[1])
            menu_bar.Append(help_menu, wordBank[2])
            self.SetMenuBar(menu_bar)
            self.Center()

            self.intro()

            self.startTutorial=wx.Button(config.panel, 20, "Start Tutorial", (450, 600))
            self.Bind(wx.EVT_BUTTON, self.onRun, self.startTutorial)
            self.startTutorial.SetDefault()
            self.startTutorial.SetSize(self.startTutorial.GetBestSize())
    
            EVT_MENU(self,ID_FILE_RUN, self.onRun)
            EVT_MENU(self,ID_LANGUAGE_ENGLISH, self.readEnglish)
            EVT_MENU(self,ID_LANGUAGE_POLISH, self.readPolish)
            EVT_MENU(self,ID_LANGUAGE_TANGALOK, self.readFilipino)

    def intro(self):
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')

            header = wx.StaticText(config.panel, -1, wordBank[18], (220, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)

            jpg = wx.Image('pyoneer.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            wx.StaticBitmap(config.panel, -1, jpg, (330, 100), (jpg.GetWidth(), jpg.GetHeight()))

            header = wx.StaticText(config.panel, -1, wordBank[19], (200, 250))
            font = wx.Font(15, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)

            header = wx.StaticText(config.panel, -1, wordBank[20], (200, 450))
            font = wx.Font(15, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)
            
    # Create an accelerator table
   
            
    def readEnglish(self,evt):   
            reader = Readerr()
            reader.reader1(0)
            self.Destroy()
            ##self.initialize()

    def readPolish(self,evt):   
            reader = Readerr()
            reader.Destroy(1)
            ##self.initialize()
    
    def readFilipino(self,evt):   
            reader = Readerr()
            reader.reader1(2)
            self.Destroy()
           ## self.initialize()
            
    def onRun(self,evt):
            config.file_menu.Enable(ID_FILE_RUN,False)
            self.startTutorial.Hide()
            config.panel.Hide()
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')
            
            str = "CHAPTER 1"
            header = wx.StaticText(config.panel, -1, str, (360, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)
            
            context=wx.StaticText(config.panel,-1, wordBank[6],(100,90))
            font2 = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            context.SetFont(font2)

            jpg = wx.Image('variable.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            wx.StaticBitmap(config.panel, -1, jpg, (100, 550), (jpg.GetWidth(), jpg.GetHeight()))
            
            nextSection=wx.Button(config.panel, 10, "Exam", (800, 650))
            self.Bind(wx.EVT_BUTTON, self.backBone, nextSection)
            nextSection.SetDefault()
            nextSection.SetSize(nextSection.GetBestSize())
            
            
    def textSection2(self):
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')
            
            str = "CHAPTER 2"
            header = wx.StaticText(config.panel, -1, str, (360, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)
            
            context=wx.StaticText(config.panel,-1,wordBank[7],(100,90))
            font2 = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            context.SetFont(font2)

            jpg = wx.Image('list.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            wx.StaticBitmap(config.panel, -1, jpg, (100, 550), (jpg.GetWidth(), jpg.GetHeight()))
            
            nextSection=wx.Button(config.panel, 10, "Exam", (800, 650))
            self.Bind(wx.EVT_BUTTON, self.backBone2, nextSection)
            nextSection.SetDefault()
            nextSection.SetSize(nextSection.GetBestSize())
            
    def textSection3(self):
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')
            
            str = "CHAPTER 3"
            header = wx.StaticText(config.panel, -1, str, (360, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)

            context=wx.StaticText(config.panel,-1,wordBank[8],(100,90))
            font2 = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            context.SetFont(font2)

            jpg = wx.Image('comparison.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            wx.StaticBitmap(config.panel, -1, jpg, (770, 380), (jpg.GetWidth(), jpg.GetHeight()))
            
            nextSection=wx.Button(config.panel, 10, "Exam", (800, 650))
            self.Bind(wx.EVT_BUTTON, self.backBone3, nextSection)
            nextSection.SetDefault()
            nextSection.SetSize(nextSection.GetBestSize())
            
    def textSection4(self):
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')
            
            str = "CHAPTER 4"
            header = wx.StaticText(config.panel, -1, str, (360, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)

            context=wx.StaticText(config.panel,-1,wordBank[9],(100,90))
            font2 = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            context.SetFont(font2)

            jpg = wx.Image('decision_making.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            wx.StaticBitmap(config.panel, -1, jpg, (720, 250), (jpg.GetWidth(), jpg.GetHeight()))
            
            nextSection=wx.Button(config.panel, 10, "Exam", (800, 650))
            self.Bind(wx.EVT_BUTTON, self.backBone4, nextSection)
            nextSection.SetDefault()
            nextSection.SetSize(nextSection.GetBestSize())

    def textSection5(self):
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')
            
            str = "CHAPTER 5"
            header = wx.StaticText(config.panel, -1, str, (360, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)

            context=wx.StaticText(config.panel,-1,wordBank[10],(100,90))
            font2 = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            context.SetFont(font2)

            jpg = wx.Image('loop (Custom).jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            wx.StaticBitmap(config.panel, -1, jpg, (740, 250), (jpg.GetWidth(), jpg.GetHeight()))
            
            nextSection=wx.Button(config.panel, 10, "Exam", (800, 650))
            self.Bind(wx.EVT_BUTTON, self.backBone5, nextSection)
            nextSection.SetDefault()
            nextSection.SetSize(nextSection.GetBestSize())

    def textSection6(self):
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')
            
            str = "CHAPTER 6"
            header = wx.StaticText(config.panel, -1, str, (360, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)

            context=wx.StaticText(config.panel,-1,wordBank[11],(100,90))
            font2 = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            context.SetFont(font2)

            nextSection=wx.Button(config.panel, 10, "Exam", (800, 650))
            self.Bind(wx.EVT_BUTTON, self.backBone6, nextSection)
            nextSection.SetDefault()
            nextSection.SetSize(nextSection.GetBestSize())

    def finalText(self):
            config.panel = wx.Window(self,size=(1000,770))
            self.SetBackgroundColour('#00ffea')
            
            str = "Final Test" 
            header = wx.StaticText(config.panel, -1, str, (360, 10))
            font = wx.Font(30, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            header.SetFont(font)

            context=wx.StaticText(config.panel,-1, wordBank[12],(100,90))
            font2 = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
            context.SetFont(font2)

            jpg = wx.Image('well done.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            wx.StaticBitmap(config.panel, -1, jpg, (270, 250), (jpg.GetWidth(), jpg.GetHeight()))
            
            nextSection=wx.Button(config.panel, 10, "Exam", (800, 650))
            self.Bind(wx.EVT_BUTTON, self.backBone7, nextSection)
            nextSection.SetDefault()
            nextSection.SetSize(nextSection.GetBestSize())
            
    def backBone(self,evt):
            while self.section1Exam() == false:
                    pass
            config.panel.Hide()
            self.textSection2()
    def backBone2(self,evt):
            while self.section2Exam() == false:
                    pass
            config.panel.Hide()
            self.textSection3()
    def backBone3(self,evt):
            while self.section3Exam() == false:
                    pass
            config.panel.Hide()
            self.textSection4()
    def backBone4(self,evt):
            while self.section4Exam() == false:
                    pass
            config.panel.Hide()
            self.textSection5()
    def backBone5(self,evt):
            while self.section5Exam() == false:
                    pass
            config.panel.Hide()
            self.textSection6()
    def backBone6(self,evt):
            while self.section6Exam() == false:
                    pass
            config.panel.Hide()
            self.finalText()
    def backBone7(self,evt):      
            while self.finalExam() == false:
                    pass
            self.Destroy()

            import myMenuApp
            print "well done you reached the End :)"
            
    def checkSection(self, userAnswers, correctAnswers):
            score = 0
            count = 0
            while (count < 5):
                if userAnswers[count] == correctAnswers[count]:
                    score += 20
                count += 1

            if score >= 80:
                return True #passed
            else:
                return False
                                    
    def proceed(self):
            dlg = wxMessageDialog(self, wordBank[21] ,'Result', wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            
    def tryAgain(self):
            dlg = wxMessageDialog(self, wordBank[22] ,'Result', wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            
    def section1Exam(self):
            pass
            """test = wxSingleChoiceDialog(self, '1. ' + wordBank[23] + '\n      num = 1  ','Section One',['(a) int','(b) string','(c) double'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[0] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, '2. ' + wordBank[23] + ' \n      num = 5.6  ','Section One',['(a) int','(b) string','(c) double'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[1] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, '3. ' + wordBank[23] + '  \n      num = 8.0  ','Section One',['(a) int','(b) string','(c) double'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[2] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, "4. " + wordBank[23] + "  \n      num = 'four' ",'Section One',['(a) int','(b) string','(c) double'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, '5. ' + wordBank[23] + '  \n      num = 5 ','Section One',['(a) int','(b) string','(c) double'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[4] = test.GetStringSelection()
                    test.Destroy()
            section1Ans = ['(a) int','(c) double','(c) double','(b) string','(a) int']

            if self.checkSection(userAnswers, section1Ans) == true:
                    self.proceed()
            else:
                    self.tryAgain()
            return self.checkSection(userAnswers, section1Ans)"""
                          
    def section2Exam(self):
            pass
            """test = wxSingleChoiceDialog(self, wordBank[24],'Section Two',['(a) list = empty','(b) list = []','(c) list = [_]'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[0] = test.GetStringSelection()
                    test.Destroy()
                    
            test = wxSingleChoiceDialog(self, wordBank[25],'Section Two',['(a) list[1]','(b) list[]','(c) list[0]'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[1] = test.GetStringSelection()
                    test.Destroy()
                    
            test = wxSingleChoiceDialog(self, wordBank[26],'Section Two',['(a) Fruit[5]','(b) Fruit[3]','(c) Fruit[1]'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[2] = test.GetStringSelection()
                    test.Destroy()
                    
            test = wxSingleChoiceDialog(self, wordBank[27],'Section Two',['(a) print Fruit[2]','(b) Fruit[0]','(c) print Fruit[0]'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetStringSelection()
                    test.Destroy()
                    
            test = wxSingleChoiceDialog(self, wordBank[28],'Section Two',['(a) Fruit[0] = watermelon','(b) Fruit[2] = watermelon','(c) Fruit = watermelon'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[4] = test.GetStringSelection()
                    test.Destroy()       
            section2Ans = ["(b) list = []","(c) list[0]","(c) Fruit[1]","(c) print Fruit[0]","(a) Fruit[0] = watermelon"]

            if self.checkSection(userAnswers, section2Ans) == true:
                    self.proceed()
            else:
                    self.tryAgain()
            return self.checkSection(userAnswers, section2Ans)"""
            
    def section3Exam(self):
            pass
            """test = wxTextEntryDialog(None, "1. " + wordBank[29] + " 9*9 ",'Section Three Q1','')
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[0] = test.GetValue()
                    test.Destroy()
            test = wxTextEntryDialog(None, "2. " + wordBank[29] + " 9**2 ",'Section Three Q2','')
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[1] = test.GetValue()
                    test.Destroy()
            test = wxTextEntryDialog(None, "3. " + wordBank[29] + " 81%9 ",'Section Three Q3','')
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[2] = test.GetValue()
                    test.Destroy()
            test = wxTextEntryDialog(None, "4. " + wordBank[29] + " 2 > 5 (True or False) ",'Section Three Q4','')
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetValue()
                    test.Destroy()
            test = wxTextEntryDialog(None, "1. " + wordBank[29] + " 5 > 9 (True or False) ",'Section Three Q5','')
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[4] = test.GetValue()
                    test.Destroy()
            section3Ans = ["81","81","0","False","False"]

            if self.checkSection(userAnswers, section3Ans) == true:
                    self.proceed()
            else:
                    self.tryAgain()
            return self.checkSection(userAnswers, section3Ans)"""
            
    def section4Exam(self):
            pass
            """test = wxSingleChoiceDialog(self, wordBank[30],'Section Four Q1',['(a) if five == 5:','(b) if 5=5','(c) if 5===5:'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[0] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[31],'Section Four Q2',['(a) if five < 4:','(b) if five == 5:','(c) if five <= 50:'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[1] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[32],'Section Four Q3',['(a) if five === 5','(b) if num:','(c) if True:'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[2] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[33] + "\n if num == 5: \n    print num \n else: \n    print 4",'Section Four Q4',['(a) 5','(b) 4','(c) None'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[34],'Section Four Q5',['(a) if statemnet must have a condition','(b) if statement must have else option','(c) else statement can exist on its own'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[4] = test.GetStringSelection()
                    test.Destroy()
            section4Ans = ["(a) if five == 5:","(a) if five < 4:","(c) if True:","(a) 5","(a) if statemnet must have a condition"]

            if self.checkSection(userAnswers, section4Ans) == true:
                    self.proceed()
            else:
                    self.tryAgain()
            return self.checkSection(userAnswers, section4Ans)"""
            
    def section5Exam(self):
            pass
            """test = wxSingleChoiceDialog(self, wordBank[35] + " \n num = 1 \n while num==1 \n        print 'Hello'",'Section Five',['(a) Yes','(b) No'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[0] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[36] + " \n num = 5\n while num > 1:\n    print 'Hello' \n    num = num -1",'Section Five',['0','1','2','3','4','5'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[1] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[37] + " \n list=[1,2,3,4] \n for x in list: \n   print x",' Section Five',['(a) Nothing','(b) Print name List','(c) Print all elemnets of List'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[2] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[38] + " \n word = ['H','a','p','p','y'] \n for letter in word: \n    print letter + ' '",'Section Five',['(a) y p p a H','(b) H a p p y','(c) letter'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[39],'Section One',['(a) Saves from writting many lines of code.','(b) No Nenifits','(c) Faster Program'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[4] = test.GetStringSelection()
                    test.Destroy()
            section5Ans = ["(b) No","4","(c) Print all elemnets of List","(b) H a p p y","(a) Saves from writting many lines of code."]

            if self.checkSection(userAnswers, section5Ans) == true:
                    self.proceed()
            else:
                    self.tryAgain()
            return self.checkSection(userAnswers, section5Ans)"""

    def section6Exam(self):
            pass
            """test = wxSingleChoiceDialog(self, wordBank[40],'Section Six',["(a) def functionName","(b) def functionName;","(c) def functionName():"  ],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[0] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[41],'Section Six',['(a) def args();','(b) def args(name,coins):','(c) def args(X):'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[1] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[42],' Section Six',['(a) def functionName()','(b) call functionName()','(c) functionName()'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[2] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[43],'Section Six',['(a) args()','(b) args(Jack,100)','(c) letter'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[44] + " \n def greater(x,y): \n   if x > y: \n       print 'Awesome' \n      else: \n       print 'Not Good'",'Section Six',['(a) Awesome','(b) Not Good','(c) greater'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[4] = test.GetStringSelection()
                    test.Destroy()
            section6Ans = ["(c) def functionName():","(b) def args(name,coins):","(c) functionName()","(b) args(Jack,100)","(b) Not Good"]

            if self.checkSection(userAnswers, section6Ans) == true:
                    self.proceed()
            else:
                    self.tryAgain()
            return self.checkSection(userAnswers, section6Ans)"""

    def finalExam(self):
            test = wxSingleChoiceDialog(self, wordBank[45],'Final Test',['(a) alphabet, numbers and roman numerals','(b) int, strings and double','(c) Fruits, Pets and Humans'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[0] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[46],'Final Test',['(a) <, >, <=, >=, !=', '(b) +, -, *, /, %', '(c) I, II, III, IV, V'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[1] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[47],'Final Test',['(a) if num:','(b) if num == 3:', '(c) if 3=3'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[48] + " \n     while ......:",'Final Test',['(a) A condition','(b) A picture','(c) An if statement'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[3] = test.GetStringSelection()
                    test.Destroy()
            test = wxSingleChoiceDialog(self, wordBank[49] ,'Final Test',['(a) if cow == 12:','(b) def count(cows):', '(c) print "A dozen of Cows"'],wx.CHOICEDLG_STYLE)
            if test.ShowModal() == wx.ID_OK:
                    userAnswers[4] = test.GetStringSelection()
                    test.Destroy()
            finalAns = ["(b) int, strings and double","(a) <, >, <=, >=, !=", "(b) if num == 3:", "(a) A condition", "(b) def count(cows):"]
                                                
            if self.checkSection(userAnswers, finalAns) == true:
                    self.proceed()
            else:
                    self.tryAgain()
            return self.checkSection(userAnswers, finalAns)
     
class myTutorialApp(wxApp):
    def OnInit(self):
            frame = TutorialFrame(NULL, -1, 'Tutorial')
            frame.Show(true)
            self.SetTopWindow(frame)
            return true

app=myTutorialApp(0)
app.MainLoop()
