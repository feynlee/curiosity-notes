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
---

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