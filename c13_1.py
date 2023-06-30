import wx
app = wx.App()
class mf(wx.Frame):
    def __init__(self):
        #初始化app
        super().__init__(None,title  =  "b",size = (400,300),pos = (100,100))
        #显示面板
        panel = wx.Panel(parent = self)
        #显示文字
        self.st = wx.StaticText(parent = panel, label = 'bruh',pos = (110,20))
        #按钮
        b = wx.Button(parent = panel, label = "ok",id = 10)
        b2 = wx.Button(parent = panel, label = "ok?",id = 11)
        
        self.Bind(wx.EVT_BUTTON,self.on_click,b)
        hb = wx.BoxSizer(wx.HORIZONTAL)
        hb
        vb = wx.BoxSizer(wx.VERTICAL)
        vb.Add(self.st,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
        hb.Add(b,proportion  =  1,flag = wx.EXPAND|wx.BOTTOM,border=10)  
        hb.Add(b2,proportion  =  1,flag = wx.EXPAND|wx.BOTTOM,border=10)
        vb.Add(hb,proportion = 1,flag = wx.CENTER)
        panel.SetSizer(vb)

        self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2 = 20)
    def on_click(self,event):
        ei=event.GetId()
        print(ei)
        if ei==10:
            self.st.SetLabelText('hw')
        else:
            self.st.SetLabelText('sd')
frm = mf()
frm.Show()
app.MainLoop()

