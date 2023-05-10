# BlackmagicMultiview
Control Blackmagic Multiview-16 using telnet protocol and PyQt5

I tried to use MVC pattern in the code but it seemed that there are some problems in passing the object of view class to controller class. so I combinec view and controller classes into one class.

# Structure of hardware
we have six screens that each contain 16 smaller screens. each of the screens are produced by a Blackmagic Multiview 16 (in a 4 by 4 matrix of videos). The Blackmagic Multiview can be controlled by telnet protocol which is briefly described in its manual. 
by selecting each of screens we can select one of the child screen upon clicking on one of the buttons 1 to 16. clicking again on one of the primary buttons that screen switches back to 4 by 4 view

![Annotation 2023-05-10 223150](https://github.com/HashemMZ/BlackmagicMultiview/assets/22125275/4a2a4cb2-b448-4331-b05f-b4ff1eefb8c4)


