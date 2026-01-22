from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from git_utils import clone_repo, read_repo_content, cleanup_repo
from ai_engine import analyze_code_chunk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    url: str

@app.get("/")
def health_check():
    return {"status": "active", "message": "GitSight Backend is running"}

@app.post("/api/analyze")
def analyze_repo(request: RepoRequest):
    repo_path = clone_repo(request.url)
    if not repo_path:
        raise HTTPException(status_code=400, detail="Failed to clone repository")

    try:
        files = read_repo_content(repo_path)
        
        ai_results = []
        file_count = 0
        
        for file_path, content in files.items():
            if file_count >= 3: 
                break
                
            review = analyze_code_chunk(file_path, content)
            
            ai_results.append({
                "file": file_path,
                "review": review
            })
            file_count += 1

        return {
            "status": "success",
            "analyzed_files": file_count,
            "total_files_in_repo": len(files),
            "results": ai_results
        }

    finally:
        cleanup_repo(repo_path)