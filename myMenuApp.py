from wxPython.wx import *
import wx, threading

#import pygame, sys, time, random
#$from pygame.locals import *
import config
import SnakeTest
import SnakeTest2
#create id for each event
ID_FILE_RESTART = wxNewId()
ID_FILE_RUN = wxNewId()
ID_FILE_RUN2 = wxNewId()
ID_FILE_EXIT = wxNewId()
ID_HELP_ABOUT = wxNewId()
ID_FUNCTION_MOVEUP = wxNewId()
ID_FUNCTION_MOVEDOWN = wxNewId()
ID_FUNCTION_MOVELEFT = wxNewId()
ID_FUNCTION_MOVERIGHT = wxNewId()
ID_FUNCTION_MOVEPICK = wxNewId()
ID_FUNCTION_MOVECHECK = wxNewId()
ID_OWN_IF = wxNewId()
ID_LANGUAGE_ENGLISH = wxNewId()
ID_LANGUAGE_POLISH = wxNewId()
ID_LANGUAGE_TANGALOK = wxNewId()


class myFrame(wxFrame):
    def __init__(self, parent, id, title):
        # create a frame
        wxFrame.__init__(self, parent, id, title,size=(800,600))
        status = self.CreateStatusBar()
        # create splitter
        self.splitter = wx.SplitterWindow(self)
        # create file menu
        file_menu = wxMenu()
        file_menu.Append(ID_FILE_RESTART, 'Restart level','Restart current level')
        file_menu.Append(ID_FILE_RUN, 'Run code','Run code')
        file_menu.Append(ID_FILE_RUN2, 'Run code2','Run code2')
        file_menu.AppendSeparator()
        file_menu.Append(ID_FILE_EXIT, 'E&xit\tAlt+X','Exit program')
        # create the 'Help' menu
        config.help_menu = wxMenu()
        config.help_menu.Append(ID_HELP_ABOUT, 'About','Help about the system')
        #create function menu
        function_menu = wxMenu()
        function_menu.Append(ID_FUNCTION_MOVEUP,'Move up','Move snake one cell up')
        function_menu.Append(ID_FUNCTION_MOVEDOWN,'Move down','Move snake one cell down')
        function_menu.Append(ID_FUNCTION_MOVELEFT,'Move left','Move snake one cell left')
        function_menu.Append(ID_FUNCTION_MOVERIGHT,'Move rigtht','Move snake one cell right')
        function_menu.Append(ID_FUNCTION_MOVEPICK,'Pick treasure','Tell snake to pick up treasure')
        function_menu.Append(ID_FUNCTION_MOVECHECK,'Check for obstacles','Check for obstacles')
        #create own function menu
        own_menu = wxMenu()
        own_menu.Append(ID_OWN_IF,'Create if statement','Create your own if statement')
        #create language menu
        language_menu = wxMenu()
        language_menu.Append(ID_LANGUAGE_ENGLISH,'English','Change language to English')
        language_menu.Append(ID_LANGUAGE_POLISH,'Polish','Change language to Polish')
        language_menu.Append(ID_LANGUAGE_TANGALOK,'Tangalok','Change language to Tangolok')
        # create menu bar and add items to it
        menu_bar = wxMenuBar()
        menu_bar.Append(file_menu, 'File')
        menu_bar.Append(function_menu, 'Function')
        menu_bar.Append(own_menu, 'Create Function')
        menu_bar.Append(language_menu,'Choose Language')
        menu_bar.Append(config.help_menu, 'Help')
        # set the menu bar (tells the system we're done)
        self.SetMenuBar(menu_bar)
        self.Center()
        
        # Split the screen
        config.panel1 = wx.Window(self.splitter,style=wx.BORDER_SUNKEN)
        config.codebox=wx.TextCtrl(config.panel1,-1,style=wx.TE_MULTILINE,size=(400,600))

        config.panel2 = wx.Window(self.splitter,style=wx.BORDER_SUNKEN)
        #wx.StaticText(config.panel2,-1,"Snake Game")

        # Create an accelerator table
        xit_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onAltX, id=xit_id)
        self.accel_tbl = wx.AcceleratorTable([((wx.ACCEL_ALT, ord('X'), xit_id))])
        self.SetAcceleratorTable(self.accel_tbl)
        
        #Disable the help_about button
        config.help_menu.Enable(ID_HELP_ABOUT,False)

        self.splitter.SplitVertically(config.panel1,config.panel2,0)
        # associate event with each id for menu items
        EVT_MENU(self, ID_FILE_RESTART, self.ToDo)
        EVT_MENU(self, ID_FILE_RUN, self.onRun)
        EVT_MENU(self, ID_FILE_RUN2, self.onRun2)
        EVT_MENU(self, ID_FILE_EXIT, self.OnFileExit)
        EVT_MENU(self, ID_FUNCTION_MOVEUP, self.onMoveUp)
        EVT_MENU(self, ID_FUNCTION_MOVEDOWN, self.onMoveDown)
        EVT_MENU(self, ID_FUNCTION_MOVELEFT, self.onMoveLeft)
        EVT_MENU(self, ID_FUNCTION_MOVERIGHT, self.onMoveRight)
        EVT_MENU(self, ID_FUNCTION_MOVEPICK, self.onMovePick)
        EVT_MENU(self, ID_FUNCTION_MOVECHECK, self.onMoveCheck)
        EVT_MENU(self, ID_OWN_IF,self.ToDo)
        EVT_MENU(self,ID_HELP_ABOUT, self.OnHelp)
        EVT_MENU(self,ID_LANGUAGE_ENGLISH, self.ToDo)
        EVT_MENU(self,ID_LANGUAGE_POLISH, self.ToDo)
        EVT_MENU(self,ID_LANGUAGE_TANGALOK, self.ToDo)

        self.listOfMoves = []
        # Create event when user decides to close the program
    def onAltX(self, event):
        """"""
        self.Close(true)
 
    def OnFileExit(self, evt):
        dlg = wxMessageDialog(self, 'Exit Program?', 'Warning!',
                              wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            self.Close(true)
        else:
            dlg.Destroy()
        # Create event when user click on help
    def OnHelp(self,evt):
        dlg = wxMessageDialog(self,'Programming tool v 1.0' ,'Version', wxOK | wxICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        # Create event when move up is choosen
    def onMoveUp(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move up ?',wxYES_NO | wxICON_QUESTION)
        config.help_menu.Enable(ID_HELP_ABOUT,True)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('MoveUp()\n')
            self.listOfMoves.append("moveUp()")
        else:
            dlg.Destroy()
        # Create event when move down is choosen
    def onMoveDown(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move Down ?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('MoveDown()\n')
        else:
            dlg.Destroy()
        # Create event when move left is choosen
    def onMoveLeft(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move Left ?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('MoveLeft()\n')
        else:
            dlg.Destroy()
        # Create event when move right is choosen
    def onMoveRight(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move Right?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('MoveRight()\n')
        else:
            dlg.Destroy()
        # Create event when pick is choosen
    def onMovePick(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move pick?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('Pick()\n')
        else:
            dlg.Destroy()
        # Create event when move up is choosen
    def onMoveCheck(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move check?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('checkFront()\n')
        else:
            dlg.Destroy()
        # Create Test for running snake game within tool
    def onRun(self,evt):
        dlg = wxMessageDialog(self,'Are you sure you want to play the game?','Are you sure?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            t = threading.Thread(target=self.crap)
            t.start()
            print "thread started \n"
            t.join()
            print "thread stoped \n"
            dlg.Destroy()
            
        else:
            dlg.Destroy()
        # Create Test Event for each function in the menu
    def onRun2(self,evt):
        dlg = wxMessageDialog(self,'Are you sure you want to play the game?','Are you sure?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            t2 = threading.Thread(target=self.crap2)
            t2.start()
            t2.join()
            dlg.Destroy()
            
        else:
            dlg.Destroy()
    def crap(self):
        print "Class intitilized \n "
        test = SnakeTest.SnakeTest(self.listOfMoves)
        print "Class finisged "
    def crap2(self):
        test =SnakeTest2.SnakeTest2(self.listOfMoves)
    def ToDo(self, evt):
        dlg = wxMessageDialog(self, 'Not Yet Implimented!', 'ToDo',
                             wxOK | wxICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
class myMenuApp(wxApp):
    def OnInit(self):
        frame = myFrame(NULL, -1, 'Programming Tool with Game')
        frame.Show(true)
        self.SetTopWindow(frame)
        return true

app=myMenuApp(0)
app.MainLoop()


