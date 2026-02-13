from google import genai

class models:
    def __init__(self, key):
        self.client = genai.Client(api_key=key)

    def ask(self, system_instruction, prompt):
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                config=genai.types.GenerateContentConfig(
                    system_instruction=system_instruction
                ),
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"خطا در ارتباط با مدل: {e}"
