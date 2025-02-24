import requests
from config.settings import OPENAI_API_KEY
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-large-squad2")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def QnA_using_offline_models(content,question,expand_answer=False):
    response = qa_pipeline(question=question, context=content)
    detailed_answer = response['answer'].strip()
    if not expand_answer:
        return detailed_answer
    else:
        expanded_answer = summarizer(detailed_answer, max_length=100, min_length=50, do_sample=False)[0]['summary_text']
        return expanded_answer

def openai_text_generator(content,question):
    API_URL = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization":f"Bearer {OPENAI_API_KEY}"}
    data={
        "model": "gpt-4",
        "messages": [{
                        "role":"system",
                        "content":f"You are a helpful assistant. You have to answer the question based on this content only : {content}"},
                    {
                        "role": "user", 
                        "content": f"{question}"
                    }],
        "temperature": 0.1,
        "max_tokens": 60
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to generate answer: {response.text}")
    answer = response.json()["choices"][0]["message"]["content"]
    return answer


