import streamlit as st

# Configuração da página
st.set_page_config(page_title="Centro Automotivo - Gestão", layout="centered")
st.title("🔧 Sistema de Fluxo - Centro Automotivo")

# Criando as abas do processo da oficina
aba_cadastro, aba_servicos, aba_status = st.tabs([
    "📋 1. Recepção e Cadastro", 
    "💰 2. Orçamento de Serviços", 
    "🚗 3. Status da Oficina"
])

# --- ABA 1: RECEPÇÃO E CADASTRO ---
with aba_cadastro:
    st.header("Cadastro do Cliente e Veículo")
    
    # Entradas de dados
    nome_cliente = st.text_input("Nome do Cliente:", "João Silva")
    veiculo = st.text_input("Modelo do Veículo:", "Vw Gol 1.0")
    placa = st.text_input("Placa:", "ABC-1234")
    
    st.info("Preencha os dados acima e siga para a aba de Orçamento.")

# --- ABA 2: ORÇAMENTO E SERVIÇOS ---
with aba_servicos:
    st.header("Seleção de Serviços e Peças")
    st.write(f"**Cliente atual:** {nome_cliente} | **Carro:** {veiculo} ({placa})")
    
    st.divider()
    
    # 1. Seção de Motor
    st.subheader("⚙️ Serviços de Motor")
    servicos_motor = st.multiselect(
        "Selecione os serviços de motor necessários:",
        ["Troca de Óleo e Filtro (R$ 250)", "Troca de Correia Dentada (R$ 450)", "Retífica de Cabeçote (R$ 1500)"]
    )
    
    # 2. Seção de Suspensão
    st.subheader("🔩 Serviços de Suspensão")
    servicos_suspenso = st.multiselect(
        "Selecione os serviços de suspensão necessários:",
        ["Troca de Amortecedores Dianteiros (R$ 850)", "Troca de Buchas da Balança (R$ 300)", "Troca de Pastilhas de Freio (R$ 200)"]
    )
    
    # 3. Seção de Alinhamento
    st.subheader("📐 Alinhamento e Balanceamento")
    alinhamento_escolhido = st.checkbox("Alinhamento 3D + Balanceamento das 4 Rodas (R$ 150)")

    st.divider()
    
    # Lógica para calcular o valor total
    valor_total = 0
    
    # Somando Motor
    for s in servicos_motor:
        if "250" in s: valor_total += 250
        if "450" in s: valor_total += 450
        if "1500" in s: valor_total += 1500
        
    # Somando Suspensão
    for s in servicos_suspenso:
        if "850" in s: valor_total += 850
        if "300" in s: valor_total += 300
        if "200" in s: valor_total += 200
        
    # Somando Alinhamento
    if alinhamento_escolhido:
        valor_total += 150

    # Mostra o valor total dinamicamente
    st.metric(label="Valor Total do Orçamento", value=f"R$ {valor_total},00")
    
    if st.button("Aprovar Orçamento e Enviar para Oficina"):
        st.success("✅ Orçamento aprovado com sucesso! Carro enviado para a fila de execução.")

# --- ABA 3: STATUS DA OFICINA ---
with aba_status:
    st.header("Acompanhamento do Processo")
    
    st.write("Acompanhe em qual estágio o veículo se encontra na oficina:")
    
    # Estado do fluxo usando um botão de seleção (Radio)
    status_atual = st.radio(
        "Mudar Status do Veículo:",
        ["Na Fila de Espera", "Em Diagnóstico", "Manutenção do Motor", "Manutenção da Suspensão", "Na Rampa de Alinhamento", "Pronto para Entrega"]
    )
    
    st.divider()
    
    # Exibição visual do status atual para o cliente ou gerente
    if status_atual == "Na Fila de Espera":
        st.warning(f"⏳ O {veiculo} de {nome_cliente} está aguardando mecânico livre.")
    elif status_atual == "Em Diagnóstico":
        st.info(f"🔍 Mecânico inspecionando o motor e a suspensão do {veiculo}.")
    elif "Manutenção" in status_atual:
        st.error(f"🛠️ Executando reparos ativos: {status_atual}.")
    elif status_atual == "Na Rampa de Alinhamento":
        st.info(f"📐 Veículo no equipamento de Alinhamento 3D e cambagem.")
    elif status_atual == "Pronto para Entrega":
        st.success(f"🎉 Tudo pronto! O {veiculo} já pode ser retirado por {nome_cliente}. Total: R$ {valor_total},00")