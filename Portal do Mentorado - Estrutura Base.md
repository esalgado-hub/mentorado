# Portal do Mentorado - Estrutura Base

## 📋 Descrição do Projeto

Este é o portal base para mentoria financeira, desenvolvido em Streamlit. O portal oferece uma interface completa para acompanhamento do progresso do mentorado, gestão de tarefas e acesso a ferramentas financeiras.

## 🚀 Funcionalidades Implementadas

### 1. Dashboard Principal
- **Fluxo de Mentoria**: Visualização das 6 etapas da mentoria com status
  - Alinhamento ✅
  - Objetivos/Metas 🔄
  - Análise Financeira ⏳
  - Revisão Financeira ⏳
  - Planejamento ⏳
  - Ajuste de Rota ⏳

- **Mini Diagnóstico**: Campos para anotações pós-sessões
- **Pontos Fortes e Melhorias**: Visualização clara com cores
- **Metas**: Acompanhamento de progresso com sliders interativos
  - Meta 1 ano (25% concluído)
  - Meta 5 anos (10% concluído)
  - Meta 10 anos (5% concluído)

### 2. Tarefas - Dever de Casa
- **Tarefas do Mentor**: Lista com checkboxes e campos de observação
- **Progresso Visual**: Métrica e barra de progresso
- **Tarefas Próprias**: Seção para o mentorado criar suas próprias tarefas
- **Funcionalidade de Adicionar**: Botão para incluir novas tarefas

### 3. Ferramentas
- **Calculadoras de Orçamento**:
  - Calculadora 50/30/20 (integrada)
  - Análise de Gastos Mensais (em desenvolvimento)

- **Simuladores de Investimento**:
  - Simulador de Juros Compostos (em desenvolvimento)
  - Calculadora de Objetivos (em planejamento)

- **Perfis e Questionários**:
  - Perfil de Investidor (em desenvolvimento)
  - Perfil Financeiro (em planejamento)

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework principal para interface web
- **Python**: Linguagem de programação
- **CSS Customizado**: Estilização personalizada
- **Pandas**: Manipulação de dados (para futuras integrações)

## 📁 Estrutura de Arquivos

```
portal_mentoria/
├── app.py              # Aplicação principal
├── README.md           # Esta documentação
└── requirements.txt    # Dependências (se necessário)
```

## 🚀 Como Executar

1. Navegue até o diretório do projeto:
   ```bash
   cd /home/ubuntu/portal_mentoria
   ```

2. Execute a aplicação:
   ```bash
   streamlit run app.py --server.port 8502
   ```

3. Acesse no navegador:
   ```
   https://8502-ik15f14mdmydx2g68z8pr-c55d69fc.manusvm.computer
   ```

## 🔗 Integração com Calculadora 50/30/20

A Calculadora 50/30/20 já desenvolvida está referenciada no portal e pode ser acessada através do link fornecido na seção Ferramentas.

**URL da Calculadora**: https://8501-ik15f14mdmydx2g68z8pr-c55d69fc.manusvm.computer

## 📈 Próximos Passos

1. **Sistema de Dados**: Implementar persistência de dados para cada mentorado
2. **Integração Completa**: Incorporar a Calculadora 50/30/20 diretamente no portal
3. **Novas Ferramentas**: Desenvolver o Simulador de Juros Compostos
4. **Autenticação**: Sistema de login para múltiplos mentorados
5. **Personalização**: Temas e configurações personalizáveis

## 💡 Observações

- O portal está totalmente funcional como estrutura base
- A navegação entre páginas funciona perfeitamente
- O design é responsivo e profissional
- Todas as funcionalidades básicas estão implementadas
- Pronto para expansão com novas ferramentas

---

**Desenvolvido para mentoria financeira** 💰📊

