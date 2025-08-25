#  Projeto Analytics – Análise de Saúde

Este repositório contém uma **análise exploratória de dados de saúde**, com **visualização interativa** e **predição de risco** utilizando **Python, Streamlit, pandas, plotly e scikit-learn**.  

 **Acesse o dashboard online aqui:** [Projeto Analytics - Streamlit App](https://projetoanalytics-ipqvruv7dlftokwavytnla.streamlit.app)

---

##  Estrutura do Projeto

- `dados/` : Base de dados utilizada na análise (`Medicaldataset.csv`).
- `scripts/` : Scripts Python, incluindo o dashboard Streamlit (`app_streamlit.py`).
- `README.md` : Este arquivo de documentação.
- `.gitignore` : Arquivos e pastas ignorados pelo Git.

---

##  Como rodar o dashboard localmente

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o Streamlit:
   ```bash
   streamlit run scripts/app_streamlit.py
   ```

---

##  Requisitos

- Python 3.8+
- pandas  
- plotly  
- scikit-learn  
- streamlit  

---

##  Insights e Principais Resultados

- **Distribuição dos Resultados:** Aproximadamente **61%** dos pacientes possuem resultado positivo para o desfecho analisado, enquanto **39%** são negativos.  
- **Idade:** Idade média de ~58 anos, com predominância de casos positivos em faixas etárias mais elevadas.  
- **Pressão Sistólica:** Mais de **95%** dos pacientes apresentam algum grau de hipertensão, principalmente entre os casos positivos.  
- **Glicose:** Pacientes com glicose elevada têm maior proporção de resultados positivos, sugerindo associação com o risco.  
- **Correlação entre Variáveis:** As maiores correlações foram entre **CK-MB e Troponin** e entre **pressão sistólica e troponina**.  
- **Outliers:** Identificados principalmente em CK-MB, Troponin e Glicose, podendo indicar casos graves ou erros de medição.  
- **Modelo Preditivo:** O modelo **Random Forest** obteve boa performance utilizando **idade, glicose e pressão sistólica** como variáveis principais.  
- **Dados Limpos:** O dataset não apresentou valores ausentes após o tratamento, aumentando a confiabilidade da análise.  
- **Visualização Interativa:** O **dashboard** permite explorar cenários e simular risco para novos pacientes.  

---

##  Contato

Desenvolvido por **Noam Coelho**.  
Dúvidas ou sugestões? Abra uma [issue](https://github.com/noamcoelho/Projeto_analytics/issues) ou acesse o dashboard interativo no [Streamlit](https://projetoanalytics-ipqvruv7dlftokwavytnla.streamlit.app).
