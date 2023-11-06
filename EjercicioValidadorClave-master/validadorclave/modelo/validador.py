from abc import ABC, abstractmethod
from modelo.errores import *

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        if len(clave) < self._longitud_esperada:
            raise NoCumpleLongitudMinimaError(f"La clave debe tener al menos {self._longitud_esperada} caracteres")

    def _contiene_mayuscula(self, clave):
        if not any(char.isupper() for char in clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(char.islower() for char in clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(char.isdigit() for char in clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")

class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave):
        if not any(char in "@_#$%" for char in clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos uno de los caracteres especiales @ _ # $ %")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        if clave.find("calisto") == -1 or clave.find("calisto").islower() or clave.find("calisto").isupper():
            raise NoTienePalabraSecretaError("La clave debe contener 'calisto' con al menos dos letras mayúsculas pero no todas en mayúsculas")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
