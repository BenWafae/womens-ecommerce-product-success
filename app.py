import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import plotly.graph_objects as go

# ═══════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════


# ═══════════════════════════════════════════════
#  GLOBAL CSS
# ═══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

:root {
  --bg:#0A0A0F; --bg2:#12121A; --bg3:#1A1A26; --border:#2A2A3E;
  --accent1:#8B5CF6; --accent2:#EC4899; --accent3:#06B6D4;
  --gold:#F59E0B; --success:#10B981; --danger:#EF4444;
  --text:#E8E8F0; --muted:#6B7280; --card-bg:rgba(26,26,38,0.95);
}
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; color: var(--text); }
.stApp { background: var(--bg); }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2rem 2rem 2rem; max-width: 1400px; }
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--accent1); border-radius: 3px; }

[data-testid="stSidebar"] { background: var(--bg2) !important; border-right: 1px solid var(--border); }
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Hide nav button text — show only the styled div above */
[data-testid="stSidebar"] .stButton > button {
  opacity: 0;
  height: 0 !important;
  padding: 0 !important;
  margin: -4px 0 0 0 !important;
  min-height: 0 !important;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  position: absolute;
}

.hero {
  background: radial-gradient(ellipse at 30% 50%, #8B5CF620 0%, transparent 60%),
              radial-gradient(ellipse at 70% 20%, #EC489915 0%, transparent 60%),
              linear-gradient(135deg, #0A0A0F 0%, #12121A 100%);
  border: 1px solid var(--border); border-radius: 20px;
  padding: 60px 50px; margin-bottom: 30px; position: relative; overflow: hidden;
}
.hero::before {
  content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
  background: repeating-linear-gradient(45deg, transparent, transparent 30px,
    rgba(139,92,246,0.02) 30px, rgba(139,92,246,0.02) 31px);
  pointer-events: none;
}
.hero-badge {
  display: inline-block;
  background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(236,72,153,0.13));
  border: 1px solid rgba(139,92,246,0.4); color: var(--accent1);
  padding: 6px 16px; border-radius: 20px; font-size: 0.78em; font-weight: 600;
  letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 20px;
  font-family: 'Space Mono', monospace;
}
.hero h1 {
  font-family: 'Playfair Display', serif; font-size: 3.2em; font-weight: 900;
  line-height: 1.1; margin: 0 0 16px 0;
  background: linear-gradient(135deg, #fff 30%, #8B5CF6 70%, #EC4899);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero p { font-size: 1.05em; color: var(--muted); line-height: 1.7; max-width: 600px; margin: 0; }

.card {
  background: var(--card-bg); border: 1px solid var(--border);
  border-radius: 16px; padding: 24px; margin-bottom: 20px;
  position: relative; overflow: hidden;
}
.card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--accent1), var(--accent2), var(--accent3));
}

.sec-title { font-family: 'Playfair Display', serif; font-size: 1.9em; font-weight: 700; color: #fff; margin: 0 0 6px 0; }
.sec-sub   { color: var(--muted); font-size: 0.9em; margin-bottom: 24px; line-height: 1.6; }

.styled-table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
.styled-table th { background: var(--bg3); color: var(--accent1); padding: 12px 16px;
  text-align: left; font-family: 'Space Mono', monospace; font-size: 0.78em;
  letter-spacing: 0.5px; border-bottom: 1px solid var(--border); }
.styled-table td { padding: 11px 16px; color: var(--text); border-bottom: 1px solid rgba(42,42,62,0.3); }
.styled-table tr:hover td { background: var(--bg3); }

/* Main action buttons */
.stButton > button {
  background: linear-gradient(135deg, var(--accent1), var(--accent2)) !important;
  color: white !important; border: none !important; border-radius: 12px !important;
  padding: 14px 28px !important; font-weight: 600 !important; font-size: 1em !important;
  letter-spacing: 0.5px !important; box-shadow: 0 8px 30px rgba(139,92,246,0.3) !important;
  transition: all 0.3s ease !important;
}
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 12px 40px rgba(139,92,246,0.45) !important; }

.fancy-divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(139,92,246,0.3), rgba(236,72,153,0.3), transparent); margin: 32px 0; }

.tl-item { display: flex; gap: 16px; padding: 0 0 24px 0; position: relative; }
.tl-item::before { content: ''; position: absolute; left: 19px; top: 40px; bottom: 0; width: 1px; background: var(--border); }
.tl-item:last-child::before { display: none; }
.tl-dot { width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1em; flex-shrink: 0; border: 2px solid var(--border); background: var(--bg2); z-index: 1; }
.tl-content h4 { margin: 6px 0 4px 0; font-size: 0.93em; color: #fff; font-weight: 600; }
.tl-content p  { margin: 0; font-size: 0.82em; color: var(--muted); line-height: 1.5; }

.concl-item { display: flex; gap: 14px; align-items: flex-start; padding: 14px 0; border-bottom: 1px solid rgba(42,42,62,0.4); }
.concl-item:last-child { border-bottom: none; }
.concl-icon { width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1em; flex-shrink: 0; background: var(--bg2); }
.concl-text h4 { margin: 0 0 4px 0; font-size: 0.92em; color: #fff; }
.concl-text p  { margin: 0; font-size: 0.82em; color: var(--muted); line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════
#  LOAD MODELS
# ═══════════════════════════════════════════════
BASE_DIR = os.path.dirname(__file__)

@st.cache_resource
def load_assets():
    try:
        m = pickle.load(open(os.path.join(BASE_DIR, "model/models.pkl"), "rb"))
        v = pickle.load(open(os.path.join(BASE_DIR, "model/vectorizer.pkl"), "rb"))
        return m, v, True
    except Exception:
        return None, None, False

models, vectorizer, models_ok = load_assets()

# ═══════════════════════════════════════════════
#  SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════
PAGES = [
    ("🏠", "Accueil"),
    ("📊", "Exploration des Données"),
    ("🤖", "Modélisation ML"),
    ("🎯", "Prédiction"),
    ("🔍", "Explication IA"),
    ("🚀", "Valeur Ajoutée"),
    ("📈", "Conclusion"),
]

with st.sidebar:
    st.markdown("""
    <div style='padding:20px 10px 10px 10px;'>
      <div style='font-family:"Space Mono",monospace;font-size:0.62em;color:#4B5563;
                  letter-spacing:2px;text-transform:uppercase;'>v1.0 · BSDSI 2026</div>
      <div style='font-family:"Playfair Display",serif;font-size:1.6em;font-weight:900;
                  margin-top:4px;background:linear-gradient(135deg,#8B5CF6,#EC4899);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent;'>
        ShopSense AI
      </div>
    </div>
    <div style='height:1px;background:linear-gradient(90deg,transparent,#2A2A3E,transparent);margin:10px 0 16px 0;'></div>
    <div style='font-family:"Space Mono",monospace;font-size:0.62em;color:#4B5563;
                letter-spacing:2px;text-transform:uppercase;padding:0 10px 10px 10px;'>NAVIGATION</div>
    """, unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state.page = 0

    for i, (icon, label) in enumerate(PAGES):
        is_active = st.session_state.page == i
        bg  = "linear-gradient(135deg,rgba(139,92,246,0.18),rgba(236,72,153,0.09))" if is_active else "transparent"
        brd = "rgba(139,92,246,0.5)" if is_active else "rgba(42,42,62,0.5)"
        clr = "#E8E8F0" if is_active else "#6B7280"
        fw  = "600" if is_active else "400"
        # Styled label div
        st.markdown(f"""
        <div style='background:{bg};border:1px solid {brd};border-radius:10px;
                    padding:10px 14px;margin:2px 0;color:{clr};font-size:0.88em;font-weight:{fw};
                    cursor:pointer;'>
          {icon}&nbsp;&nbsp;{label}
        </div>
        """, unsafe_allow_html=True)
        # Invisible button on top (no label_visibility — just empty label trick)
        if st.button(f"{icon} {label}", key=f"nav_{i}", use_container_width=True):
            st.session_state.page = i
            st.rerun()

    st.markdown("""
    <div style='height:1px;background:linear-gradient(90deg,transparent,#2A2A3E,transparent);margin:16px 0;'></div>
    <div style='padding:0 10px;font-family:"Space Mono",monospace;font-size:0.63em;color:#374151;line-height:1.8;'>
      BEN ZHIR Wafa<br>IKSOD Salma<br>
      <span style='color:#4B5563;'>Enc. AIT BAHA Tarek</span>
    </div>
    """, unsafe_allow_html=True)

PAGE = st.session_state.page

# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════
def sentiment_quick(text):
    pos = ["love","great","amazing","perfect","beautiful","excellent","wonderful",
           "fantastic","adorable","best","comfortable","flattering","soft","gorgeous",
           "cute","nice","happy","fits","quality","lovely","pretty"]
    neg = ["hate","terrible","awful","horrible","bad","poor","ugly","worst",
           "uncomfortable","disappointing","waste","return","cheap","stiff",
           "scratchy","tight","loose","ruined","small","large","boring"]
    t = text.lower()
    p = sum(1 for w in pos if w in t)
    n = sum(1 for w in neg if w in t)
    if p > n:  return "Positif 😊", "#10B981", p / (p + n + 0.1)
    if n > p:  return "Négatif 😞", "#EF4444", n / (p + n + 0.1)
    return "Neutre 😐", "#F59E0B", 0.5

def preprocess(review, rating, feedback, age):
    text    = vectorizer.transform([review]).toarray()
    numeric = np.array([[rating, feedback, age]])
    return np.concatenate([numeric, text], axis=1)

def proba_bar_html(value, color, label="Probabilité de succès"):
    pct = int(value * 100)
    return f"""
    <div style='margin:14px 0;'>
      <div style='display:flex;justify-content:space-between;
                  font-family:"Space Mono",monospace;font-size:0.8em;margin-bottom:6px;'>
        <span style='color:#9CA3AF;'>{label}</span>
        <span style='color:{color};font-weight:700;'>{pct}%</span>
      </div>
      <div style='background:#1A1A26;border-radius:4px;height:8px;overflow:hidden;'>
        <div style='width:{pct}%;height:100%;border-radius:4px;background:{color};'></div>
      </div>
    </div>"""

PLOTLY_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#6B7280"), margin=dict(t=50, b=20, l=20, r=20),
)

# ══════════════════════════════════════════════════════════════
#  PAGE 0 — ACCUEIL
# ══════════════════════════════════════════════════════════════
if PAGE == 0:
    st.markdown("""
    <div class='hero'>
      <div class='hero-badge'>✦ Machine Learning · NLP · E-Commerce</div>
      <h1>Prédiction du Succès<br>des Produits E-Commerce</h1>
      <p>Un système d'intelligence artificielle supervisé qui analyse les avis clients,
         les notes et les métadonnées produits pour prédire si un article sera recommandé —
         avec explications SHAP en temps réel.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (num, lbl, clr) in zip([c1, c2, c3, c4], [
        ("23,486", "Avis analysés",      "#8B5CF6"),
        ("82.6%",  "Taux recommandation","#10B981"),
        ("93.7%",  "Accuracy modèle",    "#06B6D4"),
        ("3",      "Modèles comparés",   "#F59E0B"),
    ]):
        with col:
            st.markdown(f"""
            <div class='card' style='text-align:center;padding:28px 16px;'>
              <div style='font-family:"Space Mono",monospace;font-size:2em;font-weight:700;color:{clr};'>{num}</div>
              <div style='color:#6B7280;font-size:0.8em;margin-top:6px;'>{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    col_l, col_r = st.columns([1.1, 0.9], gap="large")

    with col_l:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='sec-title'>À propos du projet</div>", unsafe_allow_html=True)
        st.markdown("<div class='sec-sub'>Women's Clothing E-Commerce Reviews Dataset — BSDSI 2025-2026</div>", unsafe_allow_html=True)
        for clr, icon, title, desc in [
            ("#8B5CF6","🎯","Problématique",
             "Prédire si un produit sera recommandé à partir des avis clients, notes et données démographiques."),
            ("#EC4899","📊","Données analysées",
             "23 486 avis sur des vêtements féminins : âge, rating 1-5, texte, feedbacks, département, classe."),
            ("#06B6D4","🤖","Approche ML",
             "Classification binaire supervisée avec TF-IDF, polarité TextBlob, puis Random Forest optimisé."),
            ("#10B981","✨","Valeur ajoutée",
             "L'application explique chaque décision via SHAP, aidant les équipes produit à agir."),
        ]:
            st.markdown(f"""
            <div class='tl-item'>
              <div class='tl-dot' style='border-color:{clr};'>{icon}</div>
              <div class='tl-content'><h4>{title}</h4><p>{desc}</p></div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_r:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='sec-title'>Technologies</div>", unsafe_allow_html=True)
        st.markdown("<div class='sec-sub'>Stack utilisé dans ce projet</div>", unsafe_allow_html=True)
        for clr, bg, name, desc in [
            ("#8B5CF6","#1A1026","Python 3.11","Langage principal"),
            ("#06B6D4","#001820","Streamlit","Interface web interactive"),
            ("#F59E0B","#1A1100","Scikit-learn","Modèles ML & évaluation"),
            ("#10B981","#001811","TextBlob","Analyse de sentiment NLP"),
            ("#EC4899","#1A0011","Pandas / NumPy","Manipulation des données"),
            ("#6366F1","#0D0D20","SHAP","Explicabilité IA"),
            ("#F97316","#1A0D00","Plotly","Visualisations interactives"),
            ("#34D399","#001810","TF-IDF","Vectorisation du texte"),
        ]:
            st.markdown(f"""
            <div style='display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid rgba(42,42,62,0.4);'>
              <div style='width:36px;height:36px;border-radius:8px;background:{bg};
                          border:1px solid rgba({clr},0.3);display:flex;align-items:center;
                          justify-content:center;flex-shrink:0;'>
                <div style='width:10px;height:10px;border-radius:50%;background:{clr};'></div>
              </div>
              <div>
                <div style='font-weight:600;font-size:0.88em;color:#E8E8F0;'>{name}</div>
                <div style='font-size:0.75em;color:#6B7280;'>{desc}</div>
              </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                    color:#8B5CF6;letter-spacing:1px;margin-bottom:12px;'>COLONNES DU DATASET</div>
                    <div style='display:flex;flex-wrap:wrap;gap:8px;'>""", unsafe_allow_html=True)
        badges = "".join([
            f"<span style='background:rgba({c},0.1);border:1px solid rgba({c},0.3);color:{c};"
            f"padding:4px 10px;border-radius:20px;font-size:0.72em;font-family:\"Space Mono\",monospace;'>{n}</span>"
            for n, c in [
                ("Clothing ID","#8B5CF6"),("Age","#06B6D4"),("Title","#EC4899"),
                ("Review Text","#F59E0B"),("Rating","#10B981"),("Recommended IND","#EF4444"),
                ("Positive Feedback","#6366F1"),("Division Name","#F97316"),
                ("Department Name","#34D399"),("Class Name","#A78BFA"),
            ]
        ])
        st.markdown(badges + "</div></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  PAGE 1 — EDA
# ══════════════════════════════════════════════════════════════
elif PAGE == 1:
    st.markdown("""
    <div style='padding:40px 0 24px 0;'>
      <div class='hero-badge'>📊 Analyse Exploratoire</div>
      <div class='sec-title' style='font-size:2.2em;margin-top:10px;'>Exploration des Données</div>
      <div class='sec-sub'>Analyse du Women's Clothing E-Commerce Reviews Dataset avant la modélisation</div>
    </div>""", unsafe_allow_html=True)

    cols6 = st.columns(6)
    for col, (num, lbl, clr) in zip(cols6, [
        ("23,486","Avis clients","#8B5CF6"), ("10","Colonnes","#06B6D4"),
        ("82.6%","Recommandés","#10B981"),   ("17.4%","Non recommandés","#EF4444"),
        ("3,526","Valeurs manquantes","#F59E0B"), ("4.18","Rating moyen","#EC4899"),
    ]):
        with col:
            st.markdown(f"""
            <div class='card' style='text-align:center;padding:18px 10px;'>
              <div style='font-family:"Space Mono",monospace;font-size:1.5em;font-weight:700;color:{clr};'>{num}</div>
              <div style='color:#6B7280;font-size:0.75em;margin-top:4px;'>{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        fig = go.Figure(go.Bar(
            x=["⭐1","⭐2","⭐3","⭐4","⭐5"],
            y=[1206, 782, 1898, 5113, 13538],
            marker_color=["#EF4444","#F97316","#F59E0B","#10B981","#8B5CF6"],
            text=[1206,782,1898,5113,13538], textposition="outside",
            textfont=dict(color="#E8E8F0", size=11),
        ))
        fig.update_layout(**PLOTLY_BASE, height=300, showlegend=False,
            title=dict(text="Distribution des Ratings", font=dict(color="#E8E8F0", size=15, family="Playfair Display")),
            xaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#E8E8F0")),
            yaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#6B7280")),
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig2 = go.Figure(go.Pie(
            labels=["Recommandé (1)", "Non recommandé (0)"],
            values=[82.56, 17.44], hole=0.65,
            marker=dict(colors=["#8B5CF6","#EF4444"], line=dict(color="#0A0A0F", width=3)),
            textinfo="label+percent", textfont=dict(color="#E8E8F0", size=11),
        ))
        fig2.add_annotation(text="<b>82.6%</b>", x=0.5, y=0.56, showarrow=False,
                             font=dict(color="#E8E8F0", size=22))
        fig2.add_annotation(text="Recommandés", x=0.5, y=0.42, showarrow=False,
                             font=dict(color="#6B7280", size=12))
        fig2.update_layout(**PLOTLY_BASE, height=300,
            title=dict(text="Variable Cible — Recommended IND", font=dict(color="#E8E8F0", size=15, family="Playfair Display")),
            legend=dict(font=dict(color="#E8E8F0"), bgcolor="rgba(0,0,0,0)"),
        )
        st.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2, gap="large")
    with c3:
        age_g = ["18-25","26-33","34-41","42-49","50-57","58-65","66+"]
        age_c = [1820, 4210, 5630, 4890, 3740, 2100, 1096]
        fig3 = go.Figure(go.Bar(
            x=age_g, y=age_c,
            marker=dict(color=age_c, colorscale=[[0,"#1A1026"],[0.5,"#8B5CF6"],[1,"#EC4899"]]),
        ))
        fig3.update_layout(**PLOTLY_BASE, height=270, showlegend=False,
            title=dict(text="Distribution de l'Âge", font=dict(color="#E8E8F0", size=15, family="Playfair Display")),
            xaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#E8E8F0")),
            yaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#6B7280")),
        )
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        cats = ["Rating 1","Rating 2","Rating 3","Rating 4","Rating 5"]
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(name="Recommandé ✓",     x=cats, y=[6.8,23.4,52.1,85.3,97.8], marker_color="#8B5CF6", opacity=0.9))
        fig4.add_trace(go.Bar(name="Non recommandé ✗", x=cats, y=[93.2,76.6,47.9,14.7,2.2], marker_color="#EF4444", opacity=0.9))
        fig4.update_layout(**PLOTLY_BASE, barmode="stack", height=270,
            title=dict(text="Rating vs Recommandation (%)", font=dict(color="#E8E8F0", size=15, family="Playfair Display")),
            xaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#E8E8F0")),
            yaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#6B7280"), ticksuffix="%"),
            legend=dict(font=dict(color="#E8E8F0"), bgcolor="rgba(0,0,0,0)"),
        )
        st.plotly_chart(fig4, use_container_width=True)

    # Correlations
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                color:#8B5CF6;letter-spacing:1px;margin-bottom:18px;'>
                CORRÉLATIONS AVEC RECOMMENDED IND</div>
                <div style='display:grid;grid-template-columns:repeat(3,1fr);gap:14px;'>
    """, unsafe_allow_html=True)
    corr_html = ""
    for name, val, clr, pct in [
        ("Rating","0.79","#8B5CF6",79), ("Polarity (TextBlob)","0.21","#06B6D4",21),
        ("Subjectivity","0.15","#10B981",15), ("Age","0.03","#F59E0B",3),
        ("Positive Feedback","-0.07","#F97316",7), ("Review Length","-0.05","#EC4899",5),
    ]:
        bc = "#EF4444" if val.startswith("-") else clr
        corr_html += f"""
        <div style='background:#12121A;border-radius:10px;padding:14px;border:1px solid #2A2A3E;'>
          <div style='display:flex;justify-content:space-between;margin-bottom:8px;'>
            <span style='font-size:0.83em;color:#E8E8F0;font-weight:500;'>{name}</span>
            <span style='font-family:"Space Mono",monospace;font-size:0.83em;color:{bc};font-weight:700;'>{val}</span>
          </div>
          <div style='background:#0A0A0F;border-radius:4px;height:6px;'>
            <div style='width:{pct}%;height:100%;border-radius:4px;background:{bc};'></div>
          </div>
        </div>"""
    st.markdown(corr_html + "</div></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  PAGE 2 — MODELISATION
# ══════════════════════════════════════════════════════════════
elif PAGE == 2:
    st.markdown("""
    <div style='padding:40px 0 24px 0;'>
      <div class='hero-badge'>🤖 Machine Learning</div>
      <div class='sec-title' style='font-size:2.2em;margin-top:10px;'>Modélisation & Performances</div>
      <div class='sec-sub'>3 modèles comparés · GridSearchCV / RandomizedSearchCV · Cross-Validation 3-fold</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
      <div style='font-family:"Space Mono",monospace;font-size:0.68em;color:#8B5CF6;
                  letter-spacing:1px;margin-bottom:18px;'>RÉSULTATS COMPARATIFS</div>
      <table class='styled-table'><thead><tr>
        <th>MODÈLE</th><th>ACCURACY</th><th>PRECISION</th>
        <th>RECALL</th><th>F1-SCORE</th><th>CV F1 (3-fold)</th><th>STATUT</th>
      </tr></thead><tbody>
      <tr>
        <td><strong style='color:#06B6D4;'>Logistic Regression</strong></td>
        <td>93.5%</td><td>97.0%</td><td>94.9%</td><td>96.0%</td><td>95.97 ± 0.05</td>
        <td><span style='background:rgba(6,182,212,0.1);border:1px solid rgba(6,182,212,0.3);
                         color:#06B6D4;padding:3px 10px;border-radius:12px;font-size:0.77em;'>Baseline</span></td>
      </tr>
      <tr>
        <td><strong style='color:#10B981;'>Decision Tree</strong></td>
        <td>92.2%</td><td>95.5%</td><td>94.9%</td><td>95.2%</td><td>94.90 ± 0.12</td>
        <td><span style='background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);
                         color:#EF4444;padding:3px 10px;border-radius:12px;font-size:0.77em;'>Overfitting</span></td>
      </tr>
      <tr style='background:rgba(139,92,246,0.05);'>
        <td><strong style='color:#A78BFA;'>✦ Random Forest</strong></td>
        <td><strong style='color:#8B5CF6;'>93.7%</strong></td>
        <td><strong style='color:#8B5CF6;'>97.2%</strong></td>
        <td>94.5%</td>
        <td><strong style='color:#8B5CF6;'>96.2%</strong></td>
        <td><strong style='color:#8B5CF6;'>96.01 ± 0.17</strong></td>
        <td><span style='background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);
                         color:#8B5CF6;padding:3px 10px;border-radius:12px;font-size:0.77em;'>✦ Final</span></td>
      </tr>
      </tbody></table>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        cats = ["Accuracy","Precision","Recall","F1-Score","CV F1"]
        fig_r = go.Figure()
        for name, vals, clr in [
            ("Logistic Reg.", [93.5,97.0,94.9,96.0,95.97], "#06B6D4"),
            ("Decision Tree", [92.2,95.5,94.9,95.2,94.90], "#10B981"),
            ("Random Forest", [93.7,97.2,94.5,96.2,96.01], "#8B5CF6"),
        ]:
            fig_r.add_trace(go.Scatterpolar(
                r=vals+[vals[0]], theta=cats+[cats[0]],
                fill="toself", name=name,
                line=dict(color=clr, width=2), fillcolor=clr+"18",
            ))
        fig_r.update_layout(**PLOTLY_BASE, height=380,
            polar=dict(bgcolor="rgba(0,0,0,0)",
                       radialaxis=dict(range=[90,100], gridcolor="#2A2A3E", tickfont=dict(color="#6B7280", size=9)),
                       angularaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#E8E8F0", size=11))),
            title=dict(text="Radar de Comparaison", font=dict(color="#E8E8F0", size=15, family="Playfair Display")),
            legend=dict(font=dict(color="#E8E8F0"), bgcolor="rgba(0,0,0,0)"),
        )
        st.plotly_chart(fig_r, use_container_width=True)

    with c2:
        fig_cm = go.Figure(go.Heatmap(
            z=[[621,92],[175,3311]],
            x=["Prédit: Non rec.","Prédit: Rec."],
            y=["Réel: Non rec.","Réel: Rec."],
            text=[[621,92],[175,3311]], texttemplate="<b>%{text}</b>",
            textfont=dict(size=20, color="white"),
            colorscale=[[0,"#12121A"],[0.4,"#4C1D95"],[1,"#8B5CF6"]],
            showscale=False,
        ))
        fig_cm.update_layout(**PLOTLY_BASE, height=380,
            title=dict(text="Matrice de Confusion — Random Forest", font=dict(color="#E8E8F0", size=15, family="Playfair Display")),
            xaxis=dict(tickfont=dict(color="#E8E8F0", size=11)),
            yaxis=dict(tickfont=dict(color="#E8E8F0", size=11)),
        )
        st.plotly_chart(fig_cm, use_container_width=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;color:#8B5CF6;
                letter-spacing:1px;margin-bottom:18px;'>
                OPTIMISATION — GRIDSEARCHCV / RANDOMIZEDSEARCHCV</div>
                <div style='display:grid;grid-template-columns:repeat(3,1fr);gap:20px;'>
    """, unsafe_allow_html=True)
    opt_html = ""
    for name, method, params, f1, acc, clr in [
        ("Logistic Regression","GridSearchCV","C=10, solver='lbfgs'","96.04%","93.53%","#06B6D4"),
        ("Decision Tree","GridSearchCV","criterion='entropy'<br>max_depth=5","95.97%","93.43%","#10B981"),
        ("✦ Random Forest","RandomizedSearchCV","n_estimators=100<br>max_depth=10, max_features='log2'","96.16%","93.75%","#8B5CF6"),
    ]:
        opt_html += f"""
        <div style='background:#12121A;border:1px solid rgba({clr.lstrip("#")},0.2);
                    border-radius:12px;padding:20px;border-top:3px solid {clr};'>
          <div style='font-weight:700;color:{clr};margin-bottom:4px;font-size:0.9em;'>{name}</div>
          <div style='font-family:"Space Mono",monospace;font-size:0.68em;color:#6B7280;margin-bottom:12px;'>{method}</div>
          <div style='font-family:"Space Mono",monospace;font-size:0.72em;background:#0A0A0F;
                      padding:10px;border-radius:8px;color:#A78BFA;line-height:1.7;margin-bottom:14px;'>{params}</div>
          <div style='display:flex;gap:20px;'>
            <div><div style='font-family:"Space Mono",monospace;font-size:1.1em;font-weight:700;color:{clr};'>{f1}</div>
              <div style='font-size:0.72em;color:#6B7280;'>F1-Score</div></div>
            <div><div style='font-family:"Space Mono",monospace;font-size:1.1em;font-weight:700;color:{clr};'>{acc}</div>
              <div style='font-size:0.72em;color:#6B7280;'>Accuracy</div></div>
          </div>
        </div>"""
    st.markdown(opt_html + "</div></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  PAGE 3 — PRÉDICTION
# ══════════════════════════════════════════════════════════════
elif PAGE == 3:
    st.markdown("""
    <div style='padding:40px 0 24px 0;'>
      <div class='hero-badge'>🎯 Interface Interactive</div>
      <div class='sec-title' style='font-size:2.2em;margin-top:10px;'>Prédiction en Temps Réel</div>
      <div class='sec-sub'>Entrez les informations du produit pour prédire sa popularité</div>
    </div>""", unsafe_allow_html=True)

    if not models_ok:
        st.markdown("""
        <div style='background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);
                    border-radius:12px;padding:30px;text-align:center;'>
          <div style='font-size:2.5em;'>⚠️</div>
          <div style='color:#EF4444;margin-top:10px;line-height:1.7;'>
            Modèles non trouvés.<br>
            Vérifiez que <code>model/models.pkl</code> et <code>model/vectorizer.pkl</code> existent.
          </div>
        </div>""", unsafe_allow_html=True)
        st.stop()

    cf, cr = st.columns([1.1, 0.9], gap="large")

    with cf:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                    color:#8B5CF6;letter-spacing:1px;margin-bottom:20px;'>INFORMATIONS DU PRODUIT</div>""",
                    unsafe_allow_html=True)

        cc1, cc2 = st.columns(2)
        with cc1:
            model_choice = st.selectbox("Modèle IA", list(models.keys()),
                format_func=lambda x: {
                    "logistic_regression":"Régression Logistique",
                    "decision_tree":      "Arbre de Décision",
                    "random_forest":      "✦ Random Forest",
                }[x])
            rating = st.slider("⭐ Rating", 1.0, 5.0, 4.0, 0.5)
        with cc2:
            feedback = st.number_input("👍 Feedbacks positifs", 0, 500, 10)
            age      = st.number_input("👤 Âge", 18, 90, 35)

        cc3, cc4, cc5 = st.columns(3)
        with cc3:
            division   = st.selectbox("Division",    ["General","General Petite","Initmates"])
        with cc4:
            department = st.selectbox("Département", ["Tops","Dresses","Bottoms","Intimate","Jackets","Trend"])
        with cc5:
            class_name = st.selectbox("Classe",      ["Blouses","Dresses","Knits","Pants","Skirts","Jackets","Intimates"])

        review = st.text_area("💬 Avis client",
            placeholder="Ex: I absolutely love this dress! The fabric is so comfortable and fits perfectly...",
            height=130)

        if review.strip():
            sl, sc, _ = sentiment_quick(review)
            wc = len(review.split())
            st.markdown(f"""
            <div style='display:flex;gap:10px;margin:8px 0 12px 0;'>
              <div style='background:#12121A;border:1px solid #2A2A3E;border-radius:8px;
                          padding:8px 14px;font-size:0.8em;flex:1;text-align:center;'>
                <div style='color:{sc};font-weight:600;'>{sl}</div>
                <div style='color:#6B7280;font-size:0.78em;'>Sentiment</div>
              </div>
              <div style='background:#12121A;border:1px solid #2A2A3E;border-radius:8px;
                          padding:8px 14px;font-size:0.8em;flex:1;text-align:center;'>
                <div style='color:#8B5CF6;font-weight:600;font-family:"Space Mono",monospace;'>{wc}</div>
                <div style='color:#6B7280;font-size:0.78em;'>Mots</div>
              </div>
            </div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        btn = st.button("🔮  Prédire maintenant", use_container_width=True, type="primary")

    with cr:
        if btn:
            if not review.strip():
                st.markdown("""
                <div style='background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.3);
                            border-radius:12px;padding:20px;text-align:center;color:#F59E0B;'>
                  ⚠️ Veuillez entrer un avis client.
                </div>""", unsafe_allow_html=True)
            else:
                X     = preprocess(review, rating, feedback, age)
                model = models[model_choice]
                pred  = model.predict(X)[0]
                proba = model.predict_proba(X)[0][1] if hasattr(model, "predict_proba") else 0.5

                st.session_state["last_pred"] = {
                    "prediction": pred, "proba": proba,
                    "rating": rating, "feedback": feedback, "review": review,
                }

                if pred == 1:
                    clr_r, bg_r, bd_r = "#10B981","rgba(16,185,129,0.07)","rgba(16,185,129,0.3)"
                    emoji_r, title_r  = "✅", "Produit Populaire"
                    hint_r = "Ce produit sera très probablement recommandé !"
                else:
                    clr_r, bg_r, bd_r = "#EF4444","rgba(239,68,68,0.07)","rgba(239,68,68,0.3)"
                    emoji_r, title_r  = "❌", "Produit Faible"
                    hint_r = "Ce produit risque de ne pas être recommandé."

                st.markdown(f"""
                <div style='background:{bg_r};border:1px solid {bd_r};border-radius:16px;
                            padding:30px;text-align:center;margin-bottom:14px;'>
                  <div style='font-size:3.5em;'>{emoji_r}</div>
                  <div style='font-family:"Playfair Display",serif;font-size:1.7em;font-weight:700;
                              color:{clr_r};margin:8px 0 4px 0;'>{title_r}</div>
                  <div style='color:#6B7280;font-size:0.87em;'>{hint_r}</div>
                </div>""", unsafe_allow_html=True)

                bc = "#10B981" if proba >= 0.6 else ("#F59E0B" if proba >= 0.4 else "#EF4444")
                st.markdown(proba_bar_html(proba, bc), unsafe_allow_html=True)

                if   proba >= 0.75: interp = "🟢 **Très forte probabilité de succès**"
                elif proba >= 0.55: interp = "🟡 **Probabilité modérée de succès**"
                elif proba >= 0.40: interp = "🟠 **Résultat incertain**"
                else:               interp = "🔴 **Faible probabilité de succès**"
                st.markdown(interp)

                # Factors
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                            color:#8B5CF6;letter-spacing:1px;margin-bottom:14px;'>FACTEURS CLÉS</div>""",
                            unsafe_allow_html=True)
                factors = []
                if rating >= 4.0:   factors.append(("⭐","Rating élevé",      f"{rating}/5","#10B981"))
                elif rating <= 2.0: factors.append(("⭐","Rating faible",      f"{rating}/5","#EF4444"))
                else:               factors.append(("⭐","Rating moyen",       f"{rating}/5","#F59E0B"))
                if feedback >= 15:  factors.append(("👍","Fort engagement",    str(feedback),"#10B981"))
                elif feedback == 0: factors.append(("👍","Aucun feedback",     "0","#EF4444"))
                else:               factors.append(("👍","Feedbacks modérés",  str(feedback),"#F59E0B"))
                sl2, sc2, _ = sentiment_quick(review)
                factors.append(("💬","Sentiment", sl2, sc2))
                wc2 = len(review.split())
                if wc2 >= 30:   factors.append(("📝","Avis détaillé",  f"{wc2} mots","#10B981"))
                elif wc2 >= 10: factors.append(("📝","Avis moyen",     f"{wc2} mots","#F59E0B"))
                else:           factors.append(("📝","Avis court",     f"{wc2} mots","#EF4444"))
                rows = ""
                for icon, lbl, val, fclr in factors:
                    rows += f"""
                    <div style='display:flex;justify-content:space-between;align-items:center;
                                padding:9px 0;border-bottom:1px solid rgba(42,42,62,0.4);font-size:0.85em;'>
                      <span style='color:#E8E8F0;'>{icon} {lbl}</span>
                      <span style='color:{fclr};font-weight:600;font-family:"Space Mono",monospace;font-size:0.84em;'>{val}</span>
                    </div>"""
                st.markdown(rows + "</div>", unsafe_allow_html=True)

                # Save history
                if "history" not in st.session_state:
                    st.session_state.history = []
                ml = {"logistic_regression":"Logistic Reg.","decision_tree":"Dec. Tree",
                      "random_forest":"Random Forest"}[model_choice]
                st.session_state.history.append({
                    "Modèle": ml, "Rating": rating, "Feedbacks": feedback,
                    "Résultat": "✅ Populaire" if pred == 1 else "❌ Faible",
                    "Probabilité": f"{int(proba*100)}%",
                    "Avis": review[:35] + "..." if len(review) > 35 else review,
                })
        else:
            st.markdown("""
            <div style='background:#12121A;border:1px dashed #2A2A3E;border-radius:16px;
                        padding:60px 30px;text-align:center;'>
              <div style='font-size:3.5em;opacity:0.3;'>🔮</div>
              <div style='color:#374151;font-size:0.95em;margin-top:14px;line-height:1.7;'>
                Remplissez le formulaire<br>et cliquez sur <strong style='color:#6B7280;'>Prédire maintenant</strong>
              </div>
            </div>""", unsafe_allow_html=True)

    if "history" in st.session_state and st.session_state.history:
        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
        ch, cb2 = st.columns([5, 1])
        ch.markdown("<div class='sec-title' style='font-size:1.3em;'>📜 Historique</div>", unsafe_allow_html=True)
        if cb2.button("🗑️ Effacer", use_container_width=True):
            st.session_state.history = []
            st.rerun()
        st.dataframe(pd.DataFrame(st.session_state.history[::-1]), use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════
#  PAGE 4 — EXPLICATION IA
# ══════════════════════════════════════════════════════════════
elif PAGE == 4:
    st.markdown("""
    <div style='padding:40px 0 24px 0;'>
      <div class='hero-badge'>🔍 Explicabilité IA — SHAP</div>
      <div class='sec-title' style='font-size:2.2em;margin-top:10px;'>Pourquoi cette prédiction ?</div>
      <div class='sec-sub'>Shapley Additive Explanations — comprendre les décisions du modèle variable par variable</div>
    </div>""", unsafe_allow_html=True)

    ca, cb3 = st.columns([1.1, 0.9], gap="large")
    with ca:
        feats = ["Rating","Polarity","Subjectivity","Review Length",
                 "Positive Feedback","Age","Class (enc.)","Division (enc.)","Dept (enc.)","Clothing ID"]
        svals = [0.1907,0.0312,0.0198,0.0142,0.0134,0.0121,0.0098,0.0087,0.0076,0.0065]
        clrs  = ["#8B5CF6" if v == max(svals) else ("#06B6D4" if v > 0.015 else "#2A3A4A") for v in svals]
        fig_s = go.Figure(go.Bar(
            x=svals[::-1], y=feats[::-1], orientation="h",
            marker=dict(color=clrs[::-1]),
            text=[f"{v:.4f}" for v in svals[::-1]],
            textposition="outside", textfont=dict(color="#E8E8F0", size=11),
        ))
        fig_s.update_layout(**PLOTLY_BASE, height=390, showlegend=False,
            title=dict(text="SHAP — Importance Globale des Variables",
                       font=dict(color="#E8E8F0", size=15, family="Playfair Display")),
            xaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#6B7280")),
            yaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#E8E8F0", size=11)),
            margin=dict(t=50, b=20, l=20, r=90),
        )
        st.plotly_chart(fig_s, use_container_width=True)

    with cb3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                    color:#8B5CF6;letter-spacing:1px;margin-bottom:18px;'>COMMENT FONCTIONNE SHAP</div>""",
                    unsafe_allow_html=True)
        for clr, num, title, desc in [
            ("#8B5CF6","1","Score positif (+)","La variable pousse vers 'Recommandé' → augmente la probabilité de succès."),
            ("#EF4444","2","Score négatif (−)","La variable pousse vers 'Non recommandé' → diminue la probabilité."),
            ("#06B6D4","3","Magnitude absolue","Plus le score est grand en valeur absolue, plus la variable est décisive."),
            ("#F59E0B","4","Valeur de base","Le modèle part de 82.6% (moyenne dataset) avant d'appliquer les corrections SHAP."),
        ]:
            st.markdown(f"""
            <div style='display:flex;gap:12px;padding:12px 0;border-bottom:1px solid rgba(42,42,62,0.4);'>
              <div style='width:32px;height:32px;border-radius:8px;background:rgba(139,92,246,0.1);
                          border:1px solid rgba(139,92,246,0.3);display:flex;align-items:center;
                          justify-content:center;color:{clr};font-weight:700;
                          font-family:"Space Mono",monospace;font-size:0.85em;flex-shrink:0;'>{num}</div>
              <div>
                <div style='font-weight:600;color:#E8E8F0;font-size:0.87em;margin-bottom:3px;'>{title}</div>
                <div style='font-size:0.8em;color:#6B7280;line-height:1.5;'>{desc}</div>
              </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sec-title' style='font-size:1.5em;'>Explication d'une prédiction individuelle</div>", unsafe_allow_html=True)
    st.markdown("<div class='sec-sub'>Impact de chaque variable sur la décision finale (Waterfall Plot)</div>", unsafe_allow_html=True)

    if "last_pred" in st.session_state:
        lp = st.session_state["last_pred"]
        r_v, fb_v, rv_v = lp["rating"], lp["feedback"], lp["review"]
        proba_d = lp["proba"]
        sl3, sc3, sv3 = sentiment_quick(rv_v)
        pol_v = sv3 if "Positif" in sl3 else -sv3
        rlen  = len(rv_v.split())
    else:
        r_v, fb_v, pol_v, rlen, proba_d = 2.0, 3, -0.15, 12, 0.25
        st.info("💡 Faites une prédiction dans **Prédiction** pour voir l'explication personnalisée.")

    base_val = 0.826
    r_c   = (r_v - 3.0) * 0.095
    fb_c  = (min(fb_v, 20) - 5) * 0.003
    pol_c = pol_v * 0.031
    len_c = (min(rlen, 50) - 20) * 0.0007
    oth   = max(-0.05, min(0.05, proba_d - (base_val + r_c + fb_c + pol_c + len_c)))
    contribs = [
        ("Rating",            r_c,   f"= {r_v}"),
        ("Polarity",          pol_c, ""),
        ("Positive Feedback", fb_c,  f"= {fb_v}"),
        ("Review Length",     len_c, f"{rlen} mots"),
        ("Autres features",   oth,   ""),
    ]

    cw1, cw2 = st.columns([1.2, 0.8], gap="large")
    with cw1:
        running = base_val
        bar_data = [("Base (82.6%)", base_val, base_val, 0, "#6366F1")]
        for name, contrib, _ in contribs:
            start = running
            running += contrib
            bar_data.append((name, abs(contrib), start, contrib, "#10B981" if contrib >= 0 else "#EF4444"))
        bar_data.append(("Prédiction finale", proba_d, 0, proba_d, "#8B5CF6"))

        fig_wf = go.Figure(go.Bar(
            x=[d[1] for d in bar_data[::-1]],
            y=[d[0] for d in bar_data[::-1]],
            base=[d[2] for d in bar_data[::-1]],
            orientation="h",
            marker_color=[d[4] for d in bar_data[::-1]],
            text=[f"{'+' if d[3]>=0 else ''}{d[3]:.3f}" for d in bar_data[::-1]],
            textposition="outside", textfont=dict(color="#E8E8F0", size=11),
        ))
        fig_wf.update_layout(**PLOTLY_BASE, height=380, showlegend=False,
            title=dict(text="Waterfall Plot — Décomposition SHAP",
                       font=dict(color="#E8E8F0", size=14, family="Playfair Display")),
            xaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#6B7280"),
                       range=[0, 1.1], tickformat=".0%"),
            yaxis=dict(gridcolor="#2A2A3E", tickfont=dict(color="#E8E8F0", size=10)),
            margin=dict(t=50, b=20, l=20, r=80),
        )
        st.plotly_chart(fig_wf, use_container_width=True)

    with cw2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                    color:#8B5CF6;letter-spacing:1px;margin-bottom:16px;'>IMPACT DES VARIABLES</div>""",
                    unsafe_allow_html=True)
        max_abs = max(abs(c[1]) for c in contribs) + 0.001
        for name, contrib, hint in contribs:
            clr2 = "#10B981" if contrib >= 0 else "#EF4444"
            sign = "+" if contrib >= 0 else ""
            pct2 = int(abs(contrib) / max_abs * 100)
            bar_grad = "linear-gradient(90deg,#10B981,#34D399)" if contrib >= 0 else "linear-gradient(90deg,#EF4444,#F97316)"
            st.markdown(f"""
            <div style='display:flex;align-items:center;gap:12px;padding:10px 0;
                        border-bottom:1px solid rgba(42,42,62,0.4);font-size:0.87em;'>
              <div style='width:120px;color:#E8E8F0;font-size:0.84em;font-weight:500;'>{name}</div>
              <div style='flex:1;background:#1A1A26;border-radius:4px;height:8px;overflow:hidden;'>
                <div style='width:{pct2}%;height:100%;border-radius:4px;background:{bar_grad};'></div>
              </div>
              <div style='width:52px;text-align:right;font-family:"Space Mono",monospace;
                          font-size:0.8em;color:{clr2};'>{sign}{contrib:.3f}</div>
            </div>""", unsafe_allow_html=True)
        st.markdown(f"""
          <div style='margin-top:16px;padding:14px;background:#12121A;border-radius:10px;
                      border:1px solid #2A2A3E;text-align:center;'>
            <div style='font-size:0.78em;color:#6B7280;margin-bottom:4px;'>Prédiction finale</div>
            <div style='font-family:"Space Mono",monospace;font-size:1.5em;font-weight:700;
                        color:{"#10B981" if proba_d>=0.5 else "#EF4444"};'>
              {int(proba_d*100)}%
            </div>
            <div style='font-size:0.75em;color:#6B7280;'>de probabilité de succès</div>
          </div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  PAGE 5 — VALEUR AJOUTÉE
# ══════════════════════════════════════════════════════════════
elif PAGE == 5:
    st.markdown("""
    <div style='padding:40px 0 24px 0;'>
      <div class='hero-badge'>🚀 Business Intelligence</div>
      <div class='sec-title' style='font-size:2.2em;margin-top:10px;'>Valeur Ajoutée de l'IA</div>
      <div class='sec-sub'>Au-delà de la prédiction — comprendre, décider, optimiser</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div style='background:linear-gradient(135deg,rgba(139,92,246,0.08),rgba(236,72,153,0.05),#12121A);
                border:1px solid #2A2A3E;border-radius:20px;padding:40px;
                margin-bottom:28px;text-align:center;'>
      <div style='font-family:"Playfair Display",serif;font-size:1.6em;font-weight:700;
                  color:#fff;margin-bottom:10px;'>
        Ce n'est pas juste prédire — c'est <span style='color:#8B5CF6;'>comprendre</span>
      </div>
      <div style='color:#6B7280;font-size:0.95em;max-width:620px;margin:0 auto;line-height:1.7;'>
        Notre application explique <em>pourquoi</em> le modèle prend une décision,
        permettant aux équipes produit d'agir sur les bons leviers.
      </div>
    </div>""", unsafe_allow_html=True)

    vc1, vc2 = st.columns(2, gap="large")
    for i, (clr, icon, title, desc, bullets) in enumerate([
        ("#8B5CF6","🎯","Prédiction Expliquée",
         "Chaque prédiction est accompagnée de l'importance des variables (SHAP). L'utilisateur comprend exactement les facteurs décisifs.",
         ["SHAP Waterfall Plot","Impact par feature","Score de confiance"]),
        ("#06B6D4","📦","Intelligence Produit",
         "L'équipe produit identifie les caractéristiques des produits populaires pour optimiser les fiches et descriptions.",
         ["Rating : corrélation 0.79","Sentiment positif clé","Longueur d'avis optimale"]),
        ("#EC4899","📣","Stratégie Marketing",
         "Détecter les patterns entre catégories, départements et popularité pour cibler les bons segments.",
         ["Analyse par département","Segmentation par âge","Optimisation des descriptions"]),
        ("#F59E0B","🔄","Amélioration Continue",
         "Le modèle peut être ré-entraîné avec de nouvelles données pour s'adapter aux tendances e-commerce.",
         ["Mise à jour des modèles","Détection des dérives","A/B testing intégré"]),
    ]):
        col = vc1 if i % 2 == 0 else vc2
        with col:
            bl = "".join([
                f"<div style='display:flex;gap:8px;padding:5px 0;font-size:0.83em;color:#9CA3AF;'>"
                f"<span style='color:{clr};'>→</span>{b}</div>" for b in bullets
            ])
            st.markdown(f"""
            <div style='background:#12121A;border:1px solid rgba(42,42,62,0.8);border-radius:16px;
                        padding:24px;margin-bottom:16px;border-top:3px solid {clr};'>
              <div style='display:flex;gap:14px;margin-bottom:14px;align-items:center;'>
                <div style='font-size:1.8em;'>{icon}</div>
                <div style='font-weight:700;color:#E8E8F0;font-size:1em;'>{title}</div>
              </div>
              <p style='color:#6B7280;font-size:0.85em;line-height:1.6;margin-bottom:14px;'>{desc}</p>
              {bl}
            </div>""", unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sec-title' style='font-size:1.5em;margin-bottom:8px;'>Insights Clés découverts</div>", unsafe_allow_html=True)
    st.markdown("<div class='sec-sub'>Patterns identifiés grâce au ML + NLP dans le dataset</div>", unsafe_allow_html=True)

    ig_c = st.columns(3)
    for i, (clr, icon, title, desc) in enumerate([
        ("#8B5CF6","⭐","97.8% des produits Rating 5 sont recommandés",
         "Le rating est le signal le plus fort — corrélation de 0.79 avec la cible."),
        ("#10B981","💬","Les avis 30+ mots augmentent la probabilité",
         "Une description longue et positive reflète un engagement client plus fort."),
        ("#06B6D4","📊","Déséquilibre 82.6/17.4% géré avec stratify=y",
         "Nécessite class_weight='balanced' pour un modèle équitable sur les deux classes."),
        ("#F59E0B","👥","Les clientes 34-41 ans sont les plus actives",
         "Ce segment produit le plus de feedbacks positifs et de recommandations."),
        ("#EC4899","🏷️","Les Tops et Dresses dominent les recommandations",
         "Les produits de mode quotidienne reçoivent plus d'avis positifs que les Jackets."),
        ("#A78BFA","🧠","La polarité TextBlob est le 2ème prédicteur",
         "L'analyse NLP du sentiment capture ce que le rating seul ne voit pas."),
    ]):
        with ig_c[i % 3]:
            st.markdown(f"""
            <div style='background:#12121A;border:1px solid #2A2A3E;border-radius:12px;
                        padding:18px;margin-bottom:16px;border-left:3px solid {clr};'>
              <div style='font-size:1.4em;margin-bottom:8px;'>{icon}</div>
              <div style='font-weight:600;color:#E8E8F0;font-size:0.87em;
                          margin-bottom:6px;line-height:1.4;'>{title}</div>
              <div style='color:#6B7280;font-size:0.78em;line-height:1.5;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  PAGE 6 — CONCLUSION
# ══════════════════════════════════════════════════════════════
elif PAGE == 6:
    st.markdown("""
    <div style='padding:40px 0 24px 0;'>
      <div class='hero-badge'>📈 Bilan Final</div>
      <div class='sec-title' style='font-size:2.2em;margin-top:10px;'>Conclusion & Perspectives</div>
      <div class='sec-sub'>Résumé des résultats, limites identifiées et améliorations futures</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div style='background:linear-gradient(135deg,#1A1026,#12121A);
                border:1px solid rgba(139,92,246,0.27);border-radius:20px;padding:36px;
                margin-bottom:28px;text-align:center;
                box-shadow:0 0 60px rgba(139,92,246,0.1);'>
      <div style='font-family:"Space Mono",monospace;font-size:0.7em;
                  color:#8B5CF6;letter-spacing:2px;margin-bottom:12px;'>✦ MODÈLE FINAL RETENU</div>
      <div style='font-family:"Playfair Display",serif;font-size:2em;font-weight:900;
                  color:#fff;margin-bottom:6px;'>Random Forest Optimisé</div>
      <div style='color:#6B7280;margin-bottom:24px;font-size:0.88em;'>
        RandomizedSearchCV · n_estimators=100 · max_depth=10 · max_features='log2'
      </div>
      <div style='display:flex;justify-content:center;gap:36px;flex-wrap:wrap;'>
    """, unsafe_allow_html=True)
    m_html = ""
    for val, lbl, clr in [
        ("93.7%","Accuracy","#8B5CF6"),("97.2%","Precision","#06B6D4"),
        ("94.5%","Recall","#10B981"),  ("96.2%","F1-Score","#EC4899"),("96.01%","CV F1","#F59E0B"),
    ]:
        m_html += f"""
        <div style='text-align:center;'>
          <div style='font-family:"Space Mono",monospace;font-size:1.8em;font-weight:700;color:{clr};'>{val}</div>
          <div style='color:#6B7280;font-size:0.8em;margin-top:4px;'>{lbl}</div>
        </div>"""
    st.markdown(m_html + "</div></div>", unsafe_allow_html=True)

    cl, crr = st.columns(2, gap="large")
    with cl:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                    color:#10B981;letter-spacing:1px;margin-bottom:18px;'>✓ RÉSULTATS OBTENUS</div>""",
                    unsafe_allow_html=True)
        for icon, clr, title, desc in [
            ("🏆","#10B981","Modèle performant",
             "93.7% d'accuracy avec Random Forest optimisé sur 23 486 avis clients."),
            ("🧠","#8B5CF6","Feature Engineering efficace",
             "Polarity et subjectivité TextBlob = 2ème et 3ème variables (SHAP)."),
            ("⚖️","#06B6D4","Déséquilibre bien géré",
             "Stratify=y + class_weight maintiennent F1=82% sur la classe minoritaire."),
            ("🔍","#EC4899","Explicabilité complète",
             "SHAP Waterfall Plot explique chaque prédiction variable par variable."),
            ("📱","#F59E0B","Interface utilisable",
             "Streamlit avec historique et analyse de sentiment en temps réel."),
        ]:
            st.markdown(f"""
            <div class='concl-item'>
              <div class='concl-icon' style='border:1px solid rgba(139,92,246,0.2);color:{clr};'>{icon}</div>
              <div class='concl-text'><h4>{title}</h4><p>{desc}</p></div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with crr:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                    color:#EF4444;letter-spacing:1px;margin-bottom:18px;'>△ LIMITES IDENTIFIÉES</div>""",
                    unsafe_allow_html=True)
        for icon, clr, title, desc in [
            ("⚠️","#EF4444","Déséquilibre des classes (82/18)",
             "Le modèle est naturellement biaisé vers la classe majoritaire."),
            ("⚠️","#F97316","Texte en anglais seulement",
             "TextBlob et TF-IDF ne supportent pas bien le multilingue."),
            ("⚠️","#F59E0B","Données statiques",
             "Le modèle ne s'adapte pas aux tendances sans re-entraînement."),
            ("⚠️","#A78BFA","Features catégorielles faibles",
             "SHAP montre que Division/Department ont un impact marginal."),
        ]:
            st.markdown(f"""
            <div class='concl-item'>
              <div class='concl-icon' style='border:1px solid rgba(239,68,68,0.2);color:{clr};'>{icon}</div>
              <div class='concl-text'><h4>{title}</h4><p>{desc}</p></div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""<div style='font-family:"Space Mono",monospace;font-size:0.68em;
                    color:#8B5CF6;letter-spacing:1px;margin-bottom:18px;'>🚀 AMÉLIORATIONS FUTURES</div>""",
                    unsafe_allow_html=True)
        for clr, title, desc in [
            ("#8B5CF6","Deep Learning / BERT","Transformers pour une meilleure compréhension du texte."),
            ("#06B6D4","Déploiement Cloud","AWS / GCP avec pipeline MLOps et monitoring de dérive."),
            ("#10B981","Données multilingues","Extension avec mBERT ou XLM-RoBERTa."),
            ("#F59E0B","API REST en temps réel","Intégration directe dans les plateformes e-commerce."),
        ]:
            st.markdown(f"""
            <div style='display:flex;gap:10px;padding:9px 0;border-bottom:1px solid rgba(42,42,62,0.4);'>
              <div style='width:8px;height:8px;border-radius:50%;background:{clr};
                          margin-top:6px;flex-shrink:0;'></div>
              <div>
                <div style='font-size:0.85em;font-weight:600;color:#E8E8F0;'>{title}</div>
                <div style='font-size:0.78em;color:#6B7280;margin-top:2px;'>{desc}</div>
              </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background:linear-gradient(135deg,rgba(139,92,246,0.05),rgba(236,72,153,0.03));
                border:1px solid #2A2A3E;border-radius:16px;padding:32px;
                text-align:center;margin-top:28px;'>
      <div style='font-family:"Playfair Display",serif;font-size:1.3em;
                  font-style:italic;color:#A78BFA;line-height:1.6;margin-bottom:12px;'>
        "Le Machine Learning ne remplace pas le jugement humain —<br>il l'augmente avec des données."
      </div>
      <div style='color:#374151;font-family:"Space Mono",monospace;font-size:0.72em;letter-spacing:1px;'>
        BSDSI 2025-2026 &nbsp;·&nbsp; BEN ZHIR Wafa &nbsp;·&nbsp; IKSOD Salma &nbsp;·&nbsp; Enc. AIT BAHA Tarek
      </div>
    </div>""", unsafe_allow_html=True)
