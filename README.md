# Project 2: Analyzing Art Data
*Due December 2, 2019 @ 11:59pm through GitHub Classroom*

Projects may be submitted up to 3 days late, with a 10% penalty per day

<h2>Overview: </h2>
Visual art provides a rich source of data. We can study the composition of a work of art (e.g., the structure, contents, colors, sizes, etc) as well as more qualitative components of the work (e.g., the emotions it allows us to feel, our preference for a piece, etc.). While many components of composition can be extracted using computer vision, others require human expertise and experience to measure. 
<br/>

Mohammad & Kiritchenko ran a large scale study to understand the emotions and preferences viewers have for different pieces of art using the WikiArt dataset (https://www.wikiart.org/). They asked people to provide different ratings about their subjective experiences with 4,105 pieces in this corpus and collected those experiences through a series of measures. More details of their experiment are at http://saifmohammad.com/WebPages/wikiartemotions.html.
<br/>

I have cleaned up the data from this experiment in WikiDataClean.csv, reducing it to 3,646 pieces with full data and numeric years (note that you are welcome to download and use the full dataset for an additional challenge). In this file, you will see a series of columns containing the following data: 
* **Style**: What stylistic period was the piece from? 
* **Category**: What artistic movement is the piece a part of? 
* **Artist**: Who created the piece? 
* **Title**: What is the piece called? 
* **Year**: When was the piece created? 
* **Image URL**: Link to the piece in WikiArt
* **Painting Info URL**: Link to details about the piece
* **Artist Info URL**: Link to details about the artist
* **Is painting**: Is the piece a painting or something else (e.g., a sculpture)?
* **Face or body**: Does the piece contain a face, a body, or no human figures (note that face takes priority over body)?
* **Mean rating**: How did the annotators like the piece on average (-3 (strongly dislike) to 3 (strongly like))?

The remaining columns represent terms that annotators could provide about the piece. In each cell of the table, you will find the average annotation for that particular term. For example, if 4 of 10 annotators labeled an image as evoking trust, Trust would contain the value 0.4 for that image.

Your goal in this project is to create visualizations that illustrate interesting features of the dataset. You can do this in one of two ways: 

1. Create at least two interactive visualizations that let users explore the data in interesting ways. 
2. Create a website that tells a story about this data through at least four different visualizations paired with explanatory text. 

<h2>Option 1: Interactive Visualizations</h2>
<h3>Minimum Requirements:</h3>
This option will allow you to build a system that lets users explore the provided art data. If you choose this option, your project must:
<ul>
<li> Include a README.md file that outlines:
  <ul>
  <li>Information about your visualizations and what they show. Include information about interactions, preprocesses, and design as appropriate. Note what tasks the visualization allows you to accomplish to derive this insight and how your design is tailored to support these tasks. </li>
  <li>Your design process (e.g., how did you go about designing, building, and refining your system? Why did you choose these representations?)</li>
  <li>Your team roles for each individual</li>
  <li>How to run your project</li>
    <li>Any additional elements of the project you consider "above and beyond" the basic requirements.</li></ul></li>
<li>Include at least two unique visualizations:
  <ul>
  <li>One visualization must include some quantitative data</li>
  <li>One visualization must include categorical data</li>
  <li>Each visualization must be interactive</li>
  <li>Your visualizations should support at least one meaningful comparison between related data attributes</li>
</ul></li>
</ul>

<h3>Above and Beyond:</h3> 
The above requirements are the minimum for a passing grade on this project. Some ideas to improve your project include (but are not limited to):<ul>
<li>Unusual Representations: Draw on some of the examples from class to represent data in ways beyond a typical scatterplot or bar chart.</li>
<li>Style: Keep the style consistent across all your views, with an eye towards intelligently applying visual design.</li>
<li>Interesting Tasks: Derive insight into the data. Highlight these insights in your readme and describe how the visualization enables them. What do these insights tell us about the data? </li>
<li>Perceptually-Informed Design: Integrate perceptual concepts into your visualization design and discuss how you've integrated those concepts in your readme.</li>
<li>Integrate Imagery: Use data from the provided URLs to add more context to your visualization. For example, you could link to or scrape text about individual paintings or artists or integrate images of the art into your visualizations.</li>
<li>Coordinated Views: Have two or more visualizations that interact with one another as you move through the data.</li></ul>

<h3>Platforms:</h3> 
You can use any development platform you'd like so long as your final project runs in the browser without having to install anything new. Your project readme should include step-by-step instructions on how to run your projects and it should run without me having to modify the code. You are welcome to use different platforms for each visualization.

Some platforms to look at include:
<ul>
<li>D3</li>
<li>WebGL or Three.js</li>
<li>ProcessingJS</li>
<li>Google Maps API</li>
<li>Open Street Map API</li>
<li>Bokeh</li>
</ul>

<h2>Option 2: Storytelling with Data</h2>
<h3>Minimum Requirements:</h3>
This option will allow you to create a website that illustrates key aspects of the data to tell a story about visual art using the results from Mohammad & Kiritchenko's experiment. The story should include a series of visualizations and texts that together form a cohesive narrative about the data.  
<br/>

The visualizations you create as part of this option can be static: you do not have to render them in the browser, but can create visualizations using any combination of tools (e.g., Photoshop, Excel, Tableau, Illustrator, D3, etc) and display them as static images. Your website could be a single page or multiple pages, but should allow for intuitive navigation and a natural story flow. 
<br/>

Some examples of professional storytelling visualization projects include: 
<ul>
  <li>https://www.newyorker.com/tech/annals-of-technology/mapping-new-york-noise-complaints</li>
  <li>http://stars.chromeexperiments.com/</li>
  <li>http://archive.nytimes.com/www.nytimes.com/interactive/2012/08/04/sports/olympics/bob-beamons-long-olympic-shadow.html?_r=2</li>
  <li>http://www.r2d3.us/visual-intro-to-machine-learning-part-1/</li>
  </ul>

https://twooctobers.com/blog/8-data-storytelling-concepts-with-examples/ has a nice set of principles for good data storytelling. 

If you choose this option, your project must:
<ul>
<li> Create a website containing four visualizations that illustrates interesting features of the data. </li>
  <li>Include at least four unique visualizations:
  <ul>
  <li>One visualization must include some quantitative data</li>
  <li>One visualization must include categorical data</li>
  <li>Your visualizations should support at least one meaningful comparison between related data attributes</li>
  <li>Your visualizations should each be accompanied by text explaining what the visualization shows. Note what tasks the visualization allows you to accomplish to derive this insight and how your design is tailored to support these tasks.
</ul></li>
  <li>Include as a part of your website a section or page with the following details:
  <ul>
  <li>Information about your data preprocessing and design as appropriate.  </li>
  <li>Your design process (e.g., how did you go about designing, building, and refining your system? Why did you choose these representations?)</li>
    <li>Any additional elements of the project you consider "above and beyond" the basic requirements.</li>
  <li>Your team roles for each individual</li>
 </ul></li>
</ul>

<h3>Above and Beyond:</h3> 
The above requirements are the minimum for a passing grade on this project. Some ideas to improve your project include (but are not limited to):<ul>
<li>Unusual Representations: Draw on some of the examples from class to represent data in ways beyond a typical scatterplot or bar chart.</li>
<li>Style: Keep the style consistent across all your views, with an eye towards intelligently applying visual design.</li>
<li>Interesting Tasks: Derive insight into the data. Highlight these insights in your readme and describe how the visualization enables them. What do these insights tell us about the data? </li>
<li>Perceptually-Informed Design: Integrate perceptual concepts into your visualization design and discuss how you've integrated those concepts.</li>
<li>Integrate Imagery: Use data from the provided URLs to add more context to your visualization. For example, you could link to or include text about individual paintings or artists or integrate images of the art into your visualizations.</li>
<li>Coordinated Views: Use visualizations that complement one another in meaningful ways to tell a deeper story than they otherwise could on their own.</li></ul>

<h3>Platforms:</h3> 
You can use any tools or platforms you'd like to create your visualizations. Your webpage should run in the browser without me having to install any additional software. 


<h2>Submissions:</h2>
All submissions must be made through GitHub with a timestamp by 11:59pm on 12.2. Your submission files should include:
<ul>
<li>Your code and/or website</li>
<li>Your README (for Option 1)</li>
</ul>
Note that each group only needs to submit one file. <br/>

This project would typically be conducted over a two-week timeline, which would give you more time to focus on your final projects. However, I do not want to require people to work over the break. Given the pending break and final projects, I will give up to 5 bonus points to teams that submit their projects early. Starting November 27, you will get one bonus point per day early. As GitHub allows you to submit continuously, please send me an email (one per group with all team members CC'ed) after submiting your project (commit AND push) letting me know you've submitted your project early to receive the bonus points.  
