---
title: Study Notes for D3.js - 7 Basic Concepts to Grasp
description: I summarize 7 basic concepts that I find very important to understand when learning D3.
summary: I summarize 7 basic concepts that I find very important to understand when learning D3.
author: Ziyue Li
toc: true
comments: true
layout: post
image: images/posts/d3_part1.png
hide: false
search_exclude: false
categories: [Data Science]
tags: [d3js]
---

In this post, I summarize 7 basic concepts that I find very important to understand when learning D3.

## 1. Compartmentalize the canvas into groups ("g" tag)

Think of the whole visualization as many small groups of elements. Each group can have its own group of elements. Use **select** and **append** to add tags. The first thing usually is to create an svg element (the canvas):

``` javascript
var svg = d3.select("body")
            .append("svg")
            .attr("width", width)
            .attr("height", height)
```

Then within the svg element, we can add many groups, for example, the legend itself is a group, within which we have two groups, each represents an entry in the legend:

``` javascript
var legend = svg.append('g')
                .attr('class','legend')
                .attr('transform', 'translate(' + (width-100) + "," + 20 + ")")
                .selectAll('g')
                .data(["Home Team", "Others"])
                .enter()
                .append('g');
```


## 2. Set positions of each group by setting attributes 'transform' to 'translate(x,y)' for that group.


As shown in the above legend example. Note that the canvas origin is at the upper left corner, so the y direction goes downwards instead of upwards.


## 3. Bind data to elements by '...selectAll.data(data).enter().append(...)'


As shown in the above legend example, 'enter()' returns placeholder elements for data that are not yet bound to any element, while 'exist()' returns elements that not yet bound to any data. 'append' then adds the element.


## 4. Use functions to assign attributes '.attr'


``` javascript
legend.append("text")
.attr("y", function(d,i){
return i * 30 + 5;
})
.attr("x", radius * 5)
.text(function(d){
return d;
});
```

Use 'd' in function for the data entry, and 'i' for index of the data entry.


## 5. Create scale to map the 'domain' of data to the 'range' on the canvas

``` javascript
var time_extent = d3.extent(data, function(d){
return d['date'];
});

var count_extent = d3.extent(data, function(d){
return d['attendance'];
});

var time_scale = d3.time.scale()
                        .range([margin, width])
                        .domain(time_extent);

var count_scale = d3.scale.linear()
                          .range([height, margin])
                          .domain(count_extent);
```

Here 'domain' is the extent of the data range, while 'range' is the extent of the the plot on canvas.

Use '.scale' method with the appropriate scale. As an example, I used the 'linear()' map above. For time, do 'd3.time.scale()'.


## 6. Axis are special functions, use '.call()' on elements to create visualization of axis.

``` javascript
var time_axis = d3.svg.axis()
                      .scale(time_scale)
                      .ticks(d3.time.years, 2);

svg.append('g')
.attr('class', 'x axis')
.attr('transform', "translate(0,"+height+")")
.call(time_axis);
```

Use 'd3.svg.axis()' to create the axis function and set '.scale' and '.ticks'.


## 7. Finally, when reading data from csv or other files, one can transform the data before passing it on to create visualization.

``` javascript
var format = d3.time.format('%d-%m-%Y (%H:%M h)');
d3.tsv("world_cup_geo.tsv", function(d){
d['date']=format.parse(d['date']);
d['attendance']=+d['attendance'];
return d;
}, draw);
```

'd3.tsv()' reads in the data, and pass it to the anonymous function, and then feeds the result to the user-defined 'draw' function for visualization. This is very convenient when one needs to convert some data format before moving on to the visualization step.

Here I parsed the 'date' column and made them into a 'Date' type, and converted the 'attendance' column from string into a number using the unary operator '+'. The 'draw' is a function that draws the visualization of the dataset.




