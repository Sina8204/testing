from google import genai

class models:
    def __init__(self, key):
        self.client = genai.Client(api_key=key)
        self.response_text = ""

    def send_requiest_to_model(self, instruction="", prompt=""):
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                config=genai.types.GenerateContentConfig(system_instruction=instruction),
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"
