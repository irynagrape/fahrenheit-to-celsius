def convert(s):
    f = float(s)    
#formula Applied below  
    c = (f - 32) * 5/9
    return c
celsius=input("Enter Values in Fahrenheit : ")
convert(celsius)
