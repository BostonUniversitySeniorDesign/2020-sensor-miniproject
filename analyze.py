#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""

from pathlib import Path
import argparse
import pandas
import matplotlib.pyplot as plt

from sp_iotsim.fileio import load_data


def plot_time(time: pandas.Series):
    """
    NOTE: in this simulation, time interval is same distribution for all sensors and rooms

    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.fit.html
    """

    ax = plt.figure().gca()
    ax.hist(time.diff().dt.total_seconds(), bins=100)
    ax.set_xlabel("Time (seconds)")
    ax.set_title("Time interval")
    ax.set_ylabel("# of occurences")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    plot_time(data["temperature"].index.to_series())

    # for k in data:
    #     data[k].hist()
    #     plt.figure()

    plt.show()
