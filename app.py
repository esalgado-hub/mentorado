import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calculadora 50/30/20",
    page_icon="💰",
    layout="wide"
)

# CSS personalizado para melhorar o visual
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .section-header {
        color: #4682B4;
        border-bottom: 2px solid #4682B4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .status-acima {
        background-color: #ffebee;
        padding: 0.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #f44336;
    }
    .status-ideal {
        background-color: #e8f5e8;
        padding: 0.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4caf50;
    }
    .status-abaixo {
        background-color: #fff3e0;
        padding: 0.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff9800;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">💰 Calculadora 50/30/20</h1>', unsafe_allow_html=True)
st.markdown("**Compare sua distribuição de gastos com o método recomendado.**")

st.markdown('<h2 class="section-header">1. Informe sua Renda e Gastos Mensais</h2>', unsafe_allow_html=True)

# Organizando em colunas para melhor layout
col1, col2 = st.columns(2)

with col1:
    renda_mensal = st.number_input(
        "💵 Renda Mensal Líquida (R$):", 
        min_value=0.0, 
        format="%.2f",
        help="Sua renda após descontos de impostos e contribuições"
    )
    
    gastos_pessoais = st.number_input(
        "🎯 Gastos Pessoais (Lazer, Hobbies, Restaurantes, etc.):", 
        min_value=0.0, 
        format="%.2f",
        help="Gastos com entretenimento, hobbies, compras não essenciais"
    )

with col2:
    gastos_essenciais = st.number_input(
        "🏠 Gastos Essenciais (Moradia, Contas, Transporte, etc.):", 
        min_value=0.0, 
        format="%.2f",
        help="Gastos obrigatórios como aluguel, contas básicas, alimentação"
    )
    
    investimentos = st.number_input(
        "📈 Investimentos e Pagamento de Dívidas:", 
        min_value=0.0, 
        format="%.2f",
        help="Valores destinados a investimentos e quitação de dívidas"
    )

# Validação dos dados
total_gastos = gastos_essenciais + gastos_pessoais + investimentos
if renda_mensal > 0 and total_gastos > renda_mensal:
    st.warning(f"⚠️ Atenção: Seus gastos totais (R$ {total_gastos:.2f}) são maiores que sua renda (R$ {renda_mensal:.2f})")

calcular_button = st.button("🔍 ANALISAR MEUS GASTOS", type="primary")

st.markdown('<h2 class="section-header">2. Resultado da Análise</h2>', unsafe_allow_html=True)

if calcular_button:
    if renda_mensal > 0:
        # Cálculos
        perc_essenciais = (gastos_essenciais / renda_mensal) * 100
        perc_pessoais = (gastos_pessoais / renda_mensal) * 100
        perc_investimentos = (investimentos / renda_mensal) * 100
        
        # Determinar status
        def get_status(atual, ideal, categoria):
            if categoria == "investimentos":
                if atual < ideal: return "🔴 Abaixo", "status-acima"
                elif atual >= ideal: return "✅ Ideal ou Acima", "status-ideal"
            else:
                if atual > ideal: return "🔴 Acima", "status-acima"
                elif abs(atual - ideal) <= 5: return "✅ Ideal", "status-ideal"
                else: return "🟡 Abaixo", "status-abaixo"
        
        status_essenciais, class_essenciais = get_status(perc_essenciais, 50, "essenciais")
        status_pessoais, class_pessoais = get_status(perc_pessoais, 30, "pessoais")
        status_investimentos, class_investimentos = get_status(perc_investimentos, 20, "investimentos")

        # Exibir distribuição atual
        st.subheader("📊 Sua Distribuição Atual")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Gastos Essenciais", f"{perc_essenciais:.1f}%", f"{perc_essenciais-50:.1f}% vs ideal")
        with col2:
            st.metric("Gastos Pessoais", f"{perc_pessoais:.1f}%", f"{perc_pessoais-30:.1f}% vs ideal")
        with col3:
            st.metric("Investimentos", f"{perc_investimentos:.1f}%", f"{perc_investimentos-20:.1f}% vs ideal")

        # Tabela comparativa
        st.subheader("📋 Comparativo com 50/30/20")
        
        df = pd.DataFrame({
            "Categoria": ["🏠 Gastos Essenciais (50%)", "🎯 Gastos Pessoais (30%)", "📈 Investimentos e Metas (20%)"],
            "Seu Resultado": [f"{perc_essenciais:.1f}%", f"{perc_pessoais:.1f}%", f"{perc_investimentos:.1f}%"],
            "Recomendado": [f"50% (R$ {0.5 * renda_mensal:.2f})", f"30% (R$ {0.3 * renda_mensal:.2f})", f"20% (R$ {0.2 * renda_mensal:.2f})"],
            "Status": [status_essenciais, status_pessoais, status_investimentos]
        })
        
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Diagnóstico personalizado
        st.subheader("🎯 Diagnóstico Rápido")
        
        if "Acima" in status_essenciais:
            st.markdown('<div class="status-acima">🔴 <strong>Gastos Essenciais:</strong> Estão acima do recomendado. Considere revisar suas despesas fixas, renegociar contratos ou buscar alternativas mais econômicas.</div>', unsafe_allow_html=True)
        elif "Ideal" in status_essenciais:
            st.markdown('<div class="status-ideal">✅ <strong>Gastos Essenciais:</strong> Estão no patamar ideal. Parabéns pelo controle!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-abaixo">🟡 <strong>Gastos Essenciais:</strong> Estão abaixo do esperado. Ótimo controle de custos!</div>', unsafe_allow_html=True)

        if "Acima" in status_pessoais:
            st.markdown('<div class="status-acima">🔴 <strong>Gastos Pessoais:</strong> Estão acima do recomendado. Avalie seus gastos variáveis e considere reduzir algumas despesas supérfluas.</div>', unsafe_allow_html=True)
        elif "Ideal" in status_pessoais:
            st.markdown('<div class="status-ideal">✅ <strong>Gastos Pessoais:</strong> Estão equilibrados. Você consegue se divertir sem comprometer o orçamento!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-abaixo">🟡 <strong>Gastos Pessoais:</strong> Estão controlados. Você pode se permitir um pouco mais de lazer, se desejar.</div>', unsafe_allow_html=True)

        if "Abaixo" in status_investimentos:
            st.markdown('<div class="status-acima">🔴 <strong>Investimentos:</strong> Estão abaixo do recomendado. Busque aumentar sua poupança para construir um futuro mais seguro.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-ideal">✅ <strong>Investimentos:</strong> Parabéns! Você está priorizando seu futuro financeiro.</div>', unsafe_allow_html=True)
            
        # Dicas adicionais
        st.subheader("💡 Dicas para Melhorar")
        if perc_essenciais > 50:
            st.info("💡 **Para reduzir gastos essenciais:** Renegocie contratos, compare preços de fornecedores, considere mudanças de hábitos que reduzam custos fixos.")
        if perc_investimentos < 20:
            st.info("💡 **Para aumentar investimentos:** Comece pequeno, automatize transferências, corte gastos desnecessários e direcione para investimentos.")

    else:
        st.error("❌ Por favor, insira uma Renda Mensal Líquida maior que zero para calcular.")

# Rodapé informativo
st.markdown("---")
st.markdown("**📚 Sobre a Regra 50/30/20:** Esta é uma diretriz popular de orçamento que sugere destinar 50% da renda para necessidades, 30% para desejos e 20% para poupança e investimentos.")


