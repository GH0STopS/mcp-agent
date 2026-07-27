from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class StoryInput(BaseModel):
    """Input model for writing a story."""
    title: str = Field(
        ..., 
        description="The title of the story",
        min_length=1,
        max_length=100
    )
    genre: str = Field(
        ...,
        description="The genre of the story (e.g., Sci-Fi, Fantasy, Romance)",
        min_length=1,
        max_length=50
    )
    story: str = Field(
        ...,
        description="The full story content",
        min_length=1
    )

class StoryOutput(BaseModel):
    """Output model for the write_story tool."""
    filename: str = Field(..., description="The generated filename")
    path: str = Field(..., description="Full path to the saved file")
    success: bool = Field(..., description="Whether the operation succeeded")
    error: Optional[str] = Field(None, description="Error message if failed")
    timestamp: datetime = Field(default_factory=datetime.now)