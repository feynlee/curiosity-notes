---
title: Export Jupyter Document With Optional Code Visibility
description: Generate an HTML file with a button to toggle code whenever the Jupyter notebook is saved
summary: Jupyter notebooks are great for data analysis, but when we need to share the analysis, some people may not care about the code. It would be great to have a solution that automatically generates reports where the code can be toggled by a button. After some online searching and experimentation, the following is my solution.
author: Ziyue Li
toc: true
comments: true
layout: post
image: images/posts/Jupyter_Auto_Convert.png
hide: false
search_exclude: false
categories: [Data Science]
tags: [Jupyter, automation]
---
## Why

Jupyter notebooks are great for data analysis, but when we need to share the analysis, some people may not care about the code. It would be great to have a solution that automatically generates reports where the code can be toggled by a button. After some online searching and experimentation, the following is my solution.

## Add Button to Toggle Code

Jupyter notebooks are web-based, we can simply add some html and javascript to make this work. One can include a raw cell at the beginning of your notebook containing the JavaScript and HTML below. This code is heavily based on [Chris Said's blog post](http://chris-said.io/2016/02/13/how-to-make-polished-jupyter-presentations-with-optional-code-visibility/), except it also hides a few other things besides the input cell, includin the numerical prompt next to the cells such as `input [1]` and `output [1]`.

```html
<script>
function code_toggle() {
    if (code_shown){
    $('div.input').hide('500');
    $('#toggleButton').val('Show Code')
    } else {
    $('div.input').show('500');
    $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
}

$( document ).ready(function() {
    code_shown=false;
    $('div.input').hide();
    $('div.prompt').hide();
    $('div.back-to-top').hide();
    $('nav#menubar').hide();
    $('.breadcrumb').hide();
    $('.hidden-print').hide();
});
</script>
<form action="javascript:code_toggle()">
<input type="submit" id="toggleButton" value="Show Code">
</form>
```

When we export the notebook to html, the added code will make a toggle button. See Chris' example [here](https://nbviewer.jupyter.org/github/csaid/polished_notebooks/blob/master/notebook_polished.ipynb).

This is good and all, but we don't want to manually add this raw cell to every notebook we create. Plus, it takes up a lot of space and does not look good in the notebook format. **_Is there a way that Jupyter can automatically add this code to the html file when exporting?_**

The answer is yes.

## Custom Template for Exporting HTML File

Most people know that we can use `nbconvert` to export html file, but few know that we can choose a template to use during this process: `jupyter nbconvert --to html 'example.ipynb' --template=custom_template.tpl`

This effectively gives us unlimited ability to format the output html file however we want. (For more details on how to make custom template, please refer to the [official document on customizing nbconvert](https://nbconvert.readthedocs.io/en/latest/customizing.html#Converting-a-notebook-to-an-(I)Python-script-and-printing-to-stdout) and the the [Jinja2 template language guide](http://jinja.pocoo.org/docs/2.10/templates/).)

Unfortunately, I found that we can not directly inherit the existing template used by nbconvert, since the position we want to insert our toggle button is not available if we inherit the existing templates. We have to alter some of the existing template to create our own.

If your jupyter is installed using anaconda in an python3.6 environment called `py3`, then the default templates for generating html files can be found under the path:

`<Anaconda_Folder>/envs/py3/lib/python3.6/site-packages/nbconvert/templates/html/`.

<!-- TODO modifications to basic.tpl -->

I copied the `full.tpl` template and added the script part in the `<head>` element:

{% raw %}
``` jinja
{%- block toggle_script -%}
<script>
function code_toggle() {
    if (code_shown){
    $('div.input').hide('500');
    $('#toggleButton').val('Show Code')
    } else {
    $('div.input').show('500');
    $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
}

$( document ).ready(function(){
    code_shown=false;
    $('div.input').hide();
    $('div.prompt').hide();
    $('div.back-to-top').hide();
    $('nav#menubar').hide();
    $('.breadcrumb').hide();
    $('.hidden-print').hide();
});
</script>
{%- endblock toggle_script -%}
```
{% endraw %}

and the html part for the button to the body.

{% raw %}

```jinja
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">
        <form action="javascript:code_toggle()">
        <input type="submit" id="toggleButton" value="Show Code">
        </form>
        {{ super() }}
    </div>
  </div>
</body>
```

{% endraw %}

See this [gist](https://gist.github.com/feynlee/701a56a239f7034e380e850865154945) for the full template code.

## Use Jupyter's Post Save Hook to Automate

We can add a function in the Jupyter configuration file to automatically export html file whenever we save a notebook. The Jupyter configuration file can be found at "~/.jupyter/jupyter_notebook_config.py" on mac.

An example code for `jupyter_notebook_config.py` that exports a html file on save for notebooks with "Report-" in their names:

```python
import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    if 'Report-' in fname:
        # generate html files
        check_call(['jupyter', 'nbconvert', '--to', 'html',
            fname, '--template=report.tpl'], cwd=d)
        print("finished creating html file {}".format(fname.replace('.ipynb', '.html')))


c = get_config()
c.FileContentsManager.post_save_hook = post_save
c.NotebookApp.open_browser = False
```

See [Jupyter documentation on file save hooks](https://jupyter-notebook.readthedocs.io/en/stable/extending/savehooks.html) for more details on how to use save hoooks.