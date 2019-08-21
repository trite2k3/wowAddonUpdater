#!/usr/bin/python3


## Copyright (C) 2019, trite
## You should have received a copy of the WTFPL
## If not, see <http://www.wtfpl.net/txt/copying/>.
##
##            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
##                    Version 2, December 2004
##
## Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
##
## Everyone is permitted to copy and distribute verbatim or modified
## copies of this license document, and changing it is allowed as long
## as the name is changed.
##
##            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
##   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
##
##  0. You just DO WHAT THE FUCK YOU WANT TO.
##


import wx
import wx.grid


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 800))

        self.grid_1 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 0))

        self.button_1 = wx.Button(self, wx.ID_ANY, "OK")
        self.button_1.Bind(wx.EVT_BUTTON,self.OnClickedOK)

        self.button_2 = wx.Button(self, wx.ID_ANY, "Save")
        self.button_2.Bind(wx.EVT_BUTTON, self.OnClickedSave)

        self.button_3 = wx.Button(self, wx.ID_ANY, "Load")
        self.button_3.Bind(wx.EVT_BUTTON, self.OnClickedLoad)

        self.button_4 = wx.Button(self, wx.ID_ANY, "Exit")
        self.button_4.Bind(wx.EVT_BUTTON, self.OnClickedExit)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("wowAddonUpdater")
        self.grid_1.CreateGrid(10, 1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.grid_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_1, 0, 0, 0)
        sizer_2.Add(self.button_2, 0, 0, 0)
        sizer_2.Add(self.button_3, 0, 0, 0)
        sizer_2.Add(self.button_4, 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def OnClicked(self, event):
        label = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", label)

    def OnClickedOK(self, event):
        #data = self.grid_1.GetCellValue(0,0)
        rows = self.grid_1.GetNumberRows()
        #print(data + " " + str(rows))

        counter = 0
        while counter < rows:
            print(self.grid_1.GetCellValue(counter,0))
            counter = counter + 1

    def OnClickedSave(self, event):
        #self.grid_1.SetCellValue(0, 0, "hadourp")
        #self.grid_1.SetCellValue(1, 0, "hadourpen")
        #self.grid_1.SetCellValue(2, 0, "hachinatsuhadourpen")
        #
        #new stuff, old was "add"
        #
        # open a file for writing and create it if it doesnt exist
        f = open("data.txt", "w+")
        #blahgoeshere
        #
        #get number of rows in grid
        rows = self.grid_1.GetNumberRows()
        #loop through it and write a line per row
        counter = 0
        while counter < rows:
            if counter == rows:
                f.write(self.grid_1.GetCellValue(counter,0))
            else:
                f.write(self.grid_1.GetCellValue(counter, 0) + "\n")
            counter = counter + 1
        #close the file
        f.close()


    def OnClickedLoad(self, event):
        #self.grid_1.SetCellValue(0, 0, "")
        #rows = self.grid_1.GetNumberRows()
        #counter = 0
        #while counter < rows:
        #    self.grid_1.SetCellValue(counter, 0, "")
        #    counter = counter + 1
        #
        #new stuff, old was "del"
        print("cannot be empty def")

    def OnClickedExit(self, event):
        self.Close()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        #File stuff for loading and saving grid data
        #open a file for writing and create it if it doesnt exist
        #f= open("data.txt", "w+")
        #just a test write
        #f.write("this is a line\n")
        #f.write("this is a new line\n")
        #close the file
        #f.close()

        #reading the file (per line)
        #f= open("data.txt", "r")
        #if f.mode == "r":
        #    lines = f.readlines()
        #    for line in lines:
        #        print(line)
        #f.close()

        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
