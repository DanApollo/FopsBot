import vertexai
from vertexai.generative_models import GenerativeModel

class GeminiClient:

    model = GenerativeModel("gemini-1.5-flash-002")

    def __init__(self):
        pass

    def initialize(self, project_id):
        vertexai.init(project=project_id, location="europe-west2")

    def generate_response(self, data):
        with open("./gemini_cloud/prompt.txt", 'r') as file:
            prompt = file.read()
            return self.model.generate_content(
                f"{prompt}\n{data}"
            ).text

gemini_client = GeminiClient()