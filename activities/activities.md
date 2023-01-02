# Creating charts with Plotly Express and adding them to a Dash app

The following activities are expected to take 2 hours to complete.

## Introduction to Plotly Express

[Plotly Express](https://plotly.com/python/plotly-express/) is a high level API for creating charts using Python. By
high level, we mean that much of the complexity of the code required to create a chart is hidden from you and provided by the API, allowing you to create charts with less code.

Plotly express is a module in the plotly Python package, though it used to be a separate package. Install [plotly Python version](https://plotly.com/python/getting-started/) using `pip install plotly`.

The [online documentation](https://plotly.com/python/plotly-express/#highlevel-features) gives lots of examples of how to create different chart types. You will need to make use of this.

The [Plotly community forum](https://community.plotly.com/) has posts you can search; and you can post your own questions.

The current version of Plotly.py at the time of writing this is 5.11. Some examples you may find online are from much earlier versions and the code is likely to need to be adapted to work with the current version.

### Create a chart using Plotly Express

In this activity you will create a line chart to answer the question 'How has the number of sports in the summer and winter paralympics changed over time?'.

Assume that the target audience is university students interested in major sporting events. Assume they have limited knowledge of the paralympics however they make extensive use of a range of technologies and are capable of understanding more complex data and charts. The activity doesn't explicitly design for this audience but you may wish to try to do so.

The data is in the events.csv. The columns you will need are: ['REF', 'TYPE', 'YEAR', 'LOCATION', 'EVENTS', 'SPORTS', 'COUNTRIES', 'MALE', 'FEMALE', 'PARTICIPANTS']

First, check you can run the paralympics_app code. In the VS Code terminal: `python paralympics_app/paralympics.py`

#### Create a basic line chart
The steps are:
1. Use pandas to read the data into a dataframe
2. Create a line chart using the Plotly Express line chart function and the data
3. Add the chart to the Dash app using the dash core components Graph function

You can either add all the code to paralympics.py, or you may prefer to add the code to create the charts to a separate python file, e.g. called `create_charts.py`. The text below suggests the latter.




#### Styling the chart


## Further practice

Re-create lollapoolza charts using the [activities/covid_dashboard.md](activities.md)

Create your own covid dashboard app (see [activities/covid.md](covid.md)).

Explore the [Plotly Express documentation](https://plotly.com/python/plotly-express/#highlevel-features) and try adding some other chart types, either to create standalone figures or add them to the Dash app.