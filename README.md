# Projeto Analytics - Análise de Saúde

Este repositório contém uma análise exploratória, visualização interativa e predição de risco em saúde utilizando Python, Streamlit, pandas, plotly e scikit-learn.

## Estrutura do Projeto

- `dados/` : Base de dados utilizada na análise (`Medicaldataset.csv`).
- `scripts/` : Scripts Python, incluindo o dashboard Streamlit (`app_streamlit.py`).
- `README.md` : Este arquivo de documentação.
- `.gitignore` : Arquivos e pastas ignorados pelo Git.

## Como rodar o dashboard

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o Streamlit:
   ```bash
   streamlit run scripts/app_streamlit.py
   ```

## Requisitos
- Python 3.8+
- pandas
- plotly
- scikit-learn
- streamlit


## Insights e Principais Resultados

- **Distribuição dos Resultados:** Aproximadamente 61% dos pacientes possuem resultado positivo para o desfecho analisado, enquanto 39% são negativos.
- **Idade:** A idade média dos pacientes é de cerca de 58 anos, com predominância de casos positivos em faixas etárias mais elevadas.
- **Pressão Sistólica:** Mais de 95% dos pacientes apresentam algum grau de hipertensão (pré-hipertensão ou hipertensão estágio 1/2), sendo que a maioria dos positivos está nas faixas mais altas de pressão.
- **Glicose:** Pacientes com glicose elevada têm maior proporção de resultados positivos, indicando associação entre glicemia e risco.
- **Correlação entre Variáveis:** As maiores correlações absolutas encontradas foram entre CK-MB e Troponin, e entre pressão sistólica e troponina, sugerindo relação entre marcadores cardíacos e pressão.
- **Outliers:** Foram identificados outliers principalmente nas variáveis laboratoriais (CK-MB, Troponin, Glicose), o que pode indicar casos graves ou erros de medição.
- **Modelo Preditivo:** O modelo Random Forest foi capaz de prever o risco de resultado positivo com boa performance, utilizando apenas idade, glicose e pressão sistólica.
- **Dados Limpos:** O dataset não apresentou valores ausentes após o tratamento, garantindo robustez nas análises.
- **Visualização Interativa:** O dashboard permite explorar diferentes cenários e simular o risco para novos pacientes, facilitando a tomada de decisão.

---

Projeto desenvolvido para análise de dados de saúde, visualização interativa e predição de risco para novos pacientes.
