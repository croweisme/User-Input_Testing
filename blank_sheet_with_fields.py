import pandas as pd
writer = pd.ExcelWriter('demowithfields.xlsx',engine='xlsxwriter')
writer.save()
blankdf = pd.read_excel('demowithfields.xlsx')
blankdf =pd.DataFrame({'Name':[],'Age':[],'Weight':[]})
blankdf.to_excel('demowithfields.xlsx', index=False)

#For some reason this didnt work, it created a new frame with columns named correctly, but it created an empty column at the far left for some reason thats called 'unnnamed'
#im going to follow the tutorial exactly and see if that solves the problem
#setting index to False solved the problem for some reason. but hey, it worked. the excel file is now prepped for things to be put into it 
