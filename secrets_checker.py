from fastapi import FastAPI 
import os
import re

app = FastAPI()

@app.get("/tools")
async def get_tools():
    return {
        "tools": [
            {
                "name": "scan_for_secrets",
                "description": "Scan a project folder for possible secrets and risky files",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "folder_path": {"type": "string", "description": "Path to project folder"}
                    },
                    "required": ["folder_path"]
                }
            }
        ]
    }

@app.post("/tools/scan_for_secrets")
async def scan_for_secrets(request: dict):
    folder_path = request.get("folder_path", ".")
    secrets_found = []
    
    # 1. Target .env specifically (your case)
    env_path = os.path.join(folder_path, ".env")
    if os.path.exists(env_path):
        secrets_found.append("🚨 Found risky file: .env")
        
        # 2. Scan .env CONTENT - matches YOUR exact format
        try:
            with open(env_path, 'r', errors='ignore') as f:
                content = f.read()
                print(f"DEBUG: .env content: {content[:100]}")  # Server log check
                
                # Patterns for YOUR .env
                patterns = [
                    r'(api[_-]?key|secret[_-]?token).*?=[^\n\r]+',
                    r'(password|database[_-]?password).*?=[^\n\r]+',
                ]
                
                for pattern in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        match_type = pattern.split('|')[0].split('(')[0].replace('[_-]?', '').upper().replace('APIKEY', 'API_KEY')

                        secrets_found.append(f"🚨 {match_type} detected in .env")
                        
        except Exception as e:
            secrets_found.append(f"Error reading .env: {str(e)}")
    
    # 3. Other secret files
    other_secrets = ["secrets.json", "config.json", ".aws/credentials"]
    for secret_file in other_secrets:
        if os.path.exists(os.path.join(folder_path, secret_file)):
            secrets_found.append(f"🚨 Found risky file: {secret_file}")
    
    return {
        "secrets_found": secrets_found,
        "message": f"Scanned {folder_path}. Found {len(secrets_found)} potential issues."
    }

if __name__ == "__main__":
    import uvicorn
    print("Secrets Checker MCP Server starting...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
