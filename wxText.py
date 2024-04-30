import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

panelhorz = wx.Panel(frame)
btn1 = wx.Button(panelhorz, label="Button1")
btn2 = wx.Button(panelhorz, label="Button2")
btn3 = wx.Button(panelhorz, label="Button3")
sizerhorz = wx.BoxSizer(wx.HORIZONTAL)
sizerhorz.Add(btn1)
sizerhorz.Add(btn2)
sizerhorz.Add(btn3)
panelhorz.SetSizer(sizerhorz)

panelvert = wx.Panel(frame)
static1 = wx.StaticText(panelvert, label="StaticText1")
static2 = wx.StaticText(panelvert, label="StaticText2")
static3 = wx.StaticText(panelvert, label="StaticText3")
sizervert = wx.BoxSizer(wx.VERTICAL)
sizervert.Add(static1)
sizervert.Add(static2)
sizervert.Add(static3)
panelvert.SetSizer(sizervert)

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(panelhorz, border = 10, flag = wx.DOWN)
box.Add(panelvert, border = 10, flag = wx.UP)

frame.Show(True)
app.MainLoop()