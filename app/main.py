import os
from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

app = FastAPI()

# API Key authentication
API_KEY = os.getenv("API_KEY", "your-default-api-key")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if not api_key_header or api_key_header != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )
    return api_key_header

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, api_key: str = Security(get_api_key)):
    return {"item_id": item_id, "message": "Protected endpoint"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)