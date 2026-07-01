from Report_parser.parser import ReportParser


async def parser_node(
    state,
):

    parser = ReportParser()

    parsed_report = parser.parse(

        state["report"]

    )

    return {

        "parsed_report": parsed_report

    }