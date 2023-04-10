#import time module
import time
#input time in seconds
seconds=input("Enter the timing in number of seconds: ")


def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer,end='\r')
        time.sleep(1)
        seconds-=1
    print("timeup")

#function call
countdown_timer(int(seconds))
