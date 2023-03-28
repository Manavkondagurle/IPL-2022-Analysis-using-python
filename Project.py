import pandas as pd 
import os
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_csv('C:/Users/manav/OneDrive/Desktop/ITW/Book_ipl22_ver_33.csv')
print(data)
figure = px.bar(data, x=data["match_winner"],
            title="Number of Matches Won in IPL 2022")
figure.show()
figure = px.bar(data, x = data["player_of_the_match"], 
                title="Most Player of the Match Awards")
figure.show()
figure = px.bar(data, x = data["best_bowling"], 
                title="Best Bowling Figures")
figure.show()
venue = data["venue"].value_counts()
label = venue.index
counts = venue.values
colors = ['skyblue','yellow']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches at each Stadium')
fig.update_traces(hoverinfo='label+percent', 
                  textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=2)))
fig.show()    