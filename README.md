<h1>Project 2: Analyzing Art Data</h1>
Ahmed Al Hasani, Alex Costinescu, and Pratik Revankar 

<br />
<br />

<h2>How to Run</h2>
<p>The links to each visualization can be found here: <a href="https://info-4602-5602.github.io/project-2-wikiart-ahmed_alex_pratik_project2/">https://info-4602-5602.github.io/project-2-wikiart-ahmed_alex_pratik_project2/</a></p>

<br />
<br />

<h2>Information About Our Visualizations</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<p>This visualization shows how user scores changed as styles evolved over time. This was achieved by aggregating the data by year and style and then taking the average of the Mean rating at each point to find the Mean rating for a given style at a point in time. Each style is represented by a different color, and styles can be filtered out by clicking on them on the legend. Viewers can also zoom in/out of the data by scrolling up/down respectively and the visualization will zoom in to the point that the user's mouse is pointing at. Alternatively, users can click and drag to draw a box around the area that they would like to zoom in to.</p>

<br />

<h3>Negative vs. Positing Painting Scores</h3>
The visualization “positive vs negative scores” is a bubble plot, where each bubble represents an artwork. The total positive and negatives scores are based on scores given for each column (e.g. love, sadness, happiness) by respondents. There are three ways to view how the scores vary which include:
•	By Style
•	By Category
•	By “Face or body”

Each selected option, the bubble’s colors will change to show how the bubbles are clustered for each option. The first and third option have 6 and 3 unique values, hence, its easy to visualize the clusters. The second option has 44 unique values, hence 44 clusters. This is difficult to visualize, but we added an interactive tool to help reading the plot which we will address below. For example, for the “face or body”, we can see that the face bubbles (artwork with faces) invoke stronger emotions, where users reported a total of positive/negative scores more than 1.0, whereas for body artwork, users reported weaker emotions. 


The data wasn’t processed heavily. We summed up positive scores for positive columns and negative scores for negative columns. The positive and negative columns include:

Positive: ['Gratitude', 'Happiness', 'Love', 'Humility', 'Trust', 'Optimism']
Negative: ['Pessimism', 'Sadness', 'Shame', 'Anger', 'Arrogance', 'Disgust', 'Fear', 'Regret']

In turn, we created two new columns, “total positive” and “total negative”. 

Additionally, each “group” or cluster in each option, for instance, the “face” cluster and the “body” cluster in the third viewing option, is assigned a unique color. To create this, we imported various color palettes, and stored each unique color for each group in each option. Hence, each bubble (each unique data row) is assigned a color for each option, to visualize how these bubbles are clustered in each viewing option. 

Hence the final dataset before creating the plot contains the positive and negative scores, three color columns (for each viewing option) and the title of the artwork so that it can be shown when the user hovers or taps a certain bubble. 

We wanted to show how bubbles are clustered for each option. For instance, for the first option “Style”, would different styles invoke emotions differently? Hence, would Renaissance Art would invoke stronger emotions than Modern Art? Would a certain style or sub option under the three options listed above vary in how negative/positive emotions are invoked in viewers? 

We wanted to build a visualization tool to answer the question above, therefore, we deemed that a scatter plot, or a bubble plot in addition to the bubbles’ color variations would be the most suitable one to visualize the data accordingly.

The visualization utilizes three main interactive tools. The first is the select tool to choose which option/categories to view, the second tool is the hover tool to view more information for each bubble, and lastly the tap tool which enables viewers to toggle bubbles for each cluster under each option while muting other clusters (by hiding their colors). 

Tasks
There are several tasks that the tool allows its users to complete and they include:
1.	Locate: Find a certain group. This is achieved by looking for certain clusters (using the legend and finding bubbles with the same colors), and to check/verify if that group exhibits a certain trait (if they have strong positive and negative emotions, or positive/negative emotions only).
2.	Browse: Look for interesting groups, find correlation through how closely are the bubbles located to one another in the same group or spread out. If a group’s bubbles are close to one another, then we can say its likely that the style invoked those emotions consistently across all viewers. 
3.	Identify: Find categories, style, or face/body portraits that viewers deem as a positively/negatively invoking artwork. This is achieved the same way browse is achieved, except that the viz’s users will beforehand have a particular style/category that they will attempt to locate and identify. 

<br />
<br />

<h2>Design Process</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<p>The goal with this visualization was to be able to explore how people's reactions to different styles evolve over time. We were curious to see if people had strong reactions towards to the beginning/end of stylistic periods or what other patterns might emerge as styles changed and evolved.</p>

<p>Based on our goal, we decided to build a line chart where styles were categorized using color. We also decided to scale the size of each point on the chart by the number of paintings being aggregated to show areas that were more represented in the data, and thus likely received  more ratings. However, while creating the chart, we realized that these points were too large and made it difficult to interpret the data because of significant overlay. To solve this issue, we decided to first scale the size of the points by the square root of the number of responses. While this helped to relieve the issue, we still wanted to make it easier to explore the data. Bokeh allows you to enable different tools to interact with the data and also to set default tools, so we added a scroll zoom and box zoom tool and enabled them as defaults. These allow the user to zoom in to the data either by scrolling or by drawing a box around a particular point, making it easier to explore.</p>

<p>Since the mean rating shows if users reacted overall positively or negative to a piece, we also decided to make draw a thicker line at y=0 so the user can easily see which styles/years received negative/postitive ratings.</p>

<p>Finally, we added a Bokeh hover tool to each point. This allows users to hover over a point and see the exact numerical values that are being portrayed by the visualization.</p>

<br />

<h3>Negative vs. Positing Painting Scores</h3>

<br />
<br />

<h2>Perceptually-Informed Design</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<p>The spatial position of points in this visualization as well as the color of the different styles makes this visualization easy to quickly scan and get the gist of. The size of points also give users a quick reference for points in the data that have more paintings and the thick line at y=0 allows users to quickly separate negative vs. positive average reactions to styles.</p>

<br />

<h3>Negative vs. Positing Painting Scores</h3>

<br />
<br />

<h2>Preprocessing Steps</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<p>For this visualization, we used Pandas in conjunction with Bokeh to processs the data. We started by grouping the data by Year and Style and applying a mean aggregation to the data to get the average values for the grouped columns. We also separately grouped the data and found the size of the groups to get a  count of the number of paintings in each group.<p>
  
<br />
  
<h3>Negative vs. Positing Painting Scores</h3>

<br />
<br />

<h2>Interactivity</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<p>As previously described, this visualization offers several avenues for interactivtiy. First, users can choose to show/hide the different styles by clicking on them in the legend. This allows users to focus in on particular styles without visual clutter. Additionally, users can hover over any point on the graph to see all of the information about that particular point, allowing them to see precisely what the values at that point are. Finally, users are able to zoom in/out of the data either by scrolling, or by drawing a box. This allows them to zoom in to a particular point and view that point with less visual clutter, making it easier to interpret/</p>

<br />

<h3>Negative vs. Positing Painting Scores</h3>

<br />
<br />

<h2>Tasks Accomplished</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<p>With this graph, we were able to show how users' ratings of styles changed over time. It was interesting to see that, which users' ratings remained almost universally positive for the most part, there was a clear and significant dip in users' feelings centered around Modern and Contemporary art in the 1960's. In fact, the only consistently negative style was Contemporary, with the other styles all consistently engendering positive reactions from users with the exception of some, small outliers. It is also clear from our graph that the data set contains a much higher quantity of Modern and Contemporary pieces than any other style, but it is not clear if this at all contributes to the more negative ratings.</p>

<br />

<h3>Negative vs. Positing Painting Scores</h3>

<br />
<br />

<h2>Data Attributes</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<ul>  
  <li>Mean rating</li>
  <li>Style</li>
  <li>Year</li>
  <li>Number of paintings</li>
</ul>

<br />

<h3>Negative vs. Positing Painting Scores</h3>

<br />
<br />

<h2>Team Member Roles</h2>

<ul>
  <li><strong>Ahmed:</strong></li>
  <li><strong>Pratik:</strong></li>
  <li><strong>Alex:</strong> Created <em>Mean User Ratings for Painting Styles Over Time</em> visualization and documentation/HTML pages.</li>
</ul>
