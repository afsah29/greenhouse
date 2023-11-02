
#MCS 260 FALL 2021 PROJECT 4
#AFSAH AHMED
#I HAVE COMPLETED THIS PROJECT ON MY OWN


import pandas as pd

greenhouse = pd.read_csv("greenhouse.csv")

print(greenhouse)


def moniter(PH_of_Soil,Temperature,Water_pH,greenhouse):
    print("*********************************************")
    soil_lis=list(greenhouse.iloc[0])
    if soil_lis[1] > PH_of_Soil:
        print("\nTo increase the PH value of soil:")
        print(soil_lis[4])
        print("Causes:")
        print(soil_lis[5])
    elif soil_lis[2] < PH_of_Soil:
        print("\nTo reduce the PH value of soil:")
        print(soil_lis[3])
        print("Causes:")
        print(soil_lis[6])
    else:
        print("Ph value of the soil is good.")
    print("*********************************************")
    temp_lis=list(greenhouse.iloc[1])
    if temp_lis[1] > Temperature:
        print("\nTo increase the Temperature:")
        print(temp_lis[4])
        print("Causes:")
        print(temp_lis[5])
    elif temp_lis[2] < Temperature:
        print("\nTo reduce the Temperature:")
        print(temp_lis[3])
        print("Causes:")
        print(temp_lis[6])
    else:
        print("Temperature is good.")
    
    
    wsoil_lis=list(greenhouse.iloc[2])
    print("*********************************************")
    if wsoil_lis[1] > Water_pH:
        print("\nTo increase the PH value of water:")
        print(wsoil_lis[4])
        print("Causes:")
        print(wsoil_lis[5])
    elif wsoil_lis[2] < Water_pH:
        print("\nTo reduce the PH value of water:")
        print(wsoil_lis[3])
        print("Causes:")
        print(wsoil_lis[6])
    else:
        print("Ph value of the water is good.")
        
 
PH_of_Soil=float(input("Enter the PH of Soil:"))
Temperature=float(input("Enter the temperature:"))
Water_pH=float(input("Enter the PH of water:"))

moniter(PH_of_Soil,Temperature,Water_pH,greenhouse)


