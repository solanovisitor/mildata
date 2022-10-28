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
class Engine:
    # Initialize the class
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        self.connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": self.connection_string})

    def connect(self):
        self.engine = create_engine(self.connection_url)
        return self.engine

# A class to pull data from our clients SQL Server
class Beneficiarios:
    # Initialize the class
    def __init__(self, connection, regional, email, celular):
        self.connection = connection
        self.regional = regional
        self.email = email
        self.celular = celular
        self.query = "SELECT * FROM dbo.Beneficiarios WHERE Regional = '" + self.regional + "' AND Email = '" + self.email + "' AND Celular = '" + self.celular + "'"
        # Pulling data from query
        self.df = pd.read_sql(self.query, self.connection)

