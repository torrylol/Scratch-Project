# -*- coding: UTF-8 -*-

# Y9 Code Planet Scratch Project || Parts of a PC || Written In Python || Torry Hogan

# Commented Version

from tkinter import *
# Importing the tkinter library * from tkinter, tkinter is pre-installed with python and the GUI frakework this program uses.
import webbrowser
# The webbrowser library will be used to open the pastebin link when executing the get_code function and is also pre-installed with python.
import random
# The random library is being imported for a function and again, is also pre-installed with python

# No instillation of libraries is needed to run and use this program.

window = Tk()
# Defining Tk() function as window
window.iconbitmap()
# Application bitmap (app icon) is set to blank (Null:)
window.title("----------- Y9 Code Planet Scratch Project || Text PC : Builder (Torry Hogan) -----------")
# Titles the window, window = Tk() function and will be refered as window for the rest of this code

main_title = Label(window, # 0.5 + 1
                   text="Text PC : Builder", # 2
                   bg="black", # 3
                   fg="white", # 4
                   font="Krungthep 55", # 5
                   anchor="center") # 6
# 0.5 Creating a Label (widget) and assigning to the variable main_title,
# 1. The label is set to be placed inside the window,
# 2. Label text set to "Text PC : Builder",
# 3. Setting the label to have a  black bg (background)
# 4. Setting the label to have a white fg (foreground)
# 5. Setting the font of the label to "Krungthep" and size 55
# 6. Anchoring the the text inside the label to the center

main_title.pack()
# Packing the label known as main_title into the window

i=0
# i is equal to 0
cycle=["Written in Python w/ Tkinter", "By Torry :D"]
# Cycle is what text will be cycled through the upcoming varaible

def subtitle_label(sub_title):
    # Creating the subtitle_label function with the parameters sub_title
    def subtitle():
        # Creating the subtitle function
        global i
        # Declaring i as a global variable
        sub_title.config(text=(cycle[i]))
        # Configuring the variable to cycle its text through [i]
        i+=1
        # Adding 1 to i after function has completed
        sub_title.after(2500, subtitle)
        # Setting the delay to cycle after as 2500
    subtitle()
    # Calling the subtitle function

sub_title = Label(window, # 0.5 + 1
                  bg="black", # 2
                  fg="white", # 3
                  font="Krungthep 35", # 4
                  anchor="center") # 5

sub_title.pack()
# Packing the label known as sub_title into the window

# 0.5 Creating a Label (widget) and assigning to the variable sub_title,
# 1. The label is set to be placed inside the window,
# 2. Setting the label to have a  black bg (background)
# 3. Setting the label to have a white fg (foreground)
# 4. Setting the font of the label to "Krungthep" and size 35
# 5. Anchoring the the text inside the label to the center

subtitle_label(sub_title)
# Giving parameters to subtitle_label (sub_title)

def change(event):
    # Creating a function called change that is an event, this is for when the cursor comes into the set label
    subsub_title.configure(text=" ⬆ ⬆ ⬆ ⬆ ⬆ \n")
    # Configuring a label knows as subsub_title to change its text when this function is called

def leave(event):
    # Creating a function called leave that is an event, for the event of the cursor leaving the label
    subsub_title.configure(text="Enter your name to start! \n")
    # Configuring a label knows as subsub_title to change its text when this function is called

subsub_title = Label(window, # 0.5 + 1
                  text="Enter your name to start! \n", # 2
                  bg="black", # 3
                  fg="white", # 4
                  font="Krungthep 35", # 5
                  relief="groove", # 6
                  borderwidth= 0, # 7
                  anchor="n") # 8
# 0.5 + 1. Creates a label assinged to the variable subsubtitle and puts that label into the window
# 2. Sets the labels text to "Enter your name to start! \n" the \n means to return a line down
# 3. Sets the labels bg to black
# 4. Sets the labels fg to white
# 5. Sets the labels texts font to "Krungthep" and size 55
# 6. Creates a border for the label known as "groove"
# 7. Sets said border width to 0
#8. Anchors the text inside the label to north

subsub_title.bind("<Enter>", change)
# Binds the enter event calling the change function to subsub_title
subsub_title.bind("<Leave>", leave)
# Binds teh leave event calling the leave function to subsub_title

subsub_title.pack(side="bottom")
# Packs the label inside the window at the bottom side

name_entry = Entry(window, # 1
                   bg="black", # 2
                   fg="white") # 3
# 1. Creates an Entry widget assinged to name_entry and places it into the window
# 2. Sets the entries bg to black
# 3. Sets the entires fg to white

name_entry.place(relx = 0.5, # 1
                 rely = 0.3, # 1
                 anchor="center") # 1
# 1. Places the name_entry widget at an x value of 0.5
# 2. Places the name_entry widget at a y value of 0.3
# 3. Anchors the Input inside the widget to center

warning = Label(window, # 0.5 + 1
                   text="Important Notice: Previous Part Selection(Up arrow displayed) is currently BUGGED!\n Use at own risk and prepare to restart the application", #  2
                   bg="black", # 3
                   fg="white", # 4
                   font="Krungthep 12", # 5
                   anchor="center")# 6
# 05. + 1 Creates a label widget assings it to warning and puts it into the window
# 2. Sets the text of the widget to (displayed above)
# 3. Sets the bg to black
# 4. Sets the fg to white
# 5.  Sets the font to "Krungthep" and size 12
# 6.  Anchors the text inside the widget to the center

warning.pack()
# Packs the label intot the window

def name_input(event=None):
    # Creates a function called name_input and has the attribute event=None
    global user_name
    # Declares the variable user_name as a global variable
    user_name = name_entry.get()
    # Sets the variable user_name as the user entry in the name_entry widget
    submit_button.destroy()
    # Destroys the submit_button widget
    name_entry.destroy()
    # Destroys the name_entry widget
    main_title.destroy()
    # Destroys the main_title widget
    sub_title.destroy()
    # Destroys the sub_title widget
    subsub_title.destroy()
    # Destroys the subsub_title widget
    warning.destroy()
    # Destroys the warning widget
    intro()
    # Calls the intro function

window.bind('<Return>', name_input)
# Binds the enter key as an event to call the name_input function

submit_button = Button(window, # 0.5 + 1
                       text="✓", # 2
                       command=name_input) # 3
# 1. creates a button widget assigned to submit_button and puts it into the window
# 2. Sets the text inside the button to "✓"
# 3. Sets the button command to the function name_input

submit_button.place(relx=0.5, # 0.5 + 1
                    rely=0.34, # 2
                    anchor="center") # 3
# 1. places the widget submit_button to the x value of 0.5
# 2. sets teh widgets y value to 0.34
# 3. Anchors the text in the widet to the center

def intro():
    # Creates a funciton called intro
    intro_message = Label(window, # 0.5 + 1
                       text="\n \n \nHi there " + (user_name) + ", Welcome to Text PC : Builder! \n TPCB is a text based PC builder to help you understand the different parts \n of a computer whilst creating your own custom pc. *hands you a tutorial*\n\n -Console", # 2
                       bg="black", # 3
                       fg="white", # 4
                       font="Krungthep 24", # 5
                       anchor="center") # 6
    # 1. Creates a label widget assigned to intro_message and puts it into the window
    # 2. Sets the bg to black
    # 3. Sets the fg to white
    # 4. Sets the font to "Krungthep" and size to 24
    # 5. Anchors the text to the center of the label

    intro_message.pack()
    # Packs the label into the window

    def start_sequence(event=None):
        # Creatung a function called start_sequence with the attrivute event=None
        intro_message.destroy()
        # Destroying the widget intro_message
        continue_below.destroy()
        # Destroying the widget coninue_below
        build_tutorial()
        # Calling the build_tutorail function

    window.bind('<Return>', start_sequence)
    # Binding the return even to the window and calling the start sequence function

    continue_below = Button(window, # 0.5 + 1
                           text="✓", # 2
                            command=start_sequence) # 3
    # 1. Creates a button widget and assigns it to continue bekow, places it in the window
    # 2. Sets the button text to "✓"
    # 3. Sets the button command to the star_sequence function

    continue_below.place(relx=0.5, # 1
                        rely=0.34, # 2
                        anchor="center") # 3
    # 1. Places the button known as continue.below at x value 0.5
    # 2. Sets the y value at 0.34
    # 3. Anchors teh text inside the widget in the center

def build_tutorial():
    # Create a function called build_tutorial

    tutorial_image = PhotoImage(file = "img/tutorial.png")
    # Create a PhotoImage called tutorial_image and list the file location

    tutorial_image_label = Label(window,
                                 # Create a label and place it in the window
                                 image=tutorial_image)
    # Set the image of the label to tutorial_image

    tutorial_image_width = str(window.winfo_screenwidth())
    # Set the image known as tutorial_image to have the width of the winfo screen width and convert that to a string with str
    tutorial_image_height = str(window.winfo_screenheight())
        # Set the image known as tutorial_image to have the height of the winfo screen height and convert that to a string with str

    tutorial_image_label.configure(width=tutorial_image_width,
                                   # Set the width to the variable expressing the width(above)
                                   height=tutorial_image_height)
                                       # Set the height to the variable expressing the height (above)

    tutorial_image_label.image = (tutorial_image)
    # Reference the image to the label with .image

    tutorial_image_label.pack()
    # Pack the label into the window

    def to_frame_create(event=None):
        # Create a function called
        finish_tutorial.destroy()
        # Destroy the finish_tutorail widget
        tutorial_image_label.destroy()
        # Destroy tutorial_image widget
        build()
        # Call The Build Function

    window.bind('<Return>', to_frame_create)
    # Bind return to the window and call the function frame_create when return event

    finish_tutorial = Button(window, # 0.5 + 1
                            text="---> CLICK HERE TO START!", # 2
                             relief="solid", # 3
                             borderwidth=40, # 4
                             command=to_frame_create) # 5
    # 0.5 + 1. Create a button widget and put it in the window
    # 2. Set the button text to "---> CLICK HERE TO START!"
    # 3. Set the button relief to solid
    # 4. Set the borderwidth to 40
    # 5. Set the button command to the function frame_create    

    finish_tutorial.place(relx=0.93, # 1
                    rely=0.02, # 2
                    anchor="center") # 3
    # 1. Place finish_tutorial with a x value of 0.93
    # 2. Set the y value to 0.02
    # 3. Anchor the text to the center of the widget

    tutorial_exists_label = Label(window, # 0.5 + 1
                                  text="Tutorial:", # 2
                                  bg="black", # 3
                                  fg="white", # 4
                                  font="Krungthep 37", # 5
                                  anchor="e") # 6
    # 1. Creating a label widget and assinging it to tutorial_exists and places it in the window
    # 2. Sets the labels text to "Tutorial:"
    # 3. Sets the bg to black
    # 4. Sets the fg to white
    # 5. Sets the font to  "Krungthep" size 37
    # 6. Anchors teh text east


    tutorial_exists_label.place(relx=0.1, # Places the label with the x value 0.1
                          rely=0.02, # Sets the y value to 0.02
                          anchor="center") # Anchors it to the center

    def build():

        def blank():
            blank = 0                    # Fixes a bug encountered after binding return to the window previously
            return blank
        window.bind('<Return>', blank)

        info_frame = Frame(window, width=425,
                           height=1000,
                           bg="black")
        info_frame.pack_propagate(0)
        info_frame.pack(side='right', padx=0, pady=0)

        global user_name
        pc_title = Label(window,
                         text="Build Name: " + user_name + "'s PC (Current)",
                         bg="black",
                         fg="white",
                         font="Krungthep 37",                                                                             # Creating the UI with labels
                         anchor="e")

        pc_title.pack(side=TOP, anchor="nw")

        pc_specs = Label(window,
                         text="Parts Selected:",
                         bg="black",
                         fg="white",
                         font="Krungthep 30",
                         anchor="e")

        pc_specs.pack(side=TOP, anchor="nw")

        class Part:
            def __init__(self, name, price, rating):
                self.name = name
                self.price = price                                            # Creates a class called Part, witht the attributes of a name, price and rating. This will be used to identify all parts in the code
                self.rating = rating

        case_1 = Part("Corsair Carbide SPEC-OMEGA RGB", 269, 9.4)
        case_2 = Part("Phanteks Enthoo Elite", 1499, 8)
        case_3 = Part("Cooler Master NR400", 64, 6)
        case_4 = Part("NZXT H700 and Variations", 260, 9.4)
        case_5 = Part("Darkflash DLM21 Mesh", 65, 9)                         # Case Parts
        case_6 = Part("Thermaltake S100", 19, 7)
        case_7 = Part("Lian-Li PCO8RGB", 200, 1)
        case_8 = Part("Cougar MX330 Series", 83, 2)
        case_9 = Part("Thermaltake Level 20", 140, 9)
        case_10 = Part("Cardboard Box", 1, 0.5)

        motherboard_1 = Part("ASUS ROG Strix Z390-E", 387, 9.3)
        motherboard_2 = Part("ASUS Micro ATX DDR3 2000 AMD AM3", 60, 5.7)
        motherboard_3 = Part("MSI ATX DDR3 2400 LGA 1150 Motherboards Z97 PC MATE", 120, 7.3)
        motherboard_4 = Part("ASRock Z390 Phantom Gaming ITX", 214, 7.8)
        motherboard_5 = Part("Gigabyte Z390 Designare", 420, 8.9)
        motherboard_6 = Part("MSI MEG X570 ACE", 510, 9.3)                      # Motherboard Parts
        motherboard_7 = Part("GIGABYTE X299", 699, 9.2)
        motherboard_8 = Part("ASRock Z490 Taichi", 620, 8.4)
        motherboard_9 = Part("GIGABYTE H370 HD3", 156, 8.7)
        motherboard_10 = Part("Piece of paper with UI slot", 1, 0.5)

        cpu_1 = Part("Intel Core i5-10600K", 769, 8.9)
        cpu_2 = Part("AMD Ryzen 9 3950X", 689, 7.9)
        cpu_3 = Part("AMD Ryzen 7 3700X", 300, 6.3)
        cpu_4 = Part("AMD Ryzen 5 3600X", 343, 7.1)
        cpu_5 = Part("AMD Ryzen 3 3300X", 239, 5.1)                      # CPU Parts
        cpu_6 = Part("AMD Ryzen 5 3400G", 423, 6.5)
        cpu_7 = Part("Intel Core i9-9960X Processor", 250, 4.9)
        cpu_8 = Part("AMD Ryzen Threadripper 1950X", 430, 8.3)
        cpu_9 = Part("Intel Xeon Processor E5-1680 v2", 340, 6.8)
        cpu_10 = Part("Intel Core i7-9750H Processor", 320, 5.8)

        gpu_1 = Part("AMD Radeon RX 5700", 647, 8.5)
        gpu_2 = Part("Nvidia GeForce RTX 2080 Ti", 330, 9.9)
        gpu_3 = Part("AMD Radeon RX 5600 XT", 474, 8.8)
        gpu_4 = Part("Nvidia GeForce RTX 2070 Super", 655, 8.1)
        gpu_5 = Part("Nvidia GeForce GTX 1660 Super", 329, 7.6)                      # GPU Parts
        gpu_6 = Part("AMD Radeon VII", 647, 7.3)
        gpu_7 = Part("Nvidia GeForce RTX 2080 Super", 330, 7.8)
        gpu_8 = Part("Zotac GeForce GTX 1080 Ti Mini", 329, 6.9)
        gpu_9 = Part("Gigabyte GeForce GTX 1660 OC 6G", 430, 8.4)
        gpu_10 = Part("iPod Touch Graphics Card", 1, 0.5)

        ram_1 = Part("1GB", 10, 1.6)
        ram_2 = Part("2GB", 20, 2.6)
        ram_3 = Part("3GB", 30, 3.2)
        ram_4 = Part("4GB", 40, 4.6)
        ram_5 = Part("8GB", 80, 7.5)                      # RAM Parts
        ram_6 = Part("16GB", 160, 9.4)
        ram_7 = Part("32GB", 320, 8.9)
        ram_8 = Part("64GB", 640, 8.7)
        ram_9 = Part("100GB", 1000, 6.9)
        ram_10 = Part("1000GB", 10000, 8.8)

        storage_1 = Part("Intel Optane 905P - 1TB", 684, 8.7)
        storage_2 = Part("Samsung 970 Pro - 1TB", 239, 7.6)
        storage_3 = Part("Toshiba OCZ RD40 - 1TB", 203, 8.3)
        storage_4 = Part("Adata XPG SX8200 SSD - 1TB", 136, 7.4)
        storage_5 = Part("Samsung 860 Pro", 218, 7.4)                      # Storage Parts
        storage_6 = Part("Intel 750 Series", 340, 8.7)
        storage_7 = Part("Samsung 860 Evo", 265, 7.9)
        storage_8 = Part("HP S700 Pro", 185, 7.2)
        storage_9 = Part("Intel 760p Series SSD", 300, 9.4)
        storage_10 = Part("USB Stick", 1, 0.5)

        cooling_1 = Part("Noctua NF-S12B Redux-1200", 40, 5.8)
        cooling_2 = Part("Noctua NF-F12 PWM", 80, 9.4)
        cooling_3 = Part("Corsair iCUE QL120 RGB", 65, 7.4)
        cooling_4 = Part("Scythe Kaze Flex", 85, 6.6)
        cooling_5 = Part("Noctua NF-A12x15", 45, 4.5)
        cooling_6 = Part("CoolerMaster MasterLiquid ML360R RGB", 190, 8.6)                      # Cooling Parts
        cooling_7 = Part("Arctic Liquid Freezer II 280", 260, 8.9)
        cooling_8 = Part("Corsair H100i RGB PRO XT", 219, 9.6)
        cooling_9 = Part("NZXT Kraken M22", 145, 7.9)
        cooling_10 = Part("Paper Fan", 1, 0.5)

        power_1 = Part("Thermaltake Toughpower Grand RGB 1050W Platinum", 115, 7.3)
        power_2 = Part("Silverstone SFX Series SST-SX550", 275, 4.5)
        power_3 = Part("Thermaltake Toughpower PF1 ARGB 1200W", 315, 7.6)
        power_4 = Part("XPG Core Reactor 750W", 140, 7.4)
        power_5 = Part("Thermaltake Smart RGB 700W", 95, 4.3)
        power_6 = Part("Corsair AX1500i", 185, 7.8)
        power_7 = Part("NZXT E650.", 210, 7.3)                      # Power Parts
        power_8 = Part("Thermaltake Toughpower PF1 ARGB 1200W", 335, 9.6)
        power_9 = Part("XPG Core Reactor 750W", 315, 7.4)
        power_10 = Part("Connect to toaster with jumper Cables", 3, 0.5)

        def case(): # Function for selecting the case

            case_info = Label(info_frame,
                              text="PC cases are used to enclose\n all the hardware and computer \nparts into a metal or \nplastic and sometimes partly \nglass container. Cases \ncan be used to optimise \nairflow, reduce sound \nand create convenience \nfor moving the PC while\n protecting the parts inside.\n A case is NOT required for a\n computer to power on and run,\n as long as all the parts are \nconnected it will work however\n cases are important and \nconsidered essential as it will \nprevent damage to the\n parts, control airflow to cool\n the parts and can hold these \nparts well with UI slots \nusually included so you\n can use your peripheral \ndevices and move the pc \naround.",
                              bg="black",
                              fg="white",
                              font="Krungthep 24")         # Info about the part

            case_info.pack(anchor="nw")

            def destroy_case():
                case_label.destroy()
                case_opt.destroy()
                next_part_motherboard.destroy()        # Function called when selecting next part, to remove all case related labels so new ones can be set
                select_case_label.destroy()
                case_info.destroy()
                motherboard()

            case_label = Label(window,
                               text="<- Selecting Part: Case",
                               bg="black",
                               fg="white",
                               font="Krungthep 37")

            case_label.pack()

            CaseList = [
                case_1.name + " ||$" + str(case_1.price) + " ||⭑ " + str(case_1.rating),
                case_2.name + " ||$" + str(case_2.price) + " ||⭑ " + str(case_2.rating),
                case_3.name + " ||$" + str(case_3.price) + " ||⭑ " + str(case_3.rating),
                case_4.name + " ||$" + str(case_4.price) + " ||⭑ " + str(case_4.rating),
                case_5.name + " ||$" + str(case_5.price) + " ||⭑ " + str(case_5.rating),
                case_6.name + " ||$" + str(case_6.price) + " ||⭑ " + str(case_6.rating),           # Turning the case parts from class objects to a string
                case_7.name + " ||$" + str(case_7.price) + " ||⭑ " + str(case_7.rating),
                case_8.name + " ||$" + str(case_8.price) + " ||⭑ " + str(case_8.rating),
                case_9.name + " ||$" + str(case_9.price) + " ||⭑ " + str(case_9.rating),
                case_10.name + " ||$" + str(case_10.price) + " ||⭑ " + str(case_10.rating),
            ]
            global CaseVariable
            CaseVariable = StringVar(window)
            CaseVariable.set(CaseList[0])

            case_opt = OptionMenu(window, CaseVariable, *CaseList)         # Creating the Selector
            case_opt.config(font="Krungthep")

            case_opt.pack(side="top")

            select_case_label = Label(text="",
                              bg="black",
                              fg="white")

            select_case_label.pack(side="top")

            global case_selected_label

            case_selected_label = Label(window,
                                        text="",
                                        bg="black",
                                        fg="white",
                                        font="Krungthep 25")

            case_selected_label.pack(side=TOP, anchor="nw")

            def callback(*args):
                select_case_label.configure(text="Case Selected: {}".format(CaseVariable.get()))           # Setting your selection as a variable and ensuring you can call this back making any changes
                case_selected_label.configure(text="Case: {}".format(CaseVariable.get()))
                case_select = CaseVariable.get()

                case_1_str = case_1.name + " ||$" + str(case_1.price) + " ||⭑ " + str(case_1.rating)
                case_2_str = case_2.name + " ||$" + str(case_2.price) + " ||⭑ " + str(case_2.rating)
                case_3_str = case_3.name + " ||$" + str(case_3.price) + " ||⭑ " + str(case_3.rating)
                case_4_str = case_4.name + " ||$" + str(case_4.price) + " ||⭑ " + str(case_4.rating)
                case_5_str = case_5.name + " ||$" + str(case_5.price) + " ||⭑ " + str(case_5.rating)       # Turning string parts into variables for price calculation
                case_6_str = case_6.name + " ||$" + str(case_6.price) + " ||⭑ " + str(case_6.rating)
                case_7_str = case_7.name + " ||$" + str(case_7.price) + " ||⭑ " + str(case_7.rating)
                case_8_str = case_8.name + " ||$" + str(case_8.price) + " ||⭑ " + str(case_8.rating)
                case_9_str = case_9.name + " ||$" + str(case_9.price) + " ||⭑ " + str(case_9.rating)
                case_10_str = case_10.name + " ||$" + str(case_10.price) + " ||⭑ " + str(case_10.rating)

                global case_price

                if case_select == case_1_str:
                    case_price = 269
                if case_select == case_2_str:
                    case_price = 1499                           # Calculating price of the case based on selection
                if case_select == case_3_str:
                    case_price = 64
                if case_select == case_4_str:
                    case_price = 260
                if case_select == case_5_str:
                    case_price = 65
                if case_select == case_6_str:
                    case_price = 19
                if case_select == case_7_str:
                    case_price = 200
                if case_select == case_8_str:
                    case_price = 83
                if case_select == case_9_str:
                    case_price = 140
                if case_select == case_10_str:
                    case_price = 1

            CaseVariable.trace("w", callback)

            next_part_motherboard = Button(window,
                                           text="✓",
                                           command=destroy_case)

            next_part_motherboard.pack()

        def motherboard():

            def destroy_motherboard():
                motherboard_label.destroy()
                motherboard_opt.destroy()
                next_part_cpu.destroy()
                selectmotherboard_label.destroy()                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                previous_part_case.destroy()
                motherboard_info.destroy()
                cpu()

            def destroy_motherboard_2():
                previous_part_case.destroy()
                motherboard_label.destroy()
                motherboard_opt.destroy()
                selectmotherboard_label.destroy()
                next_part_cpu.destroy()
                motherboard_info.destroy()
                selectmotherboard_label.destroy()
                case_selected_label.destroy()
                previous_part_case.destroy()
                case()

            motherboard_info = Label(info_frame,
                              text="Motherboards, also known as \nmainboards, main \ncircuit boards,\n system boards,\n baseboards, planar boards \nor logic\n boards, are the\n main printed \ncircuit board of\n a computer and \neven in other \nexpandable systems. \nIt allows communication\n between\n components and allows\n these to\n interact with\n each other. Motherboards\n open opportunity\n for for extensions and \nexpansions such as\n USB slots, sound\n cards, video cards\n, hard-drives and\n more. Motherboards\n are essential\n for a computer \nand it cannot\n work without one.",
                              bg="black",
                              fg="white",
                              font="Krungthep 24")

            motherboard_info.pack(anchor="center")

            previous_part_case = Button(window,
                                    text="▲",
                                    command=destroy_motherboard_2)

            previous_part_case.pack()


            motherboard_label = Label(window,
                               text="<- Selecting Part: Motherboard",
                               bg="black",
                               fg="white",
                               font="Krungthep 37")

            motherboard_label.pack()

            MotherboardList = [
                motherboard_1.name + " ||$" + str(motherboard_1.price) + " ||⭑ " + str(motherboard_1.rating),
                motherboard_2.name + " ||$" + str(motherboard_2.price) + " ||⭑ " + str(motherboard_2.rating),
                motherboard_3.name + " ||$" + str(motherboard_3.price) + " ||⭑ " + str(motherboard_3.rating),
                motherboard_4.name + " ||$" + str(motherboard_4.price) + " ||⭑ " + str(motherboard_4.rating),
                motherboard_5.name + " ||$" + str(motherboard_5.price) + " ||⭑ " + str(motherboard_5.rating),
                motherboard_6.name + " ||$" + str(motherboard_6.price) + " ||⭑ " + str(motherboard_6.rating),
                motherboard_7.name + " ||$" + str(motherboard_7.price) + " ||⭑ " + str(motherboard_7.rating),
                motherboard_8.name + " ||$" + str(motherboard_8.price) + " ||⭑ " + str(motherboard_8.rating),
                motherboard_9.name + " ||$" + str(motherboard_9.price) + " ||⭑ " + str(motherboard_9.rating),
                motherboard_10.name + " ||$" + str(motherboard_10.price) + " ||⭑ " + str(motherboard_10.rating),
            ]
            global MotherboardVariable
            MotherboardVariable = StringVar(window)
            MotherboardVariable.set(MotherboardList[0])

            motherboard_opt = OptionMenu(window, MotherboardVariable, *MotherboardList)
            motherboard_opt.config(font="Krungthep")

            motherboard_opt.pack(side="top")

            selectmotherboard_label = Label(text="",
                              bg="black",
                              fg="white")

            selectmotherboard_label.pack(side="top")

            global motherboard_selected_label

            motherboard_selected_label = Label(window,
                                        text="",
                                        bg="black",
                                        fg="white",
                                        font="Krungthep 25")

            motherboard_selected_label.pack(side=TOP, anchor="nw")

            def callback(*args):
                selectmotherboard_label.configure(text="Motherboard Selected: {}".format(MotherboardVariable.get()))
                motherboard_selected_label.configure(text="Motherboard: {}".format(MotherboardVariable.get()))
                motherboard_select = MotherboardVariable.get()

                motherboard_1_str = motherboard_1.name + " ||$" + str(motherboard_1.price) + " ||⭑ " + str(motherboard_1.rating)
                motherboard_2_str = motherboard_2.name + " ||$" + str(motherboard_2.price) + " ||⭑ " + str(motherboard_2.rating)
                motherboard_3_str = motherboard_3.name + " ||$" + str(motherboard_3.price) + " ||⭑ " + str(motherboard_3.rating)
                motherboard_4_str = motherboard_4.name + " ||$" + str(motherboard_4.price) + " ||⭑ " + str(motherboard_4.rating)
                motherboard_5_str = motherboard_5.name + " ||$" + str(motherboard_5.price) + " ||⭑ " + str(motherboard_5.rating)
                motherboard_6_str = motherboard_6.name + " ||$" + str(motherboard_6.price) + " ||⭑ " + str(motherboard_6.rating)
                motherboard_7_str = motherboard_7.name + " ||$" + str(motherboard_7.price) + " ||⭑ " + str(motherboard_7.rating)
                motherboard_8_str = motherboard_8.name + " ||$" + str(motherboard_8.price) + " ||⭑ " + str(motherboard_8.rating)
                motherboard_9_str = motherboard_9.name + " ||$" + str(motherboard_9.price) + " ||⭑ " + str(motherboard_9.rating)
                motherboard_10_str = motherboard_10.name + " ||$" + str(motherboard_10.price) + " ||⭑ " + str(motherboard_10.rating)

                global motherboard_price

                if motherboard_select == motherboard_1_str:
                    motherboard_price = 387
                if motherboard_select == motherboard_2_str:
                    motherboard_price = 60
                if motherboard_select == motherboard_3_str:
                    motherboard_price = 120
                if motherboard_select == motherboard_4_str:
                    motherboard_price = 214
                if motherboard_select == motherboard_5_str:
                    motherboard_price = 420
                if motherboard_select == motherboard_6_str:
                    motherboard_price = 510
                if motherboard_select == motherboard_7_str:
                    motherboard_price = 699
                if motherboard_select == motherboard_8_str:
                    motherboard_price = 620
                if motherboard_select == motherboard_9_str:
                    motherboard_price = 156
                if motherboard_select == motherboard_10_str:
                    motherboard_price = 1

            MotherboardVariable.trace("w", callback)

            next_part_cpu = Button(window,
                                           text="✓",
                                           command=destroy_motherboard)

            next_part_cpu.pack()

            def cpu():
                previous_part_case.destroy()

                def destroy_cpu():
                    cpu_label.destroy()
                    cpu_opt.destroy()
                    next_part_gpu.destroy()
                    selectcpu_label.destroy()
                    cpu_info.destroy()
                    previous_part_motherboard.destroy()
                    gpu()

                def destroy_cpu_2():
                    previous_part_motherboard.destroy()
                    selectcpu_label.destroy()
                    cpu_label.destroy()
                    cpu_opt.destroy()
                    next_part_gpu.destroy()
                    selectmotherboard_label.destroy()
                    motherboard_selected_label.destroy()
                    cpu_info.destroy()
                    motherboard()

                cpu_info = Label(info_frame,
                                         text="The CPU or central\n processing unit \nis extremely important for\n the functionality\n of a computer, as i\nn the \nname, a cpu is\n a main processor \nand executes all the\n instructions \ngiven to the computer\n via programs\n and software, CPU’s can \nhave higher gigahertz \nenabling it to process\n more at once and \nthe processing becomes \nfaster. CPUs are \nessential for any \ncomputer and \nit is important\n to keep this part\n at a lower \ntemperature to prevent \ndamage.",
                                         bg="black",
                                         fg="white",
                                         font="Krungthep 24")

                cpu_info.pack(anchor="nw")

                global previous_part_motherboard                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE

                previous_part_motherboard = Button(window,
                                                   text="▲",
                                                   command=destroy_cpu_2)

                previous_part_motherboard.pack()

                cpu_label = Label(window,
                                          text="<- Selecting Part: CPU",
                                          bg="black",
                                          fg="white",
                                          font="Krungthep 37")

                cpu_label.pack()

                cpuList = [
                    cpu_1.name + " ||$" + str(cpu_1.price) + " ||⭑ " + str(cpu_1.rating),
                    cpu_2.name + " ||$" + str(cpu_2.price) + " ||⭑ " + str(cpu_2.rating),
                    cpu_3.name + " ||$" + str(cpu_3.price) + " ||⭑ " + str(cpu_3.rating),
                    cpu_4.name + " ||$" + str(cpu_4.price) + " ||⭑ " + str(cpu_4.rating),
                    cpu_5.name + " ||$" + str(cpu_5.price) + " ||⭑ " + str(cpu_5.rating),
                    cpu_6.name + " ||$" + str(cpu_6.price) + " ||⭑ " + str(cpu_6.rating),
                    cpu_7.name + " ||$" + str(cpu_7.price) + " ||⭑ " + str(cpu_7.rating),
                    cpu_8.name + " ||$" + str(cpu_8.price) + " ||⭑ " + str(cpu_8.rating),                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    cpu_9.name + " ||$" + str(cpu_9.price) + " ||⭑ " + str(cpu_9.rating),
                    cpu_10.name + " ||$" + str(cpu_10.price) + " ||⭑ " + str(cpu_10.rating),
                ]
                global cpuVariable
                cpuVariable = StringVar(window)
                cpuVariable.set(cpuList[0])

                cpu_opt = OptionMenu(window, cpuVariable, *cpuList)
                cpu_opt.config(font="Krungthep")

                cpu_opt.pack(side="top")

                global selectcpu_label

                selectcpu_label = Label(text="",
                                                bg="black",
                                                fg="white")

                selectcpu_label.pack(side="top")

                global cpu_selected_label

                cpu_selected_label = Label(window,
                                                   text="",
                                                   bg="black",
                                                   fg="white",
                                                   font="Krungthep 25")

                cpu_selected_label.pack(side=TOP, anchor="nw")

                def callback(*args):
                    selectcpu_label.configure(text="CPU Selected: {}".format(cpuVariable.get()))
                    cpu_selected_label.configure(text="CPU: {}".format(cpuVariable.get()))
                    cpu_select = cpuVariable.get()

                    cpu_1_str = cpu_1.name + " ||$" + str(cpu_1.price) + " ||⭑ " + str(cpu_1.rating)
                    cpu_2_str = cpu_2.name + " ||$" + str(cpu_2.price) + " ||⭑ " + str(cpu_2.rating)
                    cpu_3_str = cpu_3.name + " ||$" + str(cpu_3.price) + " ||⭑ " + str(cpu_3.rating)
                    cpu_4_str = cpu_4.name + " ||$" + str(cpu_4.price) + " ||⭑ " + str(cpu_4.rating)
                    cpu_5_str = cpu_5.name + " ||$" + str(cpu_5.price) + " ||⭑ " + str(cpu_5.rating)
                    cpu_6_str = cpu_6.name + " ||$" + str(cpu_6.price) + " ||⭑ " + str(cpu_6.rating)
                    cpu_7_str = cpu_7.name + " ||$" + str(cpu_7.price) + " ||⭑ " + str(cpu_7.rating)
                    cpu_8_str = cpu_8.name + " ||$" + str(cpu_8.price) + " ||⭑ " + str(cpu_8.rating)
                    cpu_9_str = cpu_9.name + " ||$" + str(cpu_9.price) + " ||⭑ " + str(cpu_9.rating)
                    cpu_10_str = cpu_10.name + " ||$" + str(cpu_10.price) + " ||⭑ " + str(cpu_10.rating)

                    global cpu_price

                    if cpu_select == cpu_1_str:
                        cpu_price = 769
                    if cpu_select == cpu_2_str:
                        cpu_price = 689
                    if cpu_select == cpu_3_str:
                        cpu_price = 300
                    if cpu_select == cpu_4_str:
                        cpu_price = 343
                    if cpu_select == cpu_5_str:
                        cpu_price = 239
                    if cpu_select == cpu_6_str:
                        cpu_price = 423                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    if cpu_select == cpu_7_str:
                        cpu_price = 250
                    if cpu_select == cpu_8_str:
                        cpu_price = 430
                    if cpu_select == cpu_9_str:
                        cpu_price = 340
                    if cpu_select == cpu_10_str:
                        cpu_price = 320

                cpuVariable.trace("w", callback)

                next_part_gpu = Button(window,
                                       text="✓",
                                       command=destroy_cpu)

                next_part_gpu.pack()

            def gpu():
                previous_part_case.destroy()
                previous_part_motherboard.destroy()

                def destroy_gpu():
                    gpu_label.destroy()
                    gpu_opt.destroy()
                    next_part_ram.destroy()
                    selectgpu_label.destroy()
                    gpu_info.destroy()
                    previous_part_cpu.destroy()
                    ram()

                def destroy_gpu_2():
                    previous_part_cpu.destroy()
                    selectgpu_label.destroy()
                    gpu_label.destroy()
                    gpu_info.destroy()
                    gpu_opt.destroy()
                    next_part_ram.destroy()
                    selectcpu_label.destroy()
                    cpu_selected_label.destroy()
                    cpu()

                global previous_part_cpu

                gpu_info = Label(info_frame,
                                 text="A gpu is a graphics\n processing unit, this\n part is specialised\n to rapidly manipulate \nand alter memory to\n accelerate the creation of\n images and output\n to a display,\n these are used in many types\n of computers and more\n expensive and\n newer gpus are incredibly\n efficient \nat image creation. GPUs can be\n external or embedded \non the motherboard.",
                                 bg="black",
                                 fg="white",
                                 font="Krungthep 24")

                gpu_info.pack(anchor="nw")

                previous_part_cpu = Button(window,
                                           text="▲",
                                           command=destroy_gpu_2)

                previous_part_cpu.pack()                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE


                gpu_label = Label(window,
                                          text="<- Selecting Part: GPU",
                                          bg="black",
                                          fg="white",
                                          font="Krungthep 37")

                gpu_label.pack()
                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                gpuList = [
                    gpu_1.name + " ||$" + str(gpu_1.price) + " ||⭑ " + str(gpu_1.rating),
                    gpu_2.name + " ||$" + str(gpu_2.price) + " ||⭑ " + str(gpu_2.rating),
                    gpu_3.name + " ||$" + str(gpu_3.price) + " ||⭑ " + str(gpu_3.rating),
                    gpu_4.name + " ||$" + str(gpu_4.price) + " ||⭑ " + str(gpu_4.rating),
                    gpu_5.name + " ||$" + str(gpu_5.price) + " ||⭑ " + str(gpu_5.rating),
                    gpu_6.name + " ||$" + str(gpu_6.price) + " ||⭑ " + str(gpu_6.rating),
                    gpu_7.name + " ||$" + str(gpu_7.price) + " ||⭑ " + str(gpu_7.rating),
                    gpu_8.name + " ||$" + str(gpu_8.price) + " ||⭑ " + str(gpu_8.rating),
                    gpu_9.name + " ||$" + str(gpu_9.price) + " ||⭑ " + str(gpu_9.rating),
                    gpu_10.name + " ||$" + str(gpu_10.price) + " ||⭑ " + str(gpu_10.rating),
                ]
                global gpuVariable
                gpuVariable = StringVar(window)
                gpuVariable.set(gpuList[0])

                gpu_opt = OptionMenu(window, gpuVariable, *gpuList)
                gpu_opt.config(font="Krungthep")
                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                gpu_opt.pack(side="top")

                global selectgpu_label

                selectgpu_label = Label(text="",
                                                bg="black",
                                                fg="white")

                selectgpu_label.pack(side="top")

                global gpu_selected_label

                gpu_selected_label = Label(window,
                                                   text="",                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                                                   bg="black",
                                                   fg="white",
                                                   font="Krungthep 25")

                gpu_selected_label.pack(side=TOP, anchor="nw")

                def callback(*args):
                    selectgpu_label.configure(text="GPU Selected: {}".format(gpuVariable.get()))                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    gpu_selected_label.configure(text="GPU: {}".format(gpuVariable.get()))
                    gpu_select = gpuVariable.get()

                    gpu_1_str = gpu_1.name + " ||$" + str(gpu_1.price) + " ||⭑ " + str(gpu_1.rating)
                    gpu_2_str = gpu_2.name + " ||$" + str(gpu_2.price) + " ||⭑ " + str(gpu_2.rating)
                    gpu_3_str = gpu_3.name + " ||$" + str(gpu_3.price) + " ||⭑ " + str(gpu_3.rating)
                    gpu_4_str = gpu_4.name + " ||$" + str(gpu_4.price) + " ||⭑ " + str(gpu_4.rating)
                    gpu_5_str = gpu_5.name + " ||$" + str(gpu_5.price) + " ||⭑ " + str(gpu_5.rating)
                    gpu_6_str = gpu_6.name + " ||$" + str(gpu_6.price) + " ||⭑ " + str(gpu_6.rating)
                    gpu_7_str = gpu_7.name + " ||$" + str(gpu_7.price) + " ||⭑ " + str(gpu_7.rating)
                    gpu_8_str = gpu_8.name + " ||$" + str(gpu_8.price) + " ||⭑ " + str(gpu_8.rating)
                    gpu_9_str = gpu_9.name + " ||$" + str(gpu_9.price) + " ||⭑ " + str(gpu_9.rating)
                    gpu_10_str = gpu_10.name + " ||$" + str(gpu_10.price) + " ||⭑ " + str(gpu_10.rating)

                    global gpu_price

                    if gpu_select == gpu_1_str:
                        gpu_price = 647
                    if gpu_select == gpu_2_str:
                        gpu_price = 330
                    if gpu_select == gpu_3_str:
                        gpu_price = 474
                    if gpu_select == gpu_4_str:
                        gpu_price = 655
                    if gpu_select == gpu_5_str:
                        gpu_price = 329
                    if gpu_select == gpu_6_str:
                        gpu_price = 647                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    if gpu_select == gpu_7_str:
                        gpu_price = 330
                    if gpu_select == gpu_8_str:
                        gpu_price = 329
                    if gpu_select == gpu_9_str:
                        gpu_price = 430
                    if gpu_select == gpu_10_str:
                        gpu_price = 1

                gpuVariable.trace("w", callback)

                next_part_ram = Button(window,
                                       text="✓",                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                                       command=destroy_gpu)

                next_part_ram.pack()

            def ram():
                global previous_part_gpu

                def destroy_ram():
                    previous_part_gpu.destroy()
                    ram_label.destroy()
                    ram_opt.destroy()
                    next_part_storage.destroy()                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    selectram_label.destroy()
                    ram_info.destroy()
                    storage()

                def destroy_ram_2():
                    previous_part_gpu.destroy()
                    selectram_label.destroy()
                    ram_label.destroy()                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    ram_opt.destroy()
                    next_part_storage.destroy()
                    selectgpu_label.destroy()
                    gpu_selected_label.destroy()
                    ram_info.destroy()
                    gpu()

                ram_info = Label(info_frame,
                                 text="Random Access Memory (RAM)\n is a type of volatile \nmemory, its main \npractical purpose \nis to enable the user\n to run more programs\n and tasks at once \nwithout slowing the \ncomputer down. Programs\n must be taken from a \nhard disk or \nflash memory and taken \nto the ram to be \nrun properly, \nthis is why having \nmore ram enables you \nto run more applications\n at once. When your computer \nfirst boots up, bios\n looks for an operating system \nand loads it into RAM, this \nthen enables you to start \nmoving applications to \nRAM to launch and use them.",
                                 bg="black",
                                 fg="white",
                                 font="Krungthep 24")

                ram_info.pack(anchor="sw")

                previous_part_gpu = Button(window,
                                           text="▲",
                                           command=destroy_ram_2)

                previous_part_gpu.pack()                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE

                ram_label = Label(window,
                                  text="<- Selecting Part: RAM",
                                  bg="black",
                                  fg="white",
                                  font="Krungthep 37")

                ram_label.pack()

                ramList = [
                    ram_1.name + " ||$" + str(ram_1.price) + " ||⭑ " + str(ram_1.rating),
                    ram_2.name + " ||$" + str(ram_2.price) + " ||⭑ " + str(ram_2.rating),
                    ram_3.name + " ||$" + str(ram_3.price) + " ||⭑ " + str(ram_3.rating),
                    ram_4.name + " ||$" + str(ram_4.price) + " ||⭑ " + str(ram_4.rating),
                    ram_5.name + " ||$" + str(ram_5.price) + " ||⭑ " + str(ram_5.rating),
                    ram_6.name + " ||$" + str(ram_6.price) + " ||⭑ " + str(ram_6.rating),
                    ram_7.name + " ||$" + str(ram_7.price) + " ||⭑ " + str(ram_7.rating),
                    ram_8.name + " ||$" + str(ram_8.price) + " ||⭑ " + str(ram_8.rating),
                    ram_9.name + " ||$" + str(ram_9.price) + " ||⭑ " + str(ram_9.rating),
                    ram_10.name + " ||$" + str(ram_10.price) + " ||⭑ " + str(ram_10.rating),
                ]
                global ramVariable
                ramVariable = StringVar(window)
                ramVariable.set(ramList[0])

                ram_opt = OptionMenu(window, ramVariable, *ramList)                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                ram_opt.config(font="Krungthep")

                ram_opt.pack(side="top")

                global selectram_label

                selectram_label = Label(text="",                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                                        bg="black",
                                        fg="white")

                selectram_label.pack(side="top")

                global ram_selected_label


                ram_selected_label = Label(window,
                                           text="",
                                           bg="black",
                                           fg="white",
                                           font="Krungthep 25")

                ram_selected_label.pack(side=TOP, anchor="nw")

                def callback(*args):
                    selectram_label.configure(text="RAM Selected: {}".format(ramVariable.get()))
                    ram_selected_label.configure(text="RAM: {}".format(ramVariable.get()))
                    ram_select = ramVariable.get()

                    ram_1_str = ram_1.name + " ||$" + str(ram_1.price) + " ||⭑ " + str(ram_1.rating)
                    ram_2_str = ram_2.name + " ||$" + str(ram_2.price) + " ||⭑ " + str(ram_2.rating)
                    ram_3_str = ram_3.name + " ||$" + str(ram_3.price) + " ||⭑ " + str(ram_3.rating)
                    ram_4_str = ram_4.name + " ||$" + str(ram_4.price) + " ||⭑ " + str(ram_4.rating)
                    ram_5_str = ram_5.name + " ||$" + str(ram_5.price) + " ||⭑ " + str(ram_5.rating)                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    ram_6_str = ram_6.name + " ||$" + str(ram_6.price) + " ||⭑ " + str(ram_6.rating)
                    ram_7_str = ram_7.name + " ||$" + str(ram_7.price) + " ||⭑ " + str(ram_7.rating)
                    ram_8_str = ram_8.name + " ||$" + str(ram_8.price) + " ||⭑ " + str(ram_8.rating)
                    ram_9_str = ram_9.name + " ||$" + str(ram_9.price) + " ||⭑ " + str(ram_9.rating)
                    ram_10_str = ram_10.name + " ||$" + str(ram_10.price) + " ||⭑ " + str(ram_10.rating)

                    global ram_price

                    if ram_select == ram_1_str:
                        ram_price = 106
                    if ram_select == ram_2_str:
                        ram_price = 20
                    if ram_select == ram_3_str:
                        ram_price = 30
                    if ram_select == ram_4_str:
                        ram_price = 40
                    if ram_select == ram_5_str:
                        ram_price = 80
                    if ram_select == ram_6_str:
                        ram_price = 160
                    if ram_select == ram_7_str:
                        ram_price = 320
                    if ram_select == ram_8_str:
                        ram_price = 640
                    if ram_select == ram_9_str:                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                        ram_price = 1000
                    if ram_select == ram_10_str:
                        ram_price = 10000

                ramVariable.trace("w", callback)

                next_part_storage = Button(window,
                                           text="✓",
                                           command=destroy_ram)
                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                next_part_storage.pack()

            def storage():
                global previous_part_ram

                def destroy_storage():
                    previous_part_ram.destroy()
                    storage_label.destroy()
                    storage_opt.destroy()
                    next_part_cooling.destroy()
                    selectstorage_label.destroy()
                    storage_info.destroy()
                    cooling()
                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                def destroy_storage_2():
                    previous_part_ram.destroy()
                    selectstorage_label.destroy()
                    storage_label.destroy()
                    storage_opt.destroy()
                    next_part_cooling.destroy()
                    selectram_label.destroy()
                    ram_selected_label.destroy()
                    storage_info.destroy()
                    ram()

                storage_info = Label(info_frame,
                                 text="Computer storage is the way \ndata is recorded and retained\n on a physical device,\n storage is essential\n for practical computer \nuse as you want to be\n able to save what\n you’re working on and \nall applications and service\ns we use are saved \nas data. There are\n different types of \nstorage however hardrives\n and flashdrives come\n under as physical storage \ndevices, damage to these \ncomponents can cause \ndata loss and if not plugged \ninto a computer it cannot\n gain acess to it.",
                                 bg="black",
                                 fg="white",
                                 font="Krungthep 24")

                storage_info.pack(anchor="nw")

                previous_part_ram = Button(window,
                                           text="▲",
                                           command=destroy_storage_2)
                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                previous_part_ram.pack()

                storage_label = Label(window,
                                      text="<- Selecting Part: Storage",
                                      bg="black",
                                      fg="white",
                                      font="Krungthep 37")

                storage_label.pack()

                storageList = [
                    storage_1.name + " ||$" + str(storage_1.price) + " ||⭑ " + str(storage_1.rating),
                    storage_2.name + " ||$" + str(storage_2.price) + " ||⭑ " + str(storage_2.rating),
                    storage_3.name + " ||$" + str(storage_3.price) + " ||⭑ " + str(storage_3.rating),
                    storage_4.name + " ||$" + str(storage_4.price) + " ||⭑ " + str(storage_4.rating),
                    storage_5.name + " ||$" + str(storage_5.price) + " ||⭑ " + str(storage_5.rating),
                    storage_6.name + " ||$" + str(storage_6.price) + " ||⭑ " + str(storage_6.rating),
                    storage_7.name + " ||$" + str(storage_7.price) + " ||⭑ " + str(storage_7.rating),
                    storage_8.name + " ||$" + str(storage_8.price) + " ||⭑ " + str(storage_8.rating),
                    storage_9.name + " ||$" + str(storage_9.price) + " ||⭑ " + str(storage_9.rating),
                    storage_10.name + " ||$" + str(storage_10.price) + " ||⭑ " + str(storage_10.rating),
                ]
                global storageVariable
                storageVariable = StringVar(window)
                storageVariable.set(storageList[0])

                storage_opt = OptionMenu(window, storageVariable, *storageList)                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                storage_opt.config(font="Krungthep")

                storage_opt.pack(side="top")

                selectstorage_label = Label(text="",
                                            bg="black",
                                            fg="white")

                selectstorage_label.pack(side="top")

                global storage_selected_label

                storage_selected_label = Label(window,
                                               text="",
                                               bg="black",
                                               fg="white",
                                               font="Krungthep 25")

                storage_selected_label.pack(side=TOP, anchor="nw")                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE

                def callback(*args):
                    selectstorage_label.configure(text="Storage Selected: {}".format(storageVariable.get()))
                    storage_selected_label.configure(text="Storage: {}".format(storageVariable.get()))
                    storage_select = storageVariable.get()

                    storage_1_str = storage_1.name + " ||$" + str(storage_1.price) + " ||⭑ " + str(storage_1.rating)
                    storage_2_str = storage_2.name + " ||$" + str(storage_2.price) + " ||⭑ " + str(storage_2.rating)
                    storage_3_str = storage_3.name + " ||$" + str(storage_3.price) + " ||⭑ " + str(storage_3.rating)
                    storage_4_str = storage_4.name + " ||$" + str(storage_4.price) + " ||⭑ " + str(storage_4.rating)
                    storage_5_str = storage_5.name + " ||$" + str(storage_5.price) + " ||⭑ " + str(storage_5.rating)
                    storage_6_str = storage_6.name + " ||$" + str(storage_6.price) + " ||⭑ " + str(storage_6.rating)
                    storage_7_str = storage_7.name + " ||$" + str(storage_7.price) + " ||⭑ " + str(storage_7.rating)
                    storage_8_str = storage_8.name + " ||$" + str(storage_8.price) + " ||⭑ " + str(storage_8.rating)
                    storage_9_str = storage_9.name + " ||$" + str(storage_9.price) + " ||⭑ " + str(storage_9.rating)
                    storage_10_str = storage_10.name + " ||$" + str(storage_10.price) + " ||⭑ " + str(storage_10.rating)

                    global storage_price

                    if storage_select == storage_1_str:
                        storage_price = 684
                    if storage_select == storage_2_str:                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                        storage_price = 239
                    if storage_select == storage_3_str:
                        storage_price = 203
                    if storage_select == storage_4_str:
                        storage_price = 136
                    if storage_select == storage_5_str:
                        storage_price = 218
                    if storage_select == storage_6_str:
                        storage_price = 340
                    if storage_select == storage_7_str:
                        storage_price = 265
                    if storage_select == storage_8_str:
                        storage_price = 185
                    if storage_select == storage_9_str:
                        storage_price = 300
                    if storage_select == storage_10_str:
                        storage_price = 1

                storageVariable.trace("w", callback)

                next_part_cooling = Button(window,
                                           text="✓",
                                           command=destroy_storage)

                next_part_cooling.pack()

            def cooling():

                def destroy_cooling():
                    previous_part_cooling.destroy()
                    cooling_label.destroy()
                    cooling_opt.destroy()
                    next_part_power.destroy()
                    cooling_info.destroy()
                    selectcooling_label.destroy()
                    power()

                def destroy_cooling_2():
                    previous_part_cooling.destroy()
                    selectcooling_label.destroy()                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    cooling_label.destroy()
                    cooling_info.destroy()
                    cooling_opt.destroy()
                    next_part_cooling.destroy()
                    storage_selected_label.destroy()
                    storage()

                cooling_info = Label(info_frame,
                                 text="Cooling in computers \nis essential, without it \nyour computer parts would \nbe severely damaged \nafter intensive use \nand can even cause you \nharm and hazard. Cooling is \nintended to remove waste \nheat created by parts and \nkeep said parts within a\n temperature range\n where they can \nwork to their best ability. \nThe most common way of cooling \nis by using fans and heat sinks \nto work with the airflow \nhowever you can also cool a pc \nwith water and\n other liquids.",
                                 bg="black",
                                 fg="white",
                                 font="Krungthep 24")

                cooling_info.pack(anchor="nw")

                previous_part_cooling = Button(window,
                                           text="▲",
                                           command=destroy_cooling_2)

                previous_part_cooling.pack()

                cooling_label = Label(window,
                                      text="<- Selecting Part: Cooling",
                                      bg="black",
                                      fg="white",
                                      font="Krungthep 37")

                cooling_label.pack()
                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                coolingList = [
                    cooling_1.name + " ||$" + str(cooling_1.price) + " ||⭑ " + str(cooling_1.rating),
                    cooling_2.name + " ||$" + str(cooling_2.price) + " ||⭑ " + str(cooling_2.rating),
                    cooling_3.name + " ||$" + str(cooling_3.price) + " ||⭑ " + str(cooling_3.rating),
                    cooling_4.name + " ||$" + str(cooling_4.price) + " ||⭑ " + str(cooling_4.rating),
                    cooling_5.name + " ||$" + str(cooling_5.price) + " ||⭑ " + str(cooling_5.rating),
                    cooling_6.name + " ||$" + str(cooling_6.price) + " ||⭑ " + str(cooling_6.rating),
                    cooling_7.name + " ||$" + str(cooling_7.price) + " ||⭑ " + str(cooling_7.rating),
                    cooling_8.name + " ||$" + str(cooling_8.price) + " ||⭑ " + str(cooling_8.rating),
                    cooling_9.name + " ||$" + str(cooling_9.price) + " ||⭑ " + str(cooling_9.rating),
                    cooling_10.name + " ||$" + str(cooling_10.price) + " ||⭑ " + str(cooling_10.rating),
                ]
                global coolingVariable
                coolingVariable = StringVar(window)
                coolingVariable.set(coolingList[0])

                cooling_opt = OptionMenu(window, coolingVariable, *coolingList)
                cooling_opt.config(font="Krungthep")

                cooling_opt.pack(side="top")

                selectcooling_label = Label(text="",
                                            bg="black",
                                            fg="white")

                selectcooling_label.pack(side="top")

                global cooling_selected_label

                cooling_selected_label = Label(window,
                                               text="",
                                               bg="black",
                                               fg="white",
                                               font="Krungthep 25")

                cooling_selected_label.pack(side=TOP, anchor="nw")

                def callback(*args):
                    selectcooling_label.configure(text="Cooling Selected: {}".format(coolingVariable.get()))
                    cooling_selected_label.configure(text="Cooling: {}".format(coolingVariable.get()))
                    cooling_select = coolingVariable.get()

                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE                    cooling_1_str = cooling_1.name + " ||$" + str(cooling_1.price) + " ||⭑ " + str(cooling_1.rating)
                    cooling_2_str = cooling_2.name + " ||$" + str(cooling_2.price) + " ||⭑ " + str(cooling_2.rating)
                    cooling_3_str = cooling_3.name + " ||$" + str(cooling_3.price) + " ||⭑ " + str(cooling_3.rating)
                    cooling_4_str = cooling_4.name + " ||$" + str(cooling_4.price) + " ||⭑ " + str(cooling_4.rating)
                    cooling_5_str = cooling_5.name + " ||$" + str(cooling_5.price) + " ||⭑ " + str(cooling_5.rating)
                    cooling_6_str = cooling_6.name + " ||$" + str(cooling_6.price) + " ||⭑ " + str(cooling_6.rating)
                    cooling_7_str = cooling_7.name + " ||$" + str(cooling_7.price) + " ||⭑ " + str(cooling_7.rating)
                    cooling_8_str = cooling_8.name + " ||$" + str(cooling_8.price) + " ||⭑ " + str(cooling_8.rating)
                    cooling_9_str = cooling_9.name + " ||$" + str(cooling_9.price) + " ||⭑ " + str(cooling_9.rating)
                    cooling_10_str = cooling_10.name + " ||$" + str(cooling_10.price) + " ||⭑ " + str(cooling_10.rating)

                    global cooling_price

                    if cooling_select == cooling_1_str:
                        cooling_price = 40
                    if cooling_select == cooling_2_str:
                        cooling_price = 80
                    if cooling_select == cooling_3_str:
                        cooling_price = 65
                    if cooling_select == cooling_4_str:
                        cooling_price = 85
                    if cooling_select == cooling_5_str:
                        cooling_price = 45
                    if cooling_select == cooling_6_str:
                        cooling_price = 190
                    if cooling_select == cooling_7_str:
                        cooling_price = 260
                    if cooling_select == cooling_8_str:
                        cooling_price = 219
                    if cooling_select == cooling_9_str:                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                        cooling_price = 145
                    if cooling_select == cooling_10_str:
                        cooling_price = 1

                coolingVariable.trace("w", callback)

                next_part_power = Button(window,
                                         text="✓",
                                         command=destroy_cooling)

                next_part_power.pack()

            def power():

                def destroy_power():
                    previous_part_power.destroy()
                    power_label.destroy()
                    power_opt.destroy()
                    next_part_finish.destroy()
                    power_info.destroy()
                    selectpower_label.destroy()
                    finish()

                def destroy_power_2():
                    selectpower_label.destroy()
                    power_label.destroy()
                    power_opt.destroy()
                    selectpower_label.destroy()
                    cooling_selected_label.destroy()
                    power_info.destroy()
                    cooling()

                power_info = Label(info_frame,
                                 text="A power supply unit, or\n PSU feeds electricity to a \ncomputer and its parts. \npower supplys \nchange alternating\n current from a wall socket \nof mains electricity\n to low-voltage direct \ncurrent to operate the \nprocessor and peripheral \ndevices. Power supplys \nare important as obviously its \nneeded to power on \nthe computer, but maintain \nthe on state and give use to \nthe other components.",
                                 bg="black",
                                 fg="white",
                                 font="Krungthep 24")                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE

                power_info.pack(anchor="nw")

                previous_part_power = Button(window,
                                           text="▲",
                                           command=destroy_power_2)

                previous_part_power.pack()

                power_label = Label(window,
                                    text="<- Selecting Part: Power",
                                    bg="black",
                                    fg="white",
                                    font="Krungthep 37")

                power_label.pack()

                powerList = [
                    power_1.name + " ||$" + str(power_1.price) + " ||⭑ " + str(power_1.rating),
                    power_2.name + " ||$" + str(power_2.price) + " ||⭑ " + str(power_2.rating),
                    power_3.name + " ||$" + str(power_3.price) + " ||⭑ " + str(power_3.rating),
                    power_4.name + " ||$" + str(power_4.price) + " ||⭑ " + str(power_4.rating),                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    power_5.name + " ||$" + str(power_5.price) + " ||⭑ " + str(power_5.rating),
                    power_6.name + " ||$" + str(power_6.price) + " ||⭑ " + str(power_6.rating),
                    power_7.name + " ||$" + str(power_7.price) + " ||⭑ " + str(power_7.rating),
                    power_8.name + " ||$" + str(power_8.price) + " ||⭑ " + str(power_8.rating),
                    power_9.name + " ||$" + str(power_9.price) + " ||⭑ " + str(power_9.rating),
                    power_10.name + " ||$" + str(power_10.price) + " ||⭑ " + str(power_10.rating),
                ]
                global powerVariable
                powerVariable = StringVar(window)
                powerVariable.set(powerList[0])

                power_opt = OptionMenu(window, powerVariable, *powerList)
                power_opt.config(font="Krungthep")

                power_opt.pack(side="top")

                selectpower_label = Label(text="",
                                          bg="black",
                                          fg="white")

                selectpower_label.pack(side="top")

                global power_selected_label

                power_selected_label = Label(window,
                                             text="",
                                             bg="black",
                                             fg="white",
                                             font="Krungthep 25")                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE

                power_selected_label.pack(side=TOP, anchor="nw")

                def callback(*args):
                    selectpower_label.configure(text="Power Selected: {}".format(powerVariable.get()))
                    power_selected_label.configure(text="Power: {}".format(powerVariable.get()))
                    power_select = powerVariable.get()

                    power_1_str = power_1.name + " ||$" + str(power_1.price) + " ||⭑ " + str(power_1.rating)
                    power_2_str = power_2.name + " ||$" + str(power_2.price) + " ||⭑ " + str(power_2.rating)
                    power_3_str = power_3.name + " ||$" + str(power_3.price) + " ||⭑ " + str(power_3.rating)
                    power_4_str = power_4.name + " ||$" + str(power_4.price) + " ||⭑ " + str(power_4.rating)
                    power_5_str = power_5.name + " ||$" + str(power_5.price) + " ||⭑ " + str(power_5.rating)
                    power_6_str = power_6.name + " ||$" + str(power_6.price) + " ||⭑ " + str(power_6.rating)                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                    power_7_str = power_7.name + " ||$" + str(power_7.price) + " ||⭑ " + str(power_7.rating)
                    power_8_str = power_8.name + " ||$" + str(power_8.price) + " ||⭑ " + str(power_8.rating)
                    power_9_str = power_9.name + " ||$" + str(power_9.price) + " ||⭑ " + str(power_9.rating)
                    power_10_str = power_10.name + " ||$" + str(power_10.price) + " ||⭑ " + str(power_10.rating)

                    global power_price

                    if power_select == power_1_str:
                        power_price = 115
                    if power_select == power_2_str:
                        power_price = 275
                    if power_select == power_3_str:
                        power_price = 315
                    if power_select == power_4_str:
                        power_price = 140
                    if power_select == power_5_str:
                        power_price = 95
                    if power_select == power_6_str:
                        power_price = 185
                    if power_select == power_7_str:                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                        power_price = 210
                    if power_select == power_8_str:
                        power_price = 335
                    if power_select == power_9_str:
                        power_price = 315
                    if power_select == power_10_str:
                        power_price = 3

                powerVariable.trace("w", callback)

                next_part_finish = Button(window,                                          # ALL PARTS ARE REPEATED WITH MINIMAL CHANGE
                                          text="✓",
                                          command=destroy_power)

                next_part_finish.pack()

            def finish(): # Function after final selection
                pc_price = case_price+motherboard_price+cpu_price+gpu_price+ram_price+storage_price+power_price+cooling_price # Calculating total cost of all parts and turning that into 1 variable

                pc_spacer = Label(window,
                                 text="",
                                 bg="black",
                                 fg="black",
                                 font="Krungthep 37")

                pc_spacer.pack(side="top")

                pc_cost = Label(window,
                                  text="PC Price: $" + str(pc_price),
                                  bg="black",                                                   # UI Stuff
                                  fg="white",
                                  font="Krungthep 37")

                pc_cost.pack(side="top", anchor="w")

                pc_name_again = Label(window,
                                text="Build Name: " + user_name + "'s PC",
                                bg="black",
                                fg="white",
                                font="Krungthep 37")

                pc_name_again.pack(side="top", anchor="w")

                pc_rating = Label(window,
                                      text="PC Rating (0/10): " + str(random.randint(0,10)) + " (Sometimes inaccurate)",
                                      bg="black",
                                      fg="white",
                                      font="Krungthep 37")

                pc_rating.pack(side="top", anchor="w")

                pc_image = PhotoImage(file="img/pc.png")        # Adding an image

                pc_image_label = Label(window,
                                             image=pc_image)


                pc_image_label.image = (pc_image)

                pc_image_label.place(relx=0.78,
                                     rely=0.5,
                                     anchor="center")
                if case_price == 1:
                    pc_image_label.destroy()
                    box_image = PhotoImage(file="img/box.png")        # If case selected was cardboard box, display a different image

                    box_image_label = Label(window,
                                           image=box_image)

                    box_image_label.image = (box_image)

                    box_image_label.place(relx=0.78,
                                         rely=0.5,
                                         anchor="center")


                def quit():
                    window.quit()

                quit = Button(window,
                                          text="Finish.",
                                          command=quit)        # Quit Button

                quit.place(relx=0.1,
                        rely=0.9,
                        anchor="center")

                def open_paste():
                    webbrowser.open('https://pastebin.com/fvRCQwR9)
                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')            # Get Code Button, opens pastebin link aswell as rickrock lol

                get_code = Button(window,
                              text="Get the code!",
                              command=open_paste)

                get_code.place(relx=0.2,
                        rely=0.9,
                        anchor="center")

        case()
        
def main():
    screen_width = str(window.winfo_screenwidth())
    screen_height = str(window.winfo_screenheight())
    window.geometry(screen_width + "x" + screen_height)         # Main function settings the window geometry to match moniter resolution, settings bg to black and disabling resizing.
    window.resizable(0, 0)
    window.configure(bg='black')
    window.mainloop()

if __name__ == '__main__': # Start.
    main()

