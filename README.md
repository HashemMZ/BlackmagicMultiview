# BlackmagicMultiview
Control Blackmagic Multiview-16 using telnet protocol and PyQt5

I tried to use MVC pattern in the code but it seemed that there are some problems in passing the object of view class to controller class. so I combinec view and controller classes into one class.

# Structure of hardware
we have six screens (TV sets) that each display 16 smaller screens. Each of these screens are fed by a Blackmagic Multiview 16 (in a 4 by 4 matrix of videos). 

![mv16and4-xl 1](https://github.com/HashemMZ/BlackmagicMultiview/assets/22125275/646a1297-3b13-43ae-987b-2489b4fc27a4)
The Blackmagic Multiview 16 can be controlled by telnet protocol which is briefly described in its manual. It has 16 input channels that can be displayed in different combination say 4x4, 2x2, or the like. 
# our requirements
We need to control BM remotely. By the way these devices use strong fans for cooling purposes that can be annoying if you insatll them in your control room. Our need is to be able to show 16 input alltogether in a 4x4 format on the screen. We also need to be able to select one of the sub-screens and watch it in full view. So I decided a GUI like this: 
![Annotation 2023-05-10 223150](https://github.com/HashemMZ/BlackmagicMultiview/assets/22125275/4a2a4cb2-b448-4331-b05f-b4ff1eefb8c4)

By selecting each of the main screens(here named Rack1 to Rack4 and Nodal SD and Nodal HD) we can go for selecting one of its sub-screen upon clicking on one of the buttons 1 to 16. clicking again on one of the main screen buttons that screen switches back to 4 by 4 view.

To name the buttons on the GUI I used a settings.txt file that simply contains the name of device and more importantly the IP's of each device on your network.



