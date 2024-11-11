import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Reading and printing complete CSV File Cars , complete information about cars")
df=pd.read_csv("cars.csv",sep=';')
df=df[1:]
print(df)
convert_dict = {'MPG':float,'Cylinders':int,'Displacement':float,'Horsepower':float,
                'Weight':float,'Acceleration':float,'Model':int
                } 
df = df.astype(convert_dict) 
print(df.dtypes) 
while True:
    print("**********************************************************************")
    print("Welcome to Car Analysis project")
    print("\t\tSubmitted by Arjun Dahiya")
    print("**********************************************************************")
    print('''1. Print all the Atributes of dataframe
            \n2. Print top records
            \n 3. Print the bottom records
           \n4.  Country name for which you want to display the Cars Names
           \n5. The number of Cylinders
           \n6. Horsepower
           \n7. Car name for which you want to display the inofrmation
           \n8. Model Number'
           \n9. Graphs\n''')
    
    m=int(input("Enter you choice"))
    if m==1:
        print("Information about DataFrame")
        print("Priting all the indexes\n",df.index)
        print("Priiting all the columns\n",df.columns)
        print("Printing all the Datatypes\n",df.dtypes)
        print("Values\n",df.values)
        print("Shape of the Dataframe\n",df.shape)
        print("Size of the Dataframe\n",df.size)
        print("Transpose of the DataFrame\n",df.T)
    elif m==2:
        n=int(input("Enter the top record which you want to display"))
        print(df.head(n))
    elif m==3:
        n=int(input("Enter the bottom record which you want to display"))
        print(df.tail(n))
    elif m==4:
        org=input("Enter the Country name for which you want to display the Cars Names")
        print(df[df.Origin==org])
    elif m==5:
        cyl=int(input("Enter the number of Cylinders"))
        print(df.Car[df.Cylinders>=cyl])
    elif m==6:
        h=int(input("Enter the horespower"))
        print(df.Car[df.Horsepower>=h])

    elif m==7:
        carname=input("Enter the car name for which you want to display the inofrmation")
        newdf=df[df.Car==carname]
        print("Inofrmation about ",carname)
        for i, j in newdf.iterrows(): 
            print(i, j) 
            print() 
    elif m==8:
        model=int(input("Enter the Model Number"))
        print(df[df.Model>=model])

    elif m==9:
        print('''\n1. Histigram for all numeric values
              \n2. Line Graph
              \n3. Bar Graph of Car and Horsepower
              \n4 Bar Graph Car', 'MPG', 'Cylinders', 'Displacement', 'Horsepower' \n''')
        g=int(input("Enter you choice"))
        if g==1:
            df.hist()
            plt.show()
        elif g==2:
            print("Line graph of top 10 records")
            dfLine=df.head(10)
            dfLine=dfLine[['MPG', 'Cylinders', 'Displacement']]
            dfLine.plot()
            plt.show()
        elif g==3:
            g1=df[['Car','Horsepower']].head(10)
            g1.plot(kind='bar')
            plt.show()
        elif g==4:
            Dfbar=df[['Car', 'MPG', 'Cylinders', 'Displacement', 'Horsepower']]
            
            np=Dfbar[Dfbar['MPG']>43]
      
            np.plot(kind='bar',x='Car',title='Car Details',color=['yellow','Red'],edgecolor='Green',linewidth=2,linestyle='--')
            
            print(np.Car)
            plt.xticks(rotation=90)
            plt.ylabel('Cars')
            plt.show()
        
    ch=input("Wish to continue y\n")
    if ch=='n' or ch=='N':
        break
