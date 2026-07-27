import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcp_server.server import create_app
import uvicorn

if __name__ == "__main__":
    app = create_app()
    print("🚀 Starting Story Writer MCP Server...")
    print("📍 Server running at: http://localhost:8000")
    print("🔧 MCP endpoint at: http://localhost:8000/mcp")
    print("💚 Health check at: http://localhost:8000/health")
    print("\nPress Ctrl+C to stop")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")