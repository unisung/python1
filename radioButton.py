import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

red = wx.RadioButton(frame, label = "빨강", style = wx.RB_GROUP)
def onred(event):
    frame.SetBackgroundColour(wx.Colour(255, 0, 0, 0))
    frame.Refresh()
red.Bind(wx.EVT_RADIOBUTTON, onred)

green = wx.RadioButton(frame, label = "초록",)
def ongreen(event):
    frame.SetBackgroundColour(wx.Colour(0, 255, 0, 0))
    frame.Refresh()
green.Bind(wx.EVT_RADIOBUTTON, ongreen)

blue = wx.RadioButton(frame, label = "파랑",)
def onblue(event):
    frame.SetBackgroundColour(wx.Colour(0, 0, 255, 0))
    frame.Refresh()
blue.Bind(wx.EVT_RADIOBUTTON, onblue)

yellow = wx.RadioButton(frame, label = "노랑",)
def onyellow(event):
    frame.SetBackgroundColour(wx.Colour(255, 255, 0, 0))
    frame.Refresh()
yellow.Bind(wx.EVT_RADIOBUTTON, onyellow)
yellow.SetValue(True)

box = wx.StaticBoxSizer(wx.VERTICAL, frame, "배경색")
frame.SetSizer(box)
box.Add(red)
box.Add(green)
box.Add(blue)
box.Add(yellow)

frame.SetBackgroundColour(wx.Colour(255, 255, 0, 0))
frame.Show(True)
app.MainLoop()