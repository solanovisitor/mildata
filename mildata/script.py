from handler import Engine, Beneficiarios
import yaml


def load_credentials(path):
    with open(path, 'r') as stream:
        try:
            parsed_creds=yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return parsed_creds

datalake = Engine(server=parsed_creds['server'], database=parsed_creds['database'], username=parsed_creds['username'], password=parsed_creds['password'])
connection = Engine.connect(datalake)
sample = Beneficiarios(connection=connection, regional='ES', email='True', celular='True', n='1000')

df = Beneficiarios.pull(sample)
print(df.head)