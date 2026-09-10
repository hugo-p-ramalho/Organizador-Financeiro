# Organizador Financeiro - Análise de Gastos com Python

Pipeline de dados em Python para controle financeiro pessoal, transformando dados brutos de CSV em insights visuais.

Projeto desenvolvido para demonstrar fundamentos de Engenharia de Dados e Análise de Dados com Python.

### Tecnologias
- **Python 3.11+**
- **Pandas** - Limpeza, tratamento e agregação de dados
- **Matplotlib** - Geração de visualizações

### Arquitetura do Pipeline
1.  **Ingestão:** Leitura de dados transacionais de `gastos_exemplo.csv`
2.  **Transformação:** Tratamento com Pandas, agrupamento por categoria e cálculo de totais
3.  **Visualização:** Geração de gráfico de distribuição de gastos

### Como executar
```bash
# Clone o repositório
git clone https://github.com/hugo-p-ramalho/Organizador-Financeiro.git

# Entre na pasta
cd Organizador-Financeiro

# Instale as dependências
pip install -r requirements.txt

# Execute
python main.py


Exemplo de Saída
O script gera um gráfico de pizza/barras mostrando para onde seu dinheiro está indo, permitindo decisões baseadas em dados.

Próximos Passos (Roadmap)
Migrar armazenamento de CSV para SQLite
Criar dashboard interativo com Streamlit
Automatizar ingestão com API bancária (Open Banking)

Desenvolvido por Hugo P. Ramalho | Em transição para Engenharia de Dados/Ciência de Dados
