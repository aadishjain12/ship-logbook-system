from markupsafe import escape

def safe_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return 0.0

def generate_report(logs):
    # HTML Table rows
    rows = "".join([
        f"<tr class='hover:bg-gray-100'>"
        f"<td class='border px-4 py-2'>{escape(log.timestamp)}</td>"
        f"<td class='border px-4 py-2'>{escape(log.ship_id)}</td>"
        f"<td class='border px-4 py-2'>{safe_float(log.latitude):.2f}</td>"
        f"<td class='border px-4 py-2'>{safe_float(log.longitude):.2f}</td>"
        f"<td class='border px-4 py-2'>{escape(log.speed or '0')}</td>"
        f"<td class='border px-4 py-2'>{escape(log.weather or 'N/A')}</td>"
        f"<td class='border px-4 py-2'>{escape(log.voice_log or '')}</td>"
        f"</tr>"
        for log in logs
    ])

    # Chart data for Chart.js
    chart_data = {
        'labels': [
            log.timestamp.split("T")[0] if log.timestamp and "T" in log.timestamp else "Unknown"
            for log in logs
        ],
        'speeds': [
            float(log.speed) if log.speed and str(log.speed).replace('.', '', 1).isdigit() else 0
            for log in logs
        ]
    }

    # Map data for Leaflet.js
    map_data = [
        {
            'lat': safe_float(log.latitude),
            'lon': safe_float(log.longitude),
            'info': f"{log.timestamp or 'Unknown'}: {log.speed or '0'} knots"
        }
        for log in logs
    ]

    # HTML table
    html_table = f"""
    <table class='table-auto border-collapse border border-gray-300 w-full text-sm'>
        <thead>
            <tr class='bg-gray-200'>
                <th class='border px-4 py-2'>Timestamp</th>
                <th class='border px-4 py-2'>Ship ID</th>
                <th class='border px-4 py-2'>Latitude</th>
                <th class='border px-4 py-2'>Longitude</th>
                <th class='border px-4 py-2'>Speed</th>
                <th class='border px-4 py-2'>Weather</th>
                <th class='border px-4 py-2'>Voice Log</th>
            </tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>
    """

    return html_table, chart_data, map_data
