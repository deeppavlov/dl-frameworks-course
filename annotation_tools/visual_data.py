import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_agg import RendererAgg

@st.cache
def get_data_deputies():
     return pd.read_csv('df_dep.csv')

@st.cache
def get_data_political_parties():
     return pd.read_csv('df_polpar.csv')

#configuration of the page
st.set_page_config(layout="wide")
#load dataframes
df_dep = get_data_deputies()
df_pol_par = get_data_political_parties()
st.title('French national assembly vizualisation tool')
st.markdown("""
This app performs simple visualization from the open data from the french national assembly!
""")
st.write(df_dep)
st.write(df_pol_par)

#Делаем визуализацию интерактивной
st.sidebar.header('Select what to display')
pol_parties = df_dep['pol party'].unique().tolist()
pol_party_selected = st.sidebar.multiselect('Political parties', pol_parties, pol_parties)
nb_deputies = df_dep['pol party'].value_counts()
nb_mbrs = st.sidebar.slider("Number of members", int(nb_deputies.min()), int(nb_deputies.max()), (int(nb_deputies.min()), int(nb_deputies.max())), 1)

# creates masks from the sidebar selection widgets
mask_pol_par = df_dep['pol party'].isin(pol_party_selected)
#get the parties with a number of members in the range of nb_mbrs
mask_mbrs = df_dep['pol party'].value_counts().between(nb_mbrs[0], nb_mbrs[1]).to_frame()
mask_mbrs= mask_mbrs[mask_mbrs['pol party'] == 1].index.to_list()
mask_mbrs= df_dep['pol party'].isin(mask_mbrs)
#
df_dep_filtered = df_dep[mask_pol_par & mask_mbrs]
st.write(df_dep_filtered)


matplotlib.use("agg")
_lock = RendererAgg.lock

# pie chart
pol_par = df_dep_filtered['pol party'].value_counts()
#merge the two dataframe to get a column with the color
df = pd.merge(pd.DataFrame(pol_par), df_pol_par, left_index=True, right_on='abreviated_name')
colors = df['color'].tolist()

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.2, 1, .2, 1, .2))
with row0_1, _lock:
    st.header("Political parties")
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(pol_par, labels=(pol_par.index + ' (' + pol_par.map(str)
    + ')'), wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white'
    }, colors=colors)
    #display a white circle in the middle of the pie chart
    p = plt.gcf()
    p.gca().add_artist(plt.Circle( (0,0), 0.7, color='white'))
    st.pyplot(fig)

with row0_2:
    df = df.reset_index(drop=True)
    t = ''
    for i in range(len(df)):
       t=t+df.loc[i,'abreviated_name']+' : '+df.loc[i,'name']+'  \n'
    for i in range(5):
       st.write("")
    st.write(t)


df = df_dep[mask_pol_par & mask_mbrs]
df_sex = pd.concat([df, pd.get_dummies((df)['sex'], prefix='sex')],axis=1)
#we group by political parties and sum the male and female
df_sex = df_sex.groupby(['pol party']).agg({'sex_female':'sum','sex_male':'sum'})
#calculate the proportion of women per parties
df_sex['pol party'] = df_sex.index
df_sex['total'] = df_sex['sex_female'].astype(int) + df_sex['sex_male']
df_sex['ratio_f'] = df_sex['sex_female']/df_sex['total']

df_sex = pd.merge(df_sex, df_pol_par, left_index=True, right_on='abreviated_name')
df_sex = df_sex.sort_values(by=['ratio_f'], ascending=False)
colors = df_sex['color'].tolist()

row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.beta_columns((0.2, 1, .2, 1, .2))
with row2_1, _lock:
    st.header('Women deputies')
    fig, ax = plt.subplots(figsize=(5, 5))
    sns.barplot(x="ratio_f", y="pol party", data=df_sex,
    ax=ax, palette=colors)
    ax.set_ylabel('Political party')
    ax.set_xlabel('Percentage of women deputies')
    i = 0
    text = (df_sex['ratio_f'].round(2)*100).astype(int).to_list()
    for rect in ax.patches:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., rect.get_y()
        + height * 3 / 4., str(text[i])+'%', ha='center',
        va='bottom', rotation=0, color='white', fontsize=12)
        i = i + 1
    st.pyplot(fig)