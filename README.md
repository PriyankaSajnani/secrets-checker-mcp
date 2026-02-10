# 🚨 Secrets Checker MCP - 2 Fast 2 MCP Hackathon

**Archestra AI agent detects secrets (API keys, passwords) in code repositories!**

[![Swagger UI](https://img.shields.io/badge/Swagger-UI-blue?logo=swagger)](http://localhost:8000/docs)
[![FastAPI](https://img.shields.io/badge/FastAPI-MCP-green?logo=fastapi)](https://fastapi.tiangolo.com/)

## 🎯 What it does

Archestra automatically calls this MCP server to scan project folders for secrets:

🚨 Found .env file

🚨 API_KEY detected (sk-fake-openai-key...)

🚨 DATABASE_PASSWORD detected (mypassword123)


 ## 🎯 Tech Stack
FastAPI - MCP server

Regex patterns - API keys, passwords, tokens

Archestra protocol - Tool discovery + JSON calls

Zero dependencies - Production ready



 ## 📋 Features
✅ Detects .env, secrets.json, config.json

✅ Regex scans: API_KEY=, PASSWORD=, SECRET_TOKEN=

✅ JSON responses for Archestra AI

✅ Swagger UI for manual testing

✅ Handles large folders (os.walk)

 ## quick start 
Clone
git clone https://github.com/PriyankaSajnani/secrets-checker-mcp.git
cd secrets-checker-mcp

Install (1 dep)
pip install fastapi uvicorn

Run MCP server
python secrets_checker.py

Test: http://localhost:8000/docs





