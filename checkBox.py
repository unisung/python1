import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

chkvisible = wx.CheckBox(frame, label = "보임")
chkvisible.SetValue(wx.CHK_CHECKED)
def onvisible(event):
    if chkvisible.GetValue() == wx.CHK_CHECKED:
        btn.Show(True)
    else:
        btn.Show(False)
chkvisible.Bind(wx.EVT_CHECKBOX, onvisible)

chkenable = wx.CheckBox(frame, label = "사용가능")
chkenable .SetValue(wx.CHK_CHECKED)
def onenable(event):
    if chkenable.GetValue() == wx.CHK_CHECKED:
        btn.Enable(True)
    else:
        btn.Enable(False)
chkenable.Bind(wx.EVT_CHECKBOX, onenable)

btn = wx.Button(frame, label="Click")
def onClick(event):
    wx.MessageBox("클릭했습니다.", "알림", wx.OK)
btn.Bind(wx.EVT_BUTTON, onClick)

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(chkvisible)
box.Add(chkenable)
box.Add(btn)

frame.Show(True)
app.MainLoop()