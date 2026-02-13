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

    def generate_image(self, prompt: str):
        try:
            response = self.client.models.generate_image(
                model="imagen-3.0-generate-001",
                prompt=prompt
            )
    
            # Gemini returns base64 image data
            image_bytes = response.image.image_bytes
            return image_bytes
    
        except Exception as e:
            return f"Error generating image: {e}"
