import seaborn as sns
from util import check_file_exist, get_dataframe
import matplotlib.pyplot as plt

def main(file_name):
    if check_file_exist(file_name=file_name):
        df = get_dataframe(file_name=file_name)
        with sns.plotting_context("poster"):
            fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(40, 25))
            sns.set(font_scale=3)
            sns.set_style("whitegrid")
            sns.despine(fig=fig, ax=axes, top=True, right=True, offset=0)
            df = df [0:200]
            barplot = sns.barplot(y='Packets', hue='Type', x='Time',
                        data=df,
                        palette=sns.color_palette('bright'), ax=axes)
            # axes.bar_label(barplot.containers[0])
            # Plots the no of interest packet got hit/misses in the time interval
            # we can compare both at same time using hue
            # Use: We can see how many hit's are generated per interest miss  
            # If hit >= miss , then we can say our cache strategy is best
            axes.set_title(label="CS Hit/Miss vs Time", fontsize=50)
            axes.set_xlabel(xlabel="Time", fontsize=30)
            axes.set_ylabel(ylabel="Packet count", fontsize=30)
            fig.savefig('./content_store-hit-miss-hue.png')

if __name__ == "__main__":
    file_name = "./../scratch/cs-tracer.log"
    main(file_name=file_name)
    # join_interval(file_name=file_name)
