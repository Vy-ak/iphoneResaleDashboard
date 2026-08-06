import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.models.types import capture

# DESIGN TOKENS — Fintech Terminal
BG_BASE       = "#0a0e14"
BG_SURFACE    = "#11161f"
BG_SURFACE_2  = "#161c28"
BORDER        = "#1c2433"
BORDER_SOFT   = "#161d2a"
TEXT_PRIMARY  = "#e8edf4"
TEXT_MUTED    = "#5a6b85"
TEXT_FAINT    = "#384357"

ACCENT_CYAN   = "#00d4ff"
ACCENT_BLUE   = "#3b82f6"
SEMANTIC_UP   = "#00e6a8"
SEMANTIC_DOWN = "#ff4d6d"
SEMANTIC_GOLD = "#ffb340"

SEQ_SCALE = [
    [0.0, "#0a2540"],
    [0.25, "#0f3d63"],
    [0.5, "#1a6b9e"],
    [0.75, "#3aa8d8"],
    [1.0, "#5ee3ff"],
]

KATEGORIKAL_PALETTE = [
    "#00d4ff", "#ff4d6d", "#ffb340", "#00e6a8",
    "#a78bfa", "#3b82f6", "#f97316", "#34d399",
    "#fb7185", "#60a5fa", "#fbbf24", "#2dd4bf",
    "#c084fc", "#f472b6", "#22d3ee", "#facc15",
]

# ── INJEKTOR CSS OTOMATIS (Bisa berjalan di VPS) ──
# Dapatkan direktori tempat file python ini berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

os.makedirs(ASSETS_DIR, exist_ok=True)
_css = f"""
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&family=Inter:wght@400;500;600;700&display=swap');

html, body, #react-entry-point {{
    height: auto !important;
    min-height: 100vh !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    background: {BG_BASE} !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(0,212,255,0.06), transparent),
        radial-gradient(ellipse 60% 40% at 100% 100%, rgba(59,130,246,0.04), transparent) !important;
    font-family: 'Inter', sans-serif !important;
}}

div[class*='outer-wrapper'], div[class*='OuterWrapper'],
div[class*='page-wrapper'], div[class*='PageWrapper'],
div[class*='Layout'], div[class*='layout-main'], .layout-main {{
    display: flex !important;
    flex-direction: row !important;
    width: 100vw !important;
    max-width: 100vw !important;
    height: auto !important;
    overflow: visible !important;
    padding: 0 !important;
    margin: 0 !important;
}}

div[class*='Sidebar'], div[class*='sidebar'], aside[class*='sidebar'],
nav[class*='sidebar'], .sidebar, [data-testid="sidebar"],
button[class*='collapse'], button[class*='Collapse'],
button[class*='toggle'], button[class*='Toggle'],
div[class*='collapse-btn'], div[class*='SidebarToggle'],
div[class*='sidebar-toggle'], div[class*='chevron'],
div[class*='Chevron'], div[class*='arrow'],
[class*='sidebar-button'], [class*='sidebar_button'] {{
    display: none !important;
    width: 0 !important;
    min-width: 0 !important;
    max-width: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: hidden !important;
    flex: 0 0 0 !important;
    border: none !important;
    opacity: 0 !important;
    pointer-events: none !important;
}}

div[class*='PageContent'], #page-content, div[class*='page-content'],
div[class*='PageInner'], div[class*='page-inner'],
.page-content-container, [data-testid="page-content"] {{
    height: auto !important;
    min-height: 100vh !important;
    display: block !important;
    overflow-y: visible !important;
    overflow-x: hidden !important;
    padding: 8px 12px !important;
    max-width: 100% !important;
    width: 100% !important;
    margin-left: 0 !important;
    flex: 1 1 100% !important;
    box-sizing: border-box !important;
}}

div[class*='Grid'], div[class*='grid'], .grid-container {{
    width: 100% !important;
    max-width: 100% !important;
    overflow: visible !important;
    height: auto !important;
    align-content: start !important;
    grid-template-rows: max-content max-content max-content max-content !important;
    gap: 24px 16px !important;
}}

div[class*='Grid'] > div, div[class*='grid'] > div {{
    overflow: visible !important;
    height: auto !important;
    min-height: 0 !important;
    box-sizing: border-box !important;
}}

.dash-graph, .js-plotly-plot, div[class*='graph-container'], .graph-container {{
    width: 100% !important;
    overflow: visible !important;
    box-sizing: border-box !important;
    height: auto !important;
}}

header, div[class*='Header'], div[class*='NavBar'], nav[class*='NavBar'] {{
    position: relative !important;
    z-index: 10 !important;
    width: 100% !important;
    box-sizing: border-box !important;
    background: {BG_SURFACE} !important;
    border-bottom: 1px solid {BORDER} !important;
}}

div[class*='Header'] h1, header h1, div[class*='NavBar'] *[class*='title'] {{
    font-family: 'JetBrains Mono', monospace !important;
    letter-spacing: 0.02em !important;
    font-weight: 700 !important;
}}

#chart_kpi_all, #chart_price_dist, #chart_listing_volume, #chart_geo, #chart_comp_matrix {{
    border: 1px solid {BORDER} !important;
    border-radius: 12px !important;
    background: linear-gradient(180deg, {BG_SURFACE_2} 0%, {BG_SURFACE} 100%) !important;
    padding: 4px !important;
    position: relative !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.02) !important;
}}

#chart_price_dist::before, #chart_listing_volume::before,
#chart_geo::before, #chart_comp_matrix::before {{
    content: '' !important;
    position: absolute !important;
    top: 0 !important; left: 12px !important; right: 12px !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, {ACCENT_CYAN}55, transparent) !important;
}}

#chart_kpi_all {{
    border-left: 3px solid {ACCENT_CYAN} !important;
    border-top: 1px solid {ACCENT_CYAN}66 !important;
    background: linear-gradient(135deg, #0d1a2e 0%, #0a1628 60%, #0d1f35 100%) !important;
    box-shadow: 0 4px 32px rgba(0,212,255,0.12), 0 0 0 1px rgba(0,212,255,0.08) !important;
    height: 140px !important;
    min-height: 140px !important;
}}
#chart_kpi_all .dash-graph, #chart_kpi_all .js-plotly-plot {{
    height: 140px !important;
    min-height: 140px !important;
    max-height: 140px !important;
}}

#chart_price_dist, #chart_listing_volume {{ min-height: 460px !important; }}
#chart_price_dist .dash-graph, #chart_price_dist .js-plotly-plot,
#chart_listing_volume .dash-graph, #chart_listing_volume .js-plotly-plot {{
    height: 460px !important; min-height: 460px !important;
}}

#chart_geo, #chart_comp_matrix {{ min-height: 420px !important; }}
#chart_geo .dash-graph, #chart_geo .js-plotly-plot,
#chart_comp_matrix .dash-graph, #chart_comp_matrix .js-plotly-plot {{
    height: 420px !important; min-height: 420px !important;
}}

.meta-footer, #chart_meta_footer {{
    color: {TEXT_MUTED} !important;
    font-size: 11px !important;
    font-family: 'JetBrains Mono', monospace !important;
    text-align: center !important;
    padding: 16px 8px 4px 8px !important;
    border-top: 1px solid {BORDER_SOFT} !important;
    margin-top: 6px !important;
    line-height: 1.7 !important;
    opacity: 0.85 !important;
}}

::-webkit-scrollbar {{ width: 8px; height: 8px; }}
::-webkit-scrollbar-track {{ background: {BG_BASE}; }}
::-webkit-scrollbar-thumb {{ background: {BORDER}; border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: {ACCENT_BLUE}; }}
"""
# Tulis file CSS ke folder assets
css_path = os.path.join(ASSETS_DIR, "custom_dashboard_style.css")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(_css)


# ── PEMBACAAN DATA ────────────────────────────────────────────────────────────
DATA_PATH = os.path.join(BASE_DIR, "data", "iphone_resale_dashboard_ready.csv")
df = pd.read_csv(DATA_PATH)

# PERBAIKAN MAP: pastikan kolom us_state berisi kode 2 huruf yang valid
if "us_state" not in df.columns:
    df["us_state"] = df["location"].str.extract(r",\s*([A-Z]{2})\s*(?:,|$)")

df["us_state"] = (
    df["us_state"]
    .astype(str)
    .str.upper()
    .str.strip()
)

VALID_STATES = {
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
    "KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
    "VA","WA","WV","WI","WY","DC"
}
df["us_state"] = df["us_state"].where(df["us_state"].isin(VALID_STATES), other=np.nan)

if "location" not in df.columns:
    df["location"] = df["us_state"]

warna_custom  = {"Pro": SEMANTIC_DOWN, "Standard": SEMANTIC_UP}
global_layout = dict(
    paper_bgcolor=BG_SURFACE,
    plot_bgcolor=BG_SURFACE,
    font_color=TEXT_PRIMARY,
    font_family="Inter, sans-serif",
    template="plotly_dark",
    legend=dict(title=dict(text="Tipe iPhone"), orientation="v")
)


# HELPER KPI
def make_kpi_row(labels, values, colors, subs):
    n    = len(labels)
    pad  = 0.12
    step = (1 - 2 * pad) / (n - 1)
    xs   = [pad + i * step for i in range(n)]
    fig  = go.Figure()

    for i in range(n):
        fig.add_annotation(x=xs[i], y=0.86, text="<b>{}</b>".format(labels[i]),
            showarrow=False, xanchor="center", yanchor="top",
            xref="paper", yref="paper",
            font=dict(size=12, color="#e8edf4", family="Inter, sans-serif"))
        fig.add_annotation(x=xs[i], y=0.46, text="<b>{}</b>".format(values[i]),
            showarrow=False, xanchor="center", yanchor="middle",
            xref="paper", yref="paper",
            font=dict(size=38, color=colors[i], family="JetBrains Mono, monospace"))
        fig.add_annotation(x=xs[i], y=0.12, text=subs[i],
            showarrow=False, xanchor="center", yanchor="top",
            xref="paper", yref="paper",
            font=dict(size=10.5, color="#8fadc7", family="Inter, sans-serif"))
        if i < n - 1:
            mid = (xs[i] + xs[i+1]) / 2
            fig.add_shape(type="line", x0=mid, x1=mid, y0=0.1, y1=0.9,
                xref="paper", yref="paper", line=dict(color=BORDER, width=1))

    fig.update_layout(
        paper_bgcolor="#0d1a2e", plot_bgcolor="#0d1a2e",
        height=140, margin=dict(l=20, r=20, t=10, b=10),
        xaxis=dict(visible=False, range=[0, 1]),
        yaxis=dict(visible=False, range=[0, 1]),
        showlegend=False,
    )
    return fig


@capture('graph')
def kpi_all(data_frame):
    d = data_frame
    n = len(d)
    return make_kpi_row(
        labels=["TOTAL LISTING", "RATA-RATA HARGA LISTING", "TOTAL TERJUAL", "STOK TERSEDIA"],
        values=[
            "{:,}".format(n),
            "${:,.0f}".format(d["price"].mean() if n else 0),
            "{:,}".format(int(d["sold"].sum())),
            "{:,}".format(int(d["available"].sum()))
        ],
        colors=[ACCENT_CYAN, SEMANTIC_GOLD, ACCENT_BLUE, ACCENT_BLUE],
        subs=[
            "{} model, {} wilayah".format(d["model_family"].nunique(), d["us_state"].nunique()),
            "Rata-rata harga pasar",
            "Unit terjual di platform",
            "Stok aktif saat ini"
        ]
    )


@capture('graph')
def pilar1(data_frame):
    top_models = data_frame['model_family'].value_counts().nlargest(12).reset_index()
    top_models.columns = ["model_family", "count"]
    fig = px.bar(
        top_models, x="model_family", y="count",
        title="Volume & Saturasi Listing Resale iPhone per Model — Tingkat Kepadatan Pasar",
        labels={"count": "Total Listing Aktif", "model_family": "Model iPhone"},
        color="count", color_continuous_scale=SEQ_SCALE
    )
    fig.update_layout(**global_layout, height=460, margin=dict(l=80, r=80, t=55, b=10), autosize=True,
                      title_font=dict(size=13, family="JetBrains Mono, monospace", color=TEXT_PRIMARY))
    fig.update_xaxes(title_text="Model iPhone", tickangle=-30, tickfont_size=11, gridcolor=BORDER_SOFT, automargin=True)
    fig.update_yaxes(title_text="Jumlah Listing", tickfont_size=11, gridcolor=BORDER_SOFT)
    fig.update_coloraxes(colorbar_title_text="Volume")
    return fig


@capture('graph')
def pilar2(data_frame):
    fig = px.box(
        data_frame, x="model_family", y="price", color="iphone_type",
        color_discrete_map=warna_custom,
        title="Distribusi Harga Listing Resale iPhone per Model — Perbandingan Tipe Pro vs Standard",
        labels={"model_family": "Model iPhone", "price": "Rentang Harga Listing (USD)", "iphone_type": "Tipe iPhone"}
    )

    for trace in fig.data:
        trace.hovertemplate = "<b>%{x}</b><br>Median: $%{median:,.0f}<br>Tertinggi: $%{upperfence:,.0f}<extra></extra>"
        trace.hoveron = "boxes"

    fig.update_layout(
        **global_layout, height=460, margin=dict(l=80, r=60, t=55, b=10),
        autosize=True, hovermode="x",
        title_font=dict(size=13, family="JetBrains Mono, monospace", color=TEXT_PRIMARY),
    )
    fig.update_xaxes(title_text="Model iPhone", tickangle=-30, tickfont_size=11, gridcolor=BORDER_SOFT, automargin=True)
    fig.update_yaxes(title_text="Harga Listing (USD)", tickfont_size=11, gridcolor=BORDER_SOFT)
    return fig


@capture('graph')
def pilar3(data_frame):
    comp_df = data_frame.groupby('model_family')[['top_seller_dominance', 'price_gap']].mean().reset_index()
    fig = px.scatter(
        comp_df, x="top_seller_dominance", y="price_gap", size="top_seller_dominance", color="model_family",
        title="Matriks Kompetisi Listing Resale iPhone — Dominasi Penjual vs Selisih Harga per Model",
        labels={"top_seller_dominance": "Dominasi Penjual Utama (%)", "price_gap": "Selisih Rentang Harga Listing (USD)", "model_family": "Model iPhone"},
        color_discrete_sequence=KATEGORIKAL_PALETTE,
    )
    fig.update_layout(**global_layout, height=420, margin=dict(l=80, r=60, t=55, b=8), autosize=True,
                      title_font=dict(size=13, family="JetBrains Mono, monospace", color=TEXT_PRIMARY))
    fig.update_xaxes(title_text="Dominasi Penjual Terbesar (%)", tickfont_size=11, gridcolor=BORDER_SOFT)
    fig.update_yaxes(title_text="Selisih Harga Listing (USD)", tickfont_size=11, gridcolor=BORDER_SOFT)
    return fig


@capture('graph')
def pilar4(data_frame):
    state_market = (
        data_frame
        .dropna(subset=["us_state"])
        .groupby("us_state")
        .size()
        .reset_index(name="Total Listing")
    )
    fig = px.choropleth(
        state_market,
        locations="us_state",
        locationmode="USA-states",
        color="Total Listing",
        scope="usa",
        title="Persebaran Geografis Listing Resale iPhone per Negara Bagian (USA)",
        labels={"Total Listing": "Total Listing Terdaftar", "us_state": "Negara Bagian"},
        color_continuous_scale=SEQ_SCALE
    )
    fig.update_layout(
        **global_layout, height=420, margin=dict(l=40, r=40, t=55, b=8), autosize=True,
        title_font=dict(size=13, family="JetBrains Mono, monospace", color=TEXT_PRIMARY),
        geo=dict(
            bgcolor=BG_SURFACE, lakecolor=BG_SURFACE,
            landcolor=BG_SURFACE_2, subunitcolor=BORDER, showlakes=True
        )
    )
    fig.update_coloraxes(colorbar_title_text="Jumlah Listing")
    return fig


# META INFORMATION
meta_text = """
**SUMBER DATA** · Dataset listing resale iPhone pada platform e-commerce (USA, 2026) &nbsp;|&nbsp; **PEMBARUAN TERAKHIR** · Sesuai tanggal generate dashboard

**CATATAN METODOLOGI** · Nilai outlier disaring menggunakan metode IQR (Interquartile Range, 1.5×) untuk menjaga representasi data yang valid.

Dashboard ini disusun untuk penelitian *"Perancangan Dashboard Market Intelligence untuk Analisis Persaingan Listing Resale iPhone pada Platform E-Commerce Menggunakan Vizro"*.
"""


# DEPLOYMENT
page_overview = vm.Page(
    title="Market Intelligence · Persaingan Listing Resale iPhone pada Platform E-Commerce",
    layout=vm.Layout(
        grid=[
            [0, 0],
            [1, 2],
            [3, 4],
            [5, 5],
        ],
        row_gap="24px",
        col_gap="16px",
        row_min_height="0px",
    ),
    components=[
        vm.Graph(id="chart_kpi_all",        figure=kpi_all(data_frame=df)),
        vm.Graph(id="chart_listing_volume", figure=pilar1(data_frame=df)),
        vm.Graph(id="chart_price_dist",     figure=pilar2(data_frame=df)),
        vm.Graph(id="chart_comp_matrix",    figure=pilar3(data_frame=df)),
        vm.Graph(id="chart_geo",            figure=pilar4(data_frame=df)),
        vm.Text(id="chart_meta_footer",     text=meta_text),
    ],
    controls=[
        vm.Filter(column="iphone_type",      selector=vm.Checklist(title="Tipe iPhone")),
        vm.Filter(column="generation_group", selector=vm.Checklist(title="Kelompok Generasi iPhone")),
        vm.Filter(column="condition_group",  selector=vm.Checklist(title="Kondisi iPhone")),
        vm.Filter(column="location",         selector=vm.Dropdown(title="Filter Negara Bagian")),
    ]
)

dashboard = vm.Dashboard(
    title="DASHBOARD MARKET INTELLIGENCE — ANALISIS PERSAINGAN LISTING RESALE IPHONE",
    pages=[page_overview]
)

vizro_app = Vizro()
vizro_app.build(dashboard)

app = vizro_app.dash.server

if __name__ == "__main__":
    vizro_app.run()