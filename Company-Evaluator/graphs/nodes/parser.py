from Report_parser.parser import ReportParser


async def parser_node(state):

    parser = ReportParser()

    raw_report = state["report"]

    cleaned_report = parser.clean(
        raw_report
    )

    parsed_report = parser.parse(
        cleaned_report
    )

    print("\n========== PARSER OUTPUT ==========")
    print("Raw Report Length:", len(raw_report))
    print("Cleaned Report Length:", len(cleaned_report))
    print("Parsed Blocks:", len(parsed_report))
    print("===================================\n")

    return {
        "cleaned_report": cleaned_report,
        "parsed_report": parsed_report,
    }