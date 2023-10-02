# routes.py

from fastapi import APIRouter
from app.schemas import ChatMessage, ChatResponse
from app.personas import youtube_creator_chat, seo_blogging_expert_chat, ceo_founder_chat
from loguru import logger
import sys

logger.add(sys.stdout, format="{time} - {level} - {message}", filter="sub.module")
router = APIRouter()



@router.post("/chat/", response_model=ChatResponse)
async def chat_endpoint(msg: ChatMessage):
    expert_type = msg.expert_type
    message = msg.message
    # TODO: Validate user token
    # TODO: Retrieve user conversation, context
    # TODO: Send context and to specific expert to handle response
    logger.debug(f'chat expert:{expert_type}, message: {message}')

    if expert_type == 'youtube':
        response = youtube_creator_chat(message)
    elif expert_type == 'seo':
        response = seo_blogging_expert_chat(message)
    elif expert_type == 'ceo':
        response = ceo_founder_chat(message)
    else:
        response = "Unknown expert type"

    return {"response": response}