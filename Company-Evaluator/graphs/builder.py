from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from state.state import CompanyState

from graphs.nodes import (
    data_collection_node,
    company_node,
    financial_node,
    news_node,
    risk_node,
    valuation_node,
    report_node,
    slide_node,
    parser_node,
    export_node,
    financial_calculator_node

)

builder = StateGraph(CompanyState)

# -----------------------
# Register Nodes
# -----------------------

builder.add_node(
    "data_collection",
    data_collection_node
)

builder.add_node(
    "financial_calculator",
    financial_calculator_node
)

builder.add_node(
    "company",
    company_node
)

builder.add_node(
    "finance",
    financial_node
)

builder.add_node(
    "news",
    news_node
)

builder.add_node(
    "risk",
    risk_node
)

builder.add_node(
    "valuation",
    valuation_node
)

builder.add_node(
    "report",
    report_node
)
builder.add_node(
    "parser",
    parser_node
)
builder.add_node(
    "slides",
    slide_node
)
builder.add_node(
    "export",
    export_node
)

# -----------------------
# Edges
# -----------------------

builder.add_edge(
    START,
    "data_collection"
)

# Parallel Branch

'''builder.add_edge(
    "data_collection",
    "company"
)

builder.add_edge(
    "data_collection",
    "news"
)

builder.add_edge(
    "data_collection",
    "finance"

)'''

builder.add_edge(
    "data_collection",
    "financial_calculator"
)

builder.add_edge(
    "financial_calculator",
    "finance"
)
builder.add_edge(
    "finance",
    "company"
)

builder.add_edge(
    "company",
    "news"
)
builder.add_edge(
    "news",
    "risk"
)



# Continue Pipeline

builder.add_edge(
    "risk",
    "valuation"
)

builder.add_edge(
    "valuation",
    "report"
)
builder.add_edge(
    "report",
    "parser"
)

builder.add_edge(
    "parser",
    "export"
)

builder.add_edge(
    "export",
    "slides"
)


builder.add_edge(
    "slides",
    END
)

company_graph = builder.compile()