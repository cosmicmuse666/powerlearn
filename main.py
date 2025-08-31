from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, Response
from src.agent import ProjectMentorAgent
from typing import Optional
import uuid
from fpdf import FPDF

app = FastAPI()

# In-memory storage for suggestions
suggestions_storage = {}

# Mount the static directory to serve index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Project Mentor Suggestions', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/suggest")
def get_suggestions(interest: str, skill_level: str, language: Optional[str] = None):
    """Endpoint to get project suggestions."""
    agent = ProjectMentorAgent()
    suggestions = agent.get_project_suggestions(interest, skill_level, language)
    
    suggestion_id = str(uuid.uuid4())
    suggestions_storage[suggestion_id] = suggestions
    
    return {"suggestions": suggestions, "suggestion_id": suggestion_id}

@app.get("/s/{suggestion_id}")
def get_shared_suggestion(suggestion_id: str):
    """Endpoint to retrieve shared suggestions as a PDF."""
    suggestions = suggestions_storage.get(suggestion_id)
    if not suggestions:
        raise HTTPException(status_code=404, detail="Suggestions not found")

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(0, 10, txt = suggestions)
    
    response = Response(content=pdf.output(dest='S').encode('latin-1'), media_type='application/pdf')
    response.headers["Content-Disposition"] = "attachment; filename=suggestions.pdf"
    return response
