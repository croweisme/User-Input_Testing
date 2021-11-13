#This program will take user input and add it as a new line in a pandas dataframe
import pandas as pd
    #For some reason I cant get Pandas to import
    #The internet says that i need to pip install pandas, so time to do that i guess

#CMD + Space = Open Spotlight search
#search for terminal
#pip has been installed

#SOLVED by going into view>Command Palette> Python: Select Interpreter > Python 3.8.8
    #I guess pandas and anaconda havent been updated to the latest version of python, so i'll have to manually switch the python version for all the files that arent made in jupyter notebooks

#Now i need to create an empty excel file that i can put data into 
#Should I put the columns into it manually or should I try and figure out how to create an excel file using the code?
#Gameplan:
#   Create Xlsx file using pandas (COMPLETE)
#   Load the new excel file (COMPLETE)
#   Figure out how to create completely empty columns and name them (COMPLETE)
#   Configure the new blank excel sheet to have the columns i need (COMPLETE)
#   Set up a simple way to take user input, and load it into a 1x3 dataframe that will be stitched onto the bottom of the excel file with fields
#   Either:
        #Use the user input to append the dataframe into the original
        #Or use the index method to add a new row (I guess i could try both)



#I have officially figured out how to create a new excel file using pandas. The new file is in the root folder
    #See: new_excel_sheet.py

#Time to load the new demo excel file

userframe = pd.read_excel('demo.xlsx') #it worked

#Now im going to try and make another blank dataframe that will be used for the user input

# inputframe_demo = pd.DataFrame({'Name':[],'Age':[],'Weight':[]})
# print(inputframe_demo)

#Awesome, so it seems like the software doesnt care that the values inside the dataframe are empty

#loading and printing the new DataFrame with fields that i just created using the other program 
fieldframe = pd.read_excel('demowithfields.xlsx')
# print(fieldframe)

#Now it's time to actually start taking user input

inputName = str(input("Enter Name:"))
inputAge = float(input("Enter Age:"))
inputWeight = float(input("Enter Weight (In Pounds):"))

#Turning the user input into a 3x1 Dataframe

inputframe = pd.DataFrame({'Name':[inputName],'Age':[inputAge],'Weight':[inputWeight]})
# print(inputframe)

#Slapping it onto the bottom of the excel sheet
#inputframe.to_excel(fieldframe, index=False,header=False,startrow=len(fieldframe)+1)           This didnt work, maybe I need to append it instead
fieldframe = fieldframe.append(inputframe,ignore_index=True)
print(fieldframe)
fieldframe.to_excel('demowithfields.xlsx',index=False)

