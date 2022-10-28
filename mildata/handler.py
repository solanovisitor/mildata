# A collection of functions to interact with our SQL Server

from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import os
import sys
import datetime
import time

# A class to pull data from our clients SQL Server
class CreateEngine:
    # Initialize the class
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        self.connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": self.connection_string})
        self.engine = create_engine(self.connection_url)

    # A function to pull data from our SQL Server
    def pull_data(self):
        self.df = pd.read_sql(self.query, self.engine)
        return self.df

# An inherited class from Pull to filter data from our clients SQL Server
class Beneficiarios(CreateEngine):
    # Initialize the class
    def __init__(self, server, database, username, password, regional, celular, email):
        super().__init__(server, database, username, password)
        self.query = "SELECT * FROM dw.Beneficiarios"
        self.regional = regional
        self.celular = celular
        self.email = email
        self.benef = CreateEngine.pull_data(self.query)

