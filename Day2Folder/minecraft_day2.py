# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def chop():
    for count in range(20):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.teleport_to_player()
    
player.on_chat("chop", chop)