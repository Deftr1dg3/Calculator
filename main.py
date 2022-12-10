#!/usr/bin/env python3


import wx
from math import *
import string


class Frame(wx.Frame):

    def __init__(self):
        super().__init__(None, size=(243, 362),
                         style=wx.MINIMIZE_BOX |
                               wx.CLOSE_BOX | wx.STAY_ON_TOP)

        self.InitUI()

    def InitUI(self):

        self.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        self.top_btn_colour = '#3D4041'
        self.top_on_click = '#a3a5a7'

        self.right_btn_colour = '#FFA800'
        self.right_on_click = '#af6b1b'
        self.right_focused_colour = '#FF5D04'

        self.middle_btn_colour = '#666A6D'
        self.middle_on_click = '#333536'

        self.panel = wx.Panel(self)

        self.divide_focused = 0
        self.mult_focused = 0
        self.minus_focused = 0
        self.plus_focused = 0

        self.on_display = '0'
        self.to_count = ''
        self.selected_operation = False
        self.selected_indicator = False
        self.last_digit_indicator = False

        self.key_indicator = False

        # .........................Display.......................

        self.display = wx.Panel(self.panel, size=(243, 80), pos=(0, 0))
        self.display.SetFocus()

        # .......................Buttons...Panel.....................

        self.buttons_panel = wx.Panel(self.panel, pos=(0, 80), size=(243, 342))

        # .......................TOP..Buttons.....................

        self.btn_ac = wx.Panel(self.buttons_panel, pos=(0, 0), size=(60, 50))
        self.btn_ac.SetBackgroundColour(self.top_btn_colour)
        wx.StaticText(self.btn_ac, label='AC', pos=(14, 13))

        self.btn_sqrt = wx.Panel(self.buttons_panel, pos=(61, 0), size=(60, 50))
        self.btn_sqrt.SetBackgroundColour(self.top_btn_colour)
        wx.StaticText(self.btn_sqrt, label='\u221a', pos=(18, 12))

        self.btn_pow = wx.Panel(self.buttons_panel, pos=(122, 0), size=(60, 50))
        self.btn_pow.SetBackgroundColour(self.top_btn_colour)
        wx.StaticText(self.btn_pow, label='X', pos=(22, 13))
        sqr = wx.StaticText(self.btn_pow, label='2', pos=(37, 5))
        sqr.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        self.btn_divide = wx.Panel(self.buttons_panel, pos=(183, 0), size=(60, 50))
        self.btn_divide.SetBackgroundColour(self.right_btn_colour)
        wx.StaticText(self.btn_divide, label='/', pos=(24, 12))

        # ......................1..ROW..Buttons.....................

        self.btn_7 = wx.Panel(self.buttons_panel, pos=(0, 51), size=(60, 50))
        self.btn_7.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_7, label='7', pos=(22, 13))

        self.btn_8 = wx.Panel(self.buttons_panel, pos=(61, 51), size=(60, 50))
        self.btn_8.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_8, label='8', pos=(22, 13))

        self.btn_9 = wx.Panel(self.buttons_panel, pos=(122, 51), size=(60, 50))
        self.btn_9.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_9, label='9', pos=(22, 13))

        self.btn_mult = wx.Panel(self.buttons_panel, pos=(183, 51), size=(60, 50))
        self.btn_mult.SetBackgroundColour(self.right_btn_colour)
        mult = wx.StaticText(self.btn_mult, label='*', pos=(22, 13))
        mult.SetFont(wx.Font(28, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        # ......................2..ROW..Buttons.....................

        self.btn_4 = wx.Panel(self.buttons_panel, pos=(0, 102), size=(60, 50))
        self.btn_4.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_4, label='4', pos=(22, 13))

        self.btn_5 = wx.Panel(self.buttons_panel, pos=(61, 102), size=(60, 50))
        self.btn_5.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_5, label='5', pos=(22, 13))

        self.btn_6 = wx.Panel(self.buttons_panel, pos=(122, 102), size=(60, 50))
        self.btn_6.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_6, label='6', pos=(22, 13))

        self.btn_minus = wx.Panel(self.buttons_panel, pos=(183, 102), size=(60, 50))
        self.btn_minus.SetBackgroundColour(self.right_btn_colour)
        mult = wx.StaticText(self.btn_minus, label='-', pos=(21, 7))
        mult.SetFont(wx.Font(28, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        # ......................3..ROW..Buttons.....................

        self.btn_1 = wx.Panel(self.buttons_panel, pos=(0, 153), size=(60, 50))
        self.btn_1.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_1, label='1', pos=(22, 13))

        self.btn_2 = wx.Panel(self.buttons_panel, pos=(61, 153), size=(60, 50))
        self.btn_2.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_2, label='2', pos=(22, 13))

        self.btn_3 = wx.Panel(self.buttons_panel, pos=(122, 153), size=(60, 50))
        self.btn_3.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_3, label='3', pos=(22, 13))

        self.btn_plus = wx.Panel(self.buttons_panel, pos=(183, 153), size=(60, 50))
        self.btn_plus.SetBackgroundColour(self.right_btn_colour)
        mult = wx.StaticText(self.btn_plus, label='+', pos=(21, 12))
        mult.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        # ......................4..ROW..Buttons.....................

        self.btn_0 = wx.Panel(self.buttons_panel, pos=(0, 204), size=(121, 50))
        self.btn_0.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_0, label='0', pos=(22, 13))

        self.btn_point = wx.Panel(self.buttons_panel, pos=(122, 204), size=(60, 50))
        self.btn_point.SetBackgroundColour(self.middle_btn_colour)
        wx.StaticText(self.btn_point, label='.', pos=(22, 13))

        self.btn_equals = wx.Panel(self.buttons_panel, pos=(183, 204), size=(60, 50))
        self.btn_equals.SetBackgroundColour(self.right_btn_colour)
        mult = wx.StaticText(self.btn_equals, label='=', pos=(21, 12))
        mult.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        # ......................Binds..........................

        self.btn_divide.Bind(wx.EVT_PAINT, self.OnPaint)
        self.btn_mult.Bind(wx.EVT_PAINT, self.OnPaint)
        self.btn_minus.Bind(wx.EVT_PAINT, self.OnPaint)
        self.btn_plus.Bind(wx.EVT_PAINT, self.OnPaint)
        self.display.Bind(wx.EVT_PAINT, self.OnPaint)

        # ...Bind...Buttons....Down.....................

        self.btn_1.Bind(wx.EVT_LEFT_DOWN, self.On_btn_1)
        self.btn_2.Bind(wx.EVT_LEFT_DOWN, self.On_btn_2)
        self.btn_3.Bind(wx.EVT_LEFT_DOWN, self.On_btn_3)
        self.btn_4.Bind(wx.EVT_LEFT_DOWN, self.On_btn_4)
        self.btn_5.Bind(wx.EVT_LEFT_DOWN, self.On_btn_5)
        self.btn_6.Bind(wx.EVT_LEFT_DOWN, self.On_btn_6)
        self.btn_7.Bind(wx.EVT_LEFT_DOWN, self.On_btn_7)
        self.btn_8.Bind(wx.EVT_LEFT_DOWN, self.On_btn_8)
        self.btn_9.Bind(wx.EVT_LEFT_DOWN, self.On_btn_9)
        self.btn_0.Bind(wx.EVT_LEFT_DOWN, self.On_btn_0)

        self.btn_ac.Bind(wx.EVT_LEFT_DOWN, self.On_ac)
        self.btn_sqrt.Bind(wx.EVT_LEFT_DOWN, self.On_sqrt)
        self.btn_pow.Bind(wx.EVT_LEFT_DOWN, self.On_pow)

        self.btn_divide.Bind(wx.EVT_LEFT_DOWN, self.On_divide)
        self.btn_mult.Bind(wx.EVT_LEFT_DOWN, self.On_mult)
        self.btn_minus.Bind(wx.EVT_LEFT_DOWN, self.On_minus)
        self.btn_plus.Bind(wx.EVT_LEFT_DOWN, self.On_plus)

        self.btn_point.Bind(wx.EVT_LEFT_DOWN, self.On_point)
        self.btn_equals.Bind(wx.EVT_LEFT_DOWN, self.On_equals)

        # .........Bind...Buttons....Up...............

        self.btn_1.Bind(wx.EVT_LEFT_UP, self.Up_btn_1)
        self.btn_2.Bind(wx.EVT_LEFT_UP, self.Up_btn_2)
        self.btn_3.Bind(wx.EVT_LEFT_UP, self.Up_btn_3)
        self.btn_4.Bind(wx.EVT_LEFT_UP, self.Up_btn_4)
        self.btn_5.Bind(wx.EVT_LEFT_UP, self.Up_btn_5)
        self.btn_6.Bind(wx.EVT_LEFT_UP, self.Up_btn_6)
        self.btn_7.Bind(wx.EVT_LEFT_UP, self.Up_btn_7)
        self.btn_8.Bind(wx.EVT_LEFT_UP, self.Up_btn_8)
        self.btn_9.Bind(wx.EVT_LEFT_UP, self.Up_btn_9)
        self.btn_0.Bind(wx.EVT_LEFT_UP, self.Up_btn_0)
        self.btn_point.Bind(wx.EVT_LEFT_UP, self.Up_point)

        self.btn_ac.Bind(wx.EVT_LEFT_UP, self.Up_ac)
        self.btn_sqrt.Bind(wx.EVT_LEFT_UP, self.Up_sqrt)
        self.btn_pow.Bind(wx.EVT_LEFT_UP, self.Up_pow)

        self.btn_divide.Bind(wx.EVT_LEFT_UP, self.Up_divide)
        self.btn_mult.Bind(wx.EVT_LEFT_UP, self.Up_mult)
        self.btn_minus.Bind(wx.EVT_LEFT_UP, self.Up_minus)
        self.btn_plus.Bind(wx.EVT_LEFT_UP, self.Up_plus)

        self.btn_equals.Bind(wx.EVT_LEFT_UP, self.Up_equals)

        # ............Bind...Key...Down.................

        self.display.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.display.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

    # ......................OnPaint........................

    def OnPaint(self, e):

        dc = wx.PaintDC(self.display)

        sizes = [4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5]

        display_font_size = 40

        try:

            if len(self.on_display) > 52:
                display_font_size = 30
                self.on_display = str(format(int(self.on_display), 'e'))

                self.display.SetFont(wx.Font(display_font_size,
                                             wx.DEFAULT, wx.NORMAL, wx.NORMAL))

                dc = wx.PaintDC(self.display)
                dc.DrawText(self.on_display, 5, 30)


            elif len(self.on_display) > 9:
                if len(self.on_display) > 26:
                    display_font_size = 14
                    self.display.SetFont(wx.Font(display_font_size,
                                                 wx.DEFAULT, wx.NORMAL, wx.NORMAL))

                    dc = wx.PaintDC(self.display)
                    dc.DrawText(self.on_display[:26], 5, 30)
                    dc.DrawText(self.on_display[26:], 5, 50)

                else:
                    index = abs(9 - (len(self.on_display)))
                    display_font_size = 40 - (int(sum(sizes[:index])))
                    self.display.SetFont(wx.Font(display_font_size,
                                                 wx.DEFAULT, wx.NORMAL, wx.NORMAL))

                    dc = wx.PaintDC(self.display)
                    dc.DrawText(self.on_display, 5, 30)


            else:

                self.display.SetFont(wx.Font(display_font_size,
                                             wx.DEFAULT, wx.NORMAL, wx.NORMAL))

                dc = wx.PaintDC(self.display)
                dc.DrawText(self.on_display, 5, 30)


        except:

            self.divide_focused = 0
            self.mult_focused = 0
            self.minus_focused = 0
            self.plus_focused = 0

            self.on_display = '0'
            self.to_count = ''
            self.selected_operation = False
            self.selected_indicator = False
            self.last_digit_indicator = False

            self.Refresh()

        focus_border = 1

        if self.divide_focused == 1:
            dc = wx.PaintDC(self.btn_divide)
            dc.SetBrush(wx.Brush('000000', wx.TRANSPARENT))
            dc.SetPen(wx.Pen(self.right_focused_colour, focus_border))
            dc.DrawRectangle(0, 0, self.btn_divide.GetSize().GetWidth(),
                             self.btn_divide.GetSize().GetHeight())

        if self.mult_focused == 1:
            dc = wx.PaintDC(self.btn_mult)
            dc.SetBrush(wx.Brush('000000', wx.TRANSPARENT))
            dc.SetPen(wx.Pen(self.right_focused_colour, focus_border))
            dc.DrawRectangle(0, 0, self.btn_divide.GetSize().GetWidth(),
                             self.btn_divide.GetSize().GetHeight())

        if self.minus_focused == 1:
            dc = wx.PaintDC(self.btn_minus)
            dc.SetBrush(wx.Brush('000000', wx.TRANSPARENT))
            dc.SetPen(wx.Pen(self.right_focused_colour, focus_border))
            dc.DrawRectangle(0, 0, self.btn_divide.GetSize().GetWidth(),
                             self.btn_divide.GetSize().GetHeight())

        if self.plus_focused == 1:
            dc = wx.PaintDC(self.btn_plus)
            dc.SetBrush(wx.Brush('000000', wx.TRANSPARENT))
            dc.SetPen(wx.Pen(self.right_focused_colour, focus_border))
            dc.DrawRectangle(0, 0, self.btn_divide.GetSize().GetWidth(),
                             self.btn_divide.GetSize().GetHeight())

    # ......................Functions.....................

    # ............On....Keys...Down.........

    def OnKeyDown(self, e):

        code = e.GetKeyCode()

        if code in (325, 49):
            self.On_btn_1(None)
        elif code in (326, 50):
            self.On_btn_2(None)
        elif code in (327, 51):
            self.On_btn_3(None)
        elif code in (328, 52):
            self.On_btn_4(None)
        elif code in (329, 53):
            self.On_btn_5(None)
        elif code in (330, 54):
            self.On_btn_6(None)
        elif code in (331, 55):
            self.On_btn_7(None)
        elif code in (332, 56):
            self.On_btn_8(None)
        elif code in (333, 57):
            self.On_btn_9(None)
        elif code in (324, 48):
            self.On_btn_0(None)
        elif code == 391:
            self.On_point(None)
        elif code == 392:
            self.On_divide(None)
        elif code == 305:
            self.On_ac(None)
        elif code == 387:
            self.On_mult(None)
        elif code == 390:
            self.On_minus(None)
        elif code == 388:
            self.On_plus(None)
        elif code in (370, 13):
            self.On_equals(None)

    # ............On....Keys...Up.........

    def OnKeyUp(self, e):

        code = e.GetKeyCode()

        if code in (325, 49):
            self.Up_btn_1(None)
        elif code in (326, 50):
            self.Up_btn_2(None)
        elif code in (327, 51):
            self.Up_btn_3(None)
        elif code in (328, 52):
            self.Up_btn_4(None)
        elif code in (329, 53):
            self.Up_btn_5(None)
        elif code in (330, 54):
            self.Up_btn_6(None)
        elif code in (331, 55):
            self.Up_btn_7(None)
        elif code in (332, 56):
            self.Up_btn_8(None)
        elif code in (333, 57):
            self.Up_btn_9(None)
        elif code in (324, 48):
            self.Up_btn_0(None)
        elif code == 391:
            self.Up_point(None)
        elif code == 392:
            self.Up_divide(None)
        elif code == 305:
            self.Up_ac(None)
        elif code == 387:
            self.Up_mult(None)
        elif code == 390:
            self.Up_minus(None)
        elif code == 388:
            self.Up_plus(None)
        elif code in (370, 13):
            self.Up_equals(None)

    # .....On...Buttons...Down............

    def On_equals(self, e):

        if self.last_digit_indicator and self.to_count:
            self.on_display = str(eval(self.to_count + self.selected_operation + self.on_display))
        self.to_count = ''
        self.selected_operation = False
        self.selected_indicator = False
        self.last_digit_indicator = False

        self.btn_equals.SetBackgroundColour(self.right_on_click)

        self.divide_focused = 0
        self.mult_focused = 0
        self.minus_focused = 0
        self.plus_focused = 0

        self.display.SetFocus()

        self.Refresh()

    # .......Top....Buttons..............

    def On_ac(self, e):

        self.divide_focused = 0
        self.mult_focused = 0
        self.minus_focused = 0
        self.plus_focused = 0

        self.on_display = '0'
        self.to_count = ''
        self.selected_operation = False
        self.selected_indicator = False
        self.last_digit_indicator = False

        self.display.SetFocus()

        self.btn_ac.SetBackgroundColour(self.top_on_click)
        self.Refresh()

    def On_sqrt(self, e):

        if self.on_display != '0':
            self.on_display = str(sqrt(float(self.on_display)))

        self.display.SetFocus()

        self.btn_sqrt.SetBackgroundColour(self.top_on_click)
        self.Refresh()

    def On_pow(self, e):

        try:
            if self.on_display != '0':
                self.on_display = str(pow(float(self.on_display), 2))
        except:

            wx.MessageBox('Math range error', 'ERROR:')

            self.divide_focused = 0
            self.mult_focused = 0
            self.minus_focused = 0
            self.plus_focused = 0

            self.on_display = '0'
            self.to_count = ''
            self.selected_operation = False
            self.selected_indicator = False
            self.last_digit_indicator = False

        self.display.SetFocus()

        self.btn_pow.SetBackgroundColour(self.top_on_click)
        self.Refresh()

    # ..............Operations................

    def On_divide(self, e):

        self.btn_divide.SetBackgroundColour(self.right_on_click)

        self.divide_focused = not self.divide_focused
        if self.divide_focused:
            self.selected_operation = '/'
            self.selected_indicator = True
            self.to_count += self.on_display
        else:
            self.selected_operation = False
            self.selected_indicator = False
            self.to_count = ''

        self.mult_focused = 0
        self.minus_focused = 0
        self.plus_focused = 0

        self.display.SetFocus()

        self.Refresh()

    def On_mult(self, e):

        self.btn_mult.SetBackgroundColour(self.right_on_click)

        self.mult_focused = not self.mult_focused
        if self.mult_focused:
            self.selected_operation = '*'
            self.selected_indicator = True
            self.to_count += self.on_display
        else:
            self.selected_operation = False
            self.selected_indicator = False
            self.to_count = ''

        self.divide_focused = 0
        self.minus_focused = 0
        self.plus_focused = 0

        self.display.SetFocus()

        self.Refresh()

    def On_minus(self, e):

        self.btn_minus.SetBackgroundColour(self.right_on_click)

        self.minus_focused = not self.minus_focused
        if self.minus_focused:
            self.selected_operation = '-'
            self.selected_indicator = True
            self.to_count += self.on_display
        else:
            self.selected_operation = False
            self.selected_indicator = False
            self.to_count = ''

        self.divide_focused = 0
        self.mult_focused = 0
        self.plus_focused = 0

        self.display.SetFocus()

        self.Refresh()

    def On_plus(self, e):

        self.btn_plus.SetBackgroundColour(self.right_on_click)

        self.plus_focused = not self.plus_focused
        if self.plus_focused:
            self.selected_operation = '+'
            self.selected_indicator = True
            self.to_count += self.on_display
        else:
            self.selected_operation = False
            self.selected_indicator = False
            self.to_count = ''

        self.divide_focused = 0
        self.minus_focused = 0
        self.mult_focused = 0

        self.display.SetFocus()

        self.Refresh()

    # ..............Middle...Buttons..................

    def On_btn_1(self, e):

        if self.selected_indicator:
            self.on_display = '1'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '1'
            else:
                self.on_display += '1'

        self.display.SetFocus()

        self.btn_1.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_2(self, e):

        if self.selected_indicator:
            self.on_display = '2'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '2'
            else:
                self.on_display += '2'

        self.display.SetFocus()

        self.btn_2.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_3(self, e):

        if self.selected_indicator:
            self.on_display = '3'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '3'
            else:
                self.on_display += '3'

        self.display.SetFocus()

        self.btn_3.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_4(self, e):

        if self.selected_indicator:
            self.on_display = '4'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '4'
            else:
                self.on_display += '4'

        self.display.SetFocus()

        self.btn_4.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_5(self, e):

        if self.selected_indicator:
            self.on_display = '5'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '5'
            else:
                self.on_display += '5'

        self.display.SetFocus()

        self.btn_5.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_6(self, e):

        if self.selected_indicator:
            self.on_display = '6'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '6'
            else:
                self.on_display += '6'

        self.display.SetFocus()

        self.btn_6.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_7(self, e):

        if self.selected_indicator:
            self.on_display = '7'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '7'
            else:
                self.on_display += '7'

        self.display.SetFocus()

        self.btn_7.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_8(self, e):

        if self.selected_indicator:
            self.on_display = '8'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '8'
            else:
                self.on_display += '8'

        self.display.SetFocus()

        self.btn_8.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_9(self, e):

        if self.selected_indicator:
            self.on_display = '9'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:

            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '9'
            else:
                self.on_display += '9'

        self.display.SetFocus()

        self.btn_9.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_btn_0(self, e):

        if self.selected_indicator:
            self.on_display = '0'
            self.selected_indicator = False
            self.last_digit_indicator = True

        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '0'
            else:
                self.on_display += '0'

        self.display.SetFocus()

        self.btn_0.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    def On_point(self, e):

        if self.selected_indicator:
            pass
        else:
            if len(self.on_display) == 1 and self.on_display == '0':
                self.on_display = '.'
            else:
                self.on_display += '.'

        self.display.SetFocus()

        self.btn_point.SetBackgroundColour(self.middle_on_click)
        self.Refresh()

    # .................On...Button...Up...................

    def Up_equals(self, e):

        self.btn_equals.SetBackgroundColour(self.right_btn_colour)
        self.Refresh()

    def Up_ac(self, e):
        self.btn_ac.SetBackgroundColour(self.top_btn_colour)
        self.Refresh()

    def Up_sqrt(self, e):
        self.btn_sqrt.SetBackgroundColour(self.top_btn_colour)
        self.Refresh()

    def Up_pow(self, e):
        self.btn_pow.SetBackgroundColour(self.top_btn_colour)
        self.Refresh()

    def Up_divide(self, e):

        self.btn_divide.SetBackgroundColour(self.right_btn_colour)
        self.Refresh()

    def Up_mult(self, e):

        self.btn_mult.SetBackgroundColour(self.right_btn_colour)
        self.Refresh()

    def Up_minus(self, e):
        self.btn_minus.SetBackgroundColour(self.right_btn_colour)
        self.Refresh()

    def Up_plus(self, e):
        self.btn_plus.SetBackgroundColour(self.right_btn_colour)
        self.Refresh()

    def Up_btn_1(self, e):

        self.btn_1.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_2(self, e):
        self.btn_2.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_3(self, e):
        self.btn_3.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_4(self, e):
        self.btn_4.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_5(self, e):
        self.btn_5.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_6(self, e):
        self.btn_6.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_7(self, e):
        self.btn_7.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_8(self, e):
        self.btn_8.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_9(self, e):
        self.btn_9.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_btn_0(self, e):
        self.btn_0.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()

    def Up_point(self, e):
        self.btn_point.SetBackgroundColour(self.middle_btn_colour)
        self.Refresh()


app = wx.App()
Frame().Show()
app.MainLoop()
