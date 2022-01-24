# ===================
# Project : StopMotionMaer
# Author : ParisNeo  (Saifeddine ALOUI)
# Description :
# A free software to create stop motion videos based on moviepy library
# ===================

import pygame
from pygame_helpers import Action, Button, HorizontalLayout, ImageBox, Slider, VerticalLayout, WindowManager, MenuBar, Menu, Timer
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
        self.time_slider = Slider()
        self.time_slider.value=0.5
        self.time_slider.valueChanged_callback = self.slider_updated
        self.time_slider.mouse_down_callback = self.slider_mouse_down
        self.test_ui1 = Button("Zone 1")
        self.test_ui3 = Button("Hello 3")

        self.layout_1.addWidget(self.test_ui1,0.2)
        self.layout_1.addWidget(self.layout_2,0.8)

        self.layout_2.addWidget(self.main_video,0.7)
        self.layout_2.addWidget(self.time_slider,0.05)
        
        self.layout_2.addWidget(self.test_ui3,0.25)

        self.addWidget(self.layout_1)

        self.motion_stuf = self.build_timer(self.do_stuf,1/24)
        self.motion_stuf.start()
        self.t=0
        self.paused = False
        self.clip = VideoFileClip(r'C:\Users\aloui\Videos\test\Terminator.mp4')

    def slider_mouse_down(self):
        self.paused = True
        
    def slider_updated(self, val):
        self.t = self.clip.duration*val
        self.paused = False

    def do_stuf(self):
        if not self.paused:
            self.main_video.setImage(self.clip.get_frame(self.t))
            self.time_slider.setValue(self.t/self.clip.duration)
            self.t += 1/24

    def fn_quit(self):
        self.Running=False
    
# =======================================================================

#
#clip.preview()
if __name__=="__main__":
    mw = MainWindow()
    mw.loop()
