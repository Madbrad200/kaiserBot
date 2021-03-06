'''
    Title: Basic IRC bot
    Last edit: 16:05 11/01/2016 (GMT -3)
    Version: 1.0

    Description:
        This is a raw irc input handle library. It's main purpose is to facaili-
        te the working with raw irc protocol. Most functions will take a text 
        variable that represents one like of full raw irc uotput. The normal
        format for this is the following:

        :<USERNAME>!<HOST>:<IP> <COMMAND>

    Functions:
        getCommand()
        getUserName()
        getChannel()
'''

#-------------------------------------------------------------------------------
#
#   Settings loader
#
#-------------------------------------------------------------------------------
#   Loads the settings from the settings.txt file
#-------------------------------------------------------------------------------

SettingsFile = open("settings.txt", 'r')
botnick = (SettingsFile.readline().split("|")[1])[:-1]
SettingsFile.close()

#-------------------------------------------------------------------------------
#
#   Loadable functions
#
#-------------------------------------------------------------------------------


def getCommand(text):
    '''
        Paramenters:
            text: String. Raw entry right out of the IRC protocol.

        Returns the command sent, which is the following:
            "!command <extra>"
    '''
    parts = text.split(":")
    return parts[len(parts)-1]

def getUserName(text):
    '''
        Paramenters:
            text: String of data, raw command that comes from irc.

        Returns:
            Username
    '''
    parts = text.split(":")
    print(parts)
    name = parts[1].split("!")[0]
    return name

def getChannel(text, botnick):
    '''
        Paramenters:
            text: String of data, raw command that comes from irc.

        Returns: "#<CHANNEL NAME>"
        If the channel the message is sent to is the name of the bot (AKA it is a PM)
        Then Returns: "<Username>" where <Username> is the username of the user
        who PMd the bot
    '''
    parts = text.split(":")
    if (parts[len(parts)-2]).split(" ")[2] == botnick.upper():
        return getUserName(text)
    else:
        return ((parts[len(parts)-2]).split(" ")[2])

