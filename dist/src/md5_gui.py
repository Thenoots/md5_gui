# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculator de MD5", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer6 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer6.AddGrowableCol( 1 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Alege un fisier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.filePicker = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Alege un fisier", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer6.Add( self.filePicker, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( fgSizer6, 0, wx.EXPAND, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextMD5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MD5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMD5.Wrap( -1 )
		fgSizer5.Add( self.m_staticTextMD5, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textOutputMD5 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.TE_READONLY )
		self.m_textOutputMD5.SetMaxLength( 0 ) 
		fgSizer5.Add( self.m_textOutputMD5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( fgSizer5, 0, wx.EXPAND, 5 )
		
		fgSizer51 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer51.AddGrowableCol( 1 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextSHA = wx.StaticText( self.m_panel1, wx.ID_ANY, u"SHA256", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSHA.Wrap( -1 )
		fgSizer51.Add( self.m_staticTextSHA, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textOutputSHA = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textOutputSHA.SetMaxLength( 0 ) 
		fgSizer51.Add( self.m_textOutputSHA, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( fgSizer51, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_calculeaza = wx.Button( self.m_panel1, wx.ID_ANY, u"Calculeaza", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_calculeaza.SetToolTipString( u"Calculeaza hashuri " )
		
		bSizer6.Add( self.m_button_calculeaza, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button_iesire = wx.Button( self.m_panel1, wx.ID_ANY, u"Iesire", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button_iesire, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer11.Add( bSizer6, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer11 )
		self.m_panel1.Layout()
		bSizer11.Fit( self.m_panel1 )
		bSizer5.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_calculeaza.Bind( wx.EVT_BUTTON, self.onClickCalculeaza )
		self.m_button_iesire.Bind( wx.EVT_BUTTON, self.onClickIesire )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onClickCalculeaza( self, event ):
		event.Skip()
	
	def onClickIesire( self, event ):
		event.Skip()
	

