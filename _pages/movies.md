---
layout: default
title: Movies
permalink: /movies/
search_exclude: true
---
# Movies I enjoyed

<div class="tab-pane show active" id="movie-list" role="tabpanel" aria-labelledby="movies-tab">{%- include movies.html -%}</div>

<script>
  $('#video-link').magnificPopup({
    type: 'inline',
    closeOnBgClick: true,
    showCloseBtn: false
  })
</script>
