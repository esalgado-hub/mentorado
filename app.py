# app.py
import streamlit as st
import pandas as pd

def main():
    # NÃO use st.set_page_config aqui quando for usado como módulo
    st.markdown("""
    <style>
      .main-header { text-align:center;color:#2E8B57;font-size:2.5rem;margin-bottom:1rem;}
      .section-header { color:#4682B4;border-bottom:2px solid #4682B4;padding-bottom:.5rem;margin-top:2rem;margin-bottom:1rem;}
      .status-acima { background:#ffebee;padding:.5rem;border-radius:.5rem;border-left:4px solid #f44336;}
      .status-ideal { background:#e8f5e8;padding:.5rem;border-radius:.5rem;border-left:4px solid #4caf50;}
      .status-abaixo { background:#fff3e0;padding:.5rem;border-radius:.5rem;border-left:4px solid #ff9800;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">💰 Calculadora 50/30/20</h1>', unsafe_allow_html=True)
    st.markdown("**Compare sua distribuição de gastos com o método recomendado.**")
    st.markdown('<h2 class="section-header">1. Informe sua Renda e Gastos Mensais</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        renda_mensal = st.number_input("💵 Renda Mensal Líquida (R$):", min_value=0.0, format="%.2f")
        gastos_pessoais = st.number_input("🎯 Gastos Pessoais:", min_value=0.0, format="%.2f")
    with col2:
        gastos_essenciais = st.number_input("🏠 Gastos Essenciais:", min_value=0.0, format="%.2f")
        investimentos = st.number_input("📈 Investimentos e Dívidas:", min_value=0.0, format="%.2f")

    total_gastos = gastos_essenciais + gastos_pessoais + investimentos
    if renda_mensal > 0 and total_gastos > renda_mensal:
        st.warning(f"⚠️ Seus gastos (R$ {total_gastos:.2f}) superam a renda (R$ {renda_mensal:.2f})")

    if st.button("🔍 ANALISAR MEUS GASTOS", type="primary"):
        if renda_mensal <= 0:
            st.error("❌ Informe uma renda maior que zero.")
            return

        perc_ess = (gastos_essenciais / renda_mensal) * 100 if renda_mensal else 0
        perc_pes = (gastos_pessoais / renda_mensal) * 100 if renda_mensal else 0
        perc_inv = (investimentos / renda_mensal) * 100 if renda_mensal else 0

        def get_status(atual, ideal, cat):
            if cat == "invest":
                return ("🔴 Abaixo", "status-acima") if atual < ideal else ("✅ Ideal ou Acima", "status-ideal")
            if atual > ideal: return ("🔴 Acima", "status-acima")
            if abs(atual - ideal) <= 5: return ("✅ Ideal", "status-ideal")
            return ("🟡 Abaixo", "status-abaixo")

        s_ess, c_ess = get_status(perc_ess, 50, "ess")
        s_pes, c_pes = get_status(perc_pes, 30, "pes")
        s_inv, c_inv = get_status(perc_inv, 20, "invest")

        st.subheader("📊 Sua Distribuição Atual")
        a, b, c = st.columns(3)
        a.metric("Essenciais", f"{perc_ess:.1f}%", f"{perc_ess-50:.1f}% vs ideal")
        b.metric("Pessoais", f"{perc_pes:.1f}%", f"{perc_pes-30:.1f}% vs ideal")
        c.metric("Investimentos", f"{perc_inv:.1f}%", f"{perc_inv-20:.1f}% vs ideal")

        st.subheader("📋 Comparativo com 50/30/20")
        df = pd.DataFrame({
            "Categoria": ["🏠 Essenciais (50%)","🎯 Pessoais (30%)","📈 Investimentos (20%)"],
            "Seu Resultado": [f"{perc_ess:.1f}%", f"{perc_pes:.1f}%", f"{perc_inv:.1f}%"],
            "Recomendado": [f"50% (R$ {0.5*renda_mensal:.2f})", f"30% (R$ {0.3*renda_mensal:.2f})", f"20% (R$ {0.2*renda_mensal:.2f})"],
            "Status": [s_ess, s_pes, s_inv],
        })
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.subheader("🎯 Diagnóstico Rápido")
        if "Acima" in s_ess:
            st.markdown('<div class="status-acima">🔴 <b>Essenciais</b> acima do recomendado.</div>', unsafe_allow_html=True)
        elif "Ideal" in s_ess:
            st.markdown('<div class="status-ideal">✅ <b>Essenciais</b> no ideal.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-abaixo">🟡 <b>Essenciais</b> abaixo.</div>', unsafe_allow_html=True)

        if "Acima" in s_pes:
            st.markdown('<div class="status-acima">🔴 <b>Pessoais</b> acima.</div>', unsafe_allow_html=True)
        elif "Ideal" in s_pes:
            st.markdown('<div class="status-ideal">✅ <b>Pessoais</b> equilibrados.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-abaixo">🟡 <b>Pessoais</b> controlados.</div>', unsafe_allow_html=True)

        if "Abaixo" in s_inv:
            st.markdown('<div class="status-acima">🔴 <b>Investimentos</b> abaixo do recomendado.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-ideal">✅ <b>Investimentos</b> ok.</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("**📚 Regra 50/30/20:** 50% necessidades, 30% desejos, 20% poupança/investimentos.")

# Permite rodar isoladamente (opcional)
if __name__ == "__main__":
    st.set_page_config(page_title="Calculadora 50/30/20", page_icon="💰", layout="wide")
    main()
