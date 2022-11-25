---
title: Code-Insertion
date: '2022-11-25'
description: A Quarto extension that enables code insertion immediately before and/or after a post/page.
draft: false
categories:
- Tools
image: images/code-insertion/code-insertion-filters.png
---

[![](../images/icons/github-logo.png){fig-align="left" width=80px}](https://github.com/feynlee/code-insertion)

## What this is

I was looking for a way to add share buttons at the bottom of each post before the comment section (see  for details).
I searched through the [Quarto](https://quarto.org) documentation, and couldn't find a viable solution, so I created this extension to enable code insertion immediately before and/or after a post/page.

- When you insert code **before** the post, it will be after the post header (section that contains author and date).
- When you insert code **after** the post, it will be before the comment section.


## Installing

```bash
quarto add feynlee/code-insertion
```

This will install the extension under the `_extensions` subdirectory.
If you're using version control, you will want to check in this directory for your Quarto website.

## Using

In the front matter of a post, the `code-insertion` filter and add `insert-before-post` and/or `insert-after-post` parameters that point to a markdown file with sections you want to insert before and/or after the post.

```yml
filters:
  - code-insertion
insert-before-post: before_post.md
insert-after-post: after_post.md
```

You need to specify the path to the markdown file that contains the code you want to insert into your post.
Currently this extension does not support inline code insertion (i.e. specifying the code to be inserted right within YAML front matter).

**Tip**: You can add this to `_metadata.yml` under the folder containing all your posts, so that all of them can share this setting.

## Example

With this extension, I was finally able to [add the social share buttons](https://feynlee.github.io/curiosity-notes/posts/2022-11-24-10_tips_for_configuring_a_quarto_website.html#add-social-share-buttons).
