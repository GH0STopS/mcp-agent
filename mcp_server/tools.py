import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Import our models
from .models import StoryInput, StoryOutput

def write_story(title: str, genre: str, story: str) -> Dict[str, Any]:
    """
    Write a story to a text file in the stories directory.
    
    This tool creates a properly formatted text file containing the story
    with metadata (title, genre, timestamp) at the top.
    
    Args:
        title: The story title
        genre: Story genre
        story: The story content
        
    Returns:
        Dict containing filename, path, success status, and error if any
    """
    try:
        # 1. Ensure the stories directory exists
        stories_dir = Path("stories")
        stories_dir.mkdir(exist_ok=True)
        
        # 2. Generate a safe filename from the title
        # Replace spaces with underscores, remove special chars
        safe_title = "".join(c for c in title if c.isalnum() or c.isspace()).strip()
        safe_title = safe_title.replace(" ", "_")
        
        # Add timestamp to avoid overwriting
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_title}_{timestamp}.txt"
        
        # 3. Create the full file path
        filepath = stories_dir / filename
        
        # 4. Write the story with metadata
        with open(filepath, "w", encoding="utf-8") as f:
            # Write header/metadata
            f.write("=" * 60 + "\n")
            f.write(f"TITLE: {title}\n")
            f.write(f"GENRE: {genre}\n")
            f.write(f"CREATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            
            # Write the story content
            f.write(story)
            f.write("\n\n" + "=" * 60 + "\n")
            f.write(f"END OF STORY - {filename}\n")
        
        # 5. Return success response
        return {
            "filename": filename,
            "path": str(filepath.absolute()),
            "success": True,
            "error": None,
            "timestamp": datetime.now().isoformat()
        }
        
    except PermissionError as e:
        return {
            "filename": None,
            "path": None,
            "success": False,
            "error": f"Permission denied: {str(e)}",
            "timestamp": datetime.now().isoformat()
        }
    except OSError as e:
        return {
            "filename": None,
            "path": None,
            "success": False,
            "error": f"File system error: {str(e)}",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "filename": None,
            "path": None,
            "success": False,
            "error": f"Unexpected error: {str(e)}",
            "timestamp": datetime.now().isoformat()
        }