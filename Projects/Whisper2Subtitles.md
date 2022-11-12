---
title: Whisper2Subtitles
date: '2022-11-09'
description: Add bilingual subtitles to videos using OpenAI's Whisper model.
draft: false
categories:
- Deep Learning
image: images/whisper2subtitles/whisper2subtitles-facecover.png
---
![](images/whisper2subtitles-facecover.png){fig-align="center" width=100%}

[![](https://colab.research.google.com/assets/colab-badge.svg){fig-align="left"}](https://colab.research.google.com/github/feynlee/whisper2subtitles/blob/main/Whisper2subtitles.ipynb)

A simple Google Colab Notebook to generate transcribed subtitles for videos/audios using OpenAI's open source [whisper model](https://github.com/openai/whisper), with options to generate translated subtitles.

You can choose to generate translations using Facebooks' [M2M100_418 model](https://huggingface.co/facebook/m2m100_418M) model or manually add translated texts from other tools. The original texts and translated texts will be combined into one bilingual subtitle.

There's also an option to burn the subtitle into video using ffmpeg directly in the notebook.

GitHub repo: [https://github.com/feynlee/whisper2subtitles](https://github.com/feynlee/whisper2subtitles)