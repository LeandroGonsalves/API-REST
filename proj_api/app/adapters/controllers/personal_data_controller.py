from flask_restful import Resource, reqparse
from ...application.services.personal_data_service import PersonalDataService
import logging

personal_data_service = PersonalDataService()

class PersonalDataController(Resource):
    def get(self, id):
        # Implementar busca por ID
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('nome', type=str)
            parser.add_argument('sobrenome', type=str)
            parser.add_argument('idade', type=int)
            parser.add_argument('pais', type=str)
            args = parser.parse_args()

            logging.info(f"Recebida requisição de criação de novo dado pessoal: {args}")

            # ... resto do código para criar o dado pessoal ...

            logging.info("Dado pessoal criado com sucesso.")

            return {"message": "Dado pessoal criado com sucesso."}, 201
        except Exception as e:
            logging.error(f"Erro ao criar dado pessoal: {e}")
            return {"message": "Erro ao criar dado pessoal."}, 500

    def patch(self, id):
        # Implementar atualização de dados por ID
        pass

    def delete(self, id):
        # Implementar exclusão de dados por ID
        pass

class PersonalDataListController(Resource):
    def get(self):
        # Implementar listagem de todos os dados
        pass

    def post(self):
        # Implementar criação de novos dados
        pass
