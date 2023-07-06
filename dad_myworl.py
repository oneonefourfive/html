import wx
import json
import time
pressed = 0

def init():

    t = time
    minet = 0
    secs = 0
    
    global app
    app = wx.App()

    f = open("config.json", "r")
    f = json.load(f)
    print(f)

    timee = f["time"]
    print(timee)
    timee = timee.split(":")

    global minute
    minute = timee[0]

    global sec
    sec = timee[1]
init()




class mf(wx.Frame):
    def __init__(self):
        self.pressed=0
        self.alltime = int(minute) * 60 + int(sec)
        super().__init__(None, title="b", size=(500, 500), pos=(100, 100))
        self.bs = 0
        self.rs = 0


        self.panel = wx.Panel(parent=self)
        self.st = wx.StaticText(parent=self.panel, label="00:00")
        self.b = wx.Button(parent=self.panel, label="START", id=10)
        st2 = wx.StaticText(self.panel,label = "select time")
        self.list_of_time=['30','60','90']
        lt = wx.ListBox(self.panel,choices = self.list_of_time, style = wx.LB_SINGLE)
        self.button_for_red = wx.Button(parent=self.panel, label="red", id=111)
        self.button_for_blue = wx.Button(parent=self.panel, label="blue", id=222)
        self.txt = wx.StaticText(self.panel,label = '0:0')
        

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_BUTTON, self.on_click, self.b)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.Bind(wx.EVT_LISTBOX,self.on_click,lt)
        self.Bind(wx.EVT_BUTTON,self.scoreing,self.button_for_blue)
        self.Bind(wx.EVT_BUTTON,self.scoreing,self.button_for_red)


        hb = wx.BoxSizer(wx.HORIZONTAL)
        hb.Add(st2,proportion = 2,flag =wx.EXPAND)
        hb.Add(lt,proportion = 2,flag =wx.FIXED_MINSIZE)
        vb = wx.BoxSizer(wx.VERTICAL)
        vb.Add(hb,proportion = 2,flag = wx.BOTTOM)
        hb2= wx.BoxSizer(wx.HORIZONTAL)
        vb2= wx.BoxSizer(wx.VERTICAL)
        vb3 = wx.BoxSizer(wx.HORIZONTAL)
        hb2.Add(vb2,proportion = 1,flag = wx.ALIGN_LEFT)
        hb2.Add(vb3,proportion = 1,flag = wx.ALIGN_CENTER)
        vb3.Add(self.button_for_blue,proportion  =  1,  flag = wx.ALIGN_LEFT)
        vb3.Add(self.button_for_red,proportion  =  1,  flag = wx.ALIGN_CENTER)
        vb3.Add(self.txt,proportion  =  2,  flag = wx.ALIGN_CENTER)
        
        
        vb2.Add(self.st,proportion = 1, flag = wx.EXPAND|wx.Top)
        vb2.Add(self.b,proportion = 1,flag = wx.TOP)
        vb.Add(hb2,proportion = 1,flag = wx.TOP)


        self.panel.SetSizer(vb)
        self.b.Bind(wx.EVT_BUTTON, self.start)
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)
        
        
    def on_click(self, event):
        lb = event.GetEventObject()
        li = lb.GetSelection()
        self.alltime = int(self.list_of_time[li])*60


    def start(self, event):
        
        if self.pressed == 0:
            self.timer.Start(1000)
            self.b.SetLabel("Stop")
            self.pressed = 1
        else:
            self.timer.Stop()
            self.pressed = 0
            self.b.SetLabel("Resume")
    def stop(self,event):
        pass

        
    def update(self, event):

        if self.alltime == 0:
            self.timer.Stop()
            return

        else:
            self.alltime -= 1
            min = self.alltime // 60
            sec = self.alltime % 60

        self.st.SetLabel("{0}:{1}".format(min, sec))

    def scoreing(self,event):
        ei=event.GetId()
        if ei ==222:
            self.bs+=1
            print(self.bs)
        elif ei ==111:
            self.rs+=1
            print(self.rs)
        self.txt.SetLabel("{0}:{1}".format(self.bs, self.rs))
        

frm = mf()
frm.Show()
app.MainLoop()


init()
