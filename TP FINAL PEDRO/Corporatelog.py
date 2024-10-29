import uuid  # Importar el módulo uuid
from Corporatedata import CorporateData
from Corporatelog import CorporateLog
import pprint

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    corporate_data = CorporateData()
    corporate_log = CorporateLog()

    uuid_session = str(uuid.uuid4())
    id_sede = 1

    data = corporate_data.getData(uuid_session, id_sede)
    print("Datos de la sede:")
    pp.pprint(data)

    cuit = corporate_data.getCUIT(uuid_session, id_sede)
    print("CUIT de la sede:")
    pp.pprint(cuit)

    seq_id = corporate_data.getSeqID(uuid_session, id_sede)
    print("ID de secuencia de la sede:")
    pp.pprint(seq_id)

    corporate_log.post(uuid_session, "getData")
    corporate_log.post(uuid_session, "getCUIT")
    corporate_log.post(uuid_session, "getSeqID")

    log_list = corporate_log.list(corporate_log.uuidCPU)
    print("Lista de logs:")
    pp.pprint(log_list)
