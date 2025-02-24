from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List
import requests
from ..utils.text_exporter import extract_text
from ..utils.text_processor import QnA_using_offline_models, openai_text_generator

router = APIRouter()


@router.websocket("/ws/query")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        data = await websocket.receive_json()
        urls = data.get("urls", [])
        question = data.get("question", "")
        expanded_answer = data.get("expanded_answer", False)
        
        await websocket.send_json({"messasge":"status","status": f"Fetching content from urls..."})
        combined_text = extract_text(urls)
        
        if not combined_text.strip():
            await websocket.send_json({"error": "No useful content extracted from URLs."})
            return
                
        await websocket.send_json({"messasge":"status","status": "Generating answer..."})
        answer=QnA_using_offline_models(combined_text, question, expanded_answer)
        # answer = openai_text_generator(combined_text, question)
            
        await websocket.send_json({"messasge":"status","status": "Returning response..."})
        await websocket.send_json({"messasge":"data","data":{"answer": answer, "source_text": combined_text[:1000]}})
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        await websocket.send_json({"message":"error","error": str(e)})

