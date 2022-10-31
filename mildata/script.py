from multiprocessing import connection
from handler import Engine, Beneficiarios
server = 'srv-sql-med-interop.database.windows.net'
database = 'med-dw-interop'
username = 'az-dw-user'
password = 'ZhBgmV*$Ts2r!cNX'
datalake = Engine(server=server, database=database, username=username, password=password)
connection = Engine.connect(datalake)