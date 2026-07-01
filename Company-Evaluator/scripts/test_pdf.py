import asyncio

from dotenv import load_dotenv

load_dotenv()

from graphs.company_graph import run_graph
from exporters.pdf_exporter import PDFExporter


async def main():

    ticker = input(
        "Enter Company Ticker: "
    ).strip().upper()

    print(f"\nGenerating report for {ticker}...\n")

    state = await run_graph(
        ticker
    )

    output_path = f"outputs/{ticker}_Report2.pdf"

    exporter = PDFExporter()

    exporter.export(
        state,
        output_path,
    )

    print("=" * 50)
    print("✅ PDF Generated Successfully!")
    print(f"📄 Saved at : {output_path}")
    print("=" * 50)


if __name__ == "__main__":

    asyncio.run(
        main()
    )