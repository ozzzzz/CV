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
    return HBarItem, draw_hbars


@app.cell
def _(HBarItem, draw_hbars, np, pd, plt):
    def define_techstack() -> dict[str, list[HBarItem]]:
        return {
            "backend": [
                HBarItem(name="QT", periods = [(np.datetime64("2015"), np.datetime64("2016"))], color="#abdda4"),
                HBarItem(name="Scala", periods = [(np.datetime64("2016"), np.datetime64("2017"))], color="#d53e4f"),
                HBarItem(name="Haskell", periods = [(np.datetime64("2017"), np.datetime64("2021-08"))], color="#5e4fa2"),
                HBarItem(name="Java", periods = [(np.datetime64("2021-08"), np.datetime64("2022-06"))], color="#3288bd"),
                HBarItem(name="PHP", periods = [(np.datetime64("2022"), np.datetime64("2023-06"))], color="#9e0142"),
                HBarItem(name="Python", periods = [(np.datetime64("2014"), np.datetime64("2015")), (np.datetime64("2018"), np.datetime64("2025"))], color="#fee08b"),
            ],
            "frontend": [
                HBarItem(name="JavaScript", periods = [(np.datetime64("2013"), np.datetime64("2015")), (np.datetime64("2022"), np.datetime64("2023"))], color="#e6f598"),
                HBarItem(name="NextJS", periods = [(np.datetime64("2019"), np.datetime64("2021-08"))], color="#abdda4"),
                HBarItem(name="React", periods = [(np.datetime64("2019"), np.datetime64("2025"))], color="#3288bd"),
            ],
            "devops": [
                HBarItem(name="Github", periods = [(np.datetime64("2016"), np.datetime64("2025"))], color="#555"),
                HBarItem(name="Gitlab + Actions", periods = [(np.datetime64("2021-08"), np.datetime64("2022-08")), (np.datetime64("2024-05"), np.datetime64("2025"))], color="#f46d43"),
                HBarItem(name="Kubernetes", periods = [(np.datetime64("2022-06"), np.datetime64("2024-05"))], color="#5e4fa2"),
                HBarItem(name="Docker", periods = [(np.datetime64("2016"), np.datetime64("2025"))], color="#3288bd"),
                HBarItem(name="Prometheus + Grafana", periods = [(np.datetime64("2018"), np.datetime64("2025"))], color="#66c2a5"),
            ],
            "other": [
                HBarItem(name="Neo4j", periods = [(np.datetime64("2017"), np.datetime64("2020"))], color="#e6f598"),
                HBarItem(name="MongoDB", periods = [(np.datetime64("2016"), np.datetime64("2021-08"))], color="#abdda4"),
                HBarItem(name="PostgreSQL", periods = [(np.datetime64("2021-08"), np.datetime64("2024-05"))], color="#5e4fa2"),
                HBarItem(name="Keycloak", periods = [(np.datetime64("2020"), np.datetime64("2021-08")), (np.datetime64("2022-08"), np.datetime64("2024-05"))], color="#66c2a5"),
                HBarItem(name="RabbitMQ", periods = [(np.datetime64("2020"), np.datetime64("2021-08"))], color="#3288bd"),
                HBarItem(name="Kafka", periods = [(np.datetime64("2022-08"), np.datetime64("2024-05"))], color="#555"),
            ]
        }

    def draw_tech_stack() -> pd.DataFrame:
        with plt.xkcd():
            data = define_techstack()
            
            fig, (ax_back, ax_front, ax_devops, ax_other) = plt.subplots(nrows=4, figsize=(18, 24))

            x_min = np.datetime64('2013-01-01')
            
            draw_hbars(axis=ax_back, title="BACKEND TECH STACK", items=data["backend"], x_min=x_min)
            ax_back.annotate(
                "INTERESTING EXPERIENCE: TYPE THEORY & MONADS",
                xy=(np.datetime64("2018"), 2),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.56, 0.79),
            )
            ax_back.annotate(
                "SIDE PROJECT, NOT\n SO INTERESTING EXPERIENCE",
                xy=(np.datetime64("2023"), 4),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.78, 0.82),
            )
            
            
            draw_hbars(axis=ax_front, title="FRONTEND TECH STACK", items=data["frontend"], x_min=x_min)
            ax_front.annotate(
                "DIDN'T HAVE A FREE FRONTEND,\n SO I STARTED TO BUILD\n A UI FOR OUR SERVICE",
                xy=(np.datetime64("2019"), 2),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.3, 0.62),
            )
            draw_hbars(axis=ax_devops, title="DEVOPS TECH STACK", items=data["devops"], x_min=x_min)
            draw_hbars(axis=ax_other, title="DATABASES, BROKERS AND OTHER", items=data["other"], x_min=x_min)
            
            plt.show()
            
    draw_tech_stack()
    return define_techstack, draw_tech_stack


@app.cell
def _(HBarItem, draw_hbars, np, pd, plt):
    def define_areas() -> list[HBarItem]:
        return [
            HBarItem(
                name="Master degree in Math",
                periods=[(np.datetime64("2010-09"), np.datetime64("2015-06")), (np.datetime64("2016-11"), np.datetime64("2017"))],
                color="#5e4fa2",
            ),
            HBarItem(
                name="Avionics",
                periods=[(np.datetime64("2015-01"), np.datetime64("2015-06"))],
                color="#abdda4",
            ),
            HBarItem(
                name="General Software Development",
                periods=[
                    (np.datetime64("2013-12"), np.datetime64("2015-01")),
                    (np.datetime64("2015-06"), np.datetime64("2016-05")),
                    (np.datetime64("2022-08"), np.datetime64("2024-05")),
                ],
                color="#3288bd",
            ),
            HBarItem(
                name="Molecular biology",
                periods=[
                    (np.datetime64("2016-05"), np.datetime64("2021-09")),
                ],
                color="#66c2a5",
            ),
            HBarItem(
                name="Simulaiton and optimization",
                periods=[
                    (np.datetime64("2021-09"), np.datetime64("2022-08")),
                ],
                color="#e6f598",
            ),
            HBarItem(
                name="Construction",
                periods=[
                    (np.datetime64("2024-05"), np.datetime64("2025")),
                ],
                color="#fee08b",
            ),
        ]


    def draw_areas() -> pd.DataFrame:
        with plt.xkcd():
            data = define_areas()

            fig, (ax) = plt.subplots(
                nrows=1, figsize=(18, 6)
            )

            x_min = np.datetime64("2010-09")
            draw_hbars(
                axis=ax,
                title="AREAS AND SCIENCE",
                items=data,
                x_min=x_min,
            )

            ax.annotate(
                "MATH ARTICLE BASED ON\nMY MASTER THESIS",
                xy=(np.datetime64("2017"), 0),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.57, 0.15),
            )
            ax.annotate(
                "ARTICLE ABOUT 3D MOLECULES\nAND FORCE FIELDS",
                xy=(np.datetime64("2018"), 3),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.4, 0.7),
            )
            ax.annotate(
                "COVID-19 STARTED, JOINED\nA TEAM TO DEVELOP A VACCINE",
                xy=(np.datetime64("2020"), 3),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.6, 0.3),
            )
            ax.annotate(
                "PATENT WO-2023287324-A1\nABOUT VACCINE",
                xy=(np.datetime64("2021"), 3),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.65, 0.7),
            )
            ax.annotate(
                "ARTICLE ABOUT VACCINE :)",
                xy=(np.datetime64("2022"), 3),
                textcoords="subfigure fraction",
                arrowprops=dict(arrowstyle="->"),
                xytext=(0.81, 0.5),
            )

            plt.show()


    draw_areas()
    return define_areas, draw_areas


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
