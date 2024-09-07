from app.infra.services.for_devs.for_devs_service import ForDevsService


class DocumentUtil:
    def __init__(self) -> None:
        self.for_devs = ForDevsService()

    def validar_cpf(self, cpf: str) -> bool:
        res = self.for_devs.validar_cpf(cpf)

        texto_lower = res.lower()

        if 'verdadeiro' in texto_lower:
            return True
        if 'falso' in texto_lower:
            return False
