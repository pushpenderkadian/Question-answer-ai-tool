from typing import List
from pydantic import BaseModel


class QnA_Query_Input(BaseModel):
    urls: List[str]
    question: str
    expanded_answer: bool = False