from llms.factory import LLMFactory


llm = LLMFactory.get_llm()

response = llm.invoke(
    "give me the financial overview of apple in year 2025?"
)

print(response.content)