import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["claps"].tolist()

claps_mean = statistics.mean(data)
claps_stdev = statistics.stdev(data)

print(claps_mean)
print(claps_stdev)

def rand_set_of_means(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)

    samp_mean = statistics.mean(dataset)
    return(samp_mean)



def main():
    mean_list = []
    for i in range(0,1000):
        set_of_means = rand_set_of_means(30)
        mean_list.append(set_of_means)
    
    mean_sample = statistics.mean(mean_list)
    stdev_sample = statistics.stdev(mean_list)

    print(mean_sample)
    print(stdev_sample)

    fig = ff.create_distplot([mean_list], ["claps"], show_hist=False)
    fig.add_trace(go.Scatter(x=[claps_mean, claps_mean], y=[0,0.1], mode="lines", name="Mean"))
    fig.show()

main()

