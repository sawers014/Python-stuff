def solution(args):
    string= ""
    lastN=args[0]

    for x in range(len(args) ):
        z=args[x] #better to put it in a local variable
        if x == 0:
            string+=str(z)
            continue
        else:       
            try:
                if lastN == z-1 and lastN == args[x+1]-2: # example -3,-2,-1
                    if string[len(string)-1] == ",": ##if we got a succesion we want to remove any possible "," at the start of a succesion
                        string = string[:-1]    
                    if string[len(string)-1] != "-": # we need to check if there is arleady an "-" in the middle of numbers
                        string+="-" 
                    
                elif x==1:  string+="," + str(z) + ","            
                elif x< len(args)-1: string+= str(z) + ","
                else: string+=str(z)    ##TODO find a way to optimize this ifs
            except:
                string+=str(z)
                pass
        lastN=args[x] #update the last Number
    return string

