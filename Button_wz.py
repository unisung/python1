import wx

app = wx.App()
frame = wx.Frame(None, title="wxPython")

btn = wx.Button(frame, label="Click")
def OnClick(event):
    wx.MessageBox("번튼을 클릭하였습니다.","알림",wx.OK)

btn.Bind(wx.EVT_BUTTON, OnClick)

frame.Show(True)
app.MainLoop()
