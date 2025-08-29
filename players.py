import streamlit as st
import pandas as pd

# 1. Carregue os dados
df = pd.read_csv('all_seasons.csv')

# 2. Renomeie as colunas para português
df = df.rename(columns={
    'player_name': 'Nome_do_Jogador',
    'pts': 'Pontos_Por_Jogo',
    'reb': 'Rebotes_Por_Jogo',
    'ast': 'Assistências_Por_Jogo',
    'ts_pct': 'Porcentagem_TS',
    'net_rating': 'Net_Rating',
    'player_height': 'Altura_do_Jogador',
    'player_weight': 'Peso_do_Jogador',
    'season': 'Temporada'
})

st.set_page_config(layout="wide")
st.title('Compare Jogadores da NBA 🏀')

# 3. Obtenha listas de nomes de jogadores e temporadas únicas
nomes_jogadores = sorted(df['Nome_do_Jogador'].unique())
temporadas_disponiveis = sorted(df['Temporada'].unique())

# 4. Crie os campos de seleção para o primeiro jogador
st.header('Primeiro Jogador')
jogador1_nome = st.selectbox('Selecione o primeiro jogador:', nomes_jogadores, key='player1')
temporada1 = st.selectbox('Selecione a temporada:', temporadas_disponiveis, key='season1')

# 5. Crie os campos de seleção para o segundo jogador
st.header('Segundo Jogador')
jogador2_nome = st.selectbox('Selecione o segundo jogador:', nomes_jogadores, key='player2')
temporada2 = st.selectbox('Selecione a temporada:', temporadas_disponiveis, key='season2')

# 6. Lógica de comparação
if jogador1_nome and jogador2_nome and temporada1 and temporada2:
    jogador1 = df[(df['Nome_do_Jogador'] == jogador1_nome) & (df['Temporada'] == temporada1)]
    jogador2 = df[(df['Nome_do_Jogador'] == jogador2_nome) & (df['Temporada'] == temporada2)]

    if not jogador1.empty and not jogador2.empty:
        # 7. Exiba os resultados
        st.write('### Comparação de Estatísticas')

        # Cria um DataFrame para exibir as estatísticas lado a lado
        stats_to_compare = ['Pontos_Por_Jogo', 'Rebotes_Por_Jogo', 'Assistências_Por_Jogo', 'Porcentagem_TS', 'Net_Rating']

        # Renomeia as colunas para melhor visualização
        df_comparacao = pd.DataFrame({
            f'{jogador1_nome} ({temporada1})': jogador1[stats_to_compare].iloc[0],
            f'{jogador2_nome} ({temporada2})': jogador2[stats_to_compare].iloc[0]
        })

        st.dataframe(df_comparacao)

    elif jogador1.empty:
        st.warning(f'Não há dados para "{jogador1_nome}" na temporada "{temporada1}".')
    elif jogador2.empty:

        st.warning(f'Não há dados para "{jogador2_nome}" na temporada "{temporada2}".')
