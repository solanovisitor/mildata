from handler import Engine, Beneficiarios

datalake = Engine(server=server, database=database, username=username, password=password)
connection = Engine.connect(datalake)
sample = Beneficiarios(connection=connection, regional='ES', email='True', celular='True', n='1000')

df = Beneficiarios.pull(sample)
print(df.head)