
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from relevance_calculator import RelevanceCalculator

app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class CandidateArticle(BaseModel):
    Name: str
    DOB: str
    Gender: str
    Nationality: str
    Languages_Preferred: str
    Permanent_Address: str
    Religion: str
    Caste_Community: str
    Ethnicity: str
    Name_enrolled_as_voter_in: str
    Self_profession: str
    Education_level: str
    Political_Base: str
    Education_Institutes_attended: str
    Current_Occupation: str
    Previous_Occupation: str
    Years_of_experience_in_leadership: int
    Political_party_affiliation: str
    Previous_Political_positions_held: str
    Political_ideology_core_beliefs: str
    Key_Areas_of_Focus: str
    Primary_Vision_for_the_Country_Region: str
    Article_Text: str

@app.post("/get_relevancy")
async def compute_relevancy(article: CandidateArticle):
    try:
        calculator = RelevanceCalculator()
        candidate_data = article.dict()
        result = calculator.compute_relevancy_score(candidate_data, article.Article_Text)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
