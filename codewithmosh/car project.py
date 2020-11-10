command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            print("the car is started")
            started = True
    elif command == "stop":
        if not started:
            print('the car is already stopped')
        else:
            print("the car is stopped")
            started = False
    elif command == "help":
        print("""
start - the car will start
stop - the car will stop
quit - exit
        """)
    elif command == "quit":
        break
    else:
        print("sorry i do not understand you")
