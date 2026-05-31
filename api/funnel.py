def calculate_funnel(events):

    visitors = set()

    billing_visitors = set()

    for event in events:

        if "visitor_id" in event:
            visitors.add(event["visitor_id"])

        if event.get("camera_id") == "CAM_5":
            billing_visitors.add(
                event.get("visitor_id", "UNKNOWN")
            )

    return {
        "store_entries": len(visitors),
        "billing_visitors": len(billing_visitors)
    }