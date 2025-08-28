from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from decouple import config

key= config("GEMINI_API_KEY")
base_url = config("GEMINI_BASE_URL")

#provider
GEMINI_CLIENT = AsyncOpenAI(
    api_key=key,
    base_url=base_url
)

#model
GEMINI_MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=GEMINI_CLIENT
)
