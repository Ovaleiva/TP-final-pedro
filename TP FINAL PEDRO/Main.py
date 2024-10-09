from Corporatedata import CorporateData
from Corporatelog import CorporateLog

if __name__ == "__main__":
    # Inicializamos las clases
    corporate_data = CorporateData()
    corporate_log = CorporateLog()

    # Aplicación hace la petición de datos
    uuid = "12345"
    sede = "Sede Central"

    # Obtener datos
    data = corporate_data.getData(uuid, sede)
    corporate_log.post(uuid, "getData")
    print(data)

    # Obtener CUIT
    cuit = corporate_data.getCUIT(uuid, sede)
    corporate_log.post(uuid, "getCUIT")
    print(cuit)

    # Obtener sequence ID
    seq_id = corporate_data.getSeqID(uuid, sede)
    corporate_log.post(uuid, "getSeqID")
    print(seq_id)
