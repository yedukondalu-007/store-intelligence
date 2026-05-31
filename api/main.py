from fastapi import FastAPI

from api.ingestion import load_events
from api.metrics import calculate_metrics
from api.funnel import calculate_funnel
app = FastAPI(
    title="Store Intelligence API"
)

EVENT_FILE = "data/processed/master_events.jsonl"


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str):

    events = load_events(EVENT_FILE)

    return calculate_metrics(events)
@app.get("/stores/{store_id}/funnel")
def funnel(store_id: str):

    events = load_events(EVENT_FILE)

    return calculate_funnel(events)
from api.anomalies import detect_anomalies

@app.get("/stores/{store_id}/anomalies")
def anomalies(store_id: str):

    events = load_events(EVENT_FILE)

    return detect_anomalies(events)
from api.heatmap import generate_heatmap

@app.get("/stores/{store_id}/heatmap")
def heatmap(store_id: str):

    events = load_events(EVENT_FILE)

    return generate_heatmap(events)