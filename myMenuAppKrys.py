# This class caters for creating GUI for the frame where the user will be usig probelm solving skills
# to complete levels of snake game. The class will inherit librieries fron wxPython in order to create the GUI.

# Import all modlues needed for the class
from wxPython.wx import *
from xmlReader import *
import wx, threading
from wx.lib.wordwrap import wordwrap
import config
import SnakeTest2

#Create id for each event in menu
ID_FILE_RESTART = wxNewId()
ID_FILE_RUN = wxNewId()
ID_FILE_RUN2 = wxNewId()
ID_FILE_RUN3 = wxNewId()
ID_FILE_RUN4 = wxNewId()
ID_FILE_EXIT = wxNewId()
ID_HELP_ABOUT = wxNewId()
ID_FUNCTION_MOVEUP = wxNewId()
ID_FUNCTION_MOVEDOWN = wxNewId()
ID_FUNCTION_MOVELEFT = wxNewId()
ID_FUNCTION_MOVERIGHT = wxNewId()
ID_FUNCTION_MOVEWAIT = wxNewId()
ID_LANGUAGE_ENGLISH = wxNewId()
ID_LANGUAGE_POLISH = wxNewId()
ID_LANGUAGE_TANGALOK = wxNewId()
ID_LEVEL_1=wxNewId()
ID_LEVEL_2=wxNewId()
ID_LEVEL_3=wxNewId()
ID_LEVEL_4=wxNewId()

# Class which will create panel
class MyPanels(wx.Panel):
    # Initilize panel
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent)
        self.parent = parent
# Main class which create menu, frame, uses class MyPanels to create panels
# Deals with the passing the user-created code the the snake game, as well
# catering for translation using class xmlReader.
class myFrame(wxFrame):
    # Function to initilize the main frame
    def __init__(self, parent, id, title):
        # create a frame with size 1000 by 600
        wxFrame.__init__(self, parent, id, title,size=(1000,600))
        # Create status bar
        status = self.CreateStatusBar()
        # Create instaces of Reader class
        self.reader = Readerr()
        self.reader.reader1(0)
        # Call method initilize
        self.initialize()
        # Call method sizee
        self.sizee()
        
    # Function which creates manu with menu items
    # It binds all menu items with specific event 
    def initialize(self):
        
        # Create icon for window
        icon = wx.Icon('pyoneer.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        # create file menu which will run supplied code
        file_menu = wxMenu()
        file_menu.Append(ID_FILE_RESTART, 'Restart level','Restart current level')
        file_menu.Append(ID_FILE_RUN, 'Run Level 1','Run Level 1')
        file_menu.Append(ID_FILE_RUN2, 'Run Level 2','Run Level 2')
        file_menu.Append(ID_FILE_RUN3, 'Run Level 3','Run Level 3')
        file_menu.Append(ID_FILE_RUN4, 'Run Level 4','Run Level 4')
        file_menu.AppendSeparator()
        # Add icon the the Exit item in menu
        quitIcon = wx.MenuItem(file_menu,ID_FILE_EXIT, 'E&xit\tCtrl+X','Exit program')
        quitIcon.SetBitmap(wx.Bitmap('exit.png'))
        file_menu.AppendItem(quitIcon)
        # create the 'Help' menu
        config.help_menu = wxMenu()
        # Add icon to the help menu 
        helpIcon = wx.MenuItem(config.help_menu,ID_HELP_ABOUT, 'About\t Ctrl+H','Help about the system')
        helpIcon.SetBitmap(wx.Bitmap('help.png'))
        config.help_menu.AppendItem(helpIcon)
        # Create level menu,whcih will display starting image of choosen snake level
        level_menu = wxMenu()
        level_menu.Append(ID_LEVEL_1,'Level 1','Level 1')
        level_menu.Append(ID_LEVEL_2,'Level 2','Level 2')
        level_menu.Append(ID_LEVEL_3,'Level 3','Level 3')
        level_menu.Append(ID_LEVEL_4,'Level 4','Level 4')
        #create function menu which will generate code choosen by user
        function_menu = wxMenu()
        function_menu.Append(ID_FUNCTION_MOVEUP,'Move up','Move snake one cell up')
        function_menu.Append(ID_FUNCTION_MOVEDOWN,'Move down','Move snake one cell down')
        function_menu.Append(ID_FUNCTION_MOVELEFT,'Move left','Move snake one cell left')
        function_menu.Append(ID_FUNCTION_MOVERIGHT,'Move rigtht','Move snake one cell right')
        function_menu.Append(ID_FUNCTION_MOVEWAIT,'Wait','Snake waits one move')
        #create language menu to change language 
        language_menu = wxMenu()
        language_menu.Append(ID_LANGUAGE_ENGLISH,'English','Change language to English')
        language_menu.Append(ID_LANGUAGE_POLISH,'Polish','Change language to Polish')
        language_menu.Append(ID_LANGUAGE_TANGALOK,'Tangalok','Change language to Tangolok')
        # create menu bar and add menu items to it
        menu_bar = wxMenuBar()
        menu_bar.Append(file_menu, wordBank[0])
        menu_bar.Append(level_menu, wordBank[3])
        menu_bar.Append(function_menu, wordBank[4])
        menu_bar.Append(language_menu,wordBank[1])
        menu_bar.Append(config.help_menu, wordBank[2])
        
        # set the menu bar (tells the system we're done)
        self.SetMenuBar(menu_bar)
        # Position the frame in the center of the screen
        self.Center()
        
        # Associate event with each id for menu items
        EVT_MENU(self, ID_FILE_RESTART, self.ToDo)
        EVT_MENU(self, ID_FILE_RUN, self.onRun)
        EVT_MENU(self, ID_FILE_RUN2, self.onRun2)
        EVT_MENU(self, ID_FILE_RUN3, self.onRun3)
        EVT_MENU(self, ID_FILE_RUN4, self.onRun4)
        EVT_MENU(self, ID_LEVEL_1, self.onLevel1)
        EVT_MENU(self, ID_LEVEL_2, self.onLevel2)
        EVT_MENU(self, ID_LEVEL_3, self.onLevel3)
        EVT_MENU(self, ID_LEVEL_4, self.onLevel4)
        EVT_MENU(self, ID_FILE_EXIT, self.OnFileExit)
        EVT_MENU(self, ID_FUNCTION_MOVEUP, self.onMoveUp)
        EVT_MENU(self, ID_FUNCTION_MOVEDOWN, self.onMoveDown)
        EVT_MENU(self, ID_FUNCTION_MOVELEFT, self.onMoveLeft)
        EVT_MENU(self, ID_FUNCTION_MOVERIGHT, self.onMoveRight)
        EVT_MENU(self, ID_FUNCTION_MOVEWAIT, self.onMoveWait)
        EVT_MENU(self,ID_HELP_ABOUT, self.OnHelp)
        EVT_MENU(self,ID_LANGUAGE_ENGLISH, self.readEnglish)
        EVT_MENU(self,ID_LANGUAGE_POLISH, self.readPolish)
        EVT_MENU(self,ID_LANGUAGE_TANGALOK, self.readFilipino)

        # Initilize the list of moves to empty list 
        self.listOfMoves = []

    # Function which will create the panels and add shortucts 
    # Left Panel will hold the choosen method to be executed
    # Rigth Panel will hold the picture of initial state of each level
    def sizee(self):
        # Create main panel
        self.panel = wx.Panel(self,-1)
        # Assign text field to left panel
        config.panel1 = MyPanels(self.panel,1)
        config.codebox=wx.TextCtrl(config.panel1,-1,style=wx.TE_MULTILINE,size=(450,600))

        # Create Rigth panel
        config.panel2 = MyPanels(self.panel,1)

        # Add boxziser to both panels so both panels can be re-scaled 
        self.basicsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.basicsizer.Add(config.panel1, 1, wx.EXPAND)
        self.basicsizer.Add(config.panel2, 1, wx.EXPAND)
        self.panel.SetSizer(self.basicsizer)
        
        # Create an accelerator table for shortucts
        # Each shortcut enables the user to perform taks quicker
        # CTRL+R - Starts Tutorial
        # CTRL+X - Exits program
        # ALT+H  - Dispalys about window
        # Create acceleretor table to use shortcuts 
        xit_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onCTRLX, id=xit_id)
        self.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('R'), ID_FILE_RUN),
                                                  (wx.ACCEL_CTRL, ord('X'), xit_id),
                                               (wx.ACCEL_ALT, ord('H'), ID_HELP_ABOUT)
                                              ])
        self.SetAcceleratorTable(self.accel_tbl)

    # If user chooses Enligh,Polish or Filipino language
    # Call the reader class and re-initilize the menu
    def readEnglish(self,evt):   
        self.reader.reader1(0)
        self.initialize()
    def readPolish(self,evt):   
        self.reader.reader1(1)
        self.initialize()
    def readFilipino(self,evt):   
        self.reader.reader1(2)
        self.initialize()
            
    # Create event when user decides to close the program using shortcut
    def onCTRLX(self, event):
        """"""
        self.Close(true)

    # Create event when the user decides to closs the program from menu
    def OnFileExit(self, evt):
        dlg = wxMessageDialog(self, 'Exit Program?', 'Warning!',
                              wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            self.Close(true)
        else:
            dlg.Destroy()

    # Create event when user click on help
    # Display Messages about the system
    # Website information
    def OnHelp(self,evt):
        info = wx.AboutDialogInfo()
        info.Name = "Pyoneer"
        info.Version = "1.0"
        info.Copyright = "(C) 2013 Krystian Jankowski"
        info.Description = wordwrap(
            "A \"Pyoneer\" program is a software program that helps secondary  "
            "students to learn programing. It provides tutorial section "
            "and a snake game where the student can use their problem solving skills",
            350, wx.ClientDC(self))
        info.WebSite = ("http://pyoneer.a-spark.co", "Pyoneer Home PAge")
        info.Developers = [ "Krystian Jankowski",
                            "Onchie Villaver ",]
        wx.AboutBox(info)
        
    # Create event when user clikc on level1
    def onLevel1(self,evt):
        config.panel2.Hide()
        config.panel2 = MyPanels(self.panel,1)
        jpg = wx.Image('level1.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticBitmap(config.panel2, -1, jpg, (-200, -100), (900, 700))
        self.basicsizer.Add(config.panel2, 1, wx.EXPAND)
        self.panel.Layout()
        self.Show(True)
    def onLevel2(self,evt):
        config.panel2.Hide()
        config.panel2 = MyPanels(self.panel,1)
        jpg = wx.Image('level2.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticBitmap(config.panel2, -1, jpg, (-150, -80),(950, 700))
        self.basicsizer.Add(config.panel2, 1, wx.EXPAND)
        self.panel.Layout()
        self.Show(True)
    def onLevel3(self,evt):
        config.panel2.Hide()
        config.panel2 = MyPanels(self.panel,1)
        jpg = wx.Image('level3.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticBitmap(config.panel2, -1, jpg, (-200, -100),(900, 700))
        self.basicsizer.Add(config.panel2, 1, wx.EXPAND)
        self.panel.Layout()
        self.Show(True)
    def onLevel4(self,evt):
        config.panel2.Hide()
        config.panel2 = MyPanels(self.panel,1)
        jpg = wx.Image('level4.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticBitmap(config.panel2, -1, jpg, (-200, -100),(900, 700))
        self.basicsizer.Add(config.panel2, 1, wx.EXPAND)
        self.panel.Layout()
        self.Show(True)
        
    # Create event when move up is choosen
    def onMoveUp(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move up ?',wxYES_NO | wxICON_QUESTION)
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
            self.listOfMoves.append("moveDown()")
        else:
            dlg.Destroy()
        # Create event when move left is choosen
    def onMoveLeft(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move Left ?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('MoveLeft()\n')
            self.listOfMoves.append("moveLeft()")
        else:
            dlg.Destroy()
        # Create event when move right is choosen
    def onMoveRight(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move Right?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('MoveRight()\n')
            self.listOfMoves.append("moveRight()")
        else:
            dlg.Destroy()

    def onMoveWait(self,evt):
        dlg = wxMessageDialog(self,'Are you sure?','Are you sure to choose Move check?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            config.codebox.AppendText('wait()\n')
            self.listOfMoves.append("wait()")
        else:
            dlg.Destroy()
            
        # Create function which runs second level of snake as thread
    def onRun2(self,evt):
        dlg = wxMessageDialog(self,'Are you sure you want to play the game?','Are you sure?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            t = threading.Thread(target=self.secondLevel)
            t.start()
            t.join()
            self.clearList()
            dlg.Destroy()     
        else:
            dlg.Destroy()
            
        # Create function which runs first level of snake as thread
    def onRun(self,evt):
        dlg = wxMessageDialog(self,'Are you sure you want to play the game?','Are you sure?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            t2 = threading.Thread(target=self.firstLevel)
            t2.start()
            t2.join()
            self.clearList()
            dlg.Destroy()   
        else:
            dlg.Destroy()
    def onRun3(self,evt):
        dlg = wxMessageDialog(self,'Are you sure you want to play the game?','Are you sure?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            t = threading.Thread(target=self.thirdLevel)
            t.start()
            t.join()
            self.clearList()
            dlg.Destroy()     
        else:
            dlg.Destroy()

    def onRun4(self,evt):
        dlg = wxMessageDialog(self,'Are you sure you want to play the game?','Are you sure?',wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            t = threading.Thread(target=self.fourthLevel)
            t.start()
            t.join()
            self.clearList()
            dlg.Destroy()     
        else:
            dlg.Destroy()        
        # Initiliaze Second Level
    def secondLevel(self):
        test = SnakeTest2.SnakeTest2(self.listOfMoves,2)
        
        # Initilize first Level
    def firstLevel(self):
        test =SnakeTest2.SnakeTest2(self.listOfMoves,1)
    # Initilize first Level
    def thirdLevel(self):
        test =SnakeTest2.SnakeTest2(self.listOfMoves,3)
    # Initilize first Level
    def fourthLevel(self):
        test =SnakeTest2.SnakeTest2(self.listOfMoves,4)
        # Clear The list after each run of the game
    def clearList(self):
        self.listOfMoves = []
        
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

