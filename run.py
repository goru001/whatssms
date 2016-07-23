from yowsup.stacks import  YowStackBuilder
from layer import EchoLayer
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env                                import YowsupEnv

fo = open("YOUR_PHONE_NUMBER.txt","r")
YOUR_PHONE_NUMBER = fo.read()
fo.close()

fo = open("PASSWORD.txt","r")
PASSWORD= fo.read()
fo.close()

credentials = (YOUR_PHONE_NUMBER, PASSWORD) # phone and password
#CREDENTIALS = DemosArgParser._getCredentials()

if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers(True)\
        .push(EchoLayer)\
        .build()

    stack.setCredentials(credentials)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    stack.loop() #this is the program mainloop
