#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" info  =============================================="""

##  calibrate.py                                   Aug 2018
##  @ Doyousketch2
##  GNU AGPLv3            gnu.org/licenses/agpl-3.0.en.html

""" required  =========================================="""

##        sudo pip3 install keyboard
##  (or)
##        sudo python3 -m pip install keyboard

""" libs  =============================================="""

import os                                   ##  commandline
import gi                         ##  GObject Introspection
gi .require_version( 'Gtk', '3.0' )
from gi .repository import Gtk
import subprocess as sp           ##  commandline processes
import keyboard
import pickle                             ##  save settings

##  ended up importing keyboard instead of keybinder
##  better examples, can get it to run, but you have to use sudo...

""" vars  =============================================="""

popup_width  = 500
popup_height  = 300
popupname  = 'calibration.py'

getmouse        = [ 'xdotool', 'getmouselocation' ]
find_minetest   = [ 'xdotool', 'search', '--name', 'Minetest .*' ]
raise_minetest  = [ 'xdotool', 'search', '--name', 'Minetest .*', 'windowactivate' ]
lower_minetest  = [ 'xdotool', 'search', '--name', 'Minetest .*', 'windowminimize' ]
raise_cali      = [ 'xdotool', 'search', '--name', 'calibration', 'windowactivate' ]

data  = {
    'craftgrid'  : {
            'upper'  : 0,
            'middle' : 0,
            'lower'  : 0,

            'left'   : 0,
            'center' : 0,
            'right'  : 0
                   },

    'crafttab' : { 'x':0,  'y':0 },
    'output'   : { 'x':0,  'y':0 },
    'trash'    : { 'x':0,  'y':0 },

    'invslots'  : {
            '1'  : 0,
            '2'  : 0,
            '3'  : 0,
            '4'  : 0,

            'a'  : 0,
            'b'  : 0,
            'c'  : 0,
            'd'  : 0,

            'e'  : 0,
            'f'  : 0,
            'g'  : 0,
            'h'  : 0
                  }
}

""" functs  ============================================"""

def xy():
    global x, y
    getlocation  = sp .Popen( getmouse,  stdout = sp .PIPE )
    location  = getlocation .communicate()[0] .decode('utf-8')

    x  = int( location .split(':') [1] .rstrip(' y') )
    y  = int( location .split(':') [2] .rstrip(' screen') )
    print( 'x:', x, 'y:', y )

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def noobtown():
    global data
    xy()

    if button == 'tab_clicked':
        data ['crafttab'] ['x']  = x
        data ['crafttab'] ['y']  = y

    elif button == 'upper_left_clicked':
        data ['craftgrid'] ['left']  = x
        data ['craftgrid'] ['upper'] = y

        calculate_craftgrid()

    elif button == 'lower_right_clicked':
        data ['craftgrid'] ['right']  = x
        data ['craftgrid'] ['lower']  = y

        calculate_craftgrid()

    elif button == 'output_clicked':
        data ['output'] ['x']  = x
        data ['output'] ['y']  = y

    elif button == 'trash_clicked':
        data ['trash'] ['x']  = x
        data ['trash'] ['y']  = y

    elif button == 'a1_clicked':
        data ['invslots'] ['a']  = x
        data ['invslots'] ['1']  = y

        calculate_invslots()

    elif button == 'h4_clicked':

        data ['invslots'] ['h']  = x
        data ['invslots'] ['4']  = y

        calculate_invslots()

    with open( 'dill.pickle', 'wb' ) as file_out:
        peck  = pickle .HIGHEST_PROTOCOL
        pickle .dump(  data,  file_out,  protocol = peck  )

    sp. call( lower_minetest )
    sp. call( raise_cali )
    sp. call( raise_cali )

keyboard .add_hotkey( '`',  noobtown )

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def calculate_craftgrid():
    x1  = data ['craftgrid'] ['left']
    y1  = data ['craftgrid'] ['upper']

    x3  = data ['craftgrid'] ['right']
    y3  = data ['craftgrid'] ['lower']

    if x1 != 0 and y1 != 0 and x3 != 0 and y3 != 0:
        x2  = int( (x3 -x1) /2 +x1 )
        y2  = int( (y3 -y1) /2 +y1 )

        data ['craftgrid'] ['middle']  = x2
        data ['craftgrid'] ['center']  = y2

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def calculate_invslots():
    x1  = data ['invslots'] ['a']
    y1  = data ['invslots'] ['1']

    x8  = data ['invslots'] ['h']
    y4  = data ['invslots'] ['4']

    if x1 != 0 and y1 != 0 and x8 != 0 and y4 != 0:
        intervalX  = (x8 -x1) /7
        intervalY  = (y4 -y1) /3

        x2  = int( x1 +intervalX )
        x3  = int( x1 +intervalX *2 )
        x4  = int( x1 +intervalX *3 )

        x5  = int( x8 -intervalX *3 )
        x6  = int( x8 -intervalX *2 )
        x7  = int( x8 -intervalX )

        y2  = int( y1 +intervalY )
        y3  = int( y1 +intervalY *2 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        data ['invslots'] ['b']  = x2
        data ['invslots'] ['c']  = x3
        data ['invslots'] ['d']  = x4

        data ['invslots'] ['e']  = x5
        data ['invslots'] ['f']  = x6
        data ['invslots'] ['g']  = x7

        data ['invslots'] ['2']  = y2
        data ['invslots'] ['3']  = y3

""" script  ============================================"""

if os .path .isfile( 'dill.pickle' ):
    with open( 'dill.pickle', 'rb' ) as file_in:
        data  = pickle .load( file_in )

        s  = '   '  ##  spaces to pad print statements
        print(  'crafttab   ',  s,
          data ['crafttab'] ['x'],  s,  data ['crafttab'] ['y']  )

        print(  'upper_left ',  s,
          data ['craftgrid'] ['left'],  s,  data ['craftgrid'] ['upper']  )

        print(  'lower_right',  s,
          data ['craftgrid'] ['right'],  s,  data ['craftgrid'] ['lower']  )

        print(  'output',  s,
          data ['output'] ['x'],  s,  data ['output'] ['y']  )

        print(  'trash ',  s,
          data ['trash'] ['x'],  s,  data ['trash'] ['y']  )

        print(  'a1    ',  s,
          data ['invslots'] ['a'],  s,  data ['invslots'] ['1']  )

        print(  'h4    ',  s,
          data ['invslots'] ['h'],  s,  data ['invslots'] ['4']  )

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class bration( Gtk .Dialog ):

    def __init__( self,  parent ):
        Gtk .Dialog .__init__(  self,  popupname,  parent,  0  )

        self .set_default_size( popup_width,  popup_height )

        horiz_box  = 0
        vert_box  = 1
        box  = self .get_content_area()

        tab_horiz  = Gtk .Box .new( horiz_box,  0 )
        box .pack_start( tab_horiz, True, True, 0 )

        tab  = Gtk .Button( label = 'Crafting Tab' )
        tab .connect( 'clicked',  self .tab_clicked )
        tab_horiz .pack_start( tab, False, False, 0 )

        back  = Gtk .Button( label = 'Back to Main Menu')
        back .connect( 'clicked',  self .back_clicked )
        tab_horiz .pack_start( back, True, True, 0 )

        help  = Gtk .Button( label = 'Help' )
        help .connect( 'clicked',  self .help_clicked )
        tab_horiz .pack_start( help, True, True, 0 )

        grid_horiz  = Gtk .Box .new( horiz_box,  0 )
        box .pack_start( grid_horiz, True, True, 15 )

        craft  = Gtk .Grid .new()
        craft .width  = 3
        craft .height  = 3
        craft .props .column_spacing  = 12
        craft .props .row_spacing  = 12
        grid_horiz .pack_start( craft, True, True, 0 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        upper_left  = Gtk .Button( label = 'Upper Left' )
        upper_left .connect( 'clicked',  self .upper_left_clicked )
        craft .attach( upper_left,  1,  2,  1,  1 )

        upper_middle  = Gtk .Label( 'Upper Center' )
        craft .attach( upper_middle,  2,  2,  1,  1 )

        upper_right  = Gtk .Label( 'Upper Right' )
        craft .attach( upper_right,  3,  2,  1,  1 )

        middle_left  = Gtk .Label( 'Middle Left' )
        craft .attach( middle_left,  1,  3,  1,  1 )

        middle_center  = Gtk .Label( 'Middle Center' )
        craft .attach( middle_center,  2,  3,  1,  1 )

        middle_right  = Gtk .Label( 'Middle Right' )
        craft .attach( middle_right,  3,  3,  1,  1 )

        lower_left  = Gtk .Label( 'Lower Left' )
        craft .attach( lower_left,  1,  4,  1,  1 )

        lower_center  = Gtk .Label( 'Lower Center' )
        craft .attach( lower_center,  2,  4,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        lower_right  = Gtk .Button( label = 'Lower Right' )
        lower_right .connect('clicked',  self .lower_right_clicked)
        craft .attach( lower_right,  3,  4,  1,  1 )

        craft_out  = Gtk .Box .new( vert_box, 0 )
        grid_horiz .pack_start( craft_out, True, True, 0 )

        output  = Gtk .Button( label = 'Output' )
        output .connect('clicked',  self .output_clicked)
        craft_out .pack_start( output, True, False, 0 )

        trash  = Gtk .Button( label = 'Trash' )
        trash .connect('clicked',  self .trash_clicked)
        craft_out .pack_start( trash, True, False, 0 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        inv  = Gtk .Grid .new()
        inv .width  = 8
        inv .height  = 4
        inv .props .column_spacing  = 38
        inv .props .row_spacing  = 15
        box .pack_start( inv, True, True, 0 )

        a1  = Gtk .Button( label = 'A1' )
        a1 .connect('clicked',  self .a1_clicked)
        inv .attach( a1,  1,  5,  1,  1 )

        a2  = Gtk .Label( 'A2' )
        inv .attach( a2,  1,  6,  1,  1 )

        a3  = Gtk .Label( 'A3' )
        inv .attach( a3,  1,  7,  1,  1 )

        a4  = Gtk .Label( 'A4' )
        inv .attach( a4,  1,  8,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        b1  = Gtk .Label( 'B1' )
        inv .attach( b1,  2,  5,  1,  1 )

        b2  = Gtk .Label( 'B2' )
        inv .attach( b2,  2,  6,  1,  1 )

        b3  = Gtk .Label( 'B3' )
        inv .attach( b3,  2,  7,  1,  1 )

        b4  = Gtk .Label( 'B4' )
        inv .attach( b4,  2,  8,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        c1  = Gtk .Label( 'C1' )
        inv .attach( c1,  3,  5,  1,  1 )

        c2  = Gtk .Label( 'C2' )
        inv .attach( c2,  3,  6,  1,  1 )

        c3  = Gtk .Label( 'C3' )
        inv .attach( c3,  3,  7,  1,  1 )

        c4  = Gtk .Label( 'C4' )
        inv .attach( c4,  3,  8,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        d1  = Gtk .Label( 'D1' )
        inv .attach( d1,  4,  5,  1,  1 )

        d2  = Gtk .Label( 'D2' )
        inv .attach( d2,  4,  6,  1,  1 )

        d3  = Gtk .Label( 'D3' )
        inv .attach( d3,  4,  7,  1,  1 )

        d4  = Gtk .Label( 'D4' )
        inv .attach( d4,  4,  8,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        e1  = Gtk .Label( 'E1' )
        inv .attach( e1,  5,  5,  1,  1 )

        e2  = Gtk .Label( 'E2' )
        inv .attach( e2,  5,  6,  1,  1 )

        e3  = Gtk .Label( 'E3' )
        inv .attach( e3,  5,  7,  1,  1 )

        e4  = Gtk .Label( 'E4' )
        inv .attach( e4,  5,  8,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        f1  = Gtk .Label( 'F1' )
        inv .attach( f1,  6,  5,  1,  1 )

        f2  = Gtk .Label( 'F2' )
        inv .attach( f2,  6,  6,  1,  1 )

        f3  = Gtk .Label( 'F3' )
        inv .attach( f3,  6,  7,  1,  1 )

        f4  = Gtk .Label( 'F4' )
        inv .attach( f4,  6,  8,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        g1  = Gtk .Label( 'G1' )
        inv .attach( g1,  7,  5,  1,  1 )

        g2  = Gtk .Label( 'G2' )
        inv .attach( g2,  7,  6,  1,  1 )

        g3  = Gtk .Label( 'G3' )
        inv .attach( g3,  7,  7,  1,  1 )

        g4  = Gtk .Label( 'G4' )
        inv .attach( g4,  7,  8,  1,  1 )

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        h1  = Gtk .Label( 'H1' )
        inv .attach( h1,  8,  5,  1,  1 )

        h2  = Gtk .Label( 'H2' )
        inv .attach( h2,  8,  6,  1,  1 )

        h3  = Gtk .Label( 'H3' )
        inv .attach( h3,  8,  7,  1,  1 )

        h4  = Gtk .Button( label = 'H4' )
        h4 .connect( 'clicked',  self .h4_clicked )
        inv .attach( h4,  8,  8,  1,  1 )

        self .show_all()

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def tab_clicked( self,  widget ):
        global button
        button  = 'tab_clicked'
        sp .call( raise_minetest )
        print( button )

    def back_clicked( self,  widget ):
        print( 'back_clicked' )
        self .do_close( self )

    def upper_left_clicked( self,  widget ):
        global button
        button  = 'upper_left_clicked'
        sp .call( raise_minetest )
        print( button )

    def lower_right_clicked( self,  widget ):
        global button
        button  = 'lower_right_clicked'
        sp .call( raise_minetest )
        print( button )

    def output_clicked( self,  widget ):
        global button
        button  = 'output_clicked'
        sp .call( raise_minetest )
        print( button )

    def trash_clicked( self,  widget ):
        global button
        button  = 'trash_clicked'
        sp .call( raise_minetest )
        print( button )

    def a1_clicked( self,  widget ):
        global button
        button  = 'a1_clicked'
        sp .call( raise_minetest )
        print( button )

    def h4_clicked( self,  widget ):
        global button
        button  = 'h4_clicked'
        sp .call( raise_minetest )
        print( button )

    def help_clicked( self,  widget ):
        print('help_clicked')
        dialog  = Gtk.MessageDialog(  self,  0,  Gtk .MessageType .INFO,
            Gtk .ButtonsType .OK,  'Noobtown calibration'  )
        dialog .format_secondary_text(
            "Make sure Minetest is open.\n\nClick one of the positional buttons.\n\nOpen your craft-grid in Minetest.\nHover mouse over the relevant location.\n\nPress the ` key  (left of number 1 key)\n\nRepeat for the other positions.")
        dialog .run()
        print('calibration help closed')
        dialog .destroy()

"""  eof  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

