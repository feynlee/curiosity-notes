---
title: Basic Customizations of Fastpages
description: Customizations of Fastpages beyond the official tutorial to make it more personal.
author: Ziyue Li
toc: true
comments: true
layout: post
image: https://github.com/fastai/fastpages/raw/master/images/diagram.png
hide: false
search_exclude: false
topic: programming
subtopic: html & css
categories: [Programming]
tags: [html & css]
---

# Custom css styles
Fastpages uses the _minima_ theme for styling. To override the default variable values and mixins, create a file `_sass/minima/custom-variables.scss`. To override the default styles, create a file `_sass/minima/custom-styles.css`. For more details, read the [documentation for minima](https://github.com/jekyll/minima#sass).

## Change page content width
For example, the default width of the page content is 800px, which I find too narrow for my taste. So I overwrote the default variable in `_sass/minima/custom-variables.scss`:

```scss
$content-width: 1000px;
```
You can find the default definitions of variables in the [minima theme](https://github.com/jekyll/minima/blob/master/_sass/minima/initialize.scss).

## Change the width of utterances comment section
If you are using [utterances](https://utteranc.es) for your comment section, its class name is simply `utterances`, so we can add the following line in `_sass/minima/custom-styles.css` to change the width:
```scss
.utterances {
  max-width: 100%;
}
```

# Add your own pages
Pages can be added under the `_pages` folder using available layouts. Refer to the Jekyll documentation on [pages](https://jekyllrb.com/docs/pages/) and [layouts](https://jekyllrb.com/docs/layouts/) for how they work.

By listing `header_pages` in `_config.yml`, you can select which pages to show on the navigation header and specify the order:

```yml
header-pages:
  - _pages/posts.html
  - _pages/books.md
  - _pages/movies.md
  - _pages/about.md
  - _pages/search.html
```

Note that you need to include the `_pages` folder in the path so that correct paths to these pages can be constructed. Also note that the file type is the source file type.


