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
        self.engine = create_engine(connection_url)

# An inherited class from Pull to filter data from our clients SQL Server
class Beneficiarios(CreateEngine):
    self.query = "SELECT * FROM dw.Beneficiarios"
    # Initialize the class
    def __init__(self, server, database, username, password):
        super().__init__(server, database, username, password)

    # Filter data from the SQL Server
    def get_benefs(self):
        self.benef = pd.read_sql_query('''SELECT * FROM [blkch].[aux_blkch_beneficiarios]''', self.engine)
        return self.benef

