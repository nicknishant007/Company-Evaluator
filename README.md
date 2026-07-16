# 🚀 AI Company Evaluator

An **AI-powered Multi-Agent Equity Research Platform** that automates company research, financial analysis, risk assessment, valuation, and professional report generation using **LangGraph**, **LangChain**, and multiple **Large Language Models (LLMs)**.

Built to demonstrate how autonomous AI agents collaborate to perform **institutional-grade equity research** with minimal human intervention.

---

# 🌟 Why This Project?

Traditional equity research requires analysts to spend hours:

- Collecting financial data
- Reading annual reports
- Understanding business models
- Tracking company news
- Calculating financial ratios
- Evaluating risks
- Preparing research reports
- Creating executive presentations

This project automates the entire workflow.

Given only a **company ticker**, the platform independently researches the company, analyzes its financial performance, evaluates risks, performs valuation analysis, and generates a professional equity research report together with an executive PowerPoint presentation.

---

# ✨ Features

## 📊 Company Intelligence

- Company Overview
- Business Model Analysis
- Industry Analysis
- Competitive Positioning
- Competitive Advantages
- Management Insights

---

## 📈 Financial Analysis

- Revenue Analysis
- Profitability Analysis
- Margin Analysis
- Balance Sheet Analysis
- Cash Flow Analysis
- Financial Health Assessment
- Growth Trend Analysis

---

## 🧮 Financial Calculator Engine

Automatically calculates:

- Revenue Growth
- EPS Growth
- ROE
- ROA
- Debt-to-Equity
- Debt Ratio
- Current Ratio
- Quick Ratio
- Gross Margin
- Operating Margin
- Net Margin
- Free Cash Flow
- Working Capital
- Interest Coverage
- Financial Ratios

---

## 📰 Market Intelligence

- Latest Company News
- Industry Developments
- Market Sentiment
- Corporate Announcements
- Strategic Partnerships
- Acquisitions
- Product Launches

---

## ⚠️ AI Risk Assessment

- Business Risk
- Financial Risk
- Market Risk
- Industry Risk
- Operational Risk
- Regulatory Risk
- Overall Investment Risk Score

---

## 💰 Valuation Analysis

- Relative Valuation
- Premium / Discount Analysis
- Investment Thesis
- Long-Term Outlook
- Buy / Hold / Sell Recommendation

---

## 📝 Professional Report Generation

The system automatically generates an institutional-style research report containing:

- Executive Summary
- Company Overview
- Industry Analysis
- Business Model Analysis
- Competitive Positioning
- Financial Performance
- Financial Ratio Analysis
- Growth Analysis
- News Summary
- Risk Assessment
- Valuation Analysis
- Investment Recommendation
- Overall Risk Rating
- Conclusion

---

## 📊 Executive Presentation Generation

Automatically converts the report into an executive PowerPoint presentation including:

- Company Snapshot
- Financial Highlights
- Business Analysis
- Risk Summary
- Valuation
- Investment Recommendation

---

# 🤖 Multi-Agent Architecture

| Agent | Responsibility |
|-------|----------------|
| 🏢 Company Agent | Business & Industry Research |
| 📈 Financial Agent | Financial Statement Analysis |
| 📰 News Agent | Market & News Analysis |
| 🧮 Financial Calculator Agent | Financial Metric Computation |
| ⚠️ Risk Agent | Risk Evaluation |
| 💰 Valuation Agent | Investment Recommendation |
| 📝 Report Agent | Professional Report Generation |
| 📄 Parser Agent | Markdown Formatting & Structured Output |
| 📊 Slide Agent | PowerPoint Generation |

---

# ⚙️ Automated Workflow

```text
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
 Yahoo Finance Financial Data Web Search
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
```

---

# 🏗️ Engineering Highlights

- ✅ Multi-Agent AI Architecture
- ✅ LangGraph Stateful Workflow
- ✅ Shared CompanyState
- ✅ Asynchronous Parallel Execution
- ✅ Modular Agent Design
- ✅ Structured Prompt Engineering
- ✅ Configurable Multi-LLM Support
- ✅ Deterministic Financial Calculations
- ✅ Markdown-Based Report Pipeline
- ✅ Automated PDF Generation
- ✅ Automated PowerPoint Generation
- ✅ Production-Oriented Project Structure

---

# 🛠️ Tech Stack

## 🤖 AI & Orchestration

- LangGraph
- LangChain

## 🧠 LLM Providers

- Google Gemini
- Groq
- Mistral
- Ollama
- OpenRouter

## 🐍 Backend

- Python
- AsyncIO
- FastAPI

## 📊 Data Sources

- Yahoo Finance
- Tavily Search
- Web Search APIs

## 📄 Export

- Markdown
- ReportLab
- python-pptx

## 🗂️ State Management

- TypedDict
- Shared CompanyState

---

# 💡 Why These Technologies?

### 🚀 LangGraph
Provides graph-based orchestration, shared state, conditional routing, and parallel execution for autonomous AI workflows.

### 🧠 LangChain
Simplifies prompt management, LLM integration, structured outputs, and reusable AI components.

### ⚡ AsyncIO
Runs independent API calls concurrently to reduce overall execution time.

### 🗂️ Shared CompanyState
Acts as centralized memory allowing every agent to collaborate without direct dependencies.

### 🧮 Financial Calculator Engine
Financial metrics are calculated deterministically in Python instead of relying on LLM reasoning, improving accuracy and consistency.

### 📝 Markdown Pipeline
A single Markdown report serves as the source for both PDF and PowerPoint generation.

### 🔄 Multi-LLM Support
Allows switching between providers based on cost, latency, and capability without changing agent logic.

---

# 📂 Project Structure

```text
AI-Company-Evaluator/
│
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
```

---

# 📄 Generated Outputs

- 📑 Institutional Equity Research Report
- 📕 Professional PDF Report
- 📊 Executive PowerPoint Presentation
- 📈 Financial Metrics
- ⚠️ Risk Assessment
- 💰 Valuation Analysis
- 📝 Investment Recommendation
- 📰 News Summary

---

# 🎯 Future Roadmap

- 🤖 Conversational Company Assistant
- 📈 Interactive Financial Charts
- 💼 Portfolio Analysis
- 🏢 Multi-Company Comparison
- 📊 DCF Valuation Engine
- 🔍 RAG-Based Knowledge Retrieval
- 🌐 React Frontend
- 🚀 FastAPI REST API
- 🐳 Docker Deployment
- ☁️ Cloud Deployment
- 📡 Real-Time Stock Monitoring
- 🔄 Automated Daily Report Generation

---

# 🌍 Vision

The goal of this project is to build an **AI-native investment research platform** capable of autonomously generating institutional-grade equity research, monitoring companies in real time, comparing investment opportunities, and assisting investors through intelligent, explainable, and scalable multi-agent workflows.

---

# 👨‍💻 Author

**Nishant Kumar**

**AI Engineer • Backend Developer • GenAI • Multi-Agent Systems • Financial AI**
