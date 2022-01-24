# ===================
# Project : StopMotionMaer
# Author : ParisNeo  (Saifeddine ALOUI)
# Description :
# A free software to create stop motion videos based on moviepy library
# ===================

import pygame
from pygame_helpers import Action, Button, HorizontalLayout, ImageBox, VerticalLayout, WindowManager, MenuBar, Menu, Timer
from moviepy.editor import VideoFileClip

# ===== Build pygame window and populate with widgets ===================
pygame.init()
class MainWindow(WindowManager):
    def __init__(self):
        WindowManager.__init__(self, "Face box", (800,600))
        self.mn_bar = self.build_menu_bar()
        self.file = Menu(self.mn_bar,"File")
        new = Action(self.file,"New")
        quit = Action(self.file,"Quit")
        quit.clicked_event_handler = self.fn_quit
        self.edit = Menu(self.mn_bar,"Edit")

        self.layout_1 = HorizontalLayout()
        self.layout_2 = VerticalLayout()

        self.main_video = ImageBox()
        self.test_ui1 = Button("Zone 1")
        self.test_ui3 = Button("Hello 3")
        self.layout_1.addWidget(self.test_ui1,0.2)
        self.layout_1.addWidget(self.layout_2,0.8)

        self.layout_2.addWidget(self.main_video,0.7)
        self.layout_2.addWidget(self.test_ui3,0.3)
        self.addWidget(self.layout_1)

        self.motion_stuf = self.build_timer(self.do_stuf,1/24)
        self.motion_stuf.start()
        self.i=0

        self.clip = VideoFileClip(r'C:\Users\aloui\Videos\test\Terminator.mp4')
    def do_stuf(self):
        self.main_video.setImage(self.clip.get_frame(self.i*1/24))
        self.i += 1

    def fn_quit(self):
        self.Running=False
    
# =======================================================================

#
#clip.preview()
if __name__=="__main__":
    mw = MainWindow()
    mw.loop()
