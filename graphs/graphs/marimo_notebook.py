import marimo

__generated_with = "0.10.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
    import pandas as pd
    return mdates, np, pd, plt


@app.cell
def _(pd):
    def define_num_of_subordinates() -> pd.DataFrame:
        data = [
            (2013, 0),
            (2014, 0),
            (2015, 0),
            (2016, 0),
            (2017, 3),
            (2018, 6),
            (2019, 12),
            (2020, 15),
            (2021, 25),
            (2022, 0),
            (2023, 0),
            (2024, 0),
        ]
        df = pd.DataFrame(data, columns=['year', 'subordinates'])
        df['year_typed'] = pd.to_datetime(df['year'], format='%Y')
        df.set_index('year', inplace=True)
        return df
    return (define_num_of_subordinates,)


@app.cell
def _(define_num_of_subordinates):
    define_num_of_subordinates().loc[2021]['subordinates']
    return


@app.cell
def _(define_num_of_subordinates, mdates, plt):
    with plt.xkcd():
        df = define_num_of_subordinates()
        annotation_point_x = define_num_of_subordinates().loc[2021]['year_typed']
        annotation_point_y = define_num_of_subordinates().loc[2021]['subordinates']
        
        x = df["year_typed"]
        y = df["subordinates"]
        fig, ax = plt.subplots(figsize=(18, 6))
        ax.set_title("NUMBER OF SUBORDINATES")
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.annotate(
            "THE MOMENT I DECIDED THAT\n WORKING WITH MY OWN HANDS\n BRINGS ME MORE SATISFACTION\nTHAN MANAGING PEOPLE",
            xy=(annotation_point_x, annotation_point_y),
            # xycoords="figure fraction",
            textcoords="figure fraction",
            arrowprops=dict(arrowstyle="->"),
            xytext=(0.63, 0.6),
        )
        ax.plot(x, y)
        plt.show()
    return annotation_point_x, annotation_point_y, ax, df, fig, x, y


@app.cell
def _(np, plt):
    def example():


        with plt.xkcd(randomness=2):
            # Based on "Stove Ownership" from XKCD by Randall Munroe
            # https://xkcd.com/418/

            fig = plt.figure()
            ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
            ax.spines[['top', 'right']].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_ylim([-30, 10])

            data = np.ones(100)
            data[70:] -= np.arange(30)

            ax.annotate(
                'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
                xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

            ax.plot(data)

            ax.set_xlabel('time')
            ax.set_ylabel('my overall health')
            fig.text(
                0.5, 0.05,
                '"Stove Ownership" from xkcd by Randall Munroe',
                ha='center')
        plt.show()
    return (example,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
