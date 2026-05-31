def calculate_metrics(events):

    visitors = set()

    billing_events = 0

    for event in events:

        if "visitor_id" in event:
            visitors.add(event["visitor_id"])

        if event.get("event_type") == "QUEUE_SNAPSHOT":
            billing_events += 1

    return {
        "unique_visitors": len(visitors),
        "total_events": len(events),
        "billing_events": billing_events
    }