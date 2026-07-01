from llms.factory import LLMFactory

from backend.services.report_service import report_service

from agents.report_agent import ReportAgent

async def report_node(state):

    llm = LLMFactory.get_llm()

    agent = ReportAgent(llm)

    report = await agent.run(state)

    report_service.save_report(
        state["ticker"],
        report
    )

    return {

        "report": report

    }