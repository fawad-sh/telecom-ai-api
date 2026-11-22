from fastapi import FastAPI
app = FastAPI(title="Telecom AI API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/subscriber/{sub_id}")
def get_subscriber(sub_id: str):
    return {"id": sub_id, "name": "Demo User", "plan": "5G Postpaid", "status": "active"}

@app.post("/support")
def support(req: dict):
    return {"reply": f"AI Agent: I found your request about '{req.get('query','')}'. Ticket created."}
