import streamlit as st
import base64

# Fonction pour convertir une image en base64
from pathlib import Path
import base64
import mimetypes
import streamlit as st

def get_image_base64_from_path(path: Path):
    if not path.exists():
        return None, None
    b64 = base64.b64encode(path.read_bytes()).decode()
    mime, _ = mimetypes.guess_type(str(path))
    if mime is None:
        mime = "image/jpeg"
    return b64, mime

base_dir = Path(__file__).parent
img_path = base_dir / "photo.jpg"  # ajustez si nécessaire

PHOTO_BASE64, PHOTO_MIME = get_image_base64_from_path(img_path)
# if PHOTO_BASE64:
#     img_src = f"data:{PHOTO_MIME};base64,{PHOTO_BASE64}"
#     st.markdown(f'<img src="{img_src}" width="100" style="border-radius:50%;">', unsafe_allow_html=True)
# else:
#     st.warning(f"Image introuvable : {img_path}")

# Configuration de la page
st.set_page_config(
    page_title="Questionnaire de Profil Investisseur - SAMUEL BROU",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé pour un design professionnel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    .intro-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #2d5a87;
        margin-bottom: 2rem;
    }
    
    .question-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid #e0e0e0;
    }
    
    .question-title {
        color: #1e3a5f;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .section-header {
        background: linear-gradient(135deg, #2d5a87 0%, #1e3a5f 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 2rem 0 1.5rem 0;
    }
    
    .stRadio > label {
        font-weight: 500;
        color: #333;
        padding: 0.8rem;
        background: #f8f9fa;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stRadio > label:hover {
        background: #e3f2fd;
        border-color: #2d5a87;
    }
    
    .progress-container {
        background: #e9ecef;
        border-radius: 10px;
        padding: 0.3rem;
        margin: 2rem 0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #2d5a87, #4a90c2);
        height: 12px;
        border-radius: 8px;
        transition: width 0.5s ease;
    }
    
    .result-card {
        background: white;
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.15);
        text-align: center;
        margin-top: 2rem;
    }
    
    .profile-badge {
        display: inline-block;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin: 1rem 0;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .profile-prudent { background: linear-gradient(135deg, #28a745, #20c997); }
    .profile-modere { background: linear-gradient(135deg, #17a2b8, #6f42c1); }
    .profile-equilibre { background: linear-gradient(135deg, #fd7e14, #ffc107); }
    .profile-croissance { background: linear-gradient(135deg, #dc3545, #fd7e14); }
    .profile-audacieux { background: linear-gradient(135deg, #6f42c1, #e83e8c); }
    
    .score-display {
        font-size: 4rem;
        font-weight: 700;
        color: #1e3a5f;
        margin: 1rem 0;
    }
    
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2d5a87;
        padding: 1.5rem;
        border-radius: 0 10px 10px 0;
        margin: 1rem 0;
    }
    
    .portfolio-structure {
        background: linear-gradient(135deg, #f1f3f4 0%, #e8eaed 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
    }
    
    .portfolio-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .percentage {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d5a87;
    }
    
    .trait-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1.5rem;
        border-radius: 0 10px 10px 0;
        margin: 1rem 0;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #2d5a87, #1e3a5f);
        color: white;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(45, 90, 135, 0.4);
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #6c757d;
        margin-top: 3rem;
        border-top: 1px solid #dee2e6;
    }
    
    .step-indicator {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .step {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        margin: 0 0.5rem;
        transition: all 0.3s ease;
    }
    
    .step-completed {
        background: #28a745;
        color: white;
    }
    
    .step-current {
        background: #2d5a87;
        color: white;
        transform: scale(1.2);
    }
    
    .step-pending {
        background: #e9ecef;
        color: #6c757d;
    }
    
    .placement-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
    }
    
    .placement-table th, .placement-table td {
        padding: 1rem;
        text-align: center;
        border: 1px solid #dee2e6;
    }
    
    .placement-table th {
        background: #2d5a87;
        color: white;
    }
    
    .placement-table tr:nth-child(even) {
        background: #f8f9fa;
    }
    
    .header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
    }
    
    .header-text {
        flex: 1;
        text-align: center;
    }
    
    .header-photo {
        position: absolute;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 4px solid rgba(255,255,255,0.3);
        object-fit: cover;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    @media (max-width: 768px) {
        .header-photo {
            width: 60px;
            height: 60px;
            right: 10px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Données des questions
questions = {
    1: {
        "section": "1ÈRE PARTIE : SITUATION PERSONNELLE ET FINANCIÈRE",
        "question": "QUEL EST VOTRE ÂGE ?",
        "options": [
            ("Plus de 65 ans", 0),
            ("51 à 65 ans", 2),
            ("41 à 50 ans", 4),
            ("31 à 40 ans", 6),
            ("30 ans et moins", 8)
        ]
    },
    2: {
        "question": "QUAND PRÉVOYEZ-VOUS PRENDRE VOTRE RETRAITE ?",
        "options": [
            ("Dans moins de 3 ans", 0),
            ("Dans 3 à 5 ans", 2),
            ("Dans 6 à 12 ans", 4),
            ("Dans 13 à 20 ans", 6),
            ("Dans plus de 20 ans", 8)
        ]
    },
    3: {
        "question": "À COMBIEN S'ÉLÈVENT VOS REVENUS MENSUELS NETS ?",
        "options": [
            ("Moins de 100 000 FCFA", 0),
            ("Entre 100 000 et 200 000 FCFA", 2),
            ("Entre 200 000 et 300 000 FCFA", 4),
            ("Entre 300 000 et 500 000 FCFA", 6),
            ("Plus de 500 000 FCFA", 8)
        ]
    },
    4: {
        "section": "2ÈME PARTIE : VOS OBJECTIFS DE PLACEMENT ET VOTRE TOLÉRANCE AU RISQUE",
        "question": "QUEL EST VOTRE PRINCIPAL OBJECTIF DE PLACEMENT ?",
        "options": [
            ("Préserver le capital", 0),
            ("Générer le maximum de revenu et une croissance modeste des titres", 2),
            ("Obtenir une croissance modérée des titres et un revenu", 4),
            ("Obtenir une forte croissance des titres et un revenu modeste", 6),
            ("Obtenir la croissance maximale des titres", 8)
        ]
    },
    5: {
        "question": "PENDANT COMBIEN DE TEMPS AVEZ-VOUS L'INTENTION D'INVESTIR VOTRE ARGENT AVANT D'EN RETIRER UNE PARTIE IMPORTANTE ?",
        "options": [
            ("1 à 3 ans", 0),
            ("4 à 5 ans", 2),
            ("6 à 10 ans", 4),
            ("11 à 15 ans", 6),
            ("Plus de 15 ans", 8)
        ]
    },
    6: {
        "question": "SI VOUS POSSEDIEZ UN PLACEMENT DONT LA VALEUR AURAIT BAISSE DE 25% SUR UNE PÉRIODE D'UN AN, QUE FERIEZ-VOUS ?",
        "options": [
            ("Je vendrais mon placement, même si cela entraînait une perte immédiate. Ce type de placement ne me convient pas.", 0),
            ("Je conserverais mon placement jusqu'à ce qu'il reprenne sa valeur initiale, puis je le transférerais vers un placement moins volatile.", 3),
            ("Je conserverais mon placement, car il faut s'attendre à des fluctuations du marché. C'est la croissance à long terme qui m'intéresse.", 5),
            ("J'investirais des sommes supplémentaires. Ce serait une occasion idéale d'acquérir davantage à un meilleur prix.", 8)
        ]
    },
    7: {
        "question": "COMPTÉ TENU DES FLUCTUATIONS, COMBIEN DE TEMPS SÉRIEZ-VOUS PRÊT À ATTENDRE AVANT QUE VOS PLACEMENTS REPRENNENT LEUR VALEUR ?",
        "options": [
            ("Moins de trois mois", 0),
            ("De trois à six mois", 2),
            ("De six mois à un an", 4),
            ("De un à deux ans", 6),
            ("De deux à trois ans", 8)
        ]
    },
    8: {
        "question": "SUPPOSONS QUE VOUS AYEZ 2 000 000 FCFA À INVESTIR. AVEC QUELLE OPTION SÉRIEZ-VOUS LE PLUS À L'AISE ?",
        "type": "table",
        "table_data": [
            ("Placement A - Valeur min: 2 000 000 | Valeur max: 2 060 000", 0),
            ("Placement B - Valeur min: 1 900 000 | Valeur max: 2 160 000", 2),
            ("Placement C - Valeur min: 1 800 000 | Valeur max: 2 300 000", 4),
            ("Placement D - Valeur min: 1 700 000 | Valeur max: 2 400 000", 6),
            ("Placement E - Valeur min: 1 500 000 | Valeur max: 2 600 000", 8)
        ],
        "options": [
            ("Placement A (Sécurité maximale, gain limité)", 0),
            ("Placement B (Faible risque, gain modéré)", 2),
            ("Placement C (Risque modéré, bon potentiel)", 4),
            ("Placement D (Risque élevé, fort potentiel)", 6),
            ("Placement E (Risque maximal, gain maximal)", 8)
        ]
    },
    9: {
        "section": "3ÈME PARTIE : VOS CONNAISSANCES ET EXPÉRIENCES EN MATIÈRE DE PLACEMENT",
        "question": "LEQUEL DES ÉNONCÉS SUIVANTS DÉCRIT LE MIEUX VOS CONNAISSANCES EN MATIÈRE DE PLACEMENT ?",
        "options": [
            ("Novice – Ma connaissance des placements est limitée.", 0),
            ("Débutant – Je sais qu'il existe différents types de placement, mais je ne sais pas comment ils diffèrent.", 2),
            ("Bonnes – Je comprends les caractéristiques des actions, obligations, ainsi que la façon dont ils diffèrent sur le plan de la volatilité.", 4),
            ("Très bonnes – J'ai une solide compréhension des différents types de placement et des risques connexes.", 6),
            ("Excellentes – J'ai une compréhension approfondie des différents types de placement et de stratégies, des risques connexes et de leur lien avec la volatilité des marchés.", 8)
        ]
    }
}

# Données des profils
profils = {
    "prudent": {
        "nom": "PRUDENT",
        "min_score": 0,
        "max_score": 9,
        "classe": "profile-prudent",
        "presentation": """L'investisseur prudent désire assurer la sécurité du capital qu'il a amassé en vue de la retraite (ou autre projet de court terme). Il cherche donc une source de revenu à travers des produits de taux et peut investir une faible portion de son portefeuille dans des produits plus risqués comme les actions.""",
        "traits": [
            "Votre objectif principal est de conserver votre capital",
            "Vous ne tolérez pas de fluctuations de rendement",
            "Vous investissez pour une très courte période de temps"
        ],
        "structure": {
            "revenu_fixe": 80,
            "actions": 20
        }
    },
    "modere": {
        "nom": "MODÉRÉ",
        "min_score": 10,
        "max_score": 27,
        "classe": "profile-modere",
        "presentation": """L'investisseur modéré veut obtenir une croissance de son capital à long terme et un revenu de placement relativement stable, mais il demeure toutefois vigilant. Il cherche un juste équilibre entre les placements boursiers et les titres de revenu.""",
        "traits": [
            "Vous vous préoccupez de la conservation du capital et désirez un revenu de placement relativement stable",
            "Vous êtes prêt à tolérer des fluctuations limitées dans votre portefeuille de placement",
            "La période de croissance de vos placements est assez courte"
        ],
        "structure": {
            "revenu_fixe": 67,
            "actions": 33
        }
    },
    "equilibre": {
        "nom": "ÉQUILIBRÉ",
        "min_score": 28,
        "max_score": 44,
        "classe": "profile-equilibre",
        "presentation": """L'investisseur équilibré recherche un bon potentiel de croissance à long terme tout en minimisant le risque global de son portefeuille. Il accepte donc d'investir dans les marchés boursiers, mais garde une portion importante en titres de revenu.""",
        "traits": [
            "Vous souhaitez obtenir de bons rendements éventuels à long terme tout en réduisant au minimum le risque global associé à votre portefeuille",
            "Vous êtes prêt à tolérer certaines fluctuations du marché et à allouer du temps pour récupérer de tout ralentissement du marché",
            "Vous n'avez pas besoin de recourir à ces placements au cours des quelques prochaines années"
        ],
        "structure": {
            "revenu_fixe": 50,
            "actions": 50
        }
    },
    "croissance": {
        "nom": "CROISSANCE",
        "min_score": 45,
        "max_score": 62,
        "classe": "profile-croissance",
        "presentation": """L'investisseur ayant un profil croissance recherche une forte croissance de son portefeuille. Il investit une portion importante de son capital dans les marchés boursiers et est prêt à subir des fluctuations à court terme.""",
        "traits": [
            "Vous êtes un investisseur axé sur la croissance, qui désire obtenir une excellente croissance de votre portefeuille",
            "Vous êtes prêt à accepter des fluctuations de marché, mais souhaitez qu'une petite partie de votre portefeuille soit investie dans des produits à revenu fixe",
            "Vous disposez d'une période de temps relativement longue avant d'avoir à toucher à ces placements"
        ],
        "structure": {
            "revenu_fixe": 33,
            "actions": 67
        }
    },
    "audacieux": {
        "nom": "AUDACIEUX",
        "min_score": 63,
        "max_score": 72,
        "classe": "profile-audacieux",
        "presentation": """L'investisseur audacieux recherche avant tout le meilleur rendement à long terme puisqu'il investit la majorité de ses avoirs dans les actions. Il est prêt à subir de fortes fluctuations de son portefeuille à court terme.""",
        "traits": [
            "Votre objectif principal est de réaliser le meilleur rendement à long terme de vos placements, et vous êtes prêt à accepter d'importantes fluctuations de marché",
            "Vous n'aurez pas besoin de toucher à ces placements pendant de nombreuses années"
        ],
        "structure": {
            "revenu_fixe": 20,
            "actions": 80
        }
    }
}

# Initialisation de l'état de session
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {}
if 'completed' not in st.session_state:
    st.session_state.completed = False
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

def get_profile(score):
    for key, profile in profils.items():
        if profile["min_score"] <= score <= profile["max_score"]:
            return key, profile
    return "prudent", profils["prudent"]

def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.scores = {}
    st.session_state.completed = False
    st.session_state.show_result = False

def next_question():
    if st.session_state.current_question < 9:
        st.session_state.current_question += 1
    else:
        st.session_state.completed = True
        st.session_state.show_result = True

def prev_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1

# En-tête
# Construction du header avec photo
header_html = """
<div class="main-header">
    <div class="header-content">
        <div class="header-text">
            <h1>📊 QUESTIONNAIRE DE PROFIL D'INVESTISSEUR</h1>
            <p>PAR SAMUEL BROU</p>
            <p style="font-size: 0.9rem; opacity: 0.8;">Plateforme d'éducation financière et de formation à l'investissement en bourse</p>
        </div>
"""

# Ajouter la photo si elle existe
if PHOTO_BASE64:
    header_html += f'<img src="data:image/jpeg;base64,{PHOTO_BASE64}" class="header-photo" alt="Photo">'
else:
    # Placeholder si la photo n'est pas trouvée
    header_html += '<div style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); width: 100px; height: 100px; border-radius: 50%; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; color: white; font-size: 0.8rem;">Photo</div>'

header_html += """
    </div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

# Introduction
if st.session_state.current_question == 0 and not st.session_state.show_result:
    st.markdown("""
    <div class="intro-box">
        <h3 style="color: #1e3a5f; margin-bottom: 1rem;">🎯 Introduction</h3>
        <p style="line-height: 1.8; text-align: justify;">
        Les produits disponibles sur les marchés financiers ne nous correspondent pas tous. En effet, ils diffèrent dans leur nature, 
        leur degré de risque, leur coût (frais de gestion) et dans le temps qu'il faut consacrer à leur gestion et leur détention. 
        Selon notre personnalité, nos besoins, nos objectifs, notre expérience et nos connaissances, certains produits seront 
        plus appropriés à notre situation que d'autres.
        </p>
        <p style="line-height: 1.8; text-align: justify; margin-top: 1rem;">
        Le but de ce test est de vous aider à vous situer entre tous ces produits. En fonction de votre profil et de votre horizon 
        de détention, vous allez vous orienter vers des actifs plus ou moins risqués. Plus précisément, ce test vous aidera à définir 
        le poids des différents actifs financiers dans votre portefeuille.
        </p>
        <p style="line-height: 1.8; text-align: justify; margin-top: 1rem;">
        Les questions qui vous seront posées couvrent plusieurs aspects importants de votre vie, tels que votre situation personnelle 
        et financière actuelle, vos objectifs de placement et votre tolérance au risque, ainsi que vos connaissances et expérience 
        en matière de placements.
        </p>
        <div class="info-box">
            <strong>💡 Conseil :</strong> Répondez-y simplement sans stress ni précipitation et soyez assurés que vos réponses resteront confidentielles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 COMMENCER LE QUESTIONNAIRE", use_container_width=True, type="primary"):
            st.session_state.current_question = 1
            st.rerun()

# Affichage des questions
elif st.session_state.current_question > 0 and not st.session_state.show_result:
    q_num = st.session_state.current_question
    q_data = questions[q_num]
    
    # Indicateur de progression
    progress = (q_num / 9) * 100
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-bar" style="width: {progress}%"></div>
    </div>
    <p style="text-align: center; color: #6c757d;">Question {q_num} sur 9</p>
    """, unsafe_allow_html=True)
    
    # Section header si présent
    if "section" in q_data:
        st.markdown(f'<div class="section-header">{q_data["section"]}</div>', unsafe_allow_html=True)
    
    # Carte de question
    st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-title">Question {q_num} : {q_data["question"]}</div>', unsafe_allow_html=True)
    
    # Tableau pour la question 8
    if q_num == 8:
        st.markdown("""
        <table class="placement-table">
            <tr>
                <th>Placement</th>
                <th>Valeur minimale après 1 an</th>
                <th>Valeur maximale après 1 an</th>
            </tr>
            <tr><td><strong>A</strong></td><td>2 000 000 FCFA</td><td>2 060 000 FCFA</td></tr>
            <tr><td><strong>B</strong></td><td>1 900 000 FCFA</td><td>2 160 000 FCFA</td></tr>
            <tr><td><strong>C</strong></td><td>1 800 000 FCFA</td><td>2 300 000 FCFA</td></tr>
            <tr><td><strong>D</strong></td><td>1 700 000 FCFA</td><td>2 400 000 FCFA</td></tr>
            <tr><td><strong>E</strong></td><td>1 500 000 FCFA</td><td>2 600 000 FCFA</td></tr>
        </table>
        """, unsafe_allow_html=True)
    
    # Options de réponse
    options_text = [opt[0] for opt in q_data["options"]]
    options_values = [opt[1] for opt in q_data["options"]]
    
    current_value = st.session_state.scores.get(q_num, None)
    default_index = options_values.index(current_value) if current_value in options_values else 0
    
    selected = st.radio(
        "Sélectionnez votre réponse :",
        options=options_text,
        index=default_index,
        key=f"q{q_num}",
        label_visibility="collapsed"
    )
    
    selected_index = options_text.index(selected)
    selected_value = options_values[selected_index]
    st.session_state.scores[q_num] = selected_value
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Boutons de navigation
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if q_num > 1:
            if st.button("⬅️ Précédent", use_container_width=True):
                prev_question()
                st.rerun()
    
    with col3:
        if q_num < 9:
            if st.button("Suivant ➡️", use_container_width=True, type="primary"):
                next_question()
                st.rerun()
        else:
            if st.button("✅ Voir mon résultat", use_container_width=True, type="primary"):
                next_question()
                st.rerun()

# Affichage du résultat
elif st.session_state.show_result:
    total_score = sum(st.session_state.scores.values())
    profile_key, profile_data = get_profile(total_score)
    
    # Répartition des scores par catégorie
    situation_score = sum([st.session_state.scores.get(i, 0) for i in [1, 2, 3]])
    objectif_score = sum([st.session_state.scores.get(i, 0) for i in [4, 5, 6, 7, 8]])
    connaissance_score = st.session_state.scores.get(9, 0)
    
    st.markdown(f"""
    <div class="result-card">
        <h2 style="color: #1e3a5f; margin-bottom: 1rem;">🎉 Votre Profil d'Investisseur</h2>
        <div class="score-display">{total_score} <span style="font-size: 1.5rem;">/ 72 points</span></div>
        <div class="profile-badge {profile_data['classe']}">{profile_data['nom']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Répartition détaillée des scores
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Situation personnelle et financière", f"{situation_score}/24")
    with col2:
        st.metric("Objectifs et tolérance au risque", f"{objectif_score}/40")
    with col3:
        st.metric("Connaissances sur les placements", f"{connaissance_score}/8")
    
    # Présentation du profil
    st.markdown(f"""
    <div class="info-box" style="margin-top: 2rem;">
        <h4 style="color: #1e3a5f; margin-bottom: 1rem;">📖 Présentation</h4>
        <p style="line-height: 1.8;">{profile_data['presentation']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Traits caractéristiques
    st.markdown('<h4 style="color: #1e3a5f; margin-top: 2rem;">✅ Vos traits caractéristiques</h4>', unsafe_allow_html=True)
    for trait in profile_data['traits']:
        st.markdown(f'<div class="trait-box">• {trait}</div>', unsafe_allow_html=True)
    
    # Structure du portefeuille recommandée
    st.markdown('<h4 style="color: #1e3a5f; margin-top: 2rem;">📊 Structure recommandée de votre portefeuille</h4>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="portfolio-structure">
            <div class="portfolio-item">
                <span>🏛️ Produits à revenu fixe (obligations, etc.)</span>
                <span class="percentage">{profile_data['structure']['revenu_fixe']}%</span>
            </div>
            <div class="portfolio-item">
                <span>📈 Produits de bourse (actions, etc.)</span>
                <span class="percentage">{profile_data['structure']['actions']}%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Graphique en camembert
        import plotly.graph_objects as go
        fig = go.Figure(data=[go.Pie(
            labels=['Revenu fixe', 'Actions'],
            values=[profile_data['structure']['revenu_fixe'], profile_data['structure']['actions']],
            hole=0.4,
            marker_colors=['#2d5a87', '#28a745']
        )])
        fig.update_layout(
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1),
            margin=dict(t=0, b=0, l=0, r=0),
            height=250
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Barre de progression visuelle
    st.markdown('<h4 style="color: #1e3a5f; margin-top: 1rem;">Répartition visuelle</h4>', unsafe_allow_html=True)
    st.progress(profile_data['structure']['revenu_fixe'] / 100, text=f"Revenu fixe: {profile_data['structure']['revenu_fixe']}%")
    st.progress(profile_data['structure']['actions'] / 100, text=f"Actions: {profile_data['structure']['actions']}%")
    
    # Notes importantes
    st.markdown("""
    <div class="info-box" style="margin-top: 2rem; background: #d4edda; border-color: #28a745;">
        <h4 style="color: #155724; margin-bottom: 1rem;">💡 Notes importantes</h4>
        <ol style="line-height: 1.8; color: #155724;">
            <li><strong>OPCVM :</strong> Il est possible d'intégrer les OPCVM dans votre stratégie financière. Cette intégration peut se faire en substituant les produits évoqués plus haut par des OPCVM correspondants. Elle peut se faire aussi en ajoutant les OPCVM comme une troisième rubrique dans la structure de votre portefeuille. Dans ce dernier cas, il faut être vigilant et vérifier que ce nouveau portefeuille respecte votre objectif et votre horizon d'investissement.</li>
            <li style="margin-top: 0.5rem;"><strong>Évolution :</strong> Votre personnalité évolue dans le temps de même que votre aversion au risque. Il est possible qu'après quelques années, vous ayez développé une meilleure tolérance aux fluctuations boursières. Dans ce cas, n'hésitez pas à refaire ce test en vue de déterminer votre nouveau profil.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Bouton pour recommencer
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Recommencer le questionnaire", use_container_width=True, type="primary"):
            reset_quiz()
            st.rerun()

# Footer
st.markdown("""
<div class="footer">
    <p><strong>PAR SAMUEL BROU </strong></p>
    <p>Plateforme d'éducation financière et de formation à l'investissement en bourse</p>
    <p style="font-size: 0.8rem; margin-top: 1rem;">Version 001 du 04 Février 2026 - SAMUEL BROU</p>
</div>
""", unsafe_allow_html=True)
