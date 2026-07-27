from fastmcp import FastMCP
from fastapi import FastAPI
from .tools import write_story

mcp = FastMCP("Story-Writer-Server")

@mcp.tool()
async def write_story_tool(title: str, genre: str, story: str):
    """
    Write a story to a file and return the file location.
    
    This tool is used to save generated stories to the filesystem.
    It creates a properly formatted text file in the stories/ directory.
    
    Args:
        title: The title of the story
        genre: The genre (Sci-Fi, Fantasy, Romance, etc.)
        story: The full story content
        
    Returns:
        Dictionary with filename, path, and success status
    """
    # Call our actual implementation
    result = write_story(title, genre, story)
    return result

def create_app():
    # Create the MCP ASGI app
    mcp_app = mcp.http_app(path="/")

    # Pass the MCP lifespan to FastAPI
    app = FastAPI(
        title="Story Writer MCP Server",
        lifespan=mcp_app.lifespan,
    )

    # Mount the MCP server
    app.mount("/mcp", mcp_app)

    @app.get("/health")
    async def health():
        return {
            "status": "healthy",
            "server": "Story-Writer-MCP",
        }

    return app

if __name__ == "__main__":
    import uvicorn
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)