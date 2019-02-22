import RPi.GPIO as G
import time

G.setmode(G.BOARD)
G.setup(7, G.out)

while True:
    G.output(7, True)
    time.sleep(1)
    G.output(7, False)
    time.sleep(1)