from pydantic import BaseModel

class ChatMessage(BaseModel):
    message: str
    expert_type: str  # Add this line

class ChatResponse(BaseModel):
    response: str
