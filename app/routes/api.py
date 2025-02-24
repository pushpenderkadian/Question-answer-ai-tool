from fastapi import APIRouter, HTTPException
from models import QnA_Query_Input
from ..utils.text_exporter import extract_text
from ..utils.text_processor import QnA_using_offline_models
router = APIRouter()

@router.post("/api/query")
async def process_qna(payload: QnA_Query_Input):
    
    combined_text = extract_text(payload.urls)
    
    if not combined_text.strip():
        raise HTTPException(status_code=400, detail="No useful content extracted from URLs.")
    
    
    answer=QnA_using_offline_models(combined_text, payload.question, payload.expanded_answer)
    # answer = openai_text_generator(combined_text, question)
    
    return {"success":True,"data":{"answer": answer, "source_text": combined_text[:1000]}}