---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Main page
description: "Welcome to my data visualization portfolio."
---

# Welcome to the Data Visualization Index


## Featured Visualizations

{% for visualization in site.visualizations %}
  <div class="visualization-preview">
    <h2><a href="{{ visualization.url }}">{{ visualization.title }}</a></h2>
    <p class="visualization-description">{{ visualization.description }}</p>
    <div class="visualization-meta">
      <time datetime="{{ visualization.date | date_to_xmlschema }}">
        {{ visualization.date | date: "%B %-d, %Y" }}
      </time>
      {% if visualization.author %}
        • {{ visualization.author }}
      {% endif %}
    </div>
  </div>
{% endfor %}

<style>
.visualization-preview {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s ease-in-out;
}

.visualization-preview:hover {
  transform: translateY(-2px);
}

.visualization-preview h2 {
  margin: 0 0 1rem 0;
  font-size: 1.8rem;
}

.visualization-preview h2 a {
  color: #333;
  text-decoration: none;
}

.visualization-preview h2 a:hover {
  color: #0366d6;
}

.visualization-description {
  color: #666;
  margin-bottom: 0.5rem;
}

.visualization-meta {
  color: #888;
  font-size: 0.9rem;
}
</style>
