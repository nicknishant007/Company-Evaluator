from abc import ABC
from abc import abstractmethod

from pathlib import Path


class BaseAgent(ABC):

    # Every child overrides this
    prompt_file = ""

    # Optional structured output schema
    output_schema = None


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


            # Structured output agent
            if self.output_schema is not None:

                structured_llm = (
                    self.llm.with_structured_output(
                        self.output_schema
                    )
                )

                response = await structured_llm.ainvoke(
                    prompt
                )

                print("Structured LLM finished")

                return response


            # Normal text agent
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