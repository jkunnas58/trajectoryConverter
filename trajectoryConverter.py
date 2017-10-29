import wx

class windowClass(wx.Frame):

  def __init__(self, parent, title):
    super(windowClass, self).__init__(parent, title=title, size=300,300))
    
    self.Show()

app = wx.App()
windowClass(None, title='Trajectory Converter')
app.MainLoop()
