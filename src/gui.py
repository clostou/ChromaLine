# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class _Frame
###########################################################################

class _Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,600 ), wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook4 = wx.Notebook( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"choosing file：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer11.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		bSizer11.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 25,25 ), wx.BORDER_NONE )
		bSizer11.Add( self.m_button4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.bSizer2.Add( bSizer11, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer2.Add( self.m_staticline1, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn1 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"origin", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		bSizer3.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"bilateral", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.SetValue( True )
		bSizer3.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"median", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_radioBtn3, 0, wx.ALL, 5 )


		self.bSizer2.Add( bSizer3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

		self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC|wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
		self.fgSizer1.SetFlexibleDirection( wx.BOTH )
		self.fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"s_space：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer7.Add( self.m_staticText1, 0, wx.TOP, 8 )

		self.m_slider1 = wx.Slider( self.m_panel5, wx.ID_ANY, 8, 1, 20, wx.DefaultPosition, wx.Size( 115,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer7.Add( self.m_slider1, 0, wx.ALL, 5 )


		self.bSizer5.Add( bSizer7, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"s_value：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer8.Add( self.m_staticText2, 0, wx.TOP, 8 )

		self.m_slider2 = wx.Slider( self.m_panel5, wx.ID_ANY, 20, 1, 100, wx.DefaultPosition, wx.Size( 125,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer8.Add( self.m_slider2, 0, wx.ALL, 5 )


		self.bSizer5.Add( bSizer8, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer1.Add( self.bSizer5, 0, wx.EXPAND|wx.ALL, 5 )

		self.bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"size：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer9.Add( self.m_staticText3, 0, wx.TOP, 8 )

		bSizer591 = wx.BoxSizer( wx.VERTICAL )

		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText34 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		bSizer60.Add( self.m_staticText34, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_slider3 = wx.Slider( self.m_panel5, wx.ID_ANY, 1, 0, 5, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer60.Add( self.m_slider3, 0, 0, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		bSizer60.Add( self.m_staticText35, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer591.Add( bSizer60, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText331 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText331.Wrap( -1 )

		bSizer591.Add( self.m_staticText331, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )


		bSizer9.Add( bSizer591, 0, wx.EXPAND, 5 )


		self.bSizer6.Add( bSizer9, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer1.Add( self.bSizer6, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel5.SetSizer( self.fgSizer1 )
		self.m_panel5.Layout()
		self.fgSizer1.Fit( self.m_panel5 )
		self.bSizer2.Add( self.m_panel5, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 20 )


		self.m_panel1.SetSizer( self.bSizer2 )
		self.m_panel1.Layout()
		self.bSizer2.Fit( self.m_panel1 )
		self.m_notebook4.AddPage( self.m_panel1, u"1. noiseSmooth", True )
		self.m_panel2 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn4 = wx.RadioButton( self.m_panel2, wx.ID_ANY, u"adaThresh", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtn4.SetValue( True )
		bSizer161.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

		self.m_radioBtn5 = wx.RadioButton( self.m_panel2, wx.ID_ANY, u"Canny", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

		self.m_radioBtn6 = wx.RadioButton( self.m_panel2, wx.ID_ANY, u"Scharr", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

		self.m_radioBtn7 = wx.RadioButton( self.m_panel2, wx.ID_ANY, u"LoG", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_radioBtn7, 0, wx.ALL, 5 )


		self.bSizer10.Add( bSizer161, 0, wx.EXPAND|wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC|wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.fgSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
		self.fgSizer2.SetFlexibleDirection( wx.BOTH )
		self.fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bSizer67 = wx.BoxSizer( wx.VERTICAL )

		self.bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText42 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"ada：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer66.Add( self.m_staticText42, 0, wx.TOP, 8 )

		m_choice3Choices = [ u"gaussian", u"mean" ]
		self.m_choice3 = wx.Choice( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer66.Add( self.m_choice3, 0, wx.ALL, 5 )


		self.bSizer191.Add( bSizer66, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"C：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer20.Add( self.m_staticText9, 0, wx.TOP, 8 )

		self.m_slider4 = wx.Slider( self.m_panel6, wx.ID_ANY, 10, 0, 30, wx.DefaultPosition, wx.Size( 120,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer20.Add( self.m_slider4, 0, wx.ALL, 5 )


		self.bSizer191.Add( bSizer20, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.bSizer67.Add( self.bSizer191, 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"size：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer21.Add( self.m_staticText10, 0, wx.TOP, 8 )

		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		bSizer65 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText40 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer65.Add( self.m_staticText40, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_slider5 = wx.Slider( self.m_panel6, wx.ID_ANY, 4, 1, 10, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		bSizer65.Add( self.m_slider5, 0, 0, 5 )

		self.m_staticText41 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer65.Add( self.m_staticText41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer64.Add( bSizer65, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText39 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer64.Add( self.m_staticText39, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )


		bSizer21.Add( bSizer64, 0, wx.EXPAND, 5 )


		self.bSizer67.Add( bSizer21, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer2.Add( self.bSizer67, 0, wx.ALL|wx.EXPAND, 5 )

		self.gSizer1 = wx.GridSizer( 2, 2, 0, 0 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"lower：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer24.Add( self.m_staticText12, 0, wx.TOP, 8 )

		self.m_slider7 = wx.Slider( self.m_panel6, wx.ID_ANY, 20, 1, 100, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer24.Add( self.m_slider7, 0, wx.ALL, 5 )


		self.gSizer1.Add( bSizer24, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"upper：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer23.Add( self.m_staticText11, 0, wx.TOP, 8 )

		self.m_slider6 = wx.Slider( self.m_panel6, wx.ID_ANY, 40, 1, 100, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer23.Add( self.m_slider6, 0, wx.ALL, 5 )


		self.gSizer1.Add( bSizer23, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"size：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer25.Add( self.m_staticText13, 0, wx.TOP, 8 )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText37 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		bSizer62.Add( self.m_staticText37, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_slider8 = wx.Slider( self.m_panel6, wx.ID_ANY, 3, 1, 3, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		bSizer62.Add( self.m_slider8, 0, 0, 5 )

		self.m_staticText38 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		bSizer62.Add( self.m_staticText38, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer61.Add( bSizer62, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		bSizer61.Add( self.m_staticText36, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )


		bSizer25.Add( bSizer61, 0, wx.EXPAND, 5 )


		self.gSizer1.Add( bSizer25, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer2.Add( self.gSizer1, 0, wx.ALL|wx.EXPAND, 5 )

		self.bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"a：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer28.Add( self.m_staticText14, 0, wx.TOP, 8 )

		self.m_slider9 = wx.Slider( self.m_panel6, wx.ID_ANY, 0, 0, 99, wx.DefaultPosition, wx.Size( 120,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer28.Add( self.m_slider9, 0, wx.ALL, 5 )


		self.bSizer27.Add( bSizer28, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"b：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer29.Add( self.m_staticText15, 0, wx.TOP, 8 )

		self.m_slider10 = wx.Slider( self.m_panel6, wx.ID_ANY, 100, 1, 100, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer29.Add( self.m_slider10, 0, wx.ALL, 5 )


		self.bSizer27.Add( bSizer29, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer2.Add( self.bSizer27, 0, wx.ALL|wx.EXPAND, 5 )

		self.bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"a：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer31.Add( self.m_staticText17, 0, wx.TOP, 8 )

		self.m_slider12 = wx.Slider( self.m_panel6, wx.ID_ANY, 0, 0, 99, wx.DefaultPosition, wx.Size( 120,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer31.Add( self.m_slider12, 0, wx.ALL, 5 )


		self.bSizer30.Add( bSizer31, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"b：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer32.Add( self.m_staticText16, 0, wx.TOP, 8 )

		self.m_slider11 = wx.Slider( self.m_panel6, wx.ID_ANY, 100, 1, 100, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer32.Add( self.m_slider11, 0, wx.ALL, 5 )


		self.bSizer30.Add( bSizer32, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer2.Add( self.bSizer30, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel6.SetSizer( self.fgSizer2 )
		self.m_panel6.Layout()
		self.fgSizer2.Fit( self.m_panel6 )
		self.bSizer10.Add( self.m_panel6, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 20 )

		self.m_staticline2 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer10.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 10 )

		bSizer171 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Advanced：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer171.Add( self.m_staticText8, 0, wx.ALL, 5 )

		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox1 = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"thinning", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"morphGrad", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.m_checkBox2, 0, wx.ALL, 5 )


		bSizer171.Add( bSizer181, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 20 )


		self.bSizer10.Add( bSizer171, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )


		self.m_panel2.SetSizer( self.bSizer10 )
		self.m_panel2.Layout()
		self.bSizer10.Fit( self.m_panel2 )
		self.m_notebook4.AddPage( self.m_panel2, u"2. edgeExtract", False )
		self.m_panel3 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.bSizer33 = wx.BoxSizer( wx.VERTICAL )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn8 = wx.RadioButton( self.m_panel3, wx.ID_ANY, u"static", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		bSizer34.Add( self.m_radioBtn8, 0, wx.ALL, 5 )

		self.m_radioBtn9 = wx.RadioButton( self.m_panel3, wx.ID_ANY, u"linear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn9.SetValue( True )
		bSizer34.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn10 = wx.RadioButton( self.m_panel3, wx.ID_ANY, u"maze", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_radioBtn10, 0, wx.ALL, 5 )


		self.bSizer33.Add( bSizer34, 0, wx.EXPAND|wx.ALL, 5 )

		self.m_panel8 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC|wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.fgSizer3 = wx.FlexGridSizer( 0, 1, 0, 0 )
		self.fgSizer3.SetFlexibleDirection( wx.BOTH )
		self.fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"direction：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer39.Add( self.m_staticText21, 0, wx.TOP, 8 )

		m_choice1Choices = [ u"LU", u"RU", u"U", u"L" ]
		self.m_choice1 = wx.Choice( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer39.Add( self.m_choice1, 0, wx.ALL, 5 )


		self.bSizer38.Add( bSizer39, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"period：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer40.Add( self.m_staticText22, 0, wx.TOP, 8 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText24 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"0.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer42.Add( self.m_staticText24, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_slider14 = wx.Slider( self.m_panel8, wx.ID_ANY, 0, -20, 20, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		bSizer42.Add( self.m_slider14, 0, 0, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"10 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer42.Add( self.m_staticText25, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer41.Add( bSizer42, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer41.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )


		bSizer40.Add( bSizer41, 0, wx.EXPAND, 5 )


		self.bSizer38.Add( bSizer40, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer3.Add( self.bSizer38, 0, wx.ALL|wx.EXPAND, 5 )

		self.bSizer35 = wx.BoxSizer( wx.VERTICAL )

		bSizer341 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"diag_len：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer36.Add( self.m_staticText18, 0, wx.TOP, 8 )

		self.m_slider13 = wx.Slider( self.m_panel8, wx.ID_ANY, 30, 10, 100, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer36.Add( self.m_slider13, 0, wx.ALL, 5 )


		bSizer341.Add( bSizer36, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox3 = wx.CheckBox( self.m_panel8, wx.ID_ANY, u"blur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True)
		bSizer37.Add( self.m_checkBox3, 0, wx.ALL, 8 )


		bSizer341.Add( bSizer37, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.bSizer35.Add( bSizer341, 0, wx.EXPAND, 5 )

		bSizer351 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText19 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"center：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer351.Add( self.m_staticText19, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, u"(0, 0)", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer351.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button6 = wx.Button( self.m_panel8, wx.ID_ANY, u"select", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer351.Add( self.m_button6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.bSizer35.Add( bSizer351, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.fgSizer3.Add( self.bSizer35, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( self.fgSizer3 )
		self.m_panel8.Layout()
		self.fgSizer3.Fit( self.m_panel8 )
		self.bSizer33.Add( self.m_panel8, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 20 )

		self.m_staticline3 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer33.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 10 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText26 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Advanced：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer43.Add( self.m_staticText26, 0, wx.ALL, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText27 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"hue_offset：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer45.Add( self.m_staticText27, 0, wx.TOP, 8 )

		self.m_slider15 = wx.Slider( self.m_panel3, wx.ID_ANY, 0, 0, 180, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer45.Add( self.m_slider15, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )


		bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )

		self.bSizer49 = wx.BoxSizer( wx.VERTICAL )

		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer47 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText28 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"saturation：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer47.Add( self.m_staticText28, 0, wx.TOP, 8 )

		self.m_slider16 = wx.Slider( self.m_panel3, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer47.Add( self.m_slider16, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )


		bSizer46.Add( bSizer47, 0, wx.EXPAND, 5 )

		bSizer48 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox4 = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"map mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetValue(True)
		bSizer48.Add( self.m_checkBox4, 0, wx.ALL, 8 )


		bSizer46.Add( bSizer48, 0, wx.EXPAND|wx.LEFT, 10 )


		self.bSizer49.Add( bSizer46, 0, wx.EXPAND, 5 )

		self.m_panel9 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC|wx.TAB_TRAVERSAL )
		self.m_panel9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText29 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"phase：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		bSizer52.Add( self.m_staticText29, 0, wx.TOP, 8 )

		m_choice2Choices = [ u"h", u"s", u"v" ]
		self.m_choice2 = wx.Choice( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 2 )
		bSizer52.Add( self.m_choice2, 0, wx.ALL, 5 )


		bSizer50.Add( bSizer52, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )

		bSizer53 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText30 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"lower：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		bSizer53.Add( self.m_staticText30, 0, wx.TOP, 8 )

		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText32 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		bSizer55.Add( self.m_staticText32, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_slider17 = wx.Slider( self.m_panel9, wx.ID_ANY, 0, 0, 40, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer55.Add( self.m_slider17, 0, 0, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		bSizer55.Add( self.m_staticText33, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer54.Add( bSizer55, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer54.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )


		bSizer53.Add( bSizer54, 0, wx.EXPAND, 5 )


		bSizer50.Add( bSizer53, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


		self.m_panel9.SetSizer( bSizer50 )
		self.m_panel9.Layout()
		bSizer50.Fit( self.m_panel9 )
		self.bSizer49.Add( self.m_panel9, 0, wx.EXPAND, 5 )


		bSizer44.Add( self.bSizer49, 0, wx.EXPAND, 5 )


		bSizer43.Add( bSizer44, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 20 )


		self.bSizer33.Add( bSizer43, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )


		self.bSizer33.Add( bSizer56, 1, wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer33.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 10 )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )


		bSizer57.Add( bSizer58, 1, wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		bSizer59 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button7 = wx.Button( self.m_panel3, wx.ID_ANY, u"export all", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self.m_panel3, wx.ID_ANY, u"export", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer57.Add( bSizer59, 0, wx.EXPAND, 5 )


		self.bSizer33.Add( bSizer57, 0, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( self.bSizer33 )
		self.m_panel3.Layout()
		self.bSizer33.Fit( self.m_panel3 )
		self.m_notebook4.AddPage( self.m_panel3, u"3. colorRender", False )

		bSizer17.Add( self.m_notebook4, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self.m_panel7, wx.ID_ANY, u"Default", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self.m_panel7, wx.ID_ANY, u"Switch", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button5, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )


		bSizer16.Add( bSizer19, 1, wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button31 = wx.Button( self.m_panel7, wx.ID_ANY, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
		bSizer15.Add( self.m_button31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer15.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer15.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer15.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button41 = wx.Button( self.m_panel7, wx.ID_ANY, u">", wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
		bSizer15.Add( self.m_button41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer16.Add( bSizer15, 0, wx.EXPAND, 5 )


		bSizer17.Add( bSizer16, 0, wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer17 )
		self.m_panel7.Layout()
		bSizer17.Fit( self.m_panel7 )
		bSizer1.Add( self.m_panel7, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open files..."+ u"\t" + u"F1", u"Open new image files.", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open image folder...", u"Open all image files in a folder.", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menu1.AppendSeparator()

		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Export to..."+ u"\t" + u"F3", u"Process and export current image.", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Export all to..."+ u"\t" + u"F4", u"Process and export all images.", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )

		self.m_menu1.AppendSeparator()

		self.m_menuItem11 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Enable tooltips"+ u"\t" + u"F5", u"Enable the query button on the caption.", wx.ITEM_CHECK )
		self.m_menu1.Append( self.m_menuItem11 )

		self.m_menu1.AppendSeparator()

		self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit"+ u"\t" + u"F8", u"Exit program.", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem5 )

		self.m_menubar.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Save configuration..."+ u"\t" + u"Ctrl+S", u"Write current configuration to file.", wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem6 )

		self.m_menuItem7 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Load configuration..."+ u"\t" + u"Shift+S", u"Read configuration from file.", wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem7 )

		self.m_menubar.Append( self.m_menu2, u"Config" )

		self.m_menu3 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Open log"+ u"\t" + u"F10", u"Open journal file.", wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem8 )

		self.m_menuItem9 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Help"+ u"\t" + u"F11", u"Show information about how to use.", wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem9 )

		self.m_menuItem10 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About program"+ u"\t" + u"F12", u"About this program.", wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem10 )

		self.m_menubar.Append( self.m_menu3, u"About" )

		self.SetMenuBar( self.m_menubar )

		self.m_statusBar = self.CreateStatusBar( 2, wx.STB_DEFAULT_STYLE, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.activate )
		self.m_notebook4.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.page_change )
		self.m_textCtrl1.Bind( wx.EVT_TEXT_ENTER, self.file_path_edit )
		self.m_button4.Bind( wx.EVT_BUTTON, self.file_choose )
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.noise_origin )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.noise_bilateral )
		self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.noise_median )
		self.m_slider1.Bind( wx.EVT_SLIDER, self.noise_bilateral_update )
		self.m_slider2.Bind( wx.EVT_SLIDER, self.noise_bilateral_update )
		self.m_slider3.Bind( wx.EVT_SLIDER, self.noise_median_update )
		self.m_radioBtn4.Bind( wx.EVT_RADIOBUTTON, self.edge_adaThresh )
		self.m_radioBtn5.Bind( wx.EVT_RADIOBUTTON, self.edge_Canny )
		self.m_radioBtn6.Bind( wx.EVT_RADIOBUTTON, self.edge_Scharr )
		self.m_radioBtn7.Bind( wx.EVT_RADIOBUTTON, self.edge_LoG )
		self.m_choice3.Bind( wx.EVT_CHOICE, self.edge_adaThresh_update1 )
		self.m_slider4.Bind( wx.EVT_SLIDER, self.edge_adaThresh_update1 )
		self.m_slider5.Bind( wx.EVT_SLIDER, self.edge_adaThresh_update2 )
		self.m_slider7.Bind( wx.EVT_SLIDER, self.edge_Canny_update1 )
		self.m_slider6.Bind( wx.EVT_SLIDER, self.edge_Canny_update1 )
		self.m_slider8.Bind( wx.EVT_SLIDER, self.edge_Canny_update2 )
		self.m_slider9.Bind( wx.EVT_SLIDER, self.edge_Scharr_update )
		self.m_slider10.Bind( wx.EVT_SLIDER, self.edge_Scharr_update )
		self.m_slider12.Bind( wx.EVT_SLIDER, self.edge_LoG_update )
		self.m_slider11.Bind( wx.EVT_SLIDER, self.edge_LoG_update )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.edge_advance_update )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.edge_advance_update )
		self.m_radioBtn8.Bind( wx.EVT_RADIOBUTTON, self.color_static )
		self.m_radioBtn9.Bind( wx.EVT_RADIOBUTTON, self.color_linear )
		self.m_radioBtn10.Bind( wx.EVT_RADIOBUTTON, self.color_maze )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.color_linear_update )
		self.m_slider14.Bind( wx.EVT_SLIDER, self.color_linear_update )
		self.m_slider13.Bind( wx.EVT_SLIDER, self.color_maze_update )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.color_maze_update )
		self.m_button6.Bind( wx.EVT_BUTTON, self.color_maze_center )
		self.m_slider15.Bind( wx.EVT_SLIDER, self.color_advance_hue_update )
		self.m_slider16.Bind( wx.EVT_SLIDER, self.color_advance_sat_update )
		self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.color_advance_sat )
		self.m_choice2.Bind( wx.EVT_CHOICE, self.color_advance_sat_update )
		self.m_slider17.Bind( wx.EVT_SLIDER, self.color_advance_sat_update )
		self.m_button7.Bind( wx.EVT_BUTTON, self.img_export_all )
		self.m_button8.Bind( wx.EVT_BUTTON, self.img_export )
		self.m_button3.Bind( wx.EVT_BUTTON, self.set_default )
		self.m_button5.Bind( wx.EVT_BUTTON, self.img_origin )
		self.m_button31.Bind( wx.EVT_BUTTON, self.file_previous )
		self.m_button41.Bind( wx.EVT_BUTTON, self.file_next )
		self.Bind( wx.EVT_MENU, self.m_file_choose, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.m_folder_choose, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.m_img_export, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.m_img_export_all, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.m_enable_tooltips, id = self.m_menuItem11.GetId() )
		self.Bind( wx.EVT_MENU, self.m_exit, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.m_config_save, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.m_config_load, id = self.m_menuItem7.GetId() )
		self.Bind( wx.EVT_MENU, self.m_log, id = self.m_menuItem8.GetId() )
		self.Bind( wx.EVT_MENU, self.m_help, id = self.m_menuItem9.GetId() )
		self.Bind( wx.EVT_MENU, self.m_about, id = self.m_menuItem10.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def activate( self, event ):
		event.Skip()

	def page_change( self, event ):
		event.Skip()

	def file_path_edit( self, event ):
		event.Skip()

	def file_choose( self, event ):
		event.Skip()

	def noise_origin( self, event ):
		event.Skip()

	def noise_bilateral( self, event ):
		event.Skip()

	def noise_median( self, event ):
		event.Skip()

	def noise_bilateral_update( self, event ):
		event.Skip()


	def noise_median_update( self, event ):
		event.Skip()

	def edge_adaThresh( self, event ):
		event.Skip()

	def edge_Canny( self, event ):
		event.Skip()

	def edge_Scharr( self, event ):
		event.Skip()

	def edge_LoG( self, event ):
		event.Skip()

	def edge_adaThresh_update1( self, event ):
		event.Skip()


	def edge_adaThresh_update2( self, event ):
		event.Skip()

	def edge_Canny_update1( self, event ):
		event.Skip()


	def edge_Canny_update2( self, event ):
		event.Skip()

	def edge_Scharr_update( self, event ):
		event.Skip()


	def edge_LoG_update( self, event ):
		event.Skip()


	def edge_advance_update( self, event ):
		event.Skip()


	def color_static( self, event ):
		event.Skip()

	def color_linear( self, event ):
		event.Skip()

	def color_maze( self, event ):
		event.Skip()

	def color_linear_update( self, event ):
		event.Skip()


	def color_maze_update( self, event ):
		event.Skip()


	def color_maze_center( self, event ):
		event.Skip()

	def color_advance_hue_update( self, event ):
		event.Skip()

	def color_advance_sat_update( self, event ):
		event.Skip()

	def color_advance_sat( self, event ):
		event.Skip()



	def img_export_all( self, event ):
		event.Skip()

	def img_export( self, event ):
		event.Skip()

	def set_default( self, event ):
		event.Skip()

	def img_origin( self, event ):
		event.Skip()

	def file_previous( self, event ):
		event.Skip()

	def file_next( self, event ):
		event.Skip()

	def m_file_choose( self, event ):
		event.Skip()

	def m_folder_choose( self, event ):
		event.Skip()

	def m_img_export( self, event ):
		event.Skip()

	def m_img_export_all( self, event ):
		event.Skip()

	def m_enable_tooltips( self, event ):
		event.Skip()

	def m_exit( self, event ):
		event.Skip()

	def m_config_save( self, event ):
		event.Skip()

	def m_config_load( self, event ):
		event.Skip()

	def m_log( self, event ):
		event.Skip()

	def m_help( self, event ):
		event.Skip()

	def m_about( self, event ):
		event.Skip()



###########################################################################
## Class _LoadingDialog
###########################################################################

class _LoadingDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Export", pos = wx.DefaultPosition, size = wx.Size( 400,120 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer67 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer68 = wx.BoxSizer( wx.VERTICAL )

		bSizer70 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText43 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Processing...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		self.m_staticText43.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer70.Add( self.m_staticText43, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.m_staticText44 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"0 / 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		self.m_staticText44.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer70.Add( self.m_staticText44, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		bSizer68.Add( bSizer70, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 10 )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge1 = wx.Gauge( self.m_panel9, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_gauge1.SetValue( 0 )
		bSizer71.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer68.Add( bSizer71, 0, wx.EXPAND|wx.ALL, 10 )


		self.m_panel9.SetSizer( bSizer68 )
		self.m_panel9.Layout()
		bSizer68.Fit( self.m_panel9 )
		bSizer67.Add( self.m_panel9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer67 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.quit )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def quit( self, event ):
		event.Skip()



###########################################################################
## Class _AboutDialog
###########################################################################

class _AboutDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 480,240 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		bSizer82 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer82.Add( self.m_bitmap2, 0, wx.ALL, 5 )

		bSizer85 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText47 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		self.m_staticText47.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText47.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer85.Add( self.m_staticText47, 0, wx.ALL, 10 )

		self.m_staticText48 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		bSizer85.Add( self.m_staticText48, 0, wx.ALL, 10 )


		bSizer82.Add( bSizer85, 1, wx.EXPAND|wx.TOP, 10 )


		bSizer81.Add( bSizer82, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 10 )

		bSizer83 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer84 = wx.BoxSizer( wx.VERTICAL )


		bSizer83.Add( bSizer84, 1, wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		self.m_button12 = wx.Button( self.m_panel13, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer83.Add( self.m_button12, 0, wx.ALL, 5 )


		bSizer81.Add( bSizer83, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel13.SetSizer( bSizer81 )
		self.m_panel13.Layout()
		bSizer81.Fit( self.m_panel13 )
		bSizer80.Add( self.m_panel13, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer80 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button12.Bind( wx.EVT_BUTTON, self.confirm )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def confirm( self, event ):
		event.Skip()



