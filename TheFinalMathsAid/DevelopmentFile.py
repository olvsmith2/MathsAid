#Used to turn user inputs into a function
from sympy import var
from sympy import sympify
from sympy import diff
from sympy import integrate
from sympy import simplify
#Maths module
import numpy as np
#Graph plotting libarys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
#Random number genorator libary
from random import uniform as ran
#Imports stats libaries
from scipy.stats import binom
from scipy.stats import norm
#Imports pi
from math import pi

#Imports function Ive made and put in other files to make them easier to keep track of
from InputValidation import *
from GUI import *
from SUVAT import *



#Create a class with the parent class Tk
class App(Tk):     
    #constructs the methods for the class
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Setup Frame
        container = Frame(self)
        #Makes the inital app size bigger and sets the window title to "Maths Aid"
        self.geometry("800x600")
        self.title("Maths Aid")
        #Pack to the top, fill horizontally and vertically and expand to fit space
        container.pack(side="top", fill="both", expand=True)
        #Creates a gid used to align wigits
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Empty oject of frames
        self.frames = {}

        #Creates a list of all of the pages
        Pages = [MainMenu, PureMenu, StatsMenu, MechMenu, Integrator, Differentiator, GraphPlotter, PolynomialSolver, SimEquations, RNG, Binomial, Normal, SUVAT, Projectile]

        #Creates an instance of the frame for each item in the list of pages
        for F in (Pages):
            #Contructs an instance of the frame for F
            frame = F(container, self)
            #Makes an entery in the frames object with the frame it just constructed
            self.frames[F] = frame
            #Makes grid for the frame that starts at 0,0 and sticks to the north south east and west
            frame.grid(row=0, column=0, stick="nsew" )

        #Shows MainMenu on initalisation of the app
        self.show_frame(MainMenu)

    #Creates the method show_frame
    def show_frame(self, frame_name):
        #Creates local variable with the passed frame to be displayed
        frame = self.frames[frame_name]
        #Diplays the frame thats called
        frame.tkraise()

#Creates main menu page page
class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #Pure button
        #Fetches image
        LoadPure = Image.open("PureButton2.jpg")
        #Resizes image
        LoadPure = LoadPure.resize((300,170))
        #Creates PhotoImage object
        RenderPure = ImageTk.PhotoImage(LoadPure)
        #Makes the button
        pure = Button(self, image=RenderPure, bd="5", relief="solid", bg="#c7a1e3", command=lambda: controller.show_frame(PureMenu))
        #Puts the image into the button
        pure.image = RenderPure
        pure.place(x=0, y=0)
        #Adds the button to the main window
        pure.pack(padx="20", pady="20", fill=BOTH, expand=True)
        
        
        #Stats button
        LoadStats = Image.open("StatsButton2.jpg")
        LoadStats = LoadStats.resize((300,170))
        RenderStats = ImageTk.PhotoImage(LoadStats) 
        stats = Button(self, image=RenderStats, bd="5", relief="solid", bg="#a3ffff", command=lambda: controller.show_frame(StatsMenu))
        stats.image = RenderStats
        stats.place(x=0, y=0)
        stats.pack(padx="20", fill=BOTH, expand=True)
        
        
        #Mech button
        LoadMech = Image.open("MechButton2.jpg")
        LoadMech = LoadMech.resize((300,170))
        RenderMech = ImageTk.PhotoImage(LoadMech)
        mech = Button(self, image=RenderMech, bd="5", relief="solid", bg="#ffff61", command=lambda: controller.show_frame(MechMenu))
        mech.image = RenderMech
        mech.place(x=0, y=0)
        mech.pack(padx="20", pady="20", fill=BOTH, expand=True)

#Creates pure menu page 
class PureMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")
        
        #Adds a back button the the page
        Back_button_pack(self, controller, MainMenu)

        #Creates module buttons
        #2d array of the button text and the page the button takes you to
        List_of_Pure_Buttons = [["Integrator", Integrator],["Differentiator", Differentiator],["Graph plotter", GraphPlotter],["Polynomial solver", PolynomialSolver],["Simultaneous equation solver", SimEquations]]
        #Makes a font using tkinter.font.Font to be used on these buttons
        ButtonFont = font.Font(size="20", weight="bold")
        #Loop to create all of the buttons in the list
        for name in List_of_Pure_Buttons:
            button = Module_Button(self, name, "#c7a1e3", ButtonFont, controller)
            button.pack(padx="20", pady="10", fill=BOTH, expand=True)

#Creates statistics menu page 
class StatsMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")
        
        #Adds a back button the the page
        Back_button_pack(self, controller, MainMenu)

        #Creates module buttons
        #2d array of the button text and the page the button takes you to
        List_of_Stats_Buttons = [["Random number generator", RNG],["Binomial distribution", Binomial],["Normal distribution", Normal]]
        #Makes a font using tkinter.font.Font to be used on these buttons
        ButtonFont = font.Font(size="20", weight="bold")
        #Loop to create all of the buttons in the list
        for name in List_of_Stats_Buttons:
            button = Module_Button(self, name, "#a3ffff", ButtonFont, controller)
            button.pack(padx="20", pady="10", fill=BOTH, expand=True)
        
#Creates mechanics menu page 
class MechMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #Adds a back button the the page
        Back_button_pack(self, controller, MainMenu)

        #Creates module buttons
        #2d array of the button text and the page the button takes you to
        List_of_Stats_Buttons = [["SUVAT calculator", SUVAT],["Projectile calculator", Projectile]]
        #Makes a font using tkinter.font.Font to be used on these buttons
        ButtonFont = font.Font(size="20", weight="bold")

        #Loop to create all of the buttons in the list
        for name in List_of_Stats_Buttons:
            button = Module_Button(self, name, "#ffff61", ButtonFont, controller)
            button.pack(padx="20", pady="10", fill=BOTH, expand=True)



#Module pages
class Integrator(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #INTERGRATOR METHODS

        #Intergrates the function
        def Intergrate_function(self):
            #Gets the input from the entry box
            Input_function = function.get()
            #Checks the limits input are valid
            Limits = Limit_validate(Upper_input.get(), Lower_input.get())
            #Converts the string into a python formatted math expression
            formatted_function = Python_formular_formator(Input_function)
            
            #Tests to see if the function is a valid function
            try: 
                #Tries to make a sympy function from the input
                expression = sympify(formatted_function)
                #Makes x the variable using the varibale Sympy libary
                x = var('x')
            except:
                Output_indefinate.config(text="Invalid function")
            
            #Tets if the function can be arithmetically intergrated
            try:
                #Intergrates the function with respect to x
                Indefinate_intergral = integrate(expression, x)
                #Puts the indefinate intergral in the output lable
                Output_indefinate.config(text=Indefinate_intergral)
            except:
                Output_indefinate.config(text="Invalid function")

            #Outputs definate intergral if valid limits are given
            if Limits == True:
                #Get the inputs from the limit boxes
                Lower_x = float(Lower_input.get())
                Upper_x = float(Upper_input.get())
                #Calculates the definate intergral between the limits
                Definate_intergral = integrate(expression, (x, Lower_x, Upper_x))
                #Checks for imaginary answers
                if Definate_intergral.is_real:
                    #Puts the definate intergral in the output lable
                    Output_definate.config(text=Definate_intergral)
                else:
                    Output_definate.config(text="Undefined")
            elif Limits == False:
                #Puts the definate intergral in the output lable
                Output_definate.config(text="Invalid limits")
       

        #INTERGRATOR WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, PureMenu)
        #Adds infomation button
        Infomation_button(self, 8, True)

        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")
        
        #Makes a label to display y= before the function entry textbox
        y_lable = Label(self, text="Y=", bg="#97ff97", font=Font)
        y_lable.grid(column=1, row=1, rowspan=2, pady="20", sticky="e")

        #Makes an input box for the function to be intergrated
        function = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        function.grid(column=2, row=1, columnspan=3, rowspan=2, padx=(5,20), pady="10", sticky="we")
        #List to define the characters the input box should allow
        Valid_characters = ["x", "(", ")", "/", "*", "+", "-", "s", "i", "n", "c", "o", "t", "a", "e", "p", "l", "g"]   
        #Holds the result of the validation from calling the validation function. Either True or False
        reg1 = self.register(Function_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        function.config(validate="key", validatecommand=(reg1, "%S", "%d", Valid_characters))

        #Makes a label to display Lower lim before the lower limit entry
        Lower_lable = Label(self, text="Lower lim", bg="#97ff97", font=Font)
        Lower_lable.grid(column=5, row=2, pady="20", sticky="e")

        #Makes an input box for the lower lim value
        Lower_input = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        Lower_input.grid(column=6, row=2, padx=(5,20), pady="10", sticky="we")
        #Holds the result of the validation from calling the validation function. Either True or False
        reg2 = self.register(Decimal_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        Lower_input.config(validate="key", validatecommand=(reg2, "%S", "%d","%P", 5))

        #Makes a label to display Upper lim before the upper limit entry
        Upper_lable = Label(self, text="Upper lim", bg="#97ff97", font=Font)
        Upper_lable.grid(column=5, row=1, pady="20", sticky="e")

        #Makes an input box for the upper limit 
        Upper_input = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        Upper_input.grid(column=6, row=1, padx=(5,20), pady="10", sticky="we")
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        Upper_input.config(validate="key", validatecommand=(reg2, "%S", "%d","%P", 5))

        #Makes the intergrate button
        Intergrate_button = Button(self, text="Intergrate", relief="solid", bd=5, font=Font, bg="white", command=lambda:Intergrate_function(self))
        Intergrate_button.grid(column=1, row=3, columnspan=4, padx="50", pady="40")

        #Makes a label to display Indefinate before the indefinate intergral output box
        Indefinate_lable = Label(self, text="Indefinate:", bg="#97ff97", font=Font)
        Indefinate_lable.grid(column=1, row=4, columnspan=2, pady="10", sticky="e")

        #indefinate intergral output lable
        Output_indefinate= Label(self, text="", bg="white", bd="5", relief="solid", font=Font)
        Output_indefinate.grid(column=3, row=4, columnspan=2, padx=(5, 20), pady="10", sticky="we")

        #Makes a label to display definate before the definate intergral output box
        Definate_lable = Label(self, text="Definate:", bg="#97ff97", font=Font)
        Definate_lable.grid(column=1, row=5, columnspan=2, pady="10", sticky="e")

        #definate intergral output lable
        Output_definate = Label(self, text="", bg="white", bd="5", relief="solid", font=Font)
        Output_definate.grid(column=3, row=5, columnspan=2, padx=(5, 20), pady="10", sticky="we")

        #Makes collums 3 and 4 fill the space avalible
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)


class Differentiator(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #DIFFERNETIATOR METHODS

        def Differentiate_function(self):
            #Gets the input from the entry box
            Input_function = function.get()
            Input_x = x_input.get()
            Not_Empty = bool(Input_x)
            #Converts the string into a python formatted math expression
            formatted_function = Python_formular_formator(Input_function)
            #Tests to see if the function can be differentiated 
            try: 
                #Tries to make a sympy function from the input
                expression = sympify(formatted_function)
                #Makes x the variable using the varibale Sympy libary
                x = var('x')
                #Differentiates the function with respect to x
                Gradient_function = diff(expression, x)
                #Puts the gradient function in the output lable
                Output_function.config(text=Gradient_function)
            #If the expression cant be evaluated error message is dispayed
            except:
                Output_function.config(text="Invalid function")
            
            #Checks to see if the x input has be left empty
            if Not_Empty == True:
                try:
                    #Converts the input into an integer
                    Input_x = float(Input_x)
                    #Checks if the x value is undefined on the original function 
                    test = expression.subs(x, Input_x)
                    #Checks for imaginary values
                    if test.is_real:
                        #Plugs the value into the gradient function
                        Gradient = Gradient_function.subs(x, Input_x)
                        #Removes decimals from integer numbers
                        if Gradient % 1 == 0:
                            Gradient = int(Gradient)
                        #Puts the calculated gradient value into the output lable
                        Output_gradient.config(text=Gradient)
                    else:
                        #Displays an error message if the x value is undefined at the given point
                        Output_gradient.config(text="Undefined")
                except:
                    Output_gradient.config(text="Invalid x")
            else:
                #If no x value is given this clears the gradient output
                Output_gradient.config(text="")

        #DIFFERNETIATOR WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, PureMenu)
        #Adds infomation button
        Infomation_button(self, 8, True)


        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")
        
        #Makes a label to display y= before the function entry textbox
        y_lable = Label(self, text="Y=", bg="#97ff97", font=Font)
        y_lable.grid(column=1, row=1, pady="20", sticky="e")

        #Makes an input box for the function to be differentiated
        function = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        function.grid(column=2, row=1, columnspan=3, padx=(5,20), pady="10", sticky="we")
        #List to define the characters the input box should allow
        Valid_characters = ["x", "(", ")", "/", "*", "+", "-", "s", "i", "n", "c", "o", "t", "a", "e", "p", "l", "g"]   
        #Holds the result of the validation from calling the validation function. Either True or False
        reg1 = self.register(Function_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        function.config(validate="key", validatecommand=(reg1, "%S", "%d", Valid_characters))

        #Makes a label to display x= before the x value entry box
        x_lable = Label(self, text="x=", bg="#97ff97", font=Font)
        x_lable.grid(column=5, row=1, pady="20", sticky="e")

        #Makes an input box for the x value
        x_input = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        x_input.grid(column=6, row=1, padx=(5,20), pady="10", sticky="we")
        #Holds the result of the validation from calling the validation function. Either True or False
        reg2 = self.register(Decimal_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        x_input.config(validate="key", validatecommand=(reg2, "%S", "%d","%P", 5))

        #Makes the differentiate button
        Differentiate_button = Button(self, text="Differentiate", relief="solid", bd=5, font=Font, bg="white", command=lambda:Differentiate_function(self))
        Differentiate_button.grid(column=1, row=2, columnspan=4, padx="50", pady="40")

        #Makes a label to display Gradient function before the gradient function output box
        Grad_function_lable = Label(self, text="Gradient function:", bg="#97ff97", font=Font)
        Grad_function_lable.grid(column=1, row=3, columnspan=2, pady="10", sticky="e")

        #Gradient function output lable
        Output_function = Label(self, text="", bg="white", bd="5", relief="solid", font=Font)
        Output_function.grid(column=3, row=3, columnspan=2, padx=(5, 20), pady="10", sticky="we")

        #Makes a label to display Gradient before the gradient output box
        Grad_lable = Label(self, text="Gradient:", bg="#97ff97", font=Font)
        Grad_lable.grid(column=1, row=4, columnspan=2, pady="10", sticky="e")

        #Gradient output lable
        Output_gradient = Label(self, text="", bg="white", bd="5", relief="solid", font=Font)
        Output_gradient.grid(column=3, row=4, columnspan=2, padx=(5, 20), pady="10", sticky="we")

        #Makes collums 3 and 4 fill the space avalible
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)


class GraphPlotter(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #GRAPH PLOTTER METHODS

        #Makes the user input into a function when the plot button is pressed and creates the list of values to be plotted
        def Get_function(self):
            #Sets the correct figure to be selected
            plt.figure(1)
            #Clears the plot
            plt.clf()
            #Clears the error message label when button is pressed
            Error_lable.config(text="")
            #Gets the input from the entry box
            Input_function = function.get()

            #Checks limits were entered and valid
            if Limit_validate(end_x_entry.get(), start_x_entry.get()) == False:
                Error_lable.config(text="Invalid limits")
                return

            #Gets the start and end values for the graph
            end_x = float(end_x_entry.get())
            start_x = float(start_x_entry.get())
            #Converts the string into a python formatted math expression
            formatted_function = Python_formular_formator(Input_function)        
            try: 
                #Tries to make a sympy function from the input
                expression = sympify(formatted_function)
                #Makes x the variable using the varibale Sympy libary
                x = var('x')
                #Caluculates the number of points to plot
                Num_of_x_values = int(round((end_x-start_x),0)*30)
                #Checks that not too many points will be plotted to avoid crashes
                if Num_of_x_values > 3000:
                    Num_of_x_values = 3000
                #Creates a np array of x values from the start to the end value with 30 points for each change in x
                x_values = np.linspace(start_x, end_x, Num_of_x_values)
                y_values=np.array([])
                #Creates a list of y values using the expression passed
                for domain in x_values:
                    value = expression.subs(x, domain)
                    #Adds the y values to a np array
                    y_values = np.append(y_values, value)

                Plot_graph(self, x_values, y_values)
            except:
                #If the input isnt a function this displays an error message
                Error_lable.config(text="Invalid function")


                #Function that takes in x and y values, clears the canvas and adds the updated graph each time the function is called
        
        def Plot_graph(self, x, y):
            #Plots the points
            plt.plot(x, y)
            #Gets the current figure and draws to it
            plt.gcf().canvas.draw()
        
        #GRAPH PLOTTER WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, PureMenu)
        #Adds infomation button to the page
        Infomation_button(self, 4, False)
        
        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")
        #makes a label to display y= before the function entry textbox
        y_lable = Label(self, text="Y=", bg="#97ff97", font=Font)
        y_lable.grid(column=0, row=1, pady="20", sticky="e")

        #Makes an input box for the function to be plotted
        function = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        function.grid(column=1, row=1, padx="5", pady=(20,10), sticky="we")
        #List to define the characters the input box should allow
        Valid_characters = ["x", "(", ")", "/", "*", "+", "-", "s", "i", "n", "c", "o", "e", "p", "l", "g"]   
        #Holds the result of the validation from calling the validation function. Either True or False
        reg1 = self.register(Function_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        function.config(validate="key", validatecommand=(reg1, "%S", "%d", Valid_characters))
    
        #Makes labes for the limit entry boxes
        Start_lable = Label(self, text="Start=", bg="#97ff97", font=Font)
        End_lable = Label(self, text="End=", bg="#97ff97", font=Font)
        #Puts them on the screen
        Start_lable.grid(column=0, row=2, padx=(20,5), pady="10", sticky="e")
        End_lable.grid(column=0, row=3, padx=(20,5), pady="10", sticky="e")
        #Makes a input boxes for start x and end x value
        start_x_entry = Entry(self, width=15, relief="solid", bd=5, font=Font)
        end_x_entry = Entry(self, width=15, relief="solid", bd=5, font=Font)
        #Puts the input boxes in the frame
        start_x_entry.grid(column=1, row=2, padx="5", pady="10", sticky="we")
        end_x_entry.grid(column=1, row=3, padx="5", pady="10", sticky="we")
        #Holds the result of the validation from calling the decimal validation function. Either True or False
        reg2 = self.register(Decimal_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #%P passes the entire string in the input box
        #3 is the max length of the integer
        start_x_entry.config(validate="key", validatecommand=(reg2, "%S", "%d","%P", 3))
        end_x_entry.config(validate="key", validatecommand=(reg2, "%S", "%d", "%P", 3))

        #Makes error message lable
        Error_lable = Label(self, text="", bg="#97ff97", font=Font)
        Error_lable.grid(column=2, row=4, padx="5", pady="10")

        #Makes the plot button
        Plot_button = Button(self, text="Plot graph", relief="solid", bd=5, font=Font, bg="white", command=lambda:Get_function(self))
        Plot_button.grid(column=1, row=4, padx="50", pady="40", sticky="we")

        #Makes a figure using the matplotlib figure function
        fig1 = plt.figure(1)

        #Puts the figure on a ktinter canvas
        canvas1 = FigureCanvasTkAgg(fig1, self)
        #Puts the canvas on the page
        canvas1.get_tk_widget().grid(column=2, row=1, columnspan=2, rowspan=3, padx="20", pady=(10,0), sticky="nsew")
        #Toolbar uses .pack internally and so it must be put into a frame which can then put onto the page using .grid 
        toolbar_frame1 = Frame(self, bg="#97ff97")
        toolbar_frame1.grid(column=3, row=4,  padx="20", pady=(0, 10), sticky="ne")
        #Adds the navigation toolbar to the canvas in the frame 
        toolbar1 = NavigationToolbar2Tk(canvas1, toolbar_frame1)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


class PolynomialSolver(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #POLYNOMIAL SOLVER METHODS

        #Checks which polynomial type is selected to change the enrty boxes avalible
        def Entry_update(Var, indx, mode):
            #Gets the selected polynomial type
            Type = Polynomial_type.get()
            #Removes/adds the nessissary wigits for cubics
            if Type == "Quadratic":
                Power_3_entry.grid_remove()
                Power_3.grid_remove()
                Solution_output3.grid_remove()
                Solutions_lable3.grid_remove()
            elif Type == "Cubic":
                Power_3_entry.grid()
                Power_3.grid()
                Solution_output3.grid()
                Solutions_lable3.grid()        

        def SolvePolynomial():
            #Gets the selected polynomial type
            Type = Polynomial_type.get()
            #Solves a quadratic
            if Type == "Quadratic":
                try:
                    #Gets the coefficients from the entry boxes
                    a = int(Power_2_entry.get())
                    b = int(Power_1_entry.get())
                    c = int(Power_0_entry.get())
                    #Creates a numpy polynomail object
                    polynomial = np.poly1d([a, b, c])
                    #Finds the roots using numerical methods
                    roots = np.roots(polynomial)
                    Solution_output1.config(text=np.round(roots[0], 10))
                    Solution_output2.config(text=np.round(roots[1], 10))
                except:
                    Solution_output1.config(text="Enter Coefficients")
                    Solution_output2.config(text="")
                    Solution_output3.config(text="")

            #Solves a cubic
            if Type == "Cubic":
                try:
                    #Gets the coefficients fromt the entry boxes
                    a = int(Power_3_entry.get())
                    b = int(Power_2_entry.get())
                    c = int(Power_1_entry.get())
                    d = int(Power_0_entry.get())
                    #Creates a numpy polynomail object
                    polynomial = np.poly1d([a, b, c, d])
                    #Finds the roots using numerical methods
                    roots = np.roots(polynomial)
                    Solution_output1.config(text=np.round(roots[0], 10))
                    Solution_output2.config(text=np.round(roots[1], 10))
                    Solution_output3.config(text=np.round(roots[2], 10))
                except:
                    Solution_output1.config(text="Enter Coefficients")
                    Solution_output2.config(text="")
                    Solution_output3.config(text="")


        #POLYNOMAIL SOLVER WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, PureMenu)

        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")

        #Makes the selection value a string that can change
        Polynomial_type = StringVar()
        #Sets the default seletion value to quadratic
        Polynomial_type.set("Cubic")
        #Makes a drop down selection box to chose the polynomail type
        Polynomial_selector = OptionMenu(self, Polynomial_type, "Quadratic", "Cubic")
        Polynomial_selector.config(relief="solid", bd=5, font=Font, bg="white")
        #Put the polynomial selector on the page
        Polynomial_selector.grid(column=3, row=1)
        #Adds a variable trace that calls the entry update function everytime the Polynomial type variable is updated
        Polynomial_type.trace_add("write", Entry_update)

        #Creates the enrty boxes for the coefficients
        Power_3_entry = Entry(self, relief="solid", bd=5, font=Font)
        Power_2_entry = Entry(self, relief="solid", bd=5, font=Font)
        Power_1_entry = Entry(self, relief="solid", bd=5, font=Font)
        Power_0_entry = Entry(self, relief="solid", bd=5, font=Font)
        #Puts the entry boxes on the frame
        Power_3_entry.grid(column=1, row=2, pady=20, padx=(50,0), sticky="e",)
        Power_2_entry.grid(column=1, row=3, pady=20, padx=(50,0), sticky="e",)
        Power_1_entry.grid(column=1, row=4, pady=20, padx=(50,0), sticky="e",)
        Power_0_entry.grid(column=1, row=5, pady=20, padx=(50,0), sticky="e",)
        #Holds the result of the validation from calling the decimal validation function. Either True or False
        reg1 = self.register(Decimal_validate)
        #Validates the input boxs when a key is pressed by by checking if reg is true of false 
        Power_3_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Power_2_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Power_1_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Power_0_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))

        #Creates lables to display the x's of the polynomial
        Power_3 = Label(self, text="x³", bg="#97ff97", font=Font)
        Power_2 = Label(self, text="x²", bg="#97ff97", font=Font)
        Power_1 = Label(self, text="x", bg="#97ff97", font=Font)
        #Puts the lables on the frame
        Power_3.grid(column=2, row=2, pady=20, padx=(0,30), sticky="w")
        Power_2.grid(column=2, row=3, pady=20, padx=(0,30), sticky="w")
        Power_1.grid(column=2, row=4, pady=20, padx=(0,30), sticky="w")

        #Creates the lables to display x= before the solutions to the polynomials
        Solutions_lable1 = Label(self, text="x=", bg="#97ff97", font=Font)
        Solutions_lable2 = Label(self, text="x=", bg="#97ff97", font=Font)
        Solutions_lable3 = Label(self, text="x=", bg="#97ff97", font=Font)
        #Puts the lables on the frame
        Solutions_lable1.grid(column=4, row=3, pady=20, padx=(20,0))
        Solutions_lable2.grid(column=4, row=4, pady=20, padx=(20,0))
        Solutions_lable3.grid(column=4, row=5, pady=20, padx=(20,0))
        #Creates ouput lable wigits
        Solution_output1 = Label(self, relief="solid", text="Enter Coefficients", bd=5, bg="white", font=Font)
        Solution_output2 = Label(self, relief="solid", bd=5, bg="white", font=Font)
        Solution_output3 = Label(self, relief="solid", bd=5, bg="white", font=Font)
        #Puts the lables on the frame
        Solution_output1.grid(column=5, row=3,  pady=20, padx=(0,50), sticky="we")
        Solution_output2.grid(column=5, row=4,  pady=20, padx=(0,50), sticky="we")
        Solution_output3.grid(column=5, row=5,  pady=20, padx=(0,50), sticky="we")

        #Makes a button which when pressed calls the polynomial solve function
        Solve_button = Button(self, text="Solve", relief="solid", bd=5, font=Font, bg="white", command=lambda:SolvePolynomial())
        Solve_button.grid(column=3, row=6, pady=20)
        
        self.grid_columnconfigure(5, weight=5)
        self.grid_columnconfigure(3, weight=1)


class SimEquations(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #Adds a back button the the page
        Back_button_grid(self, controller, PureMenu)

        #SIMULTANIOUS EQUATION SOLVER METHODS

        #Checks how many equations are selected to change the enrty boxes avalible
        def Entry_update(Var, indx, mode):
            #Gets the selected polynomial type
            Number = Num_of_equations.get()
            #Removes/ adds the wigits needed for 3 equations
            if Number == "Two":
                Entry_0_2.grid_remove()
                Entry_1_2.grid_remove()
                Entry_2_0.grid_remove()
                Entry_2_1.grid_remove()
                Entry_2_2.grid_remove()
                Entry_2_3.grid_remove()
                z_0.grid_remove()
                z_1.grid_remove()
                z_2.grid_remove()
                y_2.grid_remove()
                x_2.grid_remove()
                Solution_output_z.grid_remove()
                Solution_z.grid_remove()
                y_0.config(text="y=")
                y_1.config(text="y=")
            elif Number == "Three":
                Entry_0_2.grid()
                Entry_1_2.grid()
                Entry_2_0.grid()
                Entry_2_1.grid()
                Entry_2_2.grid()
                Entry_2_3.grid()
                z_0.grid()
                z_1.grid()
                z_2.grid()
                y_2.grid()
                x_2.grid()
                Solution_output_z.grid()
                Solution_z.grid()
                y_0.config(text="y +")
                y_1.config(text="y +")

        #Works out the determinant of a 2x2 matrix
        def Determinant(Matrix):
            #Equation for the determinant of a 2x2 matrix
            Det = Matrix[0][0]*Matrix[1][1] - Matrix[0][1]*Matrix[1][0]
            return Det

        def Consistancy(Mat1, Mat2):
            #These are all the senarios where there is a 0 to divide by but still infinate solutions
            #Checks if all three of one row = 0
            if Mat1[0][0] == Mat1[0][1] == Mat2[0][0] == 0 or Mat1[1][0] == Mat1[1][1] == Mat2[1][0] == 0:
                return True

            #Checks if both x coefficients are 0
            elif Mat1[0][0] == Mat1[1][0] == 0:
                try:
                    #If both x are 0 then the y and constant values must have the same ratio for infinate solutions
                    if Mat1[0][1]/Mat1[1][1] == Mat2[0][0]/Mat2[1][0]:
                        return True
                    else:
                        return False
                except:
                    return False

            #Checks if both y coefficients are 0
            elif Mat1[0][1] == Mat1[1][1] == 0:
                try:
                    #If both y are 0 then the x and constant values must have the same ratio for infinate solutions
                    if Mat1[0][0]/Mat1[1][0] == Mat2[0][0]/Mat2[1][0]:
                        return True
                    else:
                        return False
                except:
                    return False

            #Checks if both constant terms are 0
            elif Mat2[0][0] == Mat2[1][0] == 0:
                try:
                    #If both constant terms are 0 then the x and y values must have the same ratio for infinate solutions
                    if Mat1[0][0]/Mat1[1][0] == Mat1[0][1]/Mat1[1][1]:
                        return True
                    else:
                        return False
                except:
                    return False  
            
            #Checks if all terms have a common ratio
            elif Mat1[0][0]/Mat1[1][0] == Mat1[0][1]/Mat1[1][1] == Mat2[0][0]/Mat2[1][0]:
                return True
            else:
                return False


        #Takes in the matrix of coefficients, matrix of constant terms (2d arrays), and the number of equations there are to solve
        def Sim_solver(Matrix_A, Matrix_C, Number):
            #Clears solution output boxes
            Solution_output_x.config(text="")
            Solution_output_y.config(text="")
            Solution_output_z.config(text="")
            Error_lable.config(text="")
            #Function for solving systems with 2 equations
            if Number == "Two":
                #Gets the derterminant of the matrix
                Det = Determinant(Matrix_A)
                #If there is no invers there is either 0 or infinate solution
                if Det == 0:
                    #Checks is the equations are consistant
                    Consistant = Consistancy(Matrix_A, Matrix_C)
                    #Changes the output depending on if the equations are consistant
                    if Consistant == True:
                        Error_lable.config(text="Infinate solutions")
                    elif Consistant == False:
                        Error_lable.config(text="No solutions")
                
                elif Det != 0:
                    Error_lable.config(text="")
                    #Caluculates the constant used to find the inverse of the matrix
                    k = 1/Det
                    #Formular for the inverse of a 2x2 matrix
                    Inverse = [[k*(Matrix_A[1][1]) , -k*(Matrix_A[0][1])],
                               [-k*(Matrix_A[1][0]) , k*(Matrix_A[0][0])]]
                    #Works out the solutions to the equations by premultiplying the inverse matrix with the constants matrix
                    Solutions = [[Inverse[0][0]*Matrix_C[0][0] + Inverse[0][1]*Matrix_C[1][0]],
                                 [Inverse[1][0]*Matrix_C[0][0] + Inverse[1][1]*Matrix_C[1][0]]]
                    #Rounds the solutions to avoid python decimal errors

                    #Displays the solutions in the output lables
                    Solution_output_x.config(text=np.round(Solutions[0][0], 10))
                    Solution_output_y.config(text=np.round(Solutions[1][0], 10))

            elif Number == "Three":
                #Makes a matrix of minors
                Minors = []
                #Loops to fill in the matrix of minors
                for i in range(0,3):
                    #List is cleared for each column
                    Column_of_minors =[]
                    for j in range(0,3):
                        #Makes lists to hold the indexes needed
                        Column = [0, 1, 2]
                        Row = [0, 1, 2]
                        #Illimination of the rows of the position we are finding the mior for
                        Column.remove(i)
                        Row.remove(j)
                        #Creates a matrix of minors 
                        Minor = [[Matrix_A[Column[0]][Row[0]], Matrix_A[Column[0]][Row[1]]],
                                 [Matrix_A[Column[1]][Row[0]], Matrix_A[Column[1]][Row[1]]]]
                        #Finds the acctual value of the minor
                        Minor = Determinant(Minor)
                        #Makes a list of the values in column
                        Column_of_minors.append(Minor)
                    #Adds the list of the specific column of minors made in that itteration to the complete matrix of minors
                    Minors.append(Column_of_minors)

                #The determinant of the 3x3 matrix is needed to tell weather there are no solutions, three solutions or infinate solutions
                Det = Matrix_A[0][0]*Minors[0][0] - Matrix_A[0][1]*Minors[0][1] + Matrix_A[0][2]*Minors[0][2]

                if Det == 0:
                    #Makes an 'equation' with the first equation rearranged to be in terms of x 
                    #     x      =                Constant+                            y+                                   z
                    Equation_1_x = [[Matrix_C[0][0]/Matrix_A[0][0]],  [-Matrix_A[0][1]/Matrix_A[0][0]], [-Matrix_A[0][2]/Matrix_A[0][0]]]
                    #Plugs the value for x into the second and third equations to make 2 more equations
                    #                                       y+                                                  z=                                                  Constant
                    #Equation_4 = [[Matrix_A[1][1] + Matrix_A[1][0]*Equation_1_x[1][0]], [Matrix_A[1][2] + Matrix_A[1][0]*Equation_1_x[2][0]], [Matrix_C[1][0] - Matrix_A[1][0]*Equation_1_x[0][0]]]
                    #                                       y+                                                  z=                                                  Constant
                    #Equation_5 = [[Matrix_A[2][1] + Matrix_A[2][0]*Equation_1_x[1][0]], [Matrix_A[2][2] + Matrix_A[2][0]*Equation_1_x[2][0]], [Matrix_C[2][0] - Matrix_A[2][0]*Equation_1_x[0][0]]]
                    
                    #Creates a 2x2 matrix with the y and z coefficients for the 2 equations
                    Coefficients = [ [ Matrix_A[1][1] + Matrix_A[1][0]*Equation_1_x[1][0], Matrix_A[1][2] + Matrix_A[1][0]*Equation_1_x[2][0] ],
                                     [ Matrix_A[2][1] + Matrix_A[2][0]*Equation_1_x[1][0], Matrix_A[2][2] + Matrix_A[2][0]*Equation_1_x[2][0] ] ]
                    
                    #Creates a 2x1 matrix of the constant terms 
                    Constants = [ [ Matrix_C[1][0] - Matrix_A[1][0]*Equation_1_x[0][0] ], 
                                  [ Matrix_C[2][0] - Matrix_A[2][0]*Equation_1_x[0][0] ] ]

                    Consistant = Consistancy(Coefficients, Constants)

                    if Consistant == True:
                        Error_lable.config(text="Infinate solutions")
                    elif Consistant == False:
                        Error_lable.config(text="No solutions")

                elif Det != 0:
                    #Makes constant term to multiply everything by
                    k = 1/Det
                    #Creates a matrix of cofactors
                    Cofactors = [[Minors[0][0], -Minors[0][1], Minors[0][2]],
                                 [-Minors[1][0], Minors[1][1], -Minors[1][2]],
                                 [Minors[2][0], -Minors[2][1], Minors[2][2]]]
                    #Transposes this matrix e.g swaps columns with rows
                    Inverse = [[k*Cofactors[0][0], k*Cofactors[1][0], k*Cofactors[2][0]],
                              [k*Cofactors[0][1], k*Cofactors[1][1], k*Cofactors[2][1]],
                              [k*Cofactors[0][2], k*Cofactors[1][2], k*Cofactors[2][2]]]

                    #Works out the solutions to the equations by premultiplying the inverse matrix with the constants matrix
                    Solutions = [[Inverse[0][0]*Matrix_C[0][0] + Inverse[0][1]*Matrix_C[1][0] + Inverse[0][2]*Matrix_C[2][0]],
                                [Inverse[1][0]*Matrix_C[0][0] + Inverse[1][1]*Matrix_C[1][0] + Inverse[1][2]*Matrix_C[2][0]],
                                [Inverse[2][0]*Matrix_C[0][0] + Inverse[2][1]*Matrix_C[1][0] + Inverse[2][2]*Matrix_C[2][0]]]

                    #Displays the solutions in the output lables
                    Solution_output_x.config(text=np.round(Solutions[0][0], 10))
                    Solution_output_y.config(text=np.round(Solutions[1][0], 10))
                    Solution_output_z.config(text=np.round(Solutions[2][0], 10))

        #Makes 2d arrays out of the input boxes and calls the equation solver passing it the matricies
        def Make_matrix():
            #Fetches the number of equations
            Number = Num_of_equations.get()
            #Checks if there are 2 or 3 equations
            if Number == "Two":
                #Makes sure coefficients have been entered
                try:
                    #Creates a 2d array to hold the input coefficients
                    Matrix_A = [[float(Entry_0_0.get()), float(Entry_0_1.get())],
                                [float(Entry_1_0.get()), float(Entry_1_1.get())]]
                    #Creates a 2d array to hold the input constant terms
                    Matrix_C = [[float(Entry_0_3.get())], 
                                [float(Entry_1_3.get())]]
                except:
                    Error_lable.config(text="Enter coefficients")
                    return
            elif Number == "Three":
                #Makes sure coefficients have been entered
                try:
                    #Creates a 2d array to hold the input coefficients
                    Matrix_A = [[float(Entry_0_0.get()), float(Entry_0_1.get()), float(Entry_0_2.get())],
                                [float(Entry_1_0.get()), float(Entry_1_1.get()), float(Entry_1_2.get())],
                                [float(Entry_2_0.get()), float(Entry_2_1.get()), float(Entry_2_2.get())]]
                    #Creates a 2d array to hold the input constant terms
                    Matrix_C = [[float(Entry_0_3.get())],
                                [float(Entry_1_3.get())],  
                                [float(Entry_2_3.get())]]
                except:
                    Error_lable.config(text="Enter coefficients")
                    return

            #Gives these matrixes to the simultanious equation solving function
            Sim_solver(Matrix_A, Matrix_C, Number)
            


        #SIMULTANIOUS EQUATION SOLVER WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, PureMenu)

        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")

        #Makes the selection value a string that can change
        Num_of_equations = StringVar()
        #Sets the default number of equations to three
        Num_of_equations.set("Three")
        #Makes a drop down selection box to chose the number of equations
        Number_selector = OptionMenu(self, Num_of_equations, "Two", "Three")
        Number_selector.config(relief="solid", bd=5, font=Font, bg="white")
        #Put the number of equations selector on the page
        Number_selector.grid(column=0, row=1, columnspan=8)
        #Adds a variable trace that calls the entry update function everytime the Number of equations variable is updated
        Num_of_equations.trace_add("write", Entry_update)

        #Creates the enrty boxes for the coefficients
        #First equation
        Entry_0_0 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_0_1 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_0_2 = Entry(self, relief="solid", bd=5, width=8, font=Font)

        #Second equation
        Entry_1_0 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_1_1 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_1_2 = Entry(self, relief="solid", bd=5, width=8, font=Font)

        #Third equation
        Entry_2_0 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_2_1 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_2_2 = Entry(self, relief="solid", bd=5, width=8, font=Font)

        #Constant terms
        Entry_0_3 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_1_3 = Entry(self, relief="solid", bd=5, width=8, font=Font)
        Entry_2_3 = Entry(self, relief="solid", bd=5, width=8, font=Font)

        #Puts the entry boxes on the frame
        #First equation
        Entry_0_0.grid(column=1, row=2, pady=20, padx=(0,10))
        Entry_0_1.grid(column=3, row=2, pady=20, padx=(0,10))
        Entry_0_2.grid(column=5, row=2, pady=20, padx=(0,10))

        #Second equation
        Entry_1_0.grid(column=1, row=3, padx=(0,10), pady=20)
        Entry_1_1.grid(column=3, row=3, padx=(0,10), pady=20)
        Entry_1_2.grid(column=5, row=3, padx=(0,10), pady=20)

        #Third equation
        Entry_2_0.grid(column=1, row=4, padx=(0,10), pady=20)
        Entry_2_1.grid(column=3, row=4, padx=(0,10), pady=20)
        Entry_2_2.grid(column=5, row=4, padx=(0,10), pady=20)

        #Constant terms
        Entry_0_3.grid(column=7, row=2, pady=20, padx=(10,30))
        Entry_1_3.grid(column=7, row=3, pady=20, padx=(10,30))
        Entry_2_3.grid(column=7, row=4, pady=20, padx=(10,30))

        #Creates lables to display the x, y and z of the simultanious equations
        #First equation
        x_0 = Label(self, text="x +", bg="#97ff97", font=Font)
        y_0 = Label(self, text="y +", bg="#97ff97", font=Font)
        z_0 = Label(self, text="z =", bg="#97ff97", font=Font)

        #Second equation
        x_1 = Label(self, text="x +", bg="#97ff97", font=Font)
        y_1 = Label(self, text="y +", bg="#97ff97", font=Font)
        z_1 = Label(self, text="z =", bg="#97ff97", font=Font)

        #Third equation
        x_2 = Label(self, text="x +", bg="#97ff97", font=Font)
        y_2 = Label(self, text="y +", bg="#97ff97", font=Font)
        z_2 = Label(self, text="z =", bg="#97ff97", font=Font)

        #Puts the lables on the frame
        x_0.grid(column=2, row=2, pady=20, padx=(0,30))
        y_0.grid(column=4, row=2, pady=20, padx=(0,30))
        z_0.grid(column=6, row=2, pady=20, padx=(0,30))

        #Puts the lables on the frame
        x_1.grid(column=2, row=3, pady=20, padx=(0,30))
        y_1.grid(column=4, row=3, pady=20, padx=(0,30))
        z_1.grid(column=6, row=3, pady=20, padx=(0,30))

        #Puts the lables on the frame
        x_2.grid(column=2, row=4, pady=20, padx=(0,30))
        y_2.grid(column=4, row=4, pady=20, padx=(0,30))
        z_2.grid(column=6, row=4, pady=20, padx=(0,30))

        #Holds the result of the validation from calling the decimal validation function. Either True or False
        reg1 = self.register(Decimal_validate)
        #Validates the input boxs when a key is pressed by by checking if reg is true of false 
        Entry_0_0.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_0_1.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_0_2.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_1_0.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_1_1.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_1_2.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_2_0.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_2_1.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))
        Entry_2_2.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 7))


        #Creates the lables to display the letter before the solution
        Solution_x = Label(self, text="x=", bg="#97ff97", font=Font)
        Solution_y = Label(self, text="y=", bg="#97ff97", font=Font)
        Solution_z = Label(self, text="z=", bg="#97ff97", font=Font)
        #Puts the lables on the frame
        Solution_x.grid(column=1, row=6, pady=20)
        Solution_y.grid(column=3, row=6, pady=20)
        Solution_z.grid(column=5, row=6, pady=20)
        #Creates ouput lable wigits
        Solution_output_x = Label(self, relief="solid", bd=5, bg="white", font=Font)
        Solution_output_y = Label(self, relief="solid", bd=5, bg="white", font=Font)
        Solution_output_z = Label(self, relief="solid", bd=5, bg="white", font=Font)
        #Puts the lables on the frame
        Solution_output_x.grid(column=2, row=6, padx=10, pady=20, sticky="we")
        Solution_output_y.grid(column=4, row=6, padx=10, pady=20, sticky="we")
        Solution_output_z.grid(column=6, row=6, padx=10, pady=20, sticky="we")

        #Makes a button which when pressed calls the Make matrix function which then calls the equation solver function
        Solve_button = Button(self, text="Solve", relief="solid", bd=5, font=Font, bg="white", command=lambda:Make_matrix())
        Solve_button.grid(column=0, row=5, columnspan=8, pady=20)

        #Makes error message lable
        Error_lable = Label(self, text="", bg="#97ff97", font=Font)
        Error_lable.grid(column=0, row=7, columnspan=8, pady="20")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)


class RNG(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #RNG METHODS

        #Generates a random number 
        def Generate_number():
            try:
                #Gets the limits for the number
                Min = float(Lower_lim.get())
                Max = float(Upper_lim.get())
                #Gets the number of decimal places the number needs to be made to 
                DP = int(Num_of_dp.get())
                #Checks the number of dp to add the correct cotinuity correction
                if DP == 0:
                    #Adds a continuity correction to the numbers
                    Min = Min - 0.5
                    Max = Max + 0.499999
                    #Generates the a random number between the range
                    Random_Number = ran(Min, Max)
                elif DP == 1:
                    #Adds a continuity correction to the numbers
                    Min = Min - 0.05
                    Max = Max + 0.0499999
                    #Generates the a random number between the range
                    Random_Number = ran(Min, Max)
                elif DP == 2:
                    #Adds a continuity correction to the numbers
                    Min = Min - 0.005
                    Max = Max + 0.00499999
                    #Generates the a random number between the range
                    Random_Number = ran(Min, Max)
                elif DP == 3:
                    #Adds a continuity correction to the numbers
                    Min = Min - 0.0005
                    Max = Max + 0.000499999
                    #Generates the a random number between the range
                    Random_Number = ran(Min, Max)
                elif DP == 4:
                    #Adds a continuity correction to the numbers
                    Min = Min - 0.00005
                    Max = Max + 0.0000499999
                    #Generates the a random number between the range
                    Random_Number = ran(Min, Max)
                #Round the number to the give number of sig fig
                Random_Number = round(Random_Number, DP)
                #Outputs the number
                Output_number.config(text=Random_Number) 
            except:
                Output_number.config(text="Enter limits")


        #RNG WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, StatsMenu)

        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")


        #Makes a label to display decimal places before the decimal place selection box
        DP_lable = Label(self, text="Decimal places", bg="#97ff97", font=Font)
        DP_lable.grid(column=1, row=1, columnspan=2, pady="20", sticky="e")
        #Makes the selection value a integer that can change
        Num_of_dp = IntVar()
        #Sets the default number of decimal places to 0
        Num_of_dp.set(0)
        #Makes a drop down selection box to chose the number of decimal places
        Number_selector = OptionMenu(self, Num_of_dp, 0, 1, 2, 3, 4)
        Number_selector.config(relief="solid", bd=5, font=Font, bg="white")
        #Put the number of equations selector on the page
        Number_selector.grid(column=3, row=1)

        #Makes a label to display Lower lim before the lower limit entry
        Lower_lable = Label(self, text="Min value", bg="#97ff97", font=Font)
        Lower_lable.grid(column=1, row=2, pady="20", sticky="e")

        #Makes an input box for the lower lim value
        Lower_lim = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        Lower_lim.grid(column=2, row=2, padx=(5,20), pady="10", sticky="we")
        #Holds the result of the validation from calling the validation function. Either True or False
        reg2 = self.register(Decimal_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        Lower_lim.config(validate="key", validatecommand=(reg2, "%S", "%d","%P", 10))

        #Makes a label to display Upper lim before the upper limit entry
        Upper_lable = Label(self, text="Max value", bg="#97ff97", font=Font)
        Upper_lable.grid(column=3, row=2, pady="20", sticky="e")

        #Makes an input box for the upper limit 
        Upper_lim = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        Upper_lim.grid(column=4, row=2, padx=(5,50), pady="10", sticky="we")
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        Upper_lim.config(validate="key", validatecommand=(reg2, "%S", "%d","%P", 10))

        #Makes a button which when pressed calls the polynomial solve function
        Generate_button = Button(self, text="Generate", relief="solid", bd=5, font=Font, bg="white", command=lambda:Generate_number())
        Generate_button.grid(column=0, row=3, columnspan=5, pady=20)

        #Number output lable
        Output_number = Label(self, text="Enter limits", bg="white", bd="5", relief="solid", font=Font)
        Output_number.grid(column=0, row=4, columnspan=5, ipadx=5, pady=20)


        #Makes these collums fill the avalible space
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(4, weight=1)


class Binomial(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #FUNCTIONS
        def Binomial_prob_calculator():
            #Validation to check the distribution has been defined with valid n, p and x values
            try:
                N = int(N_input.get())
                p = float(p_input.get())
                x = int(x_input.get())
            except:
                Error_lable.config(text="Invalid distribution")
                Output_prob.config(text="")
                return
            #Makes sure all inputs are positive, x is less than n and that p is between 1 and 0
            if N < 1 or x > N or p > 1 or x < 0 or p < 0:
                Error_lable.config(text="Invalid distribution")
                Output_prob.config(text="")
                return
            #Clears error lable
            Error_lable.config(text="")
            #Gets the selected operation value
            Operation = Sign_var.get()
            #Creates a list of the values needed
            r = []
            #Adds the correct values to the list r depending on the sign selected
            if Operation == "=":
                r.append(x)
            elif Operation == "<":
                for i in range(0, x):
                    r.append(i)
            elif Operation == "≤":
                for i in range(0, x+1):
                    r.append(i)
            elif Operation == ">":
                for i in range(x+1, N+1):
                    r.append(i)
            elif Operation == "≥":
                for i in range(x, N+1):
                    r.append(i)

            #Creates a list of the probabilities for each value of r
            Probability_Mass_Function = binom.pmf(r, N, p)
            Probability = 0
            #Adds those probabilities
            for i in Probability_Mass_Function:
                Probability = Probability + i

            Output_prob.config(text=round(Probability, 5))


        #WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, StatsMenu)

        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")

        #Text lables to display N and p before the probability and n inputs
        N_lable = Label(self, text="N=", bg="#97ff97", font=Font)
        N_lable.grid(column=2, row=1, pady="20", padx=10, sticky="e")
        p_lable = Label(self, text="p=", bg="#97ff97", font=Font)
        p_lable.grid(column=2, row=2, pady="20", padx=10, sticky="e")

        #Input entry for the N and p values
        N_input = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        N_input.grid(column=3, row=1, padx=(5,20), pady="20", sticky="we")
        #Holds the result of the validation from calling the validation function. Either True or False
        reg1 = self.register(Int_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        N_input.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 5))

        #Input entry for the N and p values
        p_input = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        p_input.grid(column=3, row=2, padx=(5,20), pady="20", sticky="we")
        #Holds the result of the validation from calling the validation function. Either True or False
        reg2 = self.register(Decimal_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        p_input.config(validate="key", validatecommand=(reg2, "%S", "%d","%P", 5))


        #Makes a label to display x before the sign
        x_lable = Label(self, text="P (x", bg="#97ff97", font=Font)
        x_lable.grid(column=1, row=3, pady="20", sticky="e")

        #Makes a sign selection variable
        Sign_var = StringVar()
        #Sets the default sign value to =
        Sign_var.set("=")
        #Makes a drop down selection box to chose the sign
        Sign = OptionMenu(self, Sign_var, "=", "<", "≤", ">", "≥" )
        Sign.config(relief="solid", bd=5, font=Font, bg="white")
        #Put the number of equations selector on the page
        Sign.grid(column=2, row=3, pady="20", padx="5")

        #Makes an input box for the x value
        x_input = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        x_input.grid(column=3, row=3, padx=5, pady="20", sticky="we")
        #Holds the result of the validation from calling the validation function. Either True or False
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        x_input.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 5))

        #Makes a label to display x before the sign
        equals_lable = Label(self, text=") =", bg="#97ff97", font=Font)
        equals_lable.grid(column=4, row=3, pady="20", padx=5, sticky="e")

        #Output lable to display the probability
        Output_prob = Label(self, width=8, bg="white", bd="5", relief="solid", font=Font)
        Output_prob.grid(column=5, row=3, columnspan=2, ipadx=5, padx=5, pady=20, sticky="we")

        #Makes a button which when pressed calls the polynomial solve function
        Calculate_button = Button(self, text="Calculate", relief="solid", bd=5, font=Font, bg="white", command=lambda:Binomial_prob_calculator())
        Calculate_button.grid(column=1, row=4, columnspan=2, pady=20)

        #Hidden output
        Error_lable = Label(self, text="", bg="#97ff97", font=Font)
        Error_lable.grid(column=3, row=4, columnspan=3, pady="20")

        #Makes these collums fill the avalible space
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(7, weight=1)


class Normal(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #Normal METHODS

        #Makes the user input into a function when the plot button is pressed and creates the list of values to be plotted
        def Normal_plot_and_calculate(self):
            #Sets the correct figure to be selected
            plt.figure(2)
            #Clears the plot
            plt.clf()
            #Clears the error message label when button is pressed
            Error_lable.config(text="")
            Output_prob.config(text="")
            try:
                #Gets the inputs from the entry box
                Mean = float(Mean_input.get())
                SD = float(Standard_dev_input.get())
            except:
                Error_lable.config(text="Define distribution")
                return


            #Checks the standard deviation isnt negative
            if SD <= 0:
                Error_lable.config(text="Invalid diviation")
                return

            #Checks limits were entered and valid
            if Limit_validate(upper_input.get(), lower_input.get()) == False:
                Error_lable.config(text="Invalid limits")
                return

            #Gets the start and end values for the normal distribution
            Lower = float(lower_input.get())
            Upper = float(upper_input.get())

            Probability = norm(Mean, SD).cdf(Upper) - norm(Mean, SD).cdf(Lower)
            Output_prob.config(text=round(Probability, 5))



            #Graph plotting

            #Find the lowes and highest values to plot, these will be 99.7% of the data
            lowest_value = Mean - 3*SD
            highest_value = Mean + 3*SD
            #Caluculates the number of points to plot
            Num_of_x_values = int((highest_value - lowest_value)*30)
            #Checks that not too many points will be plotted to avoid crashes
            if Num_of_x_values > 3000:
                Num_of_x_values = 3000

            #Calculates the transformed limits
            Standard_lower = (Lower - Mean)/SD
            Standard_upper = (Upper - Mean)/SD
            
            #Makes the x values for the shaded regions
            Shaded_domain = np.linspace(Lower, Upper, Num_of_x_values)
            Standard_shaded_domain = np.linspace(Standard_lower, Standard_upper, Num_of_x_values)

            #Creates the x values for the main plots
            domain = np.linspace(lowest_value, highest_value, Num_of_x_values)
            Standard_domain = np.linspace(-3, 3, 180)

            
            #Plots a normal distribution for the points defined in domain
            plt.plot(domain, norm.pdf(domain, Mean, SD))
            #Plots the standard Normal distribution
            plt.plot(Standard_domain, norm.pdf(Standard_domain, 0, 1))
            #Fills in the area under the graph
            plt.fill_between(Shaded_domain, norm.pdf(Shaded_domain, Mean, SD))
            #Fills in the area under standard normal the graph
            plt.fill_between(Standard_shaded_domain, norm.pdf(Standard_shaded_domain, 0, 1))
            #Gets the current figure and draws on it
            plt.gcf().canvas.draw()

        
        #Normal WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, StatsMenu)

        
        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")

        #Makes the labels to display Mu= and sigma= before the mean and standard deviation entry boxes
        Mu_lable = Label(self, text="μ=", bg="#97ff97", font=Font)
        Mu_lable.grid(column=0, row=1, pady="20", sticky="e")

        Sigma_lable = Label(self, text="σ=", bg="#97ff97", font=Font)
        Sigma_lable.grid(column=0, row=2, pady="20", sticky="e")

        #Makes an input box for the mean and sd
        Mean_input = Entry(self, relief="solid", bd=5, font=Font)
        Standard_dev_input = Entry(self, relief="solid", bd=5, font=Font)
        #Puts input box in the frame
        Mean_input.grid(column=1, row=1, padx="5", columnspan=5, pady=(20,10), sticky="we")
        Standard_dev_input.grid(column=1, row=2, padx="5", columnspan=5, pady=(20,10), sticky="we")
        #Holds the result of the validation from calling the validation function. Either True or False
        reg1 = self.register(Decimal_validate)
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        Mean_input.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 4))
        Standard_dev_input.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 4))

        #Makes a label to display p ( before the sign limits
        x_lable = Label(self, text="P (", bg="#97ff97", font=Font)
        x_lable.grid(column=0, row=3, pady="20", sticky="e")

        #Makes an input box for the lower value
        lower_input = Entry(self, relief="solid", bd=5, width=5, font=Font)
        #Puts input box in the frame
        lower_input.grid(column=1, row=3, padx="5", pady="20")
        #Holds the result of the validation from calling the validation function. Either True or False
        #Validates the input box when a key is pressed by by checking if reg is true of false 
        #%S passes the sting of what is being changed
        #%d passes the action being made e.g insert = 1 delete = 0 
        #Valid_characters passes the list of allowed characters for this specific function
        lower_input.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 4))

        #Makes a label to display  x before the sign
        x_lable = Label(self, text="< x <", bg="#97ff97", font=Font)
        x_lable.grid(column=2, row=3, pady="20", sticky="e")


        #Same for upper input
        upper_input = Entry(self, relief="solid", bd=5, width=5, font=Font)
        upper_input.grid(column=3, row=3, padx="5", pady="20")
        upper_input.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 4))

        #Makes a label to display x before the sign
        equals_lable = Label(self, text=") =", bg="#97ff97", font=Font)
        equals_lable.grid(column=4, row=3, pady="20", padx=5, sticky="e")

        #Output lable to display the probability
        Output_prob = Label(self, width=8, bg="white", bd="5", relief="solid", font=Font)
        Output_prob.grid(column=5, row=3, ipadx=5, padx="5", pady=20, sticky="we")
    


        #Makes error message lable
        Error_lable = Label(self, text="", bg="#97ff97", font=Font)
        Error_lable.grid(column=4, row=4, columnspan=2, padx="5", pady="20")

        #Makes the calculate probability button
        Plot_button = Button(self, text="Calculate", relief="solid", bd=5, font=Font, bg="white", command=lambda:Normal_plot_and_calculate(self))
        Plot_button.grid(column=1, row=4, padx="5", columnspan=3, pady="20", sticky="we")

        #Makes a figure using the matplotlib figure function
        fig2 = plt.figure(2)

        #Puts the figure on a ktinter canvas
        canvas2 = FigureCanvasTkAgg(fig2, self)
        #Puts the canvas on the page
        canvas2.get_tk_widget().grid(column=6, row=1, rowspan=3, padx="20", pady=(10,0), sticky="nsew")
        #Toolbar uses .pack internally and so it must be put into a frame which can then put onto the page using .grid 
        toolbar_frame2 = Frame(self, bg="#97ff97")
        toolbar_frame2.grid(column=6, row=4,  padx="20", pady=(0, 10), sticky="ne")
        #Adds the navigation toolbar to the canvas in the frame 
        toolbar2 = NavigationToolbar2Tk(canvas2, toolbar_frame2)


        self.grid_columnconfigure(5, weight=1)


class SUVAT(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #SUVAT METHODS
        def Calculate_SUVAT():

            Error_lable.config(text="")

            #Makes boolian variabels holding True of False based on weather an input has been made into each entry box
            S_bool = bool(S_entry.get())
            U_bool = bool(U_entry.get())
            V_bool = bool(V_entry.get())
            A_bool = bool(A_entry.get())
            T_bool = bool(T_entry.get())
            
            try:
                #If statments to figure out which variables have and havent been given by the user
                if S_bool and U_bool and V_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    AT = No_AT(float(S_entry.get()), float(U_entry.get()), float(V_entry.get()))
                    #Outputs these values into the entry box
                    A.set(AT[0])
                    T.set(AT[1])


                elif S_bool and U_bool and A_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    VT = No_VT(float(S_entry.get()), float(U_entry.get()), float(A_entry.get()))
                    #Outputs these values into the entry box
                    V.set(VT[0])
                    T.set(VT[1])

                elif S_bool and U_bool and T_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    VA = No_VA(float(S_entry.get()), float(U_entry.get()), float(T_entry.get()))
                    #Outputs these values into the entry box
                    V.set(VA[0])
                    A.set(VA[1])

                elif S_bool and V_bool and A_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    UT = No_UT(float(S_entry.get()), float(V_entry.get()), float(A_entry.get()))
                    #Outputs these values into the entry box
                    U.set(UT[0])
                    T.set(UT[1])

                elif S_bool and V_bool and T_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    UA = No_UA(float(S_entry.get()), float(V_entry.get()), float(T_entry.get()))
                    #Outputs these values into the entry box
                    U.set(UA[0])
                    A.set(UA[1])

                elif S_bool and A_bool and T_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    UV = No_UV(float(S_entry.get()), float(A_entry.get()), float(T_entry.get()))
                    #Outputs these values into the entry box
                    U.set(UV[0])
                    V.set(UV[1])

                elif U_bool and V_bool and A_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    ST = No_ST(float(U_entry.get()), float(V_entry.get()), float(A_entry.get()))
                    #Outputs these values into the entry box
                    S.set(ST[0])
                    T.set(ST[1])

                elif U_bool and V_bool and T_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    SA = No_SA(float(U_entry.get()), float(V_entry.get()), float(T_entry.get()))
                    #Outputs these values into the entry box
                    S.set(SA[0])
                    A.set(SA[1])

                elif U_bool and A_bool and T_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    SV = No_SV(float(U_entry.get()), float(A_entry.get()), float(T_entry.get()))
                    #Outputs these values into the entry box
                    S.set(SV[0])
                    V.set(SV[1])

                elif V_bool and A_bool and T_bool:
                    #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                    SU = No_SU(float(V_entry.get()), float(A_entry.get()), float(T_entry.get()))
                    #Outputs these values into the entry box
                    S.set(SU[0])
                    U.set(SU[1])

                else:
                    Error_lable.config(text="Not enough infomation")
            except:
                Error_lable.config(text="Invalid input")     

        def Clear_entries():
            S.set("")
            U.set("")
            V.set("")
            A.set("")
            T.set("")

        #SUVAT WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, MechMenu)

        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")

        #Creates string variables for the text in each entry box
        S = StringVar()
        U = StringVar()
        V = StringVar()
        A = StringVar()
        T = StringVar()
        #Creates the enrty boxes for the coefficients
        S_entry = Entry(self, relief="solid", bd=5, textvariable=S, font=Font)
        U_entry = Entry(self, relief="solid", bd=5, textvariable=U, font=Font)
        V_entry = Entry(self, relief="solid", bd=5, textvariable=V, font=Font)
        A_entry = Entry(self, relief="solid", bd=5, textvariable=A, font=Font)
        T_entry = Entry(self, relief="solid", bd=5, textvariable=T, font=Font)
        #Puts the entry boxes on the frame
        S_entry.grid(column=2, row=1, pady=20, padx=(0,50), sticky="w")
        U_entry.grid(column=2, row=2, pady=20, padx=(0,50), sticky="w")
        V_entry.grid(column=2, row=3, pady=20, padx=(0,50), sticky="w")
        A_entry.grid(column=2, row=4, pady=20, padx=(0,50), sticky="w")
        T_entry.grid(column=2, row=5, pady=20, padx=(0,50), sticky="w")
        #Holds the result of the validation from calling the decimal validation function. Either True or False
        reg1 = self.register(Decimal_validate)
        #Validates the input boxs when a key is pressed by by checking if reg is true of false 
        S_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 5))
        U_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 5))
        V_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 5))
        A_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 5))
        T_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 5))

        #Creates lables to display the letter before each entry
        S_lable = Label(self, text="S=", bg="#97ff97", font=Font)
        U_lable = Label(self, text="U=", bg="#97ff97", font=Font)
        V_lable = Label(self, text="V=", bg="#97ff97", font=Font)
        A_lable = Label(self, text="A=", bg="#97ff97", font=Font)
        T_lable = Label(self, text="T=", bg="#97ff97", font=Font)

        #Puts the lables on the frame
        S_lable.grid(column=1, row=1, pady=10, padx=(20,0), sticky="e")
        U_lable.grid(column=1, row=2, pady=10, padx=(20,0), sticky="e")
        V_lable.grid(column=1, row=3, pady=10, padx=(20,0), sticky="e")
        A_lable.grid(column=1, row=4, pady=10, padx=(20,0), sticky="e")
        T_lable.grid(column=1, row=5, pady=10, padx=(20,0), sticky="e")

        #Button to calculate remaining SUVAT values
        Generate_button = Button(self, text="Calculate", relief="solid", bd=5, font=Font, bg="white", command=lambda:Calculate_SUVAT())
        Generate_button.grid(column=1, row=6, columnspan=2, pady="10")
        
        #Error lable when invalid variables have been given
        Error_lable = Label(self, text="", bg="#97ff97", font=Font)
        Error_lable.grid(column=1, row=8, columnspan=2, pady="10")

        #Button to clear the entry boxes
        Clear_button = Button(self, text="Clear entries", relief="solid", bd=5, font=Font, bg="white", command=lambda:Clear_entries())
        Clear_button.grid(column=1, row=7, columnspan=2, pady="10")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


class Projectile(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#97ff97")

        #Function to check that enough infomation has been given to work out the rest of the variables
        def Validate_projectile():
            #Clears the error lable
            Error_lable.config(text="")
            #Makes boolean variables to see which values have inputs
            Initial_speed_bool = bool(Ispeed_entry.get())
            Initial_angle_bool = bool(Iangle_entry.get())
            Final_speed_bool = bool(Fspeed_entry.get())
            Final_angle_bool = bool(Fangle_entry.get())
            Horizontal_S_bool = bool(Hs_entry.get())    
            Vertical_S_bool = bool(Vs_entry.get())
            Vertical_A_bool = bool(Va_entry.get())
            Time_bool = bool(Time_entry.get())

            #Checks both initial speed and angle have been given if one is given
            if Initial_speed_bool and not Initial_angle_bool or not Initial_speed_bool and Initial_angle_bool:
                Error_lable.config(text="Enter full initial velocity")
                return
            #Checks both final speed and angle have been given if one is given
            elif Final_speed_bool and not Final_angle_bool or not Final_speed_bool and Final_angle_bool:
                Error_lable.config(text="Enter full final velocity")
                return
            #If both inital speed and angle are given this calculates the horizontal and vertical components of the initial velocity
            if Initial_speed_bool and Initial_angle_bool: 
                #Tempary variables to hold the values of the horizontal and vertical velocities
                Temp_H = np.cos(np.deg2rad(float(Iangle_entry.get())))*float(Ispeed_entry.get())
                Temp_V = np.sin(np.deg2rad(float(Iangle_entry.get())))*float(Ispeed_entry.get())
                #Rounds these values to avoid python inaccuracys with number storage
                Horizontal_UV.set(str(round(Temp_H, 5)))
                Vertical_U.set(str(round(Temp_V, 5)))
            #If both final speed and angle are given this calculates the horizontal and vertical components of the final velocity
            if Final_speed_bool and Final_angle_bool: 
                #Tempary variables to hold the values of the horizontal and vertical velocities
                Temp_H = np.cos(np.deg2rad(float(Fangle_entry.get())))*float(Fspeed_entry.get())
                Temp_V = np.sin(np.deg2rad(float(Fangle_entry.get())))*float(Fspeed_entry.get())
                #Rounds these values to avoid python inaccuracys with number storage
                Horizontal_UV.set(str(round(Temp_H, 5)))
                Vertical_V.set(str(round(Temp_V, 5)))

            #Gets the boolean for these after the checks for lanuch and landing speed and angle
            Horizontal_UV_bool = bool(Huv_entry.get())
            Vertical_U_bool = bool(Vu_entry.get())
            Vertical_V_bool = bool(Vv_entry.get())

            #List to hold horizontal components
            Horizontal = [Horizontal_S_bool, Horizontal_UV_bool]
            #List to hold vertical components
            Vertical = [Vertical_S_bool, Vertical_U_bool, Vertical_V_bool, Vertical_A_bool]

            #Variables to hold the number of horizontal and vertical variables given
            Num_of_H = 0
            Num_of_V = 0
            #For loop to count how many horizontal variables are given
            for counter in Horizontal:
                if counter == True:
                    Num_of_H = Num_of_H + 1

            #For loop to count how many vertical variables are given:
            for counter in Vertical:
                if counter == True:
                    Num_of_V = Num_of_V + 1

            #Possibilities when time is given
            if Time_bool == True:
                #Checks to see if enough infomation is given along with time
                if Num_of_H >= 1 and Num_of_V >= 2:
                    #SUVAT calculator ajusted for the vertical component of the projectile
                    try:
                        #If statments to figure out which variables have and havent been given by the user
                        if Vertical_S_bool and Vertical_U_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            VA = No_VA(float(Vs_entry.get()), float(Vu_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_V.set(VA[0])
                            Vertical_A.set(VA[1])


                        elif Vertical_S_bool and Vertical_V_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            UA = No_UA(float(Vs_entry.get()), float(Vv_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_U.set(UA[0])
                            Vertical_A.set(UA[1])

                        elif Vertical_S_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            UV = No_UV(float(Vs_entry.get()), float(Va_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_U.set(UV[0])
                            Vertical_V.set(UV[1])

                        elif Vertical_U_bool and Vertical_V_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            SA = No_SA(float(Vu_entry.get()), float(Vv_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_S.set(SA[0])
                            Vertical_A.set(SA[1])

                        elif Vertical_U_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            SV = No_SV(float(Vu_entry.get()), float(Va_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_S.set(SV[0])
                            Vertical_V.set(SV[1])

                        elif Vertical_V_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            SU = No_SU(float(Vv_entry.get()), float(Va_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_S.set(SU[0])
                            Vertical_U.set(SU[1])
                    except:
                        Error_lable.config(text="Invalid input")
                        return
                    #Calculates the horizontal variables
                    try:
                        #If displacment is given this calculates uv
                        if Horizontal_S_bool:
                            H_speed = round(float(Hs_entry.get()) / float(Time_entry.get()), 5)
                            Horizontal_UV.set(H_speed)
                        #If uv is given this calculates displacment
                        elif Horizontal_UV_bool:
                            H_displacement = round(float(Huv_entry.get()) * float(Time_entry.get()), 5)
                            Horizontal_S.set(H_displacement)
                    except:
                        Error_lable.config(text="Invalid input")
                        return
                else:
                    Error_lable.config(text="Not enough infomation")

            #If time isnt given different checks to see if enough infomation is given must take place
            elif Time_bool == False:
                #First situation where enough infomation is given
                if Num_of_H == 1 and Num_of_V >= 3:
                    try:
                        #If statments to figure out which variables have and havent been given by the user
                        if Vertical_U_bool and Vertical_V_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            ST = No_ST(float(Vu_entry.get()), float(Vv_entry.get()), float(Va_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_S.set(ST[0])
                            Time.set(ST[1])

                        elif Vertical_S_bool and Vertical_V_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            UT = No_UT(float(Vs_entry.get()), float(Vv_entry.get()), float(Va_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_U.set(UT[0])
                            Time.set(UT[1])

                        elif Vertical_S_bool and Vertical_U_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            VT = No_VT(float(Vs_entry.get()), float(Vu_entry.get()), float(Va_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_V.set(VT[0])
                            Time.set(VT[1])

                        elif Vertical_S_bool and Vertical_U_bool and Vertical_V_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            AT = No_AT(float(Vs_entry.get()), float(Vu_entry.get()), float(Vv_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_A.set(AT[0])
                            Time.set(AT[1])
                    except:
                        Error_lable.config(text="Invalid input")
                        print("test")
                        return
                    #Then works out the horizontal stuff now time has been calculated
                    try:
                        #Gets the string from the time box
                        Temp_time = Time.get()
                        #Seperates the string at the space if there are 2 values 
                        Temp_time_list = Temp_time.partition(" ")
                        #Checks is there are one of 2 time values
                        if len(Temp_time_list) == 3:
                            #Gets the first time
                            Time1 = Temp_time_list[0]
                            #Removes extra character and converts the string into a float
                            Time1 = float(Time1[1:-1])
                            #Gets the second time
                            Time2 = Temp_time_list[2]
                            #Removes exrta character and converts the string into a float
                            Time2 = float(Time2[:-1])
                            #If displacment is given this calculates uv
                            if Horizontal_S_bool:
                                H_speed = [ round(float(Hs_entry.get()) / Time1, 5), round(float(Hs_entry.get()) / Time2, 5)]
                                Horizontal_UV.set(H_speed)
                            #If uv is given this calculates displacment
                            elif Horizontal_UV_bool:
                                H_displacement = [ round(float(Huv_entry.get()) * Time1, 5), round(float(Huv_entry.get()) * Time2, 5)]
                                Horizontal_S.set(H_displacement)
                        #If there is only one time given
                        elif len(Temp_time_list) == 1:   
                            #If displacment is given this calculates uv
                            if Horizontal_S_bool:
                                H_speed = round(float(Hs_entry.get()) / float(Time_entry.get()), 5)
                                Horizontal_UV.set(H_speed)
                            #If uv is given this calculates displacment
                            elif Horizontal_UV_bool:
                                H_displacement = round(float(Huv_entry.get()) * float(Time_entry.get()), 5)
                                Horizontal_S.set(H_displacement)

                    except:
                        Error_lable.config(text="Invalid input")
                        return

                #Second situation where enough infomation is given and time isnt given
                elif Num_of_H >= 2 and Num_of_V >= 2:
                    try:
                        #Calculates time from the 2 other given horizontal components
                        T = round(float(Hs_entry.get()) / float(Huv_entry.get()), 5)
                        Time.set(T)
                        
                    except:
                        Error_lable.config(text="Invalid input")
                        return
                    #This is the same code as eariler as you are trying to work out the vertical variables and you have 2 random variables + time
                    try:
                        #If statments to figure out which variables have and havent been given by the user
                        if Vertical_S_bool and Vertical_U_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            VA = No_VA(float(Vs_entry.get()), float(Vu_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_V.set(VA[0])
                            Vertical_A.set(VA[1])


                        elif Vertical_S_bool and Vertical_V_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            UA = No_UA(float(Vs_entry.get()), float(Vv_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_U.set(UA[0])
                            Vertical_A.set(UA[1])

                        elif Vertical_S_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            UV = No_UV(float(Vs_entry.get()), float(Va_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_U.set(UV[0])
                            Vertical_V.set(UV[1])

                        elif Vertical_U_bool and Vertical_V_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            SA = No_SA(float(Vu_entry.get()), float(Vv_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_S.set(SA[0])
                            Vertical_A.set(SA[1])

                        elif Vertical_U_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            SV = No_SV(float(Vu_entry.get()), float(Va_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_S.set(SV[0])
                            Vertical_V.set(SV[1])

                        elif Vertical_V_bool and Vertical_A_bool:
                            #Calls the correct function from SUVAT.py to calculate the remaining 2 SUVAT values
                            SU = No_SU(float(Vv_entry.get()), float(Va_entry.get()), float(Time_entry.get()))
                            #Outputs these values into the entry box
                            Vertical_S.set(SU[0])
                            Vertical_U.set(SU[1])
                    except:
                        Error_lable.config(text="Invalid input")
                        return

                else:
                    Error_lable.config(text="Not enough infomation")

        def Clear_entries():
            #Sets all the entry boxes to empty
            Initial_speed.set("")
            Initial_angle.set("")
            Final_speed.set("")
            Final_angle.set("")

            Horizontal_S.set("")
            Horizontal_UV.set("")
            
            Vertical_S.set("")
            Vertical_U.set("")
            Vertical_V.set("")
            Vertical_A.set("")

            Time.set("")


        #PROJECTILE WIGITS

        #Adds a back button the the page
        Back_button_grid(self, controller, MechMenu)

        #Font for the page
        Font = font.Font(family="Helvetica", size=18, weight="bold")


        #Creates string variables for the text in each entry box
        Initial_speed = StringVar()
        Initial_angle = StringVar()
        Final_speed = StringVar()
        Final_angle = StringVar()

        Horizontal_S = StringVar()
        Horizontal_UV = StringVar()
        
        Vertical_S = StringVar()
        Vertical_U = StringVar()
        Vertical_V = StringVar()
        Vertical_A = StringVar()

        Time = StringVar()
        #Creates the enrty boxes for the variables. I = inital, F = final, H = horizontal and V = vertiacal
        Ispeed_entry = Entry(self, relief="solid", bd=5, textvariable=Initial_speed, width=15, font=Font)
        Iangle_entry = Entry(self, relief="solid", bd=5, textvariable=Initial_angle, width=15, font=Font)
        Fspeed_entry = Entry(self, relief="solid", bd=5, textvariable=Final_speed, width=15, font=Font)
        Fangle_entry = Entry(self, relief="solid", bd=5, textvariable=Final_angle, width=15, font=Font)

        Hs_entry = Entry(self, relief="solid", bd=5, textvariable=Horizontal_S, width=15, font=Font)
        Huv_entry = Entry(self, relief="solid", bd=5, textvariable=Horizontal_UV, width=15, font=Font)

        Vs_entry = Entry(self, relief="solid", bd=5, textvariable=Vertical_S, width=15, font=Font)
        Vu_entry = Entry(self, relief="solid", bd=5, textvariable=Vertical_U, width=15, font=Font)
        Vv_entry = Entry(self, relief="solid", bd=5, textvariable=Vertical_V, width=15, font=Font)
        Va_entry = Entry(self, relief="solid", bd=5, textvariable=Vertical_A, width=15, font=Font)

        Time_entry = Entry(self, relief="solid", bd=5, textvariable=Time, width=15, font=Font)
        #Puts the entry boxes on the frame
        Ispeed_entry.grid(column=2, row=0, pady=20, padx=(0,50), sticky="w")
        Iangle_entry.grid(column=4, row=0, pady=20, padx=(0,150), sticky="w")
        Fspeed_entry.grid(column=2, row=1, pady=20, padx=(0,50), sticky="w")
        Fangle_entry.grid(column=4, row=1, pady=20, padx=(0,150), sticky="w")
        Hs_entry.grid(column=2, row=2, pady=(50,20), padx=(0,50), sticky="w")
        Huv_entry.grid(column=2, row=3, pady=20, padx=(0,50), sticky="w")
        Vs_entry.grid(column=4, row=2, pady=(50,20), padx=(0,150), sticky="w")
        Vu_entry.grid(column=4, row=3, pady=20, padx=(0,150), sticky="w")
        Vv_entry.grid(column=4, row=4, pady=20, padx=(0,150), sticky="w")
        Va_entry.grid(column=4, row=5, pady=20, padx=(0,150), sticky="w")
        Time_entry.grid(column=2, row=5, pady=20, padx=(0,50), sticky="w")
        #Holds the result of the validation from calling the decimal validation function. Either True or False
        reg1 = self.register(Decimal_validate)
        #Validates the input boxs when a key is pressed by by checking if reg is true of false 
        Ispeed_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Iangle_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Fspeed_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Fangle_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Hs_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Huv_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Vs_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Vu_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Vv_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Va_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))
        Time_entry.config(validate="key", validatecommand=(reg1, "%S", "%d","%P", 8))

        

        #Creates lables to display the name of the entry before each entry
        Ispeed_lable = Label(self, text="Launch speed=", bg="#97ff97", font=Font)
        Iangle_lable = Label(self, text="Launch angle (°)=", bg="#97ff97", font=Font)
        Fspeed_lable = Label(self, text="Landing speed=", bg="#97ff97", font=Font)
        Fangle_lable = Label(self, text="Landing angle (°)=", bg="#97ff97", font=Font)
        Hs_lable = Label(self, text="Horizontal displacement=", bg="#97ff97", font=Font)
        Huv_lable = Label(self, text="Horizontal velocity=", bg="#97ff97", font=Font)
        Vs_lable = Label(self, text="Vertical displacement=", bg="#97ff97", font=Font)
        Vu_lable = Label(self, text="Vertical initial velocity=", bg="#97ff97", font=Font)
        Vv_lable = Label(self, text="Vertical final velocity=", bg="#97ff97", font=Font)
        Va_lable = Label(self, text="Vertical acceleration=", bg="#97ff97", font=Font)
        Time_lable = Label(self, text="Time=", bg="#97ff97", font=Font)


        #Puts the lables on the frame

        Ispeed_lable.grid(column=1, row=0, pady=20, padx=(20,0), sticky="e")
        Iangle_lable.grid(column=3, row=0, pady=20, padx=(20,0), sticky="e")
        Fspeed_lable.grid(column=1, row=1, pady=20, padx=(20,0), sticky="e")
        Fangle_lable.grid(column=3, row=1, pady=20, padx=(20,0), sticky="e")
        Hs_lable.grid(column=1, row=2, pady=(50,20), padx=(20,0), sticky="e")
        Huv_lable.grid(column=1, row=3, pady=20, padx=(20,0), sticky="e")
        Vs_lable.grid(column=3, row=2, pady=(50,20), padx=(20,0), sticky="e")
        Vu_lable.grid(column=3, row=3, pady=20, padx=(20,0), sticky="e")
        Vv_lable.grid(column=3, row=4, pady=20, padx=(20,0), sticky="e")
        Va_lable.grid(column=3, row=5, pady=20, padx=(20,0), sticky="e")
        Time_lable.grid(column=1, row=5, pady=20, padx=(20,0), sticky="e")

        #Button to calculate remaining SUVAT values
        Generate_button = Button(self, text="Calculate", relief="solid", bd=5, font=Font, bg="white", command=lambda:Validate_projectile())
        Generate_button.grid(column=2, row=6, pady="20")
        
        #Button to clear the entry boxes
        Clear_button = Button(self, text="Clear entries", relief="solid", bd=5, font=Font, bg="white", command=lambda:Clear_entries())
        Clear_button.grid(column=1, row=6, pady="20")

        #Error lable when invalid variables have been given
        Error_lable = Label(self, text="", bg="#97ff97", font=Font)
        Error_lable.grid(column=3, row=6, columnspan=2, pady=20)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)


#Code to initalise the App object and run it
app = App()
app.mainloop()
