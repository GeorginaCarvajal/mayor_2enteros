# programa para verificar cual de dos numeros enteros  es el mayor
print("--------------------------")
print("-----MAYOR 2 ENTEROS------")
print("--------------------------")


# input
x= int(input("dijite el valor de x: "))


y= int(input("dijite el valor de y: "))
#processing
#output
if x == y:
    
    print("los numeros son iguales...")
elif x > y: 
    print("el mayor entre" , str(x) , " y " , str(y) , " es " , str(x))
else:
    print("el mayor entre" , str(x) , " y " , str(y) , " es " , str(y))

