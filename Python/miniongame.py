def minion_game(string):
    vowels="AEIOUaeiou"
    kevinScore=0
    stuartScore=0
    for i in range(len(string)):
        if string[i] in vowels:
            kevinScore += (len(string)-i)
        else:
            stuartScore += (len(string)-i)
        
    if kevinScore > stuartScore:
        print ("Kevin",kevinScore) 
    elif kevinScore < stuartScore:
        print ("Stuart",stuartScore)
    else:
        print ("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)