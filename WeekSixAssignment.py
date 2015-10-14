__author__ = 'trevorbillwaite'

# WeekSixAssignment.py
# Introduction to Computer Science



# A function definition for the following functions: populate, display, generation
# Each function should have the following parameters: (world,h,w)
def populate(world,h,w):
    pass
def display(world,h,w):
    pass
def generation(world,h,w):
    pass
    
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
       # prompts the user to enter a key
       initialPrompt = input('Please insert any key (enter "q" to quit): ')
    
# Run main
main()


    
    
    