import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn1 = wx.Button(frame, label="Button1")
btn2 = wx.Button(frame, label="Button2")
btn3 = wx.Button(frame, label="Button3")

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(btn1)
box.Add(btn2)
box.Add(btn3)

frame.Show(True)
app.MainLoop()