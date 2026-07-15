🚀 AI Company Evaluator

An AI-powered Multi-Agent Equity Research Platform that automates company research, financial analysis, risk assessment, valuation, and professional report generation using LangGraph, LangChain, and Large Language Models.

Built to demonstrate how autonomous AI agents can collaborate to perform institutional-grade equity research with minimal human intervention.

🌟 Why This Project?

Traditional equity research requires analysts to spend hours collecting financial data, reading annual reports, analyzing company news, calculating financial ratios, assessing risks, and preparing investment reports.

This project automates that entire workflow.

Given only a company ticker, the system independently researches the company, analyzes its financial performance, evaluates risks, generates an investment recommendation, and produces both a professional research report and an executive PowerPoint presentation.

✨ Features
📊 Company Intelligence
🏢 Business Overview
🌍 Industry Analysis
⚔️ Competitive Positioning
💼 Business Model Evaluation
👨‍💼 Management Insights
📈 Financial Analysis
Revenue Analysis
Profitability Analysis
Margin Analysis
Balance Sheet Review
Cash Flow Analysis
Financial Health Assessment
Growth Trend Analysis
🧮 Financial Calculator Engine

Automatically calculates

Revenue Growth
EPS Growth
ROE
ROA
Debt-to-Equity
Current Ratio
Quick Ratio
Operating Margin
Net Margin
Free Cash Flow
Working Capital
Interest Coverage
Additional Financial Ratios
📰 Market Intelligence
Latest Company News
Industry Developments
Market Sentiment
Major Corporate Events
Product Launches
Strategic Partnerships
Acquisition Analysis
⚠️ Risk Assessment
Business Risk
Financial Risk
Industry Risk
Operational Risk
Regulatory Risk
Investment Risk Score
💰 Valuation Analysis
Relative Valuation
Premium / Discount Analysis
Investment Thesis
Long-Term Outlook
Buy / Hold / Sell Recommendation
📝 AI Report Generation

Generates a complete institutional-style research report including

Executive Summary
Company Overview
Industry Analysis
Business Analysis
Financial Performance
Financial Metrics
Risk Assessment
Valuation
Investment Recommendation
Overall Risk Rating
Conclusion
📊 Presentation Generation

Automatically creates an executive PowerPoint presentation containing

Company Snapshot
Financial Highlights
Business Analysis
Risks
Valuation
Recommendation
🤖 Multi-Agent Architecture

The platform uses specialized AI agents where every agent focuses on a single responsibility.

🤖 Agent	Responsibility
🏢 Company Agent	Business & Industry Research
📈 Financial Agent	Financial Statement Analysis
📰 News Agent	Market & News Analysis
🧮 Financial Calculator	Financial Metric Computation
⚠️ Risk Agent	Risk Evaluation
💰 Valuation Agent	Investment Recommendation
📝 Report Agent	Professional Report Generation
📄 Parser Agent	Markdown & Structured Output
📊 Slide Agent	PowerPoint Generation
⚙️ Automated Workflow
                 User Input
                      │
                      ▼
              Company Ticker
                      │
                      ▼
          Data Collection Layer
                      │
     ┌─────────┬─────────┬─────────┐
     ▼         ▼         ▼
 Yahoo      Financial   Web Search
 Finance      Data
     └─────────┴─────────┘
               │
               ▼
          Shared CompanyState
               │
               ▼
      LangGraph StateGraph
               │
      ┌────────┼────────┐
      ▼        ▼        ▼
 Company   Financial   News
  Agent      Agent     Agent
               │
               ▼
      Financial Calculator
               │
               ▼
          Risk Agent
               │
               ▼
       Valuation Agent
               │
               ▼
         Report Agent
               │
               ▼
         Parser Agent
               │
               ▼
          Slide Agent
               │
        ┌──────┴──────┐
        ▼             ▼
      PDF Export   PPT Export
🏗️ Engineering Highlights

✅ Multi-Agent AI Architecture

✅ Shared State Management using LangGraph

✅ Asynchronous Parallel Execution

✅ Typed State Management

✅ Modular Agent Design

✅ Configurable Multi-LLM Support

✅ Structured Prompt Engineering

✅ Automated Report Generation

✅ Automated PowerPoint Generation

✅ Deterministic Financial Calculations

✅ Markdown-Based Export Pipeline

✅ Production-Oriented Project Structure

🛠️ Tech Stack
🤖 AI & Orchestration
LangGraph
LangChain
🧠 Large Language Models
Gemini
Groq
Mistral
Ollama
OpenRouter
🐍 Backend
Python
AsyncIO
FastAPI
📊 Financial Data Sources
Yahoo Finance
Tavily Search
Web Search APIs
📄 Report Generation
Markdown
ReportLab
python-pptx
🗂️ State Management
TypedDict
Shared CompanyState
💡 Why These Technologies?
🚀 LangGraph

Provides stateful orchestration for coordinating multiple AI agents with shared memory, conditional execution, and parallel workflows.

🧠 LangChain

Simplifies prompt management, LLM integration, structured outputs, and agent implementation.

⚡ AsyncIO

Allows independent data collection and analysis tasks to execute concurrently, reducing overall processing time.

🗂️ Shared CompanyState

Acts as a centralized memory that enables all agents to collaborate without direct dependencies.

🧮 Financial Calculator Engine

Performs deterministic financial calculations in Python instead of relying on LLMs, improving numerical accuracy and consistency.

📝 Markdown Pipeline

Generates reports in Markdown first, allowing the same content to be converted into both PDF and PowerPoint formats.

🔄 Multi-LLM Support

Supports multiple providers, enabling flexibility in balancing model quality, latency, and operational cost.

📂 Project Structure
AI-Company-Evaluator/

├── agents/
├── graphs/
├── state/
├── llms/
├── prompts/
├── data_sources/
├── financial_engine/
├── exporters/
├── parsers/
├── backend/
├── cache/
├── outputs/
├── config/
└── README.md
📄 Generated Outputs
📑 Institutional Equity Research Report
📕 Professional PDF Report
📊 Executive PowerPoint Presentation
📈 Financial Metrics
⚠️ Risk Assessment
💰 Valuation Analysis
📝 Investment Recommendation
📰 News Summary
🎯 Future Roadmap
🤖 Conversational Company Assistant
📈 Interactive Financial Charts
💼 Portfolio Analysis
🏢 Multi-Company Comparison
📊 DCF Valuation Engine
🔍 RAG-Based Company Knowledge
🌐 React Dashboard
🚀 FastAPI REST API
🐳 Docker Deployment
☁️ Cloud Deployment
📡 Real-Time Market Monitoring
🔄 Automated Daily Research Reports
🌍 Vision

The vision of this project is to build an AI-native investment research platform capable of autonomously generating institutional-grade equity research, continuously monitoring companies, and assisting investors through intelligent, explainable, and scalable multi-agent workflows.

👨‍💻 Author

Nishant Kumar

AI Engineer • Backend Developer • GenAI • Multi-Agent Systems • Financial AI
