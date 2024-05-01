import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

menubar = wx.MenuBar()
file = wx.Menu()
menubar.Append(file, "파일")
about = wx.MenuItem(id = wx.ID_ANY, text="소개")
file.Append(about)
file.AppendSeparator()
exit = wx.MenuItem(id = wx.ID_ANY, text="종료")
file.Append(exit)
frame.SetMenuBar(menubar)


def onAbout(event):
    wx.MessageBox("메뉴를 사용하는 프로그램입니다.", "알림", wx.OK)
frame.Bind(wx.EVT_MENU, onAbout, about)

def onExit(event):
    frame.Close()
frame.Bind(wx.EVT_MENU, onExit, exit)

frame.Show(True)
app.MainLoop()