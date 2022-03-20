# Author: Harsh Master
'''
Prank your friends by unusual continuous rotation of screen.
'''

# Importing Dependencies
import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation

consent = input("Don't press 'y' and 'enter' key: ")
if consent == 'y':
    print("************ 🎉🎉 Ready for some action !!! 🎉🎉 ************")
    time.sleep(2)

    print("5...")
    # For God's sake dont delete this statement else you'll need to say Goodbye to the system.
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

else:
    counter = 0
    while True:
        if counter >= 5:
            if counter == 5:
                print("__________ Hey idiot, don't you understand? 👿 👿_________")
            elif counter > 5:
                consent = input("Press 'y' and 'enter' key: ")
                if counter >= 10:
                    print("__________ Beta tumse naa ho payega, rehne do!!! __________")
                    print("************ 😈😈 Punishment time !!! 😈😈 ************")
                    time.sleep(2)
                    print("5...")
                    time.sleep(1)
                    print("4...")
                    time.sleep(1)
                    print("3...")
                    time.sleep(1)
                    print("2...")
                    time.sleep(1)
                    print("1...")
                    time.sleep(1)
                    break
        else:
            consent = input("Don't press 'y' and 'enter' key: ")

        if consent == 'y':
            break
        else:
            pass
            counter = counter + 1


while True:
    try:
        for i in range(1, 5):
            pos = abs((start_pos - i*90) % 360)  # getting screen position
            screen.rotate_to(pos)
            time.sleep(1.5)
    except KeyboardInterrupt:
        screen.rotate_to(start_pos)
        break
