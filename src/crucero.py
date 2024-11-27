class Crucero:
    def __init__(self, **kwargs) -> None:
        self._id = kwargs["id"]
        self._nombre = kwargs["nombre"]
        self._capacidad = kwargs["capacidad"]
        self._empresa = kwargs["empresa"]
        self._pais_origen = kwargs["pais_origen"]

        return None

    def __str__(self) -> str:
        return "La empresa {} nos a facilitado el crucero con ID {} el cual es conocido como {} de origen {} con una capacidad de {} personas.".format(
            self._empresa, self._nombre, self._pais_origen, self._capacidad
        )
