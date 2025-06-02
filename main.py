from flask import send_file
import pandas as pd
import sqlite3
import os
import json
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from monitor import check_site
from collections import defaultdict

# Carrega lista de sites
with open("sites.json") as f:
    sites = json.load(f)

# Função para calcular uptime com base no banco SQLite
def calculate_uptime():
    if not os.path.exists("monitor.db"):
        return {}

    conn = sqlite3.connect("monitor.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url, status FROM logs")
    logs = cursor.fetchall()
    conn.close()

    stats = defaultdict(lambda: {"up": 0, "total": 0})

    for url, status in logs:
        stats[url]["total"] += 1
        if status == "200":
            stats[url]["up"] += 1

    return {
        url: round((stat["up"] / stat["total"]) * 100, 1)
        for url, stat in stats.items()
    }

# Cria app Dash
app = dash.Dash(__name__)
app.title = "Site Monitor"

# Rota para exportar CSV
@app.server.route("/export")
def export_csv():
    if not os.path.exists("monitor.db"):
        return "Banco de dados não encontrado.", 404

    conn = sqlite3.connect("monitor.db")
    df = pd.read_sql_query("SELECT * FROM logs", conn)
    conn.close()

    csv_path = "export.csv"
    df.to_csv(csv_path, index=False)

    return send_file(csv_path, mimetype='text/csv', as_attachment=True)

# Layout da interface
app.layout = html.Div([
    html.H1("🔍 Monitor de Sites"),
    html.Button("Atualizar", id="refresh-btn"),
    html.Div(id="status-table"),
    html.Br(),
    html.A("📥 Exportar histórico em CSV", href="/export", target="_blank")
])

# Callback para atualizar a tabela
@app.callback(
    Output("status-table", "children"),
    [Input("refresh-btn", "n_clicks")]
)
def update_status(n):
    results = [check_site(site) for site in sites]
    uptime = calculate_uptime()

    return html.Table([
        html.Tr([html.Th("URL"), html.Th("Status"), html.Th("Tempo (s)"), html.Th("Uptime (%)")])
    ] + [
        html.Tr([
            html.Td(res["url"]),
            html.Td(res["status"], style={"color": "green" if res["status"] == "200" else "red"}),
            html.Td(res["response_time"] if res["response_time"] else "-"),
            html.Td(f"{uptime.get(res['url'], 0)}%")
        ]) for res in results
    ])

if __name__ == "__main__":
    app.run(debug=True)
