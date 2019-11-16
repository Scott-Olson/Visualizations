import plotly.graph_objects as go
import pandas as pd
import math


df = pd.read_csv('prime_gap.csv')


# order_test = []
# for item in df['order']:
#     order_test.append(int(item)/math.pi)

fig = go.Figure(
    go.Scatterpolar(
        r = df['order'],
        theta = df["gap"],
        thetaunit = "radians",
        mode = 'markers',
    ))

fig.update_layout(showlegend=False)



# fig = go.Figure()
# fig.add_trace(go.Scatterpolar(
#         r = order_test,
#         theta = df['gap'],
#         thetaunit = 'radians',
#         mode = 'lines',
#         line_color = 'blue',
#     ))

fig.show()