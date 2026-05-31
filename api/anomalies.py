def detect_anomalies(events):

    anomalies = []

    queue_events = [
        e for e in events
        if e.get("event_type") == "QUEUE_SNAPSHOT"
    ]

    if len(queue_events) > 30:
        anomalies.append({
            "type": "HIGH_QUEUE_ACTIVITY",
            "severity": "MEDIUM"
        })

    return anomalies