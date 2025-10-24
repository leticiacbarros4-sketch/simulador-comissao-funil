# 💰 Simulador de Comissões - Streamlit

Aplicação interativa para simulação de comissões com base nas taxas de conversão do funil comercial.

## 🚀 Como Executar

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
streamlit run simulador_comissao.py
```

A aplicação abrirá automaticamente no seu navegador em `http://localhost:8501`

## ✨ Funcionalidades

### 📊 Funil Interativo
- **Edite números diretamente**: Clique nos campos de cada etapa do funil e altere os valores
- **Ajuste pelas taxas**: Use os sliders para modificar as taxas de conversão
- **Visualização gráfica**: Funil visual mostrando o fluxo de conversão

### 💰 Cálculos Automáticos
- **Comissão em destaque**: Visualização grande da comissão potencial
- **Faturamento**: Cálculo automático baseado no ticket médio
- **Taxas dinâmicas**: Taxas de conversão recalculadas automaticamente

### 🎯 Simulações
- **Configurações personalizáveis**: Ajuste oportunidades, ticket médio e % de comissão
- **Análise de impacto**: Veja o que acontece com uma melhoria de 5% nas taxas
- **Gráficos comparativos**: Compare cenário atual vs. potencial

### 🎨 Design Moderno
- **Tema escuro**: Fundo preto com textos brancos
- **Visual profissional**: Gradientes e cores vibrantes
- **Responsivo**: Funciona em diferentes tamanhos de tela

## 📋 Estrutura do Funil

1. **Oportunidades** → Total de leads no topo do funil
2. **Inscritos** → Leads que se inscreveram
3. **Grupo** → Leads que participaram do grupo
4. **Qualificados** → Leads qualificados para venda
5. **Vendas (Pitch)** → Vendas fechadas

## 🔧 Configurações

Na barra lateral você pode ajustar:
- **Oportunidades Totais**: Número de leads no início
- **Ticket Médio**: Valor médio de cada venda
- **Percentual de Comissão**: Sua comissão sobre o faturamento

## 💡 Dicas de Uso

1. **Teste cenários otimistas**: Aumente as taxas gradualmente para ver o impacto
2. **Identifique gargalos**: Veja qual etapa tem a menor conversão
3. **Simule metas**: Ajuste os números para suas metas de vendas
4. **Compare cenários**: Use a análise de impacto para ver o potencial

## 📊 Dados Base (Exemplo)

- Oportunidades: 2.850
- Inscritos: 1.334
- Grupo: 863
- Qualificados: 503
- Vendas: 188
- Ticket Médio: R$ 3.470,93
- Comissão: 5%

## 🛠️ Tecnologias

- **Streamlit**: Framework para aplicações web em Python
- **Plotly**: Biblioteca de visualização interativa
- **Python 3.7+**: Linguagem de programação

## 📝 Notas

- Todos os valores são editáveis em tempo real
- As taxas de conversão são calculadas automaticamente
- Os cálculos financeiros são atualizados instantaneamente
- A aplicação mantém o estado durante a sessão

---

Desenvolvido para maximizar suas comissões! 🚀
