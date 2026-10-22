
import streamlit as st

st.set_page_config(
    page_title="Aluguel de Bicicletas",
    page_icon="🚲",
    layout="wide"
)

# Cores e estilo visual
st.markdown("""
<style>
    .stApp {
        background-color: #f4f8f4;
    }

    h1 {
        color: #1d5739;
        font-weight: 800;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    div[data-testid="stTabs"] button {
        font-weight: 600;
        font-size: 16px;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #e0e9e1;
        padding: 20px;
        border-radius: 15px;
    }

    div.stButton > button {
        background-color: #247a50;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #174b34;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# Cabeçalho
st.title("🚲 Aluguel de Bicicletas")
st.caption("Praticidade, liberdade e sustentabilidade em cada pedalada.")

st.markdown("""
<div style="
    background: linear-gradient(120deg, #1d5739, #39875a);
    padding: 25px;
    border-radius: 16px;
    color: white;
    margin-bottom: 25px;
">
    <h2 style="color:white;">Bem-vindo ao Pedal Livre!</h2>
    <p>Cadastre seus dados, escolha seu aluguel e prepare-se para pedalar.</p>
</div>
""", unsafe_allow_html=True)

# Informações
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🚲 Modalidade", "Aluguel")

with col2:
    st.metric("⏱️ Duração", "Por minutos")

with col3:
    st.metric("🌿 Mobilidade", "Sustentável")


st.divider()

# Abas originais mantidas
pag1, pag2 = st.tabs(["👤 Cadastro Cliente", "🚲 Aluguel"])


# ABA 1 - CADASTRO
with pag1:
    st.subheader("👤 Cadastro de Clientes")
    st.write("Preencha seus dados para começar.")

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )

    with col2:
        with st.container(border=True):
            nome = st.text_input("Nome completo", placeholder="Digite seu nome")
            email = st.text_input("E-mail", placeholder="seuemail@exemplo.com")
            telefone = st.text_input("Telefone", placeholder="(11) 99999-9999")

            if st.button("Cadastrar cliente", use_container_width=True):
                if nome.strip() and email.strip() and telefone.strip():
                    st.session_state.cliente = {
                        "nome": nome,
                        "email": email,
                        "telefone": telefone
                    }
                    st.success(f"Cadastro realizado! Bem-vindo(a), {nome}.")
                else:
                    st.warning("Preencha todos os campos para continuar.")


# ABA 2 - ALUGUEL
with pag2:
    st.subheader("🚲 Concluir Aluguel")
    st.write("Escolha a duração do aluguel para calcular o valor.")

    if "cliente" in st.session_state:
        st.info(f"Cliente: {st.session_state.cliente['nome']}")
    else:
        st.info("Você pode realizar o cadastro na primeira aba.")

    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            minutos = st.number_input(
                "Minutos alugados",
                min_value=0,
                max_value=200,
                value=0,
                step=5
            )

        with col2:
            valor_minuto = st.number_input(
                "Valor por minuto (R$)",
                min_value=0.0,
                value=0.50,
                step=0.10,
                format="%.2f"
            )

        valor_total = minutos * valor_minuto

        st.metric("💰 Valor estimado", f"R$ {valor_total:.2f}")

        if st.button(
            "Calcular usando Machine Learning",
            use_container_width=True
        ):
            if minutos > 0:
                st.success("Deu certo! Cálculo realizado.")
                st.write(f"**Tempo alugado:** {minutos} minutos")
                st.write(f"**Valor total:** R$ {valor_total:.2f}")
            else:
                st.warning("Informe uma quantidade de minutos maior que zero.")