# GenAI-Powered Knowledge Management System 
(GAI_KMS_01)

This is a prototype of a solution like 
Agentic RAG (Retrieval-Augmented Generation) based on LangGraph with data from Jira and Confluence

## Description

![GenAI_Powered_KMS_02.png](Images%2FGenAI_Powered_KMS_02.png)

The "GenAI-Powered Knowledge Management System" is designed to streamline and optimize the management of knowledge within an organization using advanced AI capabilities.

**1. User Interaction:**

* **User**: The process starts with the User who asks a question to the AI agents.
* **GenAI_Agent**: The GenAI Agents are key components, receiving questions from the users and providing answers.

**2. Context Management:**

* **Data Context**: The GenAI Agents interact with the Data Context hosted on the Chat history. They both receive context data and update it as needed, ensuring up-to-date information flow.

**3. Tool Utilization:**

* **Search Tool & Summary Tool**: To provide accurate and relevant answers, GenAI Agents use the Search and Summary tools. These tools interact with Vector Databases to retrieve relevant chunks of information.

**4. External Search:**

* **WebSearch**: In addition to internal data, the GenAI Agents can perform web searches to gather additional information that may be relevant to the user's question.

**5. Data Ingestion:**

* **Document Loaders**: These components populate Vector Databases with data from various source systems—Jira, Confluence, and Git, ensuring that the GenAI agents have a rich dataset to work with.


This architecture enables seamless data integration and intelligent query resolution, leveraging both structured internal data and external resources to enhance knowledge management.

### Materials used:

Course: **AI Agents in LangGraph** https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/1/introduction

Documentation: https://python.langchain.com/v0.2/docs/introduction/

GitHub: https://github.com/langchain-ai/langgraph/tree/main

LangGraph and RAG: https://github.com/langchain-ai/langgraph/tree/main/examples/rag

Agentic RAG: https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_agentic_rag.ipynb

# Implementation

## 0.Synthetic data generation

### 0.1. Generate synthetic data in JSON format to emulate Confluence data.
_01_SyntheticDataGeneration_Confluence.py_ script will generate the requested number of synthetic data entries, 
complete with metadata and descriptions, and save them to the specified JSON file.

The data is dedicated to the description of a fictitious software product called "Moon Flight System".

### 0.2. Generates synthetic data in CSV format to emulate Jira data.

_02_SyntheticDataGeneration_Jira.py_ script uses the Faker library to generate realistic random data for various fields.

The data contains Jira ticket information for a fictitious software product called "Moon Flight System".

### 1.1. Creating a new Vector Knowledge Base for Jira

_11_Create_Vector_Db_Jira.py_

### 1.2. Creating a new Vector Knowledge Base for Confluence

_12_Create_Vector_Db_Confluence.py_

### 2.1. Simple RAG for Jira

_21_RAG_Jira.py_

### 2.2. Simple RAG for Confluence
_22_RAG_Confluence.py_

### 3.0. Agents

_30_Agents.py_ module integrates various AI tools to create an intelligent agent capable of answering queries 
related to Jira tickets and Confluence documentation. 
It leverages retrievers for fetching relevant information from pre-loaded databases, 
linguistic models for interpreting and generating responses, 
and a workflow graph for managing the agent's decision process.

1. **Loading Databases**:
   - Loads Jira and Confluence databases into retrievers for querying.

2. **Creating Retriever Tools**:
   - Sets up tools for querying Jira tickets and Confluence documentation.

3. **Agent State Definition**:
   - Defines the state for agent, which will include messages.

4. **Graph Nodes**:
   - **Agent**: Handles invocation of the agent model.
   - **Retrieve**: Retrieves documents using retrievers.
   - **Rewrite**: Rewrites queries to be more effective.
   - **Generate**: Generates responses based on relevant documents.

5. **Graph Edges**:
   - Defines the workflow for how different nodes interact based on conditions.

6. **Main Execution**:
   - Initializes logging and demonstrates usage with sample queries.

By integrating various AI components, this module provides an interactive agent capable of handling complex queries 
and fetching relevant information dynamically.

#### 3.0.1. Nodes and Edges

We can lay out an agentic RAG graph like this:

* The state is a set of messages
* Each node will update (append to) state
* Conditional edges decide which node to visit next

![Nodes_Edges_01.png](Images%2FNodes_Edges_01.png)

## Configuration
1. In the folder "./Python" you need to create a file ".env" with the value of the OPENAI_API_KEY, example:

API_KEY = 'sk-***' # Open AI API Key