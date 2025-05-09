from agents import Agent, Runner, set_default_openai_key
import asyncio

OPENAI_API_KEY="your_open_ai_key"


from agents import Agent, Runner, set_default_openai_key

#set_default_openai_key("your-api-key-here")
set_default_openai_key(OPENAI_API_KEY)


french_agent = Agent(
    name="French agent",
    instructions="You only speak French.",
)

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[french_agent, spanish_agent, english_agent],
)


async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)
    # ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?


if __name__ == "__main__":
    asyncio.run(main())