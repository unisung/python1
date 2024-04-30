import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()