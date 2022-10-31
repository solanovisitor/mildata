from handler import Engine, Beneficiarios

path_to_credentials = '/home/dsazureuser/mildata/mildata/credentials/creds.yaml'
parsed_creds = Engine.load_credentials(path_to_credentials)
datalake = Engine(server=parsed_creds['server'], database=parsed_creds['database'], username=parsed_creds['username'], password=parsed_creds['password'])
connection = Engine.connect(datalake)
sample = Beneficiarios(connection=connection, regional='ES', email='True', celular='True', n='1000')

df = Beneficiarios.pull(sample)
print(df.head)