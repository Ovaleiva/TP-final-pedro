import boto3
import uuid
import platform
from datetime import datetime


dynamodb = boto3.resource('dynamodb')

corporate_data_table = dynamodb.Table('CorporateData')
corporate_log_table = dynamodb.Table('CorporateLog')

uniqueID = str(uuid.uuid4())         
CPUid = str(uuid.getnode())       
sessionid = str(uuid.uuid4())      
timestamp = datetime.now().isoformat() 

domicilio = "1667 Don Bosco"
localidad = "Concepcion del Uruguay"
codigoPostal = "3260"
provincia = "Entre Ríos"
metodo = "POST"

data_response = corporate_data_table.put_item(
    Item={
        'sessionID': sessionid,
        'cpuID': CPUid,
        'id': uniqueID,
        'domicilio': domicilio,
        'localidad': localidad,
        'codigoPostal': codigoPostal,
        'provincia': provincia
    }
)

print("Registro en CorporateData:")
print(f"sessionID: {sessionid}, cpuID: {CPUid}, id: {uniqueID}, domicilio: {domicilio}, localidad: {localidad}, codigoPostal: {codigoPostal}, provincia: {provincia}")
print("Código de estado de la inserción en CorporateData:", data_response['ResponseMetadata']['HTTPStatusCode'])

log_response = corporate_log_table.put_item(
    Item={
        'id': uniqueID,       
        'sessionID': sessionid,
        'cpuID': CPUid,
        'timeStamp': timestamp,
        'metodo': metodo
    }
)

print("\nRegistro en CorporateLog:")
print(f"id: {uniqueID}, sessionID: {sessionid}, cpuID: {CPUid}, timeStamp: {timestamp}, metodo: {metodo}")
print("Código de estado de la inserción en CorporateLog:", log_response['ResponseMetadata']['HTTPStatusCode'])
