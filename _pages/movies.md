---
layout: default
title: Movies
categories: []
tags: []
order: 2
permalink: /movies/
---
<div class="tab-pane show active" id="movie-list" role="tabpanel" aria-labelledby="movies-tab">{%- include movies.html -%}</div>

<script>
  $('#video-link').magnificPopup({
    type: 'inline',
    closeOnBgClick: true,
    showCloseBtn: false
  })
</script>
