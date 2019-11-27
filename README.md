<h1>Project 2: Analyzing Art Data</h1>
Ahmed Al Hasani, Alex Costinescu, and Pratik Revankar 

<br />
<br />

<h2>How to Run</h2>
<p>The links to each visualization can be found here: </p>

<br />
<br />

<h2>Information About Our Visualizations</h2>

<h3>Mean User Ratings for Painting Styles Over Time</h3>
<p>This visualization shows how user scores changed as styles evolved over time. This was achieved by aggregating the data by year and style and then taking the average of the Mean rating at each point to find the Mean rating for a given style at a point in time. Each style is represented by a different color, and styles can be filtered out by clicking on them on the legend. Viewers can also zoom in/out of the data by scrolling up/down respectively and the visualization will zoom in to the point that the user's mouse is pointing at. Alternatively, users can click and drag to draw a box around the area that they would like to zoom in to.</p>

<br />

<h3>Negative vs. Positing Painting Scores</h3>

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
