import wx
app = wx.App()
class mf(wx.Frame):
    def __init__(self):
        #初始化app
        super().__init__(None,title  =  "b",size = (400,300),pos = (100,100))
        #显示面板
        panel = wx.Panel(parent = self)
        #显示文字
        uid = wx.StaticText(parent = panel, label = 'enter uid')
        #按钮
        b1 = wx.TextCtrl(panel)
        b2 = wx.TextCtrl(panel,style = wx.TE_PASSWORD)
        b3 = wx.TextCtrl(panel,style = wx.TE_MULTILINE)        
        vb = wx.BoxSizer(wx.VERTICAL)
        vb.Add(uid,proportion  =  1,flag = wx.EXPAND|wx.LEFT,border=10)  
        vb.Add(b1,proportion  =  1,flag = wx.EXPAND|wx.ALL,border=10)  
        vb.Add(b2,proportion  =  1,flag = wx.EXPAND|wx.ALL,border=10)  
        vb.Add(b3,proportion  =  1,flag = wx.EXPAND|wx.ALL,border=10)
        panel.SetSizer(vb)
        b1.SetValue(' ')
        print("{0}".format(b1.GetValue()))
frm = mf()
frm.Show()
app.MainLoop()