import marimo

__generated_with = "0.10.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
    import pandas as pd
    import pydantic
    from datetime import date, timedelta
    return date, mdates, np, pd, plt, pydantic, timedelta


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
def _(define_num_of_subordinates, mdates, plt):
    def draw_num_of_subordinates():
        with plt.xkcd():
            df = define_num_of_subordinates()

            x = df["year_typed"]
            y = df["subordinates"]
            fig, ax = plt.subplots(figsize=(18, 6))
            ax.set_title("NUMBER OF SUBORDINATES")
            ax.xaxis.set_major_locator(mdates.YearLocator())
            ax.plot(x, y)

            annotation_point_0_x = x.loc[2017]
            annotation_point_0_y = y.loc[2017]
            ax.annotate(
                "STARTED COORDINATING THE WORK\n OF TALENTED STUDENTS,\n OUR FUTURE EMPLOYEES",
                xy=(annotation_point_0_x, annotation_point_0_y),
                textcoords="figure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.13, 0.4),
            )

            annotation_point_1_x = x.loc[2021]
            annotation_point_1_y = y.loc[2021]
            ax.annotate(
                "THE MOMENT I DECIDED THAT\n WORKING WITH MY OWN HANDS\n BRINGS ME MORE SATISFACTION\nTHAN MANAGING PEOPLE",
                xy=(annotation_point_1_x, annotation_point_1_y),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.76, 0.6),
            )

            plt.show()

    draw_num_of_subordinates()
    return (draw_num_of_subordinates,)


@app.cell
def _(mdates, np, pydantic):
    class HBarItem(pydantic.BaseModel):
        name: str
        periods: list[tuple[np.datetime64, np.datetime64]]
        color: str

        model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)

    def draw_hbars(axis, title: str, items: list[HBarItem], x_min: np.datetime64, x_max: np.datetime64 = np.datetime64('now')):
        axis.set_title(title)
        axis.set_xlim(x_min, x_max)
        axis.xaxis.set_major_locator(mdates.YearLocator())
        axis.set_ylim(-1, len(items) + 1)
        axis.set_yticks(list(range(len(items))))
        axis.set_yticklabels([item.name for item in items])

        bar_height = 0.5
        for index, item in enumerate(items):
            typed_periods = []
            for start, end in item.periods:
                typed_start = np.datetime64(str(start))
                typed_delta = np.datetime64(str(end)) - typed_start
                typed_periods.append((typed_start, typed_delta))
            axis.broken_barh(typed_periods, (index - bar_height / 2, bar_height), facecolors =(item.color))

    def define_techstack() -> dict[str, list[HBarItem]]:
        return {
            "backend": [
                HBarItem(name="QT", periods = [(np.datetime64("2015"), np.datetime64("2016"))], color="#16C47F"),
                HBarItem(name="Scala", periods = [(np.datetime64("2016"), np.datetime64("2017"))], color="#F93827"),
                HBarItem(name="Haskell", periods = [(np.datetime64("2017"), np.datetime64("2021-08"))], color="#441752"),
                HBarItem(name="Java", periods = [(np.datetime64("2021-08"), np.datetime64("2022-06"))], color="#2E5077"),
                HBarItem(name="PHP", periods = [(np.datetime64("2022"), np.datetime64("2023-06"))], color="#A294F9"),
                HBarItem(name="Python", periods = [(np.datetime64("2014"), np.datetime64("2015")), (np.datetime64("2018"), np.datetime64("2025"))], color="#FFD65A"),
            ],
            "frontend": [
                HBarItem(name="JavaScript", periods = [(np.datetime64("2013"), np.datetime64("2015")), (np.datetime64("2022"), np.datetime64("2023"))], color="#FFD65A"),
                HBarItem(name="NextJS", periods = [(np.datetime64("2019"), np.datetime64("2021-08"))], color="#999999"),
                HBarItem(name="React", periods = [(np.datetime64("2019"), np.datetime64("2025"))], color="#A5BFCC"),
            ],
            "devops": [
                HBarItem(name="Github", periods = [(np.datetime64("2016"), np.datetime64("2025"))], color="#333"),
                HBarItem(name="Gitlab + Actions", periods = [(np.datetime64("2021-08"), np.datetime64("2022-08")), (np.datetime64("2024-05"), np.datetime64("2025"))], color="#E16A54"),
                HBarItem(name="Kubernetes", periods = [(np.datetime64("2022-06"), np.datetime64("2024-05"))], color="#001A6E"),
                HBarItem(name="Docker", periods = [(np.datetime64("2016"), np.datetime64("2025"))], color="#074799"),
            ],
            "other": [
                HBarItem(name="Neo4j", periods = [(np.datetime64("2017"), np.datetime64("2020"))], color="#074799"),
                HBarItem(name="MongoDB", periods = [(np.datetime64("2016"), np.datetime64("2021-08"))], color="#5DB996"),
                HBarItem(name="PostgreSQL", periods = [(np.datetime64("2021-08"), np.datetime64("2024-05"))], color="#074799"),
                HBarItem(name="Keycloak", periods = [(np.datetime64("2020"), np.datetime64("2021-08")), (np.datetime64("2022-08"), np.datetime64("2024-05"))], color="#777777"),
                HBarItem(name="RabbitMQ", periods = [(np.datetime64("2020"), np.datetime64("2021-08"))], color="#074799"),
                HBarItem(name="Kafka", periods = [(np.datetime64("2022-08"), np.datetime64("2024-05"))], color="#333"),
            ]
        }
    return HBarItem, define_techstack, draw_hbars


@app.cell
def _(define_techstack, draw_hbars, np, pd, plt):
    def draw_tech_stack() -> pd.DataFrame:
        with plt.xkcd():
            data = define_techstack()
            
            fig, (ax_back, ax_front, ax_devops, ax_other) = plt.subplots(nrows=4, figsize=(18, 24))

            x_min = np.datetime64('2013-01-01')
            draw_hbars(axis=ax_back, title="BACKEND TECH STACK", items=data["backend"], x_min=x_min)
            draw_hbars(axis=ax_front, title="FRONTEND TECH STACK", items=data["frontend"], x_min=x_min)
            draw_hbars(axis=ax_devops, title="DEVOPS TECH STACK", items=data["devops"], x_min=x_min)
            draw_hbars(axis=ax_other, title="DATABASES, BROKERS AND OTHER", items=data["other"], x_min=x_min)
            
            plt.show()
            
    draw_tech_stack()
    return (draw_tech_stack,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
