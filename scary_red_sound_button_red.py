from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.pixels.fill((50, 0, 0))
        cpx.play_file("Evil_Laugh.wav")
        
    if cpx.button_b:
        cpx.pixels.fill((50, 0, 0))
        cpx.play_file("exorcist2.wav")
        
