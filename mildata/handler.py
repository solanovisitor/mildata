# A collection of functions to interact with our SQL Server

import pyodbc
import pandas as pd
import numpy as np
import os
import sys
import datetime
import time

# A class to pull data from our clients SQL Server
class Pull():
    # Initialize the class
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.cnxn.cursor()

# An inherited class from Pull to filter data from our clients SQL Server
class Beneficiarios(Pull):
    # Initialize the class
    def __init__(self, server, database, username, password):
        super().__init__(server, database, username, password)

    # Filter data from the SQL Server
    def filter(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

