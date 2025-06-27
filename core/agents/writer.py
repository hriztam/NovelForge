import google.generativeai as genai
from config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

def spin_chapter(content: str) -> str:
    model = genai.GenerativeModel(settings.LLM_MODEL)
    prompt = f"""
    Rewrite this book chapter creatively while preserving:
    - Core plot points
    - Character relationships
    - Key events
    
    Modify:
    - Writing style
    - Dialogue presentation
    - Descriptive elements
    
    Output ONLY the rewritten text without additional commentary.
    
    ORIGINAL CHAPTER:
    {content}
    """
    response = model.generate_content(prompt)
    return response.text
