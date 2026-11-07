# 🤖 DataPilot – Multi-Agent AI Data Analyst

DataPilot is an AI-powered multi-agent system designed to automate routine data operations using natural language instructions. Built with **LangChain and LangGraph**, it enables users to interact with databases, extract data from external APIs, and perform data transformations without manually writing SQL queries or Python scripts.

The system uses a supervisor-based architecture that delegates tasks to specialized agents depending on the user's requirements.

## 🏗️ Architecture

The system consists of three primary agents:

### 1. Parent Data Agent (Supervisor)
- Acts as the central entry point for user requests.
- Understands user intent and determines whether the task requires SQL operations or ETL processing.
- Routes requests to the appropriate sub-agent.

### 2. SQL Analyst Agent (Stateful Workflow)
Handles database-related operations through a structured LangGraph workflow.

- **Prompt Curation:** Refines user queries into structured instructions.
- **Context Engineering:** Retrieves database schema details, including tables, columns and data types.
- **SQL Generation:** Generates SQL queries using LLMs.
- **Safety Validation:** Checks generated queries before execution.
- **Query Execution:** Executes validated queries against PostgreSQL.
- **Result Representation:** Converts query results into understandable responses.

### 3. ETL Analyst Agent (ReAct Loop)
Handles dynamic data extraction and transformation using a Reasoning + Acting (ReAct) architecture.

- Extracts data from external APIs.
- Dynamically selects appropriate Python tools based on user requirements.
- Generates and executes Python code for data transformations.
- Evaluates intermediate outputs and iterates when necessary.
- Saves processed data in formats such as CSV, JSON and Parquet.

## ✨ Key Features

- Natural language interaction for database and ETL operations.
- Intelligent task routing using a supervisor agent.
- Automated SQL generation with database schema awareness.
- SQL safety validation before query execution.
- API-based data extraction and Pandas transformations.
- ReAct-based dynamic Python tool execution.
- Stateful workflow orchestration using LangGraph.
- Structured state management and validation using Pydantic.
- Flexible multi-LLM integration based on task complexity.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Language | Python |
| AI Frameworks | LangChain, LangGraph |
| LLM Integration | LangChain OpenRouter |
| Database | PostgreSQL |
| Data Processing | Pandas |
| State Management | Pydantic |
| Package Management | UV |

## 🧠 LLM Configuration

The project uses a flexible LLM selection mechanism through `ChatOpenRouter`, allowing different language models to be assigned to different nodes depending on their complexity and requirements.

For example:
- **Low complexity:** Query curation and simple formatting.
- **Medium complexity:** SQL query generation.
- **High complexity:** Result interpretation and representation.

You can configure different **free or paid LLMs** for individual tasks. For example, you can use lightweight models for simpler operations and more capable models for complex reasoning and code generation.

This project currently uses freely available models through **OpenRouter**, including NVIDIA Nemotron, to keep experimentation and development cost-effective.

To customize the models, modify the `pick_llm()` function in `utils/llm_pick.py` and configure the corresponding model identifiers.

## 📁 Project Structure

```text
data_agent/
│
├── agents/
│   ├── Data_agent.py
│   ├── sql_analyst.py
│   └── etl_analyst.py
│
├── models/
│   └── schema.py
│
├── utils/
│   ├── database.py
│   ├── etl_tools.py
│   └── llm_pick.py
│
├── data/
│   ├── extract/
│   └── transform/
│
├── main.py
├── feed_db.py
├── pyproject.toml
└── README.md
```

## ⚙️ Setup & Configuration

**1. Clone the repository**

```bash
git clone <repository-url>
cd Data_Agent
```

**2. Create and activate a virtual environment**

```bash
uv venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

**3. Install dependencies**

```bash
uv pip install -e .
```

**4. Configure environment variables**

Create a `.env` file in the project root and add your credentials:

```env
OPENROUTER_API_KEY=your_api_key

host=localhost
port=5432
user=postgres
password=your_password
database=data_agent_db
```

Configure the PostgreSQL database before executing database-related operations.

**5. Run the application**

```bash
python main.py
```

## 💡 Example Use Cases

**SQL Operations:**
- Find the total revenue generated during a particular month.
- Identify the top-performing drivers.
- Calculate average ride ratings.

**ETL Operations:**
- Extract Pokémon data from an external API and save it as CSV.
- Filter a dataset to include only specific records.
- Transform CSV data and save the output in JSON format.

---

**Built with Python, LangChain, LangGraph and OpenRouter.**
