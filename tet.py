
import wx


class MainFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, wx.ID_ANY, 'Application')
        standardFont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        standardFont.SetPointSize(100)
        # self.SetFont(standardFont)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.txt = wx.StaticText(self, wx.ID_ANY, "text")
        sizer.Add(self.txt, 5)
        self.SetSizer(sizer)
        self.Layout()
        self.Show()
        wx.CallAfter( self.print_size )

    def print_size(self):
        print( self.txt.GetSize() )


if __name__ == '__main__':
    app = wx.App(False)
    mf = MainFrame()
    app.MainLoop()