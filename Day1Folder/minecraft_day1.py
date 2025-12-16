# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################

def addition(num1, num2):
    print(num1 * num2)

addition(32, 41)

#division
#multiplication
#subtraction

def teleport():
    agent.teleport_to_player()
player.on_chat("come", teleport)

#tl : turn left
def tl():
    agent.turn(TurnDirection.LEFT)
player.on_chat("tl", tl)
################## On Chat Commands Section #####################
