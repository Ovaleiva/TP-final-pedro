from singleton_meta import SingletonMeta

class CorporateData(metaclass=SingletonMeta):
    """Clase que maneja los datos corporativos con implementación Singleton."""
    
    def __init__(self):
        self.data = {
            'Domicilio': "Urquiza 1115",
            'Localidad': "Concepcion del Uruguay",
            'CodigoPostal': "3260",
            'Provincia': "Entre Ríos",
            'CUIT': "20-12345678-9",
            'idSeq': 1001 
        }

    def getData(self, uuid, id_sede):
        """Retorna los datos de una sede específica en formato diccionario."""
        if not uuid or not isinstance(uuid, str):
            raise ValueError("UUID no es válido o está ausente.")
        if not isinstance(id_sede, int) or id_sede <= 0:
            raise ValueError("El ID de la sede debe ser un número entero positivo.")
        
        return {
            'ID': id_sede,
            'Domicilio': self.data['Domicilio'],
            'Localidad': self.data['Localidad'],
            'CodigoPostal': self.data['CodigoPostal'],
            'Provincia': self.data['Provincia']
        }

    def getCUIT(self, uuid, id_sede):
        """Retorna el CUIT de una sede específica."""
        if not uuid or not isinstance(uuid, str):
            raise ValueError("UUID no es válido o está ausente.")
        if not isinstance(id_sede, int) or id_sede <= 0:
            raise ValueError("El ID de la sede debe ser un número entero positivo.")
        
        return {'idSede': id_sede, 'CUIT': self.data['CUIT']}

    def getSeqID(self, uuid, id_sede):
        """Incrementa y retorna el ID de secuencia para una sede específica."""
        if not uuid or not isinstance(uuid, str):
            raise ValueError("UUID no es válido o está ausente.")
        if not isinstance(id_sede, int) or id_sede <= 0:
            raise ValueError("El ID de la sede debe ser un número entero positivo.")
        
        self.data['idSeq'] += 1
        return {'idSede': id_sede, 'seqID': self.data['idSeq']}
