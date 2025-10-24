import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Simulador de Comissões",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para tema escuro
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        text-align: center;
        color: #9CA3AF;
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }
    
    .tip-box {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid #3B82F6;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 2rem;
        color: #93C5FD;
    }
    
    .big-metric {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(16, 185, 129, 0.3);
    }
    
    .big-metric-label {
        color: #D1FAE5;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .big-metric-value {
        color: white;
        font-size: 3.5rem;
        font-weight: bold;
        line-height: 1;
    }
    
    .big-metric-subtitle {
        color: #D1FAE5;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    
    .stage-card {
        background: rgba(17, 24, 39, 0.8);
        border: 2px solid;
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    
    .stage-card:hover {
        transform: scale(1.02);
    }
    
    .stage-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .stage-value {
        font-size: 2rem;
        font-weight: bold;
        color: white;
    }
    
    .stage-rate {
        color: #9CA3AF;
        font-size: 0.9rem;
        margin-top: 0.3rem;
    }
    
    .financial-summary {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid #374151;
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
    }
    
    .summary-item {
        text-align: center;
        padding: 1rem;
    }
    
    .summary-label {
        color: #9CA3AF;
        font-size: 0.85rem;
        margin-bottom: 0.3rem;
    }
    
    .summary-value {
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    .summary-value-highlight {
        color: #10B981;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    /* Estilo para inputs */
    .stNumberInput input {
        background-color: #1F2937 !important;
        color: white !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }
    
    /* Estilo para sliders */
    .stSlider {
        padding: 1rem 0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    /* Headers de seção */
    .section-header {
        color: white;
        font-size: 2rem;
        font-weight: bold;
        margin: 2rem 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar estado da sessão
if 'initialized' not in st.session_state:
    st.session_state.oportunidades = 2850
    st.session_state.inscritos = 1334
    st.session_state.grupo = 863
    st.session_state.qualificados = 503
    st.session_state.vendas = 188
    st.session_state.ticket_medio = 3470.93
    st.session_state.percentual_comissao = 5.0
    st.session_state.initialized = True

# Funções auxiliares
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_numero(valor):
    return f"{valor:,}".replace(",", ".")

def calcular_taxa(valor_final, valor_inicial):
    if valor_inicial == 0:
        return 0
    return (valor_final / valor_inicial) * 100

# Header
st.markdown('<div class="main-header">⚡ Simulador de Comissões</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ajuste as taxas de conversão e visualize o impacto na sua comissão</div>', unsafe_allow_html=True)
st.markdown("""
<div class="tip-box">
    💡 <strong>Dica:</strong> Você pode editar os números diretamente no funil OU ajustar as taxas de conversão nos sliders. Experimente as duas formas!
</div>
""", unsafe_allow_html=True)

# Sidebar - Configurações Base
with st.sidebar:
    st.markdown("## ⚙️ Configurações Base")
    
    st.session_state.oportunidades = st.number_input(
        "🎯 Oportunidades Totais",
        min_value=0,
        value=st.session_state.oportunidades,
        step=1,
        help="Número total de oportunidades no topo do funil"
    )
    
    st.session_state.ticket_medio = st.number_input(
        "💰 Ticket Médio (R$)",
        min_value=0.0,
        value=st.session_state.ticket_medio,
        step=100.0,
        format="%.2f",
        help="Valor médio de cada venda"
    )
    
    st.session_state.percentual_comissao = st.number_input(
        "📊 Percentual de Comissão (%)",
        min_value=0.0,
        max_value=100.0,
        value=st.session_state.percentual_comissao,
        step=0.5,
        format="%.2f",
        help="Percentual de comissão sobre o faturamento"
    )
    
    st.markdown("---")
    st.markdown("### 📝 Sobre")
    st.markdown("""
    Este simulador permite testar diferentes cenários de conversão e visualizar o impacto na sua comissão.
    
    **Ajuste:**
    - Números diretamente
    - Taxas de conversão
    - Configurações base
    """)

# Calcular taxas de conversão
taxa_oportunidades_inscritos = calcular_taxa(st.session_state.inscritos, st.session_state.oportunidades)
taxa_inscritos_grupo = calcular_taxa(st.session_state.grupo, st.session_state.inscritos)
taxa_grupo_qualificados = calcular_taxa(st.session_state.qualificados, st.session_state.grupo)
taxa_qualificados_vendas = calcular_taxa(st.session_state.vendas, st.session_state.qualificados)

# Calcular valores financeiros
faturamento = st.session_state.vendas * st.session_state.ticket_medio
comissao = faturamento * (st.session_state.percentual_comissao / 100)

# Destaque de Comissão
st.markdown(f"""
<div class="big-metric">
    <div class="big-metric-label">💰 COMISSÃO POTENCIAL</div>
    <div class="big-metric-value">{formatar_moeda(comissao)}</div>
    <div class="big-metric-subtitle">
        Faturamento: {formatar_moeda(faturamento)} | Vendas: {formatar_numero(st.session_state.vendas)}
    </div>
</div>
""", unsafe_allow_html=True)

# Layout principal - Funil Visual
st.markdown('<div class="section-header">📊 Funil de Conversão</div>', unsafe_allow_html=True)
st.markdown("Clique nos números para editá-los diretamente:")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="stage-card" style="border-color: #3B82F6;">
        <div class="stage-title">👥 Oportunidades</div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.oportunidades = st.number_input(
        "Valor",
        min_value=0,
        value=st.session_state.oportunidades,
        step=1,
        key="oportunidades_input",
        label_visibility="collapsed"
    )

with col2:
    st.markdown(f"""
    <div class="stage-card" style="border-color: #06B6D4;">
        <div class="stage-title">✍️ Inscritos</div>
        <div class="stage-rate">Taxa: {taxa_oportunidades_inscritos:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.inscritos = st.number_input(
        "Valor",
        min_value=0,
        value=st.session_state.inscritos,
        step=1,
        key="inscritos_input",
        label_visibility="collapsed"
    )

with col3:
    st.markdown(f"""
    <div class="stage-card" style="border-color: #8B5CF6;">
        <div class="stage-title">👨‍👩‍👧‍👦 Grupo</div>
        <div class="stage-rate">Taxa: {taxa_inscritos_grupo:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.grupo = st.number_input(
        "Valor",
        min_value=0,
        value=st.session_state.grupo,
        step=1,
        key="grupo_input",
        label_visibility="collapsed"
    )

with col4:
    st.markdown(f"""
    <div class="stage-card" style="border-color: #EC4899;">
        <div class="stage-title">🎯 Qualificados</div>
        <div class="stage-rate">Taxa: {taxa_grupo_qualificados:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.qualificados = st.number_input(
        "Valor",
        min_value=0,
        value=st.session_state.qualificados,
        step=1,
        key="qualificados_input",
        label_visibility="collapsed"
    )

with col5:
    st.markdown(f"""
    <div class="stage-card" style="border-color: #10B981;">
        <div class="stage-title">💵 Vendas</div>
        <div class="stage-rate">Taxa: {taxa_qualificados_vendas:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.vendas = st.number_input(
        "Valor",
        min_value=0,
        value=st.session_state.vendas,
        step=1,
        key="vendas_input",
        label_visibility="collapsed"
    )

# Gráfico de Funil
st.markdown("### 📉 Visualização do Funil")

fig = go.Figure()

# Dados do funil
stages = ['Oportunidades', 'Inscritos', 'Grupo', 'Qualificados', 'Vendas']
values = [
    st.session_state.oportunidades,
    st.session_state.inscritos,
    st.session_state.grupo,
    st.session_state.qualificados,
    st.session_state.vendas
]
colors = ['#3B82F6', '#06B6D4', '#8B5CF6', '#EC4899', '#10B981']

fig.add_trace(go.Funnel(
    y=stages,
    x=values,
    textposition="inside",
    textinfo="value+percent initial",
    marker=dict(color=colors),
    connector=dict(line=dict(color="#374151", width=2))
))

fig.update_layout(
    height=400,
    paper_bgcolor='#000000',
    plot_bgcolor='#000000',
    font=dict(color='white', size=14),
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Ajuste de Taxas de Conversão
st.markdown('<div class="section-header">🎚️ Taxas de Conversão</div>', unsafe_allow_html=True)
st.markdown("Use os sliders para ajustar as taxas e ver o impacto automaticamente:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 👥 Oportunidades → Inscritos")
    nova_taxa_oi = st.slider(
        "Taxa (%)",
        min_value=0.0,
        max_value=100.0,
        value=taxa_oportunidades_inscritos,
        step=0.1,
        key="slider_oi",
        label_visibility="collapsed"
    )
    if abs(nova_taxa_oi - taxa_oportunidades_inscritos) > 0.01:
        st.session_state.inscritos = int(st.session_state.oportunidades * (nova_taxa_oi / 100))
        st.rerun()
    
    st.markdown(f"**Taxa atual:** {taxa_oportunidades_inscritos:.2f}%")
    
    st.markdown("#### 👨‍👩‍👧‍👦 Grupo → Qualificados")
    nova_taxa_gq = st.slider(
        "Taxa (%)",
        min_value=0.0,
        max_value=100.0,
        value=taxa_grupo_qualificados,
        step=0.1,
        key="slider_gq",
        label_visibility="collapsed"
    )
    if abs(nova_taxa_gq - taxa_grupo_qualificados) > 0.01:
        st.session_state.qualificados = int(st.session_state.grupo * (nova_taxa_gq / 100))
        st.rerun()
    
    st.markdown(f"**Taxa atual:** {taxa_grupo_qualificados:.2f}%")

with col2:
    st.markdown("#### ✍️ Inscritos → Grupo")
    nova_taxa_ig = st.slider(
        "Taxa (%)",
        min_value=0.0,
        max_value=100.0,
        value=taxa_inscritos_grupo,
        step=0.1,
        key="slider_ig",
        label_visibility="collapsed"
    )
    if abs(nova_taxa_ig - taxa_inscritos_grupo) > 0.01:
        st.session_state.grupo = int(st.session_state.inscritos * (nova_taxa_ig / 100))
        st.rerun()
    
    st.markdown(f"**Taxa atual:** {taxa_inscritos_grupo:.2f}%")
    
    st.markdown("#### 🎯 Qualificados → Vendas")
    nova_taxa_qv = st.slider(
        "Taxa (%)",
        min_value=0.0,
        max_value=100.0,
        value=taxa_qualificados_vendas,
        step=0.1,
        key="slider_qv",
        label_visibility="collapsed"
    )
    if abs(nova_taxa_qv - taxa_qualificados_vendas) > 0.01:
        st.session_state.vendas = int(st.session_state.qualificados * (nova_taxa_qv / 100))
        st.rerun()
    
    st.markdown(f"**Taxa atual:** {taxa_qualificados_vendas:.2f}%")

# Resumo Financeiro
st.markdown('<div class="section-header">💼 Resumo Financeiro</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="summary-item">
        <div class="summary-label">Ticket Médio</div>
        <div class="summary-value">{formatar_moeda(st.session_state.ticket_medio)}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="summary-item">
        <div class="summary-label">Faturamento Potencial</div>
        <div class="summary-value">{formatar_moeda(faturamento)}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="summary-item">
        <div class="summary-label">Comissão Total ({st.session_state.percentual_comissao:.1f}%)</div>
        <div class="summary-value-highlight">{formatar_moeda(comissao)}</div>
    </div>
    """, unsafe_allow_html=True)

# Análise de Impacto
st.markdown('<div class="section-header">📈 Análise de Impacto</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 O que acontece se você melhorar 5% em cada taxa?")
    
    # Simular melhoria de 5%
    oportunidades_sim = st.session_state.oportunidades
    inscritos_sim = int(oportunidades_sim * (taxa_oportunidades_inscritos + 5) / 100)
    grupo_sim = int(inscritos_sim * (taxa_inscritos_grupo + 5) / 100)
    qualificados_sim = int(grupo_sim * (taxa_grupo_qualificados + 5) / 100)
    vendas_sim = int(qualificados_sim * (taxa_qualificados_vendas + 5) / 100)
    faturamento_sim = vendas_sim * st.session_state.ticket_medio
    comissao_sim = faturamento_sim * (st.session_state.percentual_comissao / 100)
    
    diferenca_vendas = vendas_sim - st.session_state.vendas
    diferenca_comissao = comissao_sim - comissao
    percentual_aumento = ((comissao_sim / comissao) - 1) * 100 if comissao > 0 else 0
    
    st.metric(
        "Vendas Extras",
        f"+{diferenca_vendas} vendas",
        f"{diferenca_vendas}"
    )
    
    st.metric(
        "Comissão Extra",
        formatar_moeda(diferenca_comissao),
        f"+{percentual_aumento:.1f}%"
    )

with col2:
    st.markdown("### 🚀 Potencial de Crescimento")
    
    # Gráfico de barras comparativo
    fig_comparacao = go.Figure()
    
    fig_comparacao.add_trace(go.Bar(
        name='Atual',
        x=['Vendas', 'Comissão (R$)'],
        y=[st.session_state.vendas, comissao],
        marker_color='#3B82F6',
        text=[st.session_state.vendas, formatar_moeda(comissao)],
        textposition='auto',
    ))
    
    fig_comparacao.add_trace(go.Bar(
        name='Com +5% nas taxas',
        x=['Vendas', 'Comissão (R$)'],
        y=[vendas_sim, comissao_sim],
        marker_color='#10B981',
        text=[vendas_sim, formatar_moeda(comissao_sim)],
        textposition='auto',
    ))
    
    fig_comparacao.update_layout(
        barmode='group',
        height=300,
        paper_bgcolor='#000000',
        plot_bgcolor='#111827',
        font=dict(color='white', size=12),
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=True,
        legend=dict(
            bgcolor='#1F2937',
            bordercolor='#374151',
            borderwidth=1
        )
    )
    
    st.plotly_chart(fig_comparacao, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; padding: 2rem 0;">
    <p>💡 <strong>Dica Pro:</strong> Pequenas melhorias consistentes em cada etapa do funil podem gerar grandes resultados!</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">Desenvolvido com ❤️ para maximizar suas comissões</p>
</div>
""", unsafe_allow_html=True)
