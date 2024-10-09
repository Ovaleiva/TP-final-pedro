class CorporateData:
    _instance = None
    sequence_id = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CorporateData, cls).__new__(cls)
            cls._init_data()
        return cls._instance

    @classmethod
    def _init_data(cls):
        cls.address = "Urquiza 1115"
        cls.cuit = "20-43482331-7"
        cls.phone_number = "+54 3442 304271"

    def getData(self, uuid, sede):
        # Simulamos obtener datos de la sede
        return {"sede": sede, "Domicilio": self.address, "Localidad": "Concepcion del Uruguay", "Cp": "3260", "provincia": "Entre Ríos"}

    def getCUIT(self, uuid, sede):
        # Retornamos el CUIT
        return {"sede": sede, "CUIT": self.cuit}

    def getSeqID(self, uuid, sede):
        # Incrementamos y devolvemos el identificador de secuencia
        self.sequence_id += 1
        return {"sede": sede, "seqID": self.sequence_id}
