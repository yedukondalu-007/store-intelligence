def generate_heatmap(events):

    zones = {}

    for event in events:

        zone = event.get("zone_id", "UNKNOWN")

        zones[zone] = zones.get(zone, 0) + 1

    return zones