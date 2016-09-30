#!/usr/bin/python
"""Concept de calculator hashuri md5 si sha256"""
import wx
import md5_gui
import hashlib


def calculeazaHasuri(cale_fisier):

    obiect = hashlib.md5()
    with open(cale_fisier, 'rb') as fisier:
        buffer = fisier.read(4096)
        while len(buffer) > 0:
            buffer = fisier.read(len(buffer))
            obiect.update(buffer)
    obiect2 = hashlib.sha256()
    with open(cale_fisier, 'rb') as fisier:
        buffer = fisier.read(4096)
        while len(buffer) > 0:
            buffer = fisier.read(len(buffer))
            obiect2.update(buffer)

    return [obiect.hexdigest(), obiect2.hexdigest()]



# Implementing mainFrame
class mainFrame(md5_gui.mainFrame):
    def __init__(self):
        """
Initializeaza Frameul principal
        """
        md5_gui.mainFrame.__init__(self, None)

    # Handlers for mainFrame events.
    def onClickCalculeaza(self, event):
        self.m_statusBar.SetStatusText("Calculating..")
        self.m_textOutputMD5.SetLabelText((calculeazaHasuri(self.filePicker.GetPath())[0]))
        self.m_textOutputSHA.SetLabelText((calculeazaHasuri(self.filePicker.GetPath())[1]))
        self.m_statusBar.SetStatusText("DONE!")
    def onClickIesire(self, event):
        # TODO: Implement onClickIesire
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    frame = mainFrame()
    frame.Show()
    app.MainLoop()
