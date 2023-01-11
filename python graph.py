import plotly.graph_objects as go
import pandas as pd
import numpy as np

import plotly.io as pio
pio.templates.default = "simple_white"
data = pd.read_csv('graph.csv')



x_axis=list(range(data.shape[0]))
y_axis= list(data.iloc[0:,0])

x_axis
frames = []
for frame in range(1,365,10):
    x_axis_frame = np.arange(frame)
    y_axis_frame = list(data.iloc[1:frame,0])
    curr_frame = go.Frame(data = [go.Scatter(x = x_axis_frame,y=y_axis_frame,mode = "lines")])
    frames.append(curr_frame)
len(frames)   
figure = go.Figure(
    data = [go.Scatter(x = np.array([1]), y=np.array([1.01]),mode="lines")],
    layout = {"title":"A Simple Line Chart",
    "updatemenus":[{"type":"buttons",
                            "buttons":[{
                                "label":"Play",
                                "method":"animate",
                                "args":[None]}]}],
                                "xaxis":{"title":"Day","range":[0,data.shape[0]]},
                                "yaxis":{"title":"Afghanistan GDP","range":[0,50]}
                            },
                            frames=frames)

figure.show()
