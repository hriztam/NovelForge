import google.generativeai as genai
from config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

def review_content(content: str) -> dict:
    model = genai.GenerativeModel(settings.LLM_MODEL)
    prompt = f"""
    Critically review this chapter draft. Provide:
    1. Continuity errors (list)
    2. Language quality score (1-10)
    3. Three improvement suggestions
    4. Overall verdict: APPROVE/REVISE
    
    CHAPTER:
    {content}
    """
    response = model.generate_content(prompt)
    return {
        "feedback": response.text,
        "verdict": "APPROVE" if "APPROVE" in response.text else "REVISE"
    }