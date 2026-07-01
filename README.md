# LIS705: Introductory Analytics for Decision Making

A university course covering the practical data-analytics toolkit: pandas, Seaborn,
data cleaning, aggregation, time series, and one applied regression/statistics unit.
All notebooks, extracted charts, and rendered PDFs in this repo are my own coursework.

## My take on this course

This is a **data-wrangling-and-visualization literacy course**, not a
data-science course in the ML sense -- and that's the right scope for its name
("Analytics for **Decision Making**"). Ten units run almost entirely on pandas
mechanics (ingestion from five file formats, cleaning, reshaping, groupby/pivot,
time-series resampling) and Seaborn storytelling; only one linear regression
exercise and one t-test touch inferential/predictive statistics, and there's no
train/test split, cross-validation, or classification anywhere in the material.
The capstone project is framed as "what's the trend, what chart shows it, what
new column do you derive" -- classic BI-analyst framing, not model-building. It's
a strong foundation for feeding decisions with clean, well-visualized data; a
student wanting to claim "data science" skills from this course alone would still
need a real ML/stats sequence layered on top.

## Course index

| Unit | Topics | Notebook / PDF |
|---|---|---|
| Stats Unit | t-test and normality check on mortality data | [stats.ipynb](stats-unit/stats.ipynb)<br>[stats.pdf](stats-unit/stats.pdf) |
| Unit 1 — JupyterLab Basics | JupyterLab basics; import and clean FiveThirtyEight-style polling data | [ex_1-1_polling.ipynb](unit-01-jupyterlab-basics/ex_1-1_polling.ipynb)<br>[ex_1-1_practice.ipynb](unit-01-jupyterlab-basics/ex_1-1_practice.ipynb)<br>[ex_1-1_polling.pdf](unit-01-jupyterlab-basics/ex_1-1_polling.pdf)<br>[ex_1-1_practice.pdf](unit-01-jupyterlab-basics/ex_1-1_practice.pdf) |
| Unit 2 — Core Pandas | Load/save/inspect a mortality dataset, wide vs long shape | [ex_2-1_mortality.ipynb](unit-02-mortality-pandas/ex_2-1_mortality.ipynb)<br>[ex_2-2_mortality.ipynb](unit-02-mortality-pandas/ex_2-2_mortality.ipynb)<br>[ex_2-1_mortality.pdf](unit-02-mortality-pandas/ex_2-1_mortality.pdf)<br>[ex_2-2_mortality.pdf](unit-02-mortality-pandas/ex_2-2_mortality.pdf) |
| Unit 3 — Visualization | First plots on the mortality dataset | [ex_3-1_mortality.ipynb](unit-03-visualization/ex_3-1_mortality.ipynb)<br>[ex_3-1_mortality.pdf](unit-03-visualization/ex_3-1_mortality.pdf) |
| Unit 4 — Seaborn Essentials | Relational, categorical, and distribution plots | [ex_4-1_mortality_Harsh_Mehta.ipynb](unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta.ipynb)<br>[ex_4-1_mortality_Harsh_Mehta.pdf](unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta.pdf) |
| Unit 5 — Data Sources | Reading data from CSV, Excel, a SQL database, Stata, and JSON | [ex_5-1_Harsh_Mehta.ipynb](unit-05-data-sources/ex_5-1_Harsh_Mehta.ipynb)<br>[ex_5-2_Harsh_Mehta.ipynb](unit-05-data-sources/ex_5-2_Harsh_Mehta.ipynb)<br>[ex_5-3_Harsh_Mehta.ipynb](unit-05-data-sources/ex_5-3_Harsh_Mehta.ipynb)<br>[ex_5-4_Harsh_Mehta.ipynb](unit-05-data-sources/ex_5-4_Harsh_Mehta.ipynb)<br>[ex_5-5_Harsh_Mehta.ipynb](unit-05-data-sources/ex_5-5_Harsh_Mehta.ipynb)<br>[ex_5-1_Harsh_Mehta.pdf](unit-05-data-sources/ex_5-1_Harsh_Mehta.pdf)<br>[ex_5-2_Harsh_Mehta.pdf](unit-05-data-sources/ex_5-2_Harsh_Mehta.pdf)<br>[ex_5-3_Harsh_Mehta.pdf](unit-05-data-sources/ex_5-3_Harsh_Mehta.pdf)<br>[ex_5-4_Harsh_Mehta.pdf](unit-05-data-sources/ex_5-4_Harsh_Mehta.pdf)<br>[ex_5-5_Harsh_Mehta.pdf](unit-05-data-sources/ex_5-5_Harsh_Mehta.pdf) |
| Unit 6 — Data Cleaning | Cleaning polling and car listing data | [ex_6-1_polls_HarshMehta.ipynb](unit-06-data-cleaning/ex_6-1_polls_HarshMehta.ipynb)<br>[ex_6-2_cars_HarshMehta.ipynb](unit-06-data-cleaning/ex_6-2_cars_HarshMehta.ipynb)<br>[ex_6-1_polls_HarshMehta.pdf](unit-06-data-cleaning/ex_6-1_polls_HarshMehta.pdf)<br>[ex_6-2_cars_HarshMehta.pdf](unit-06-data-cleaning/ex_6-2_cars_HarshMehta.pdf) |
| Unit 7 — Data Wrangling | Indexes, combining datasets, forest fire and car data | [ex_7-1_fires_HarshMehta.ipynb](unit-07-data-wrangling/ex_7-1_fires_HarshMehta.ipynb)<br>[ex_7-2_cars_HarshMehta.ipynb](unit-07-data-wrangling/ex_7-2_cars_HarshMehta.ipynb)<br>[ex_7-1_fires_HarshMehta.pdf](unit-07-data-wrangling/ex_7-1_fires_HarshMehta.pdf)<br>[ex_7-2_cars_HarshMehta.pdf](unit-07-data-wrangling/ex_7-2_cars_HarshMehta.pdf) |
| Unit 8 — Aggregation | groupby, pivot tables, binning, melting, ranking, quantiles | [ex_8-1_fires_HarshMehta.ipynb](unit-08-aggregation/ex_8-1_fires_HarshMehta.ipynb)<br>[ex_8-2_cars_HarshMehta.ipynb](unit-08-aggregation/ex_8-2_cars_HarshMehta.ipynb)<br>[ex_8-1_fires_HarshMehta.pdf](unit-08-aggregation/ex_8-1_fires_HarshMehta.pdf)<br>[ex_8-2_cars_HarshMehta.pdf](unit-08-aggregation/ex_8-2_cars_HarshMehta.pdf) |
| Unit 9 — Time Series Basics | Date ranges, reindexing, resampling, rolling windows | [ex_9-1_stocks.ipynb](unit-09-time-series-basics/ex_9-1_stocks.ipynb)<br>[ex_9-1_stocks.pdf](unit-09-time-series-basics/ex_9-1_stocks.pdf) |
| Unit 10 — Regression | Linear regression and correlation on fish measurement data | [ex_10-1_fish.ipynb](unit-10-regression/ex_10-1_fish.ipynb)<br>[ex_10-1_fish.pdf](unit-10-regression/ex_10-1_fish.pdf) |
| Time Series Project | Capstone time-series analysis project | [LIS705_Time_Series_Project.ipynb](time-series-project/LIS705_Time_Series_Project.ipynb)<br>[LIS705_Time_Series_Project.pdf](time-series-project/LIS705_Time_Series_Project.pdf) |
| Project Assignment 4 | Applied BI project — trend analysis and decision-support write-up | [LIS705_ProjectAssignment4.pdf](project-assignment-4/LIS705_ProjectAssignment4.pdf) |

See [`docs/roadmap.md`](docs/roadmap.md) for how this repo was rolled out.

## Visualization gallery

Every chart produced across the course (73 total), grouped by unit.
Click a unit to expand.

<details>
<summary><strong>Stats Unit</strong> (1 charts)</summary>

![stats__fig-01](assets/images/stats-unit/stats__fig-01.png)

</details>


<details>
<summary><strong>Unit 1 — JupyterLab Basics</strong> (2 charts)</summary>

![ex_1-1_polling__fig-01](assets/images/unit-01-jupyterlab-basics/ex_1-1_polling__fig-01.png)
![ex_1-1_polling__fig-02](assets/images/unit-01-jupyterlab-basics/ex_1-1_polling__fig-02.png)

</details>


<details>
<summary><strong>Unit 2 — Core Pandas</strong> (3 charts)</summary>

![ex_2-1_mortality__fig-01](assets/images/unit-02-mortality-pandas/ex_2-1_mortality__fig-01.png)
![ex_2-1_mortality__fig-02](assets/images/unit-02-mortality-pandas/ex_2-1_mortality__fig-02.png)
![ex_2-2_mortality__fig-01](assets/images/unit-02-mortality-pandas/ex_2-2_mortality__fig-01.png)

</details>


<details>
<summary><strong>Unit 3 — Visualization</strong> (10 charts)</summary>

![ex_3-1_mortality__fig-01](assets/images/unit-03-visualization/ex_3-1_mortality__fig-01.png)
![ex_3-1_mortality__fig-02](assets/images/unit-03-visualization/ex_3-1_mortality__fig-02.png)
![ex_3-1_mortality__fig-03](assets/images/unit-03-visualization/ex_3-1_mortality__fig-03.png)
![ex_3-1_mortality__fig-04](assets/images/unit-03-visualization/ex_3-1_mortality__fig-04.png)
![ex_3-1_mortality__fig-05](assets/images/unit-03-visualization/ex_3-1_mortality__fig-05.png)
![ex_3-1_mortality__fig-06](assets/images/unit-03-visualization/ex_3-1_mortality__fig-06.png)
![ex_3-1_mortality__fig-07](assets/images/unit-03-visualization/ex_3-1_mortality__fig-07.png)
![ex_3-1_mortality__fig-08](assets/images/unit-03-visualization/ex_3-1_mortality__fig-08.png)
![ex_3-1_mortality__fig-09](assets/images/unit-03-visualization/ex_3-1_mortality__fig-09.png)
![ex_3-1_mortality__fig-10](assets/images/unit-03-visualization/ex_3-1_mortality__fig-10.png)

</details>


<details>
<summary><strong>Unit 4 — Seaborn Essentials</strong> (39 charts)</summary>

![Ex_4-1_Barcharts__manual-01](assets/images/unit-04-seaborn-essentials/Ex_4-1_Barcharts__manual-01.png)
![Ex_4-1_Barcharts__manual-02](assets/images/unit-04-seaborn-essentials/Ex_4-1_Barcharts__manual-02.png)
![ex_4-1_mortality_Harsh_Mehta__fig-01](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-01.png)
![ex_4-1_mortality_Harsh_Mehta__fig-02](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-02.png)
![ex_4-1_mortality_Harsh_Mehta__fig-03](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-03.png)
![ex_4-1_mortality_Harsh_Mehta__fig-04](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-04.png)
![ex_4-1_mortality_Harsh_Mehta__fig-05](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-05.png)
![ex_4-1_mortality_Harsh_Mehta__fig-06](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-06.png)
![ex_4-1_mortality_Harsh_Mehta__fig-07](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-07.png)
![ex_4-1_mortality_Harsh_Mehta__fig-08](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-08.png)
![ex_4-1_mortality_Harsh_Mehta__fig-09](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-09.png)
![ex_4-1_mortality_Harsh_Mehta__fig-10](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-10.png)
![ex_4-1_mortality_Harsh_Mehta__fig-11](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-11.png)
![ex_4-1_mortality_Harsh_Mehta__fig-12](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-12.png)
![ex_4-1_mortality_Harsh_Mehta__fig-13](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-13.png)
![ex_4-1_mortality_Harsh_Mehta__fig-14](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-14.png)
![ex_4-1_mortality_Harsh_Mehta__fig-15](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-15.png)
![ex_4-1_mortality_Harsh_Mehta__fig-16](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-16.png)
![ex_4-1_mortality_Harsh_Mehta__fig-17](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-17.png)
![ex_4-1_mortality_Harsh_Mehta__fig-18](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-18.png)
![ex_4-1_mortality_Harsh_Mehta__fig-19](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-19.png)
![ex_4-1_mortality_Harsh_Mehta__fig-20](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-20.png)
![ex_4-1_mortality_Harsh_Mehta__fig-21](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-21.png)
![ex_4-1_mortality_Harsh_Mehta__fig-22](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-22.png)
![ex_4-1_mortality_Harsh_Mehta__fig-23](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-23.png)
![ex_4-1_mortality_Harsh_Mehta__fig-24](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-24.png)
![ex_4-1_mortality_Harsh_Mehta__fig-25](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-25.png)
![ex_4-1_mortality_Harsh_Mehta__fig-26](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-26.png)
![ex_4-1_mortality_Harsh_Mehta__fig-27](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-27.png)
![ex_4-1_mortality_Harsh_Mehta__fig-28](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-28.png)
![ex_4-1_mortality_Harsh_Mehta__fig-29](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-29.png)
![ex_4-1_mortality_Harsh_Mehta__fig-30](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-30.png)
![ex_4-1_mortality_Harsh_Mehta__fig-31](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-31.png)
![ex_4-1_mortality_Harsh_Mehta__fig-32](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-32.png)
![ex_4-1_mortality_Harsh_Mehta__fig-33](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-33.png)
![ex_4-1_mortality_Harsh_Mehta__fig-34](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-34.png)
![ex_4-1_mortality_Harsh_Mehta__fig-35](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-35.png)
![ex_4-1_mortality_Harsh_Mehta__fig-36](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-36.png)
![ex_4-1_mortality_Harsh_Mehta__fig-37](assets/images/unit-04-seaborn-essentials/ex_4-1_mortality_Harsh_Mehta__fig-37.png)

</details>








<details>
<summary><strong>Unit 8 — Aggregation</strong> (2 charts)</summary>

![ex_8-2_cars_HarshMehta__fig-01](assets/images/unit-08-aggregation/ex_8-2_cars_HarshMehta__fig-01.png)
![ex_8-2_cars_HarshMehta__fig-02](assets/images/unit-08-aggregation/ex_8-2_cars_HarshMehta__fig-02.png)

</details>


<details>
<summary><strong>Unit 9 — Time Series Basics</strong> (3 charts)</summary>

![ex_9-1_stocks__fig-01](assets/images/unit-09-time-series-basics/ex_9-1_stocks__fig-01.png)
![ex_9-1_stocks__fig-02](assets/images/unit-09-time-series-basics/ex_9-1_stocks__fig-02.png)
![ex_9-1_stocks__fig-03](assets/images/unit-09-time-series-basics/ex_9-1_stocks__fig-03.png)

</details>


<details>
<summary><strong>Unit 10 — Regression</strong> (8 charts)</summary>

![ex_10-1_fish__fig-01](assets/images/unit-10-regression/ex_10-1_fish__fig-01.png)
![ex_10-1_fish__fig-02](assets/images/unit-10-regression/ex_10-1_fish__fig-02.png)
![ex_10-1_fish__fig-03](assets/images/unit-10-regression/ex_10-1_fish__fig-03.png)
![ex_10-1_fish__fig-04](assets/images/unit-10-regression/ex_10-1_fish__fig-04.png)
![ex_10-1_fish__fig-05](assets/images/unit-10-regression/ex_10-1_fish__fig-05.png)
![ex_10-1_fish__fig-06](assets/images/unit-10-regression/ex_10-1_fish__fig-06.png)
![ex_10-1_fish__fig-07](assets/images/unit-10-regression/ex_10-1_fish__fig-07.png)
![ex_10-1_fish__fig-08](assets/images/unit-10-regression/ex_10-1_fish__fig-08.png)

</details>


<details>
<summary><strong>Time Series Project</strong> (5 charts)</summary>

![LIS705_Time_Series_Project__fig-01](assets/images/time-series-project/LIS705_Time_Series_Project__fig-01.png)
![LIS705_Time_Series_Project__fig-02](assets/images/time-series-project/LIS705_Time_Series_Project__fig-02.png)
![LIS705_Time_Series_Project__fig-03](assets/images/time-series-project/LIS705_Time_Series_Project__fig-03.png)
![LIS705_Time_Series_Project__fig-04](assets/images/time-series-project/LIS705_Time_Series_Project__fig-04.png)
![LIS705_Time_Series_Project__fig-05](assets/images/time-series-project/LIS705_Time_Series_Project__fig-05.png)

</details>



