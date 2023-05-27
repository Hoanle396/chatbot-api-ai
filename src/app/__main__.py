from app import app
import app.settings as settings
from controllers.route import registryRouter
from models.model import Chatbot

model = Chatbot()

if __name__ == "__main__":
    registryRouter(app, model)
    app.run(host=settings.BE_HOST, port=settings.BE_PORT, debug=settings.ENV != "PROD")
