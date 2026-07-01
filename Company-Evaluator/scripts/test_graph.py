import asyncio
from dotenv import load_dotenv
load_dotenv()

import os

# Then import and run your graph

from graphs.company_graph import (
    run_graph
)


async def main():

    result = await run_graph(
        "TATASILV.NSE"
    )

    print(
        result["report"]
    )


if __name__ == "__main__":

    asyncio.run(
        main()
    )