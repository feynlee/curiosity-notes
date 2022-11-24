---
title: Tips for Configuring a Quarto Website
author: ziyue li
categories:
- code
date: '2022-11-24'
# description: how parallel transport can be understood.
draft: true
# image: images/posts/
toc: true
format:
    html:
        number-sections: true
---

## Different Sidebars for Different Contents

## Enable Line Numbers in Code Blocks

## Add A Comment Section that Supports Latex

[Giscus](https://giscus.app) is a comments system powered by [GitHub Discussions](https://docs.github.com/en/discussions).
It supports Latex, so that visitors can type math equations in the comment section.

## Add RSS Feed

1. Add `feed: true` in the listing page
    Include a feed for your listing by including the `feed` option in your listing page:

    ```yml
    listing:
      contents: posts
      feed: true
    ```

    An RSS file will automatically be generated using the name of the the file in the same location as the listing page. For example, `index.qmd` will produce a feed at `index.xml`.

2. Include the path to the xml file

    We need to explicitly include links to these xml files.
    In this website, I created 3 RSS feeds: Posts, TIL and Projects, and included them in `_quarto.yml` under a menu on the right side of the navigation bar:

    ```yml
    website:
      navbar:
        right:
          - icon: rss
            menu:
            - text: Subscribe to Posts
                icon: rss
                href: https://feynlee.github.io/curiosity-notes/index.xml
                aria-label: Posts RSS
            - text: Subscribe to TIL
                icon: rss
                href: https://feynlee.github.io/curiosity-notes/TIL.xml
                aria-label: TIL RSS
            - text: Subscribe to Projects
                icon: rss
                href: https://feynlee.github.io/curiosity-notes/projects.xml
                aria-label: Projects RSS
    ```

## Add Social Share Buttons

## Add An Annotation Tool

You can enable [hypothes](https://web.hypothes.is) on your website so that visitors can highlight and annotate your posts.

```yml
comments:
  hypothesis:
    theme: clean
```

This is enabled for my website.
You can see the Hypothesis UI at the far right of the page.
You can also drag cursor over texts to make your own highlights and annotations on this page.

## Enable Anchor Sections

Hover over a section title to see an anchor link.
An anchor link makes it possible to share and reference the exact position of the specified section.
Enable/disable this behavior with:

```yml
format:
  html:
    anchor-sections: true
```

Anchor links are also automatically added to figures and tables that have a [cross reference](https://quarto.org/docs/authoring/cross-references.html) defined.

## A Custom Listing Page

[How to enable sorting, filtering and pagination](https://quarto.org/docs/websites/website-listings-custom.html#sorting-filtering-and-pagination)

<div class="sharethis-inline-share-buttons pt-5"></div>
