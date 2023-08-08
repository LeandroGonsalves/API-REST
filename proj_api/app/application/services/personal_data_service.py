from ...domain.models import PersonalData

class PersonalDataService:
    def create_personal_data(self, nome, sobrenome, idade, pais):
        return PersonalData(nome, sobrenome, idade, pais)
