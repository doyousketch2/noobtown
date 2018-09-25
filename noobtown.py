#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" info  =============================================="""

##  noobtown.py                                   Sept 2018
##  @ Doyousketch2
##  GNU AGPLv3            gnu.org/licenses/agpl-3.0.en.html

""" required  =========================================="""

##        sudo pip3 install keyboard
##  (or)
##        sudo python3 -m pip install keyboard

""" libs  =============================================="""

import gi                         ##  GObject Introspection
gi .require_version( 'Gtk', '3.0' )
from gi .repository import Gtk
from gi .repository import Gdk
import calibration as cali

##  ended up importing keyboard instead of keybinder
##  better examples, can get it to run, but you have to use sudo...

""" vars  =============================================="""

x, y  = 0, 0
button  = ''

default_width   = 400
default_height  = 250

appname  = 'noobtown.py'
ver    = '1.2'

window  = Gdk .get_default_root_window()

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##  https://stackoverflow.com/questions/1605350/how-can-i-grab-the-color-of-a-pixel-on-my-desktop-linux

def PixelAt(x, y):
    pixel  = Gdk .pixbuf_get_from_window(  window,  x,  y,  1,  1  )
    return tuple( pixel .get_pixels() )

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MainWindow( Gtk .Window ):

    def __init__( self ):
        Gtk .Window .__init__( self,  title = appname )
        horiz_box  = 0
        vert_box  = 1
        container  = Gtk .Box .new( horiz_box, 0 )
        self .add( container )

        label  = Gtk .Label .new()
        label .set_markup( "<span foreground='blue' size='26000' font_weight='bold' underline='double'>Noobtown</span>" )
        label .set_angle( 90 )
        container .pack_start( label, False, False, 40 )

        vert  = Gtk .Box .new( vert_box, 0 )
        container .pack_start( vert, True, True, 0 )

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        about  = Gtk .Button( label = 'About' )
        about .connect( 'clicked',  self .about_clicked )
        vert .pack_start( about, True, True, 0 )

        help  = Gtk .Button( label = 'Help' )
        help .connect( 'clicked',  self .help_clicked )
        vert .pack_start( help, True, True, 0 )

        calibration  = Gtk .Button( label = 'Calibration' )
        calibration .connect( 'clicked',  self .calibration_clicked )
        vert .pack_start( calibration, True, True, 0 )

        new  = Gtk .Button( label = 'Create New Script' )
        new .connect( 'clicked',  self .new_clicked )
        vert .pack_start( new, True, True, 0 )

        select  = Gtk .Button( label = 'Select a Script' )
        select .connect( 'clicked',  self .select_clicked )
        vert .pack_start( select, True, True, 0 )

        cont  = Gtk .Button( label = 'Continue a Script' )
        cont .connect( 'clicked',  self .cont_clicked )
        vert .pack_start( cont, True, True, 0 )

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def help_clicked( self,  widget ):
        print( 'help_clicked' )
        dialog  = Gtk.MessageDialog( self, 0, Gtk.MessageType .INFO,
            Gtk .ButtonsType .OK, 'Noobtown')
        dialog .format_secondary_text(
            "Make sure Minetest is open.\n\nClick Calibration.\n\nRead Help in there to get started.")
        dialog .run()
        print('main help closed')
        dialog .destroy()


    def calibration_clicked( self,  widget ):
        print( 'calibration_clicked' )
        subwindow  = cali .bration( self )
        subwindow .run()
        print( 'calibration closed' )
        subwindow .destroy()

    def new_clicked( self,  widget ):
        print( 'new_clicked' )

    def select_clicked( self,  widget ):
        print( 'select_clicked' )

    def cont_clicked( self,  widget ):
        print( 'cont_clicked' )

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def about_clicked( self,  widget ):
        print('about_clicked')
        popup  = Gtk .AboutDialog(  self,  logo  = None,
                                    authors  = [ 'Eli Innis',
                                                 'in-game:  Sketch2',
                                                 'twitter:  @Doyousketch2',
                                                 'email:  Doyousketch2 @ yahoo.com' ],
                                    copyright  = 'Copyright 2018',
                                    license_type  = Gtk .License .GPL_3_0,
                                    version  = ver  )
        popup .set_transient_for( self )
        popup .set_modal( True )
        popup .run()
        popup .destroy()

"""  main  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

win  = MainWindow()
win .connect( 'destroy',  Gtk .main_quit )
win .set_default_size( default_width,  default_height )
win .set_position( Gtk .WindowPosition .CENTER_ALWAYS )
win .set_title( appname )
win .show_all()
Gtk .main()

"""  eof  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

