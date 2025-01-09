def example(a, b=2, c=3): #Correct
    print(a,b,c)

def example2(a=1, b, c): #Incorrect - will raise a SyntaxError
    print(a,b,c)