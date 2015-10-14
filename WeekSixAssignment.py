__author__ = 'trevorbillwaite'

# WeekSixAssignment.py
# Introduction to Computer Science
# Collaboration with Nicole Ignasiak, Josiah Hardacre, Nathan Pugh



# A function definition for the following functions: populate, display, generation
# Each function should have the following parameters: (world,h,w)

# funct populate will make the initial cell configuration
# this function will not return anything
def populate(world,h,w):
    pass
# funct display will simply display as an image the cell configuration of the populate function
# this function will not return anything
def display(world,h,w):
    pass
# funct generation is what is run after the user inputs any key other than "q", it moves the cell configuration along one generation
# this function will return a value
def generation(world,h,w):
    pass
    
# funct main is the function that puts all the other functions together and prepares the program to run and actually do something
def main ():
    import random
    # define intitial world, height, and weight
    world = [ ]
    # h = height
    h = 80
    # w = width
    w = 22
    # run populate and display functions
    populate(world,h,w)
    display(world,h,w)
    # Prompt user for an input
    initialPrompt = [ ]
    while initialPrompt != 'q':
       # Run the generation function, replacing the current world with the newly generated world
       generation(world,h,w)
       # display the new world
       display(world,h,w)
       # prompts the user to enter another key, causing the program to loop until "q" is entered
       initialPrompt = input('Please insert any key (enter "q" to quit): ')
    
# Run main
main()


    
    
    