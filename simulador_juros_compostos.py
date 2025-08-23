import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def simulador_juros_compostos():
    st.markdown("""
    **📈 Simulador de Juros Compostos**
    
    Veja o poder do tempo e dos juros trabalhando a seu favor! Esta ferramenta mostra como pequenos aportes regulares podem se transformar em grandes patrimônios ao longo do tempo.
    """)

    # Layout em duas colunas
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 💰 Parâmetros da Simulação")
        
        valor_inicial = st.number_input(
            "💵 Valor Inicial (R$):", 
            min_value=0.0, 
            value=1000.0, 
            step=100.0,
            help="Valor que você já possui para começar a investir",
            key="juros_valor_inicial"
        )
        
        aporte_mensal = st.number_input(
            "📅 Aporte Mensal (R$):", 
            min_value=0.0, 
            value=100.0, 
            step=50.0,
            help="Valor que você pretende investir todo mês",
            key="juros_aporte_mensal"
        )
        
        taxa_juros_anual = st.number_input(
            "📊 Taxa de Juros Anual (%):", 
            min_value=0.0, 
            max_value=50.0,
            value=6.0, 
            step=0.5,
            help="Taxa de retorno anual esperada do investimento",
            key="juros_taxa_anual"
        )
        
        periodo_anos = st.slider(
            "⏰ Período (Anos):", 
            min_value=1, 
            max_value=50, 
            value=10,
            help="Por quantos anos você pretende manter o investimento",
            key="juros_periodo_anos"
        )

        # Botão de simulação
        simular = st.button("🚀 Simular Crescimento", key="simular_juros_compostos_btn", type="primary")

    with col2:
        st.markdown("### 📋 Cenários de Comparação")
        
        # Opções de cenários pré-definidos
        cenario_selecionado = st.selectbox(
            "Escolha um cenário para comparar:",
            ["Personalizado", "Conservador (4% a.a.)", "Moderado (8% a.a.)", "Arrojado (12% a.a.)"],
            key="cenario_comparacao"
        )
        
        # Informações educativas
        st.info("""
        **💡 Dica Importante:**
        
        Os juros compostos são chamados de "oitava maravilha do mundo" por Einstein. 
        O segredo está na **consistência** e no **tempo**!
        
        - 🎯 **Consistência:** Aportes regulares, mesmo pequenos
        - ⏳ **Tempo:** Quanto mais cedo começar, melhor
        - 📈 **Paciência:** Deixe os juros trabalharem para você
        """)

    # Área de resultados (será preenchida quando o botão for clicado)
    if simular:
        st.markdown("---")
        st.subheader("📊 Resultados da Simulação")
        
        # Cálculos dos juros compostos
        taxa_mensal = taxa_juros_anual / 100 / 12  # Converte para taxa mensal decimal
        meses_total = periodo_anos * 12
        
        # Listas para armazenar os dados da simulação
        meses = []
        valores_acumulados = []
        aportes_totais = []
        juros_acumulados = []
        
        valor_atual = valor_inicial
        aporte_total = valor_inicial
        
        for mes in range(meses_total + 1):
            meses.append(mes)
            valores_acumulados.append(valor_atual)
            aportes_totais.append(aporte_total)
            juros_acumulados.append(valor_atual - aporte_total)
            
            # Aplica juros e adiciona aporte (exceto no último mês)
            if mes < meses_total:
                valor_atual = valor_atual * (1 + taxa_mensal) + aporte_mensal
                aporte_total += aporte_mensal
        
        # Valores finais
        valor_final = valores_acumulados[-1]
        total_aportes = aportes_totais[-1]
        total_juros = juros_acumulados[-1]
        
        # Cálculo do cenário de comparação
        cenarios_taxa = {
            "Conservador (4% a.a.)": 4.0,
            "Moderado (8% a.a.)": 8.0,
            "Arrojado (12% a.a.)": 12.0
        }
        
        if cenario_selecionado != "Personalizado":
            taxa_comparacao = cenarios_taxa[cenario_selecionado] / 100 / 12
            valor_comparacao = valor_inicial
            aporte_total_comp = valor_inicial
            
            for mes in range(meses_total):
                valor_comparacao = valor_comparacao * (1 + taxa_comparacao) + aporte_mensal
                aporte_total_comp += aporte_mensal
        
        # Criação do DataFrame para o gráfico
        df_simulacao = pd.DataFrame({
            'Mês': meses,
            'Valor Acumulado': valores_acumulados,
            'Aportes Totais': aportes_totais,
            'Juros Acumulados': juros_acumulados
        })
        
        # Convertendo meses para anos para melhor visualização
        df_simulacao['Ano'] = df_simulacao['Mês'] / 12
        
        # Gráfico interativo
        st.markdown("### 📈 Evolução do Patrimônio")
        
        fig = go.Figure()
        
        # Linha do valor total acumulado
        fig.add_trace(go.Scatter(
            x=df_simulacao['Ano'],
            y=df_simulacao['Valor Acumulado'],
            mode='lines',
            name='Valor Total',
            line=dict(color='#1f77b4', width=3),
            hovertemplate='<b>Ano %{x:.1f}</b><br>Valor Total: R$ %{y:,.2f}<extra></extra>'
        ))
        
        # Linha dos aportes totais
        fig.add_trace(go.Scatter(
            x=df_simulacao['Ano'],
            y=df_simulacao['Aportes Totais'],
            mode='lines',
            name='Aportes Totais',
            line=dict(color='#ff7f0e', width=2),
            hovertemplate='<b>Ano %{x:.1f}</b><br>Aportes: R$ %{y:,.2f}<extra></extra>'
        ))
        
        # Linha dos juros acumulados
        fig.add_trace(go.Scatter(
            x=df_simulacao['Ano'],
            y=df_simulacao['Juros Acumulados'],
            mode='lines',
            name='Juros Acumulados',
            line=dict(color='#2ca02c', width=2),
            fill='tonexty',
            hovertemplate='<b>Ano %{x:.1f}</b><br>Juros: R$ %{y:,.2f}<extra></extra>'
        ))
        
        # Linha de comparação (se aplicável)
        if cenario_selecionado != "Personalizado":
            anos_comparacao = [i/12 for i in range(meses_total + 1)]
            valores_comparacao = []
            valor_comp_atual = valor_inicial
            aporte_comp_total = valor_inicial
            
            for mes in range(meses_total + 1):
                valores_comparacao.append(valor_comp_atual)
                if mes < meses_total:
                    valor_comp_atual = valor_comp_atual * (1 + taxa_comparacao) + aporte_mensal
            
            fig.add_trace(go.Scatter(
                x=anos_comparacao,
                y=valores_comparacao,
                mode='lines',
                name=f'Cenário {cenario_selecionado}',
                line=dict(color='#d62728', width=2, dash='dash'),
                hovertemplate=f'<b>Ano %{{x:.1f}}</b><br>{cenario_selecionado}: R$ %{{y:,.2f}}<extra></extra>'
            ))
        
        fig.update_layout(
            title='Evolução do Patrimônio ao Longo do Tempo',
            xaxis_title='Anos',
            yaxis_title='Valor (R$)',
            hovermode='x unified',
            height=500,
            showlegend=True
        )
        
        # Formatação do eixo Y para valores em reais
        fig.update_layout(yaxis=dict(tickformat=',.0f'))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Resumo financeiro
        st.markdown("### 💰 Resumo Financeiro")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="💵 Valor Final",
                value=f"R$ {valor_final:,.2f}",
                delta=f"R$ {total_juros:,.2f} em juros"
            )
        
        with col2:
            st.metric(
                label="📊 Total Investido",
                value=f"R$ {total_aportes:,.2f}",
                delta=f"{periodo_anos} anos de aportes"
            )
        
        with col3:
            rentabilidade = ((valor_final / total_aportes) - 1) * 100
            st.metric(
                label="📈 Rentabilidade Total",
                value=f"{rentabilidade:.1f}%",
                delta=f"{taxa_juros_anual:.1f}% ao ano"
            )
        
        # Tabela detalhada (apenas anos principais)
        st.markdown("### 📋 Evolução Detalhada (Por Ano)")
        
        # Filtra dados apenas para o final de cada ano
        df_anual = df_simulacao[df_simulacao['Mês'] % 12 == 0].copy()
        df_anual['Ano'] = df_anual['Mês'] // 12
        df_anual = df_anual[['Ano', 'Valor Acumulado', 'Aportes Totais', 'Juros Acumulados']]
        
        # Formatação da tabela
        df_anual['Valor Acumulado'] = df_anual['Valor Acumulado'].apply(lambda x: f"R$ {x:,.2f}")
        df_anual['Aportes Totais'] = df_anual['Aportes Totais'].apply(lambda x: f"R$ {x:,.2f}")
        df_anual['Juros Acumulados'] = df_anual['Juros Acumulados'].apply(lambda x: f"R$ {x:,.2f}")
        
        st.dataframe(df_anual, use_container_width=True, hide_index=True)
        
        # Análise e insights
        st.markdown("### 🎯 Análise e Insights")
        
        # Cálculo de insights
        participacao_juros = (total_juros / valor_final) * 100
        valor_sem_juros = total_aportes
        multiplicador = valor_final / total_aportes
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"""
            **🔍 Análise do Seu Investimento:**
            
            • **Participação dos Juros:** {participacao_juros:.1f}% do valor final
            • **Multiplicador:** Seu dinheiro cresceu {multiplicador:.1f}x
            • **Poder dos Juros:** R$ {total_juros:,.2f} "de graça"
            """)
        
        with col2:
            if participacao_juros > 50:
                st.success(f"""
                **🎉 Excelente Estratégia!**
                
                Os juros representam mais da metade do seu patrimônio final. 
                Isso mostra o poder dos juros compostos trabalhando a seu favor!
                """)
            elif participacao_juros > 30:
                st.warning(f"""
                **👍 Boa Estratégia!**
                
                Os juros já representam uma parte significativa do patrimônio. 
                Considere aumentar o período ou a taxa para potencializar ainda mais.
                """)
            else:
                st.error(f"""
                **💡 Dica de Melhoria:**
                
                Os juros ainda representam uma pequena parte. 
                Considere aumentar o período de investimento ou buscar melhores taxas.
                """)
        
        # Comparação com cenário (se aplicável)
        if cenario_selecionado != "Personalizado":
            diferenca = valor_final - valor_comparacao
            if diferenca > 0:
                st.success(f"""
                **📊 Comparação com {cenario_selecionado}:**
                
                Sua estratégia atual resultaria em **R$ {diferenca:,.2f} a mais** 
                comparado ao cenário {cenario_selecionado.lower()}.
                """)
            else:
                st.warning(f"""
                **📊 Comparação com {cenario_selecionado}:**
                
                O cenário {cenario_selecionado.lower()} resultaria em **R$ {abs(diferenca):,.2f} a mais** 
                que sua estratégia atual.
                """)
        
        # Dicas finais
        st.markdown("---")
        st.markdown("""
        **💡 Dicas para Maximizar seus Resultados:**
        
        1. **🎯 Consistência é Fundamental:** Mantenha os aportes regulares, mesmo que pequenos
        2. **⏰ Comece Hoje:** Cada mês que você adia, perde o poder dos juros compostos
        3. **📈 Reinvista os Rendimentos:** Deixe os juros trabalharem para gerar mais juros
        4. **🔍 Revise Periodicamente:** Ajuste a estratégia conforme sua situação muda
        5. **🎓 Continue Aprendendo:** Busque conhecimento para tomar melhores decisões
        """)



