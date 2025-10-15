
#create a class called Datapipeline

class Datapipeline:
    def __init__(self, name, source, destination):
        self.name=name
        self.source=source
        self.destination=destination

    def extract(self):
        print(f"extracting the data from {self.source}")   

    def transform(self):
        print("Transforming the data")     

    def load(self):
        print(f"loading the data from {self.destination}")  

    def run(self):
        print(f"running the pipeline {self.name}")
        self.extract()
        self.transform()
        self.load() 

#create an object called pipiline

pipeline=Datapipeline("sales_data","csv files","database")
pipeline.run()