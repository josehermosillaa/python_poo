from abc import ABC, abstractmethod


class SolicitudCredito(ABC):

    @abstractmethod
    def validar_monto(self, monto: str):
        pass

    @abstractmethod
    def validar_correo(self, correo: str):
        pass


class SolicitudCreditoDeConsumo(SolicitudCredito):

    def __init__(self, monto: int, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__coreo = self.validar_correo(correo)

    __terminaciones = (".cl", ".com")

    @property
    def monto(self):
        pass

    @monto.setter
    def monto(self, monto: int):
        pass

    @property
    def correo(self):
        pass

    @correo.setter
    def correo(self, monto: int):
        pass

    def validar_monto(self, monto: int):
        if monto < 1000000:
            monto = 1000000
        elif monto > 5000000:
            monto = 5000000

        return monto

    def validar_correo(self, correo: str):
        valido = (
            correo
            if correo.count("@") == 1
            and correo.endswith(SolicitudCreditoDeConsumo.__terminaciones)
            else ""
        )

        return valido[0]
