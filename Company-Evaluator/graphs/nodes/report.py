from llms.factory import LLMFactory

from backend.services.report_service import report_service

from agents.report_agent import ReportAgent


async def report_node(
    state,
):

    llm = LLMFactory.get_llm()

    agent = ReportAgent(llm)

    result = await agent.run(state)
    print("result",result)
    print("Type",type(result))

    report_service.save_report(
        state["ticker"],
        result.report
    )

    print("\n========== REPORT OUTPUT ==========")
    print("Recommendation:",result.recommendation)
    print("Overall Risk:",result.overall_risk)
    print("Report Length:",len(result.report))
    print("===================================\n")


    return {
        "report": result.report,

        "report_metadata": {
            "recommendation":result.recommendation,
            "overall_risk":result.overall_risk,
        }

    }