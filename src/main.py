# ===================
# Project : StopMotionMaer
# Author : ParisNeo  (Saifeddine ALOUI)
# Description :
# A free software to create stop motion videos based on moviepy library
# ===================

import pygame
from pygame_helpers import Action, WindowManager, MenuBar, Menu, Timer
from moviepy.editor import VideoFileClip

# ===== Build pygame window and populate with widgets ===================
pygame.init()
class MainWindow(WindowManager):
    def __init__(self):
        WindowManager.__init__(self, "Face box", (800,600))
        self.mn_bar = self.build_menu_bar()
        self.file = Menu(self.mn_bar,"File")
        quit = Action(self.file,"Quit")
        quit.clicked_event_handler = self.fn_quit
        self.edit = Menu(self.mn_bar,"Edit")

        self.motion_stuf = self.build_timer(self.do_stuf,1)
        self.motion_stuf.start()
        self.i=0
    def do_stuf(self):
        print(f"{self.i}")
        self.i += 1

    def fn_quit(self):
        self.Running=False
    
# =======================================================================

#clip = VideoFileClip(r'C:\Users\aloui\Videos\test\Terminator.mp4')
#clip.preview()
if __name__=="__main__":
    mw = MainWindow()
    mw.loop()
