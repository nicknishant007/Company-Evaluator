from abc import ABC
from abc import abstractmethod

from pathlib import Path


class BaseAgent(ABC):

    # Every child overrides this
    prompt_file = ""

    def __init__(
        self,
        llm,
    ):

        self.llm = llm

        if self.prompt_file:

            prompt_path = (
                Path(__file__).parent
                / "prompts"
                / self.prompt_file
            )

            self.prompt = prompt_path.read_text(
                encoding="utf-8"
            )

        else:

            self.prompt = ""

    @abstractmethod
    def build_prompt(
        self,
        state: dict,
    ) -> str:
        pass


    async def run(
        self,
        state: dict,
    ):

        try:

            prompt = self.build_prompt(
                state
            )

            print("Prompt built")

            response = await self.llm.ainvoke(
                prompt
            )

            print("LLM finished")

            return response.content

        except Exception as e:

            print("\n====== AGENT ERROR ======")
            print(type(e))
            print(e)
            print("=========================\n")

            raise