def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always

    print(events)
    while events:
        ev=events[0]
        
        if state == "CLOSED": #the only permitted options when closed.    
            if ev == "APP_PASSIVE_OPEN":
                state = "LISTEN"
            elif ev == "APP_ACTIVE_OPEN":
                state= "SYN_SENT"
            else:   #if it is not open then it is a error.
                state = "ERROR"
        
        elif state == "LISTEN":
            if ev == "RCV_SYN":
                state ="SYN_RCVD"
            elif ev == "APP_SEND":
                state = "SYN_SENT"
            elif ev == "APP_CLOSE":
                state = "CLOSED"
            else:   #if it is not one of those then it is a error
                state = "ERROR"

        elif state == "SYN_RCVD":
            if ev == "APP_CLOSE":
                state = "FIN_WAIT_1"
            elif ev == "RCV_ACK":
                state = "ESTABLISHED"
            else:   #if it is not one of those then it is a error
                state = "ERROR"

        elif state == "SYN_SENT":
            if ev == "RCV_SYN":
                state = "SYN_RCVD"
            elif ev == "RCV_SYN_ACK":
                state = "ESTABLISHED"
            elif ev == "APP_CLOSE":
                state = "CLOSED"
            else:   #if it is not one of those then it is a error
                state = "ERROR"

        elif state == "ESTABLISHED":
            if ev == "APP_CLOSE":
                state = "FIN_WAIT_1"
            elif ev == "RCV_FIN":
                state = "CLOSE_WAIT"
            else:   #same as before
                state = "ERROR"

        elif state == "FIN_WAIT_1":
            if ev == "RCV_FIN":
                state = "CLOSING"
            elif ev == "RCV_FIN_ACK":
                state = "TIME_WAIT"
            elif ev == "RCV_ACK":
                state = "FIN_WAIT_2"
            else: state = "ERROR"   #almost forgot

        elif state == "CLOSING":    #there is a shorter way to do this but its easier to understand to have it this way rather 
            if ev == "RCV_ACK":   state = "TIME_WAIT"  #than a longer and concatened condition      
            else: state = "ERROR"
        
        elif state == "FIN_WAIT_2": # same as before
            if ev == "RCV_FIN": state = "TIME_WAIT"         
            else: state = "ERROR"

        elif state == "TIME_WAIT":
            if ev == "APP_TIMEOUT": state = "CLOSED"
            else: state = "ERROR"    

        elif state == "CLOSE_WAIT":
            if ev == "APP_CLOSE": state = "LAST_ACK"
            else: state = "ERROR"
        
        elif state == "LAST_ACK":
            if ev == "RCV_ACK": state = "CLOSED"
            else: state = "ERROR"

        try:    #remove the first event of the array
            events.pop(0)
        except:
            pass

    return state