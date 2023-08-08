from flask import Flask
from flask_restful import Api
from app.adapters.controllers.personal_data_controller import (
    PersonalDataController,
    PersonalDataListController,
)
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('api.log'), # Salvar logs em um arquivo
        logging.StreamHandler() # Mostrar logs no console
    ]
)


app = Flask(__name__)
api = Api(app)

api.add_resource(PersonalDataController, '/personal-data/<int:id>')
api.add_resource(PersonalDataListController, '/personal-data')

if __name__ == '__main__':
    app.run(debug=True)
