---
aliases:
- /Programming/2019/06/16/three-simple-steps-to-start-using-css-grid-template
author: Ziyue Li
categories:
- Programming
date: '2019-06-16'
description: Start using this today, and skip all the headaches of webpage layout
hide: false
image: images/css_grid.png
layout: post
search_exclude: false
summary: Here's a quick 3-step guide to start using css grid for easy layout.
tags:
- html & css
title: Three Simple Steps to Start Using CSS Grid Template
toc: true

---

## Step 1: Display Grid
First, we change the display to be "grid":

```css
div.container {
    display: grid;
}
```

## Step 2: Define Grid

We then define the grid using "fr" (short for fraction) as the following:

```scss
div.container {
    display: grid;
    grid-template-columns: 5fr 1fr 1fr;
    grid-template-rows: 1fr 1fr;
}
```

![](images/css_grid.png){width=70% fig-align="center"}

Think of each fraction as 1 unit. So the above code defines a grid with 3 columns with width 5, 1, 1 respectively and two rows with equal height. One can also define the grid using px, percentages and other units, but I find "fr" to be very convenient.

## Step 3: Place Content Into the Grid
The easiest way is to use grid-template-areas:

```scss
div.container {
    display: grid;
    grid-template-columns: 5fr 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    grid-template-areas:
        "description social rss"
        "description social rss";
}

div.description {
    grid-area: description;
    justify-self: stretch;
    align-self: stretch;
}
div.social {
    grid-area: social;
    justify-self: stretch;
    align-self: stretch;
}
div.rss {
    grid-area: rss;
    justify-self: stretch;
    align-self: stretch;
}
```

We assign the **grid-area** attribute for each block that we want to place into the grid, and then use **grid-template-areas** to easily specify how they should be layed out within the grid. The **justify-self** and **align-self** attributes further specifies how they should be justified and aligned within their grid space.

That should get you started! It's really that simple!

For more features and details about css grid, you can look up this wonderful guide: [A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/).
