#Imports tkinter to make the GUI 
from tkinter import *
#Imports pillow to make images
from PIL import Image, ImageTk
#Imports font module
import tkinter.font as font

#Function which makes buttons for menu pages
def Module_Button(self, properties, colour, font, controller):
    button = Button(self, text=properties[0], font=font, bg=colour, bd="5", relief="solid", command=lambda: controller.show_frame(properties[1]))
    return button

#Function to add a back button to a page using grid geometry manager
def Back_button_grid(self, controller, previous_page):

    #Creates back button
    #Fetches image
    LoadBack = Image.open("BackButton.jpg")
    #Resizes image
    LoadBack = LoadBack.resize((80,40), Image.ANTIALIAS)
    #Creates PhotoImage object
    RenderBack = ImageTk.PhotoImage(LoadBack)
    #Makes a back button with the image
    back = Button(self, image=RenderBack, bd="0", bg="#97ff97", command=lambda: controller.show_frame(previous_page))
    #Places the image on the button
    back.image = RenderBack
    #Puts the back button in the top left hand corner of the page
    back.grid(column=0, row=0, padx="10", pady="10", sticky="nw")

#Function to add a back button to a page using pack geometry manager
def Back_button_pack(self, controller, previous_page):
    
    #Creates back button
    #Fetches image
    LoadBack = Image.open("BackButton.jpg")
    #Resizes image
    LoadBack = LoadBack.resize((80,40), Image.ANTIALIAS)
    #Creates PhotoImage object
    RenderBack = ImageTk.PhotoImage(LoadBack)
    #Makes a back button with the image
    back = Button(self, image=RenderBack, bd="0", bg="#97ff97", command=lambda: controller.show_frame(previous_page))
    #Places the image on the button
    back.image = RenderBack
    #Puts the back button in the top right hand corner of the page
    back.pack(padx="10", pady="10", anchor="nw")

#Creates an infomation button which brings up the key for entering function, uses .grid
def Infomation_button(self, number_of_colunms, full_trig):
    #Fetches image
    LoadInfo = Image.open("InfomationButton.jpg")
    #Resizes image
    LoadInfo = LoadInfo.resize((50,50), Image.ANTIALIAS)
    #Creates PhotoImage object
    RenderInfo = ImageTk.PhotoImage(LoadInfo)
    if full_trig == True:
        #Makes a back button with the image for all trig functions
        info = Button(self, image=RenderInfo, bd="0", bg="#97ff97", height=50, width=50, command=Show_info)
    elif full_trig == False:
        #Makes a back button with the image for limited trig functions
        info = Button(self, image=RenderInfo, bd="0", bg="#97ff97", height=50, width=50, command=Show_info_limited_trig)
    #Places the image on the button
    info.image = RenderInfo
    #Puts the info button in the top right hand corner of the page
    info.grid(column=number_of_colunms-1, row=0, padx="10", pady="10", sticky="ne")

#Creates a popup window with user guidance page on it
def Show_info_limited_trig():
    #Makes the tk window
    popup = Toplevel(height=350, width=400)
    #Sets the title
    popup.wm_title("Commands")
    #Gets the image to put in the window
    #Fetches image
    Loadkey = Image.open("Key_limited.jpg")
    #Resizes image
    Loadkey = Loadkey.resize((350,250), Image.ANTIALIAS)
    #Creates PhotoImage object
    Renderkey = ImageTk.PhotoImage(Loadkey)
    #Makes a lable to hold the image
    key = Label(popup, image=Renderkey, bd="0", bg="#97ff97")
    #Places the image in the lable
    key.image = Renderkey
    #Puts the lable on the page
    key.pack(fill=BOTH, expand=True)

#Creates a popup window with user guidance page on it
def Show_info():
    #Makes the tk window
    popup = Toplevel(height=350, width=400)
    #Sets the title
    popup.wm_title("Commands")
    #Gets the image to put in the window
    #Fetches image
    Loadkey = Image.open("Key_full.jpg")
    #Resizes image
    Loadkey = Loadkey.resize((350,250), Image.ANTIALIAS)
    #Creates PhotoImage object
    Renderkey = ImageTk.PhotoImage(Loadkey)
    #Makes a lable to hold the image
    key = Label(popup, image=Renderkey, bd="0", bg="#97ff97")
    #Places the image in the lable
    key.image = Renderkey
    #Puts the lable on the page
    key.pack(fill=BOTH, expand=True)

    #Makes a loop to hold the popup window
    popup.mainloop()
