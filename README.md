# GAI_KMS_01
GenAI-Powered Knowledge Management System

## 0.Synthetic data generation

### 0.1. Generate synthetic data in JSON format to emulate Confluence data.
01_SyntheticDataGeneration_Confluence.py script will generate the requested number of synthetic data entries, 
complete with metadata and descriptions, and save them to the specified JSON file.

The data is dedicated to the description of a fictitious software product called "Moon Flight System".

### 0.2. Generates synthetic data in CSV format to emulate Jira data.

02_SyntheticDataGeneration_Jira.py script uses the Faker library to generate realistic random data for various fields.

The data contains Jira ticket information for a fictitious software product called "Moon Flight System".

### 1.1. Creating a new Vector Knowledge Base for Jira

11_Create_Vector_Db_Jira.py

### 1.2. Creating a new Vector Knowledge Base for Confluence

12_Create_Vector_Db_Confluence.py