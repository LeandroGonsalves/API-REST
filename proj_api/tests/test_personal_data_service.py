from app.application.services.personal_data_service import PersonalDataService

def test_create_personal_data():
    service = PersonalDataService()
    data = service.create_personal_data("João", "Silva", 30, "Brasil")
    assert data.nome == "João"
    assert data.sobrenome == "Silva"
    assert data.idade == 30
    assert data.pais == "Brasil"