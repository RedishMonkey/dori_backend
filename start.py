import uvicorn
from os import getenv
port = getenv("PORT")

if port is None:
    port = 8000

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        # env_file="./.env",/
        reload=True
    )
