# 🚀 AI Company Evaluator

An **AI-powered Multi-Agent Equity Research System** that automatically collects company data, analyzes financial performance, evaluates business risks, performs valuation analysis, and generates **professional investment research reports and PowerPoint presentations**.

Built using **LangGraph**, **LangChain**, **LLMs**, and multiple financial data sources to automate the workflow of a professional equity research analyst.

---

# ✨ Features

* 📊 Automated Company Data Collection
* 📈 Financial Statement Analysis
* 📰 Real-Time News & Market Analysis
* ⚠️ AI-Based Risk Assessment
* 💰 Valuation Analysis
* 📝 Professional Equity Research Report Generation
* 📄 Automatic PDF Export
* 📊 Automatic PowerPoint Presentation Generation
* 🤖 Multi-Agent AI Architecture
* 🔄 Asynchronous Parallel Workflow using LangGraph
* 🌐 Web Research Integration
* 📉 Financial Metrics & Ratio Calculation (Planned)
* 🧠 Multi-LLM Support (Groq, Gemini, Mistral, Ollama)
* 💬 Conversational Company Analysis (Upcoming)
* 📈 Interactive Dashboard (Upcoming)

---

# 🏗️ System Architecture

```
                    User Input
                         │
                         ▼
                 Company Ticker
                         │
                         ▼
              Data Collection Service
                         │
      ┌──────────┬────────────┬──────────┐
      ▼          ▼            ▼
 Yahoo Finance  NewsAPI    Tavily Search
      │          │            │
      └──────────┴────────────┘
                 │
                 ▼
             Company State
                 │
                 ▼
         LangGraph Multi-Agent System
                 │
 ┌────────┬────────┬────────┬─────────┐
 ▼        ▼        ▼        ▼
Company Financial News    Calculator
Agent    Agent     Agent      (Planned)
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
            Slide Agent
                 │
      ┌──────────┴─────────┐
      ▼                    ▼
   PDF Exporter      PPT Exporter
```

---

# 🤖 AI Agents

## Company Research Agent

* Business overview
* Industry analysis
* Competitive positioning
* Business model analysis

---

## Financial Analysis Agent

* Revenue analysis
* Profitability analysis
* Margin analysis
* Financial health assessment

---

## News Analysis Agent

* Recent developments
* Sentiment analysis
* Industry news
* Market updates

---

## Risk Analysis Agent

* Business risk
* Market risk
* Financial risk
* Industry risk
* Regulatory risk

---

## Valuation Agent

* Relative valuation
* Premium/discount analysis
* Investment thesis
* Long-term outlook

---

## Report Agent

Generates a professional 4-5 page equity research report using all previous agent outputs.

---

## Slide Agent

Converts the research report into a structured 10-slide presentation optimized for PowerPoint generation.

---

# 🛠️ Tech Stack

## AI

* LangGraph
* LangChain
* Groq
* Gemini
* Mistral
* Ollama

---

## Backend

* Python
* AsyncIO

---

## Data Sources

* Yahoo Finance
* NewsAPI
* Tavily Search

---

## Report Generation

* ReportLab
* python-pptx

---

## State Management

* TypedDict
* Shared CompanyState
* Multi-Agent Memory

---

# 📂 Project Structure

```
AI-Company-Evaluator/

│

├── agents/

├── graphs/

├── data_sources/

├── exporters/

├── financial_engine/

├── llms/

├── state/

├── cache/

├── scripts/

├── outputs/

└── README.md
```

---

# 🚀 Workflow

```
Ticker

↓

Collect Company Data

↓

Parallel AI Analysis

↓

Company Analysis

↓

Financial Analysis

↓

News Analysis

↓

Risk Analysis

↓

Valuation Analysis

↓

Research Report

↓

Slide Generation

↓

PDF Export

↓

PowerPoint Export
```

---

# 📄 Generated Outputs

* Professional Equity Research Report (PDF)
* Executive Presentation (PPTX)
* Investment Recommendation
* Risk Assessment
* Business Analysis
* Financial Analysis

---

# 🔥 Upcoming Features

* AI Chat with Company Reports
* Conversational Investment Assistant
* Financial Calculator Engine
* DCF Valuation Engine
* Interactive Charts
* Portfolio Analysis
* Company Comparison
* RAG-based Knowledge Retrieval
* AI Financial Advisor
* FastAPI REST API
* Streamlit Dashboard
* React Frontend
* Docker Deployment
* Multi-LLM Failover Architecture
* Real-Time Stock Monitoring
* Automated Daily Report Generation

---

# 📈 Future Vision

The goal of this project is to build an AI-powered investment research platform capable of generating institutional-grade equity research reports with minimal human intervention by leveraging multi-agent orchestration and large language models.

---

# 👨‍💻 Author

Nishant Kumar

AI • Backend • GenAI • Multi-Agent Systems • Financial AI
