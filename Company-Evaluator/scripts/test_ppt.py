import asyncio

from dotenv import load_dotenv

load_dotenv()

from graphs.company_graph import run_graph

from exporters.ppt_exporter import PPTExporter


async def main():

    ticker = input(
        "Enter Company Ticker: "
    ).strip().upper()

    print(
        f"\nGenerating report for {ticker}...\n"
    )

    state = await run_graph(
        ticker
    )

    exporter = PPTExporter()

    output_path = (
        f"outputs/{ticker}_Report.pptx"
    )

    exporter.export(
        state,
        output_path,
    )

    print("=" * 50)

    print(
        " PPT Generated Successfully!"
    )

    print(
        f" Saved at : {output_path}"
    )

    print("=" * 50)


if __name__ == "__main__":

    asyncio.run(
        main()
    )