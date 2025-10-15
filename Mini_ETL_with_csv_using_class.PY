
import pandas as pd 

class Datapipeline:
    def __init__(self,name,source,destination):
        self.name=name
        self.source=source
        self.destination=destination
        self.data=None

    def extract(self):
        print(f"\n extracting data from {self.source}")  
        self.data=pd.read_csv(self.source)  
        print("Data extracted succesfully\n")
        print(self.data.head())

    def transformation(self):   
        print(f"tranformming the data \n")
        self.data[total]=self.data[price]*self.data[quantity]
        print(f"succesfully transformed the data \n")
        print(self.data.head())

    def loading(self):
        print(f"Loading the data to {self.destination}")
        self.data.to_csv(self.destination, index=false)  
        print(f"Data loaded succesfully \n") 

    def run(self):
        print(f"\n Running the pipeline {self.name}")
        self.extract() 
        self.transformation()
        self.loading()
        print(f"succesfully pipeline finished")

#create an object
pipeline=Datapipeline("Sales_ETL", "sales_data.csv", "transformed_sales.csv")    
pipeline.run()    


