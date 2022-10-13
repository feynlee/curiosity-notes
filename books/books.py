import yaml

with open('pages/books/books.yml', 'r') as stream:
   books = yaml.load(stream, Loader=yaml.Loader)

entries = [
"""---
format:
  html:
    page-layout: article
title: Books
description: Some books that I enjoyed reading.
toc: false
---

:::::::{.collection-container}
"""
]
for book in books:
   if book.get('subtitle', None):
      block = \
f"""
::::::{{.collection-item}}
:::::{{.collection-item-inner}}
::::{{.collection-item_img}}
:::{{.collection-item-img-link}}
[[goodreads]({book['goodreads_url']})]{{#collection-item-img-link}}
<br>
[[amazon]({book['amazon_url']})]{{#collection-item-img-link}}
:::
![]({book['img_url']})
::::
::::{{.collection-item_description}}
:::{{.collection-item-name}}
{book['title']}
:::
:::{{.collection-item-subtitle}}
{book['subtitle']}
:::
:::{{.collection-item-quotes}}
{book['description']}
:::
::::
:::::
::::::
"""
   else:
      block = \
f"""
::::::{{.collection-item}}
:::::{{.collection-item-inner}}
::::{{.collection-item_img}}
:::{{.collection-item-img-link}}
[[goodreads]({book['goodreads_url']})]{{#collection-item-img-link}}
<br>
[[amazon]({book['amazon_url']})]{{#collection-item-img-link}}
:::
![]({book['img_url']})
::::
::::{{.collection-item_description}}
:::{{.collection-item-name}}
{book['title']}
:::
:::{{.collection-item-quotes}}
{book['description']}
:::
::::
:::::
::::::
"""

   entries.append(block)

entries.append(":::::::")
book_list = '\n'.join(entries)

with open("pages/books/books.md", "w") as f:
    f.write(book_list)