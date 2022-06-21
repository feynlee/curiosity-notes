---
title: Parallel Transport and The Mathematical Rabbit Hole of Differential Geometry
description:
author: Ziyue Li
toc: true
comments: true
layout: post
image: images/posts/
hide: false
search_exclude: false
topic: General Relativity
subtopic: Riemannian Geometry
categories: [Physics Math]
tags: [riemannian geometry, vector bundle, metric connection]
---

# Introduction


# True Parallel Transport

## Overview

How do we parallel transport a vector on a curved surface?

The most intuitive method is to look at parallel transport in a very small local area where it can be approximated as a flat surface.
In this small area, the parallel lines are easily defined, and we can therefore figure out how the coordinates rotate and twist relative to the parallel lines when we step in different directions.

We can denote the change of the basis vectors when we move on the surface as the follows:

$$\partial_{\mu}{\bold{e}_j}=\Gamma_{\mu j}^{i} \bold{e}_i$$

The change of a arbitrary vector field is therefore

$$\partial_{\bold{v}}\bold{s} = v^{\mu}\partial_{\mu} (s^{i} \bold{e}_{i}) = v^{\mu} (\partial_\mu s^i + \Gamma_{\mu j}^{i} \bold{e}_i s^j)$$

We can define the covariant derivate:

$$D_\mu = \partial_\mu s^i + \Gamma_{\mu j}^{i} \bold{e}_i s^j$$

which takes into account the change of coordinate basis on the curved surface, and thus is a true comparison of parallel transported vectors at the same location.

All we need to do now is figure out the Christoffel symbols $\Gamma^{i}_{\mu j}$ for parallel transport.

## Parallel Transport on a 2D Sphere

The metric tensor for the sphere encodes all the information we need to figure out how coordinates rotates relative to parallel transport.

Let's use the surface of a sphere for illustration.
Written on the spherical coordinates, the metric tensor for a sphere of radius $r=1$ is

$$g_{ij} = \left(\begin{matrix}
1 & 0 \\
0 & \sin^2\theta
\end{matrix}\right)$$

Because $g_{ij}=\bold{e}_i\cdot\bold{e}_j$, we have

$$\begin{align}
|\bold{e}_\theta|&=1 \\
|\bold{e}_\phi|&=\sin\theta \\
\bold{e}_\theta\cdot\bold{e}_\phi&=0
\end{align}$$

This gives us the magnitude of each basis vector and the angle between them ($90\degree$).
We now have everything we need to draw the local changes of the coordinate basis as follows:

<figure>
  <a href="">
    <img src="{{ site.baseurl }}/images/posts/parallel_transport-coordinate_basis.svg">
  </a>
  <figcaption>
    Fig 1. Local changes of coordinate basis for a 2D sphere
  </figcaption>
</figure>

We can clearly see, that because $\bold{e}_\phi \propto \sin\theta$, the $\bold{e}_\theta'$ is rotated.
The rotation angle $\alpha \approx \tan\alpha = d(\sin\theta)/d\theta = \cos\theta$.
And because the basis vectors here are alway orthogonal to each other, $\bold{e}_\phi$ is also rotated by the same angle $\alpha$.
Note that $\bold{e}_\theta'$ should have the same length as $\bold{e}_\theta$ according to the metric tensor, but it's impossible to draw this on a flat 2-d surface.
In order to satisfy the conditions spesified by the metric tensor, the surface has to be curved.
This demonstrates to us how the metric tensor specifies rotations and twist of coordinate basis and the geometry of the space.

Focusing on the local changes of the basis vectors, we have

$$
\begin{align}
\frac{\partial\bold{e}_\theta}{\partial\theta} &= \bold{e}_\theta' - \bold{e}_\theta=0 \\
\frac{\partial\bold{e}_\theta}{\partial\phi} &= \bold{e}_\theta'' - \bold{e}_\theta=\cos\theta/\sin\theta \bold{e}_\phi = \cot\theta \cdot\bold{e}_\phi \\
\frac{\partial\bold{e}_\phi}{\partial\theta} &= \bold{e}_\phi' - \bold{e}_\phi=\bold{e}_\theta'' - \bold{e}_\theta = \cot\theta \cdot\bold{e}_\phi \\
\frac{\partial\bold{e}_\phi}{\partial\phi} &= \bold{e}_\phi'' - \bold{e}_\phi=\tan\alpha \cdot|\bold{e}_\phi| \cdot(-\bold{e}_\theta)=-\cos\theta \sin\theta \cdot\bold{e}_\theta\\
\end{align}$$

In other words,

$$
\begin{align}
\Gamma^{\theta}_{ij} &= \left(\begin{matrix}1 & 0 \\ 0 & -\sin\theta\cos\theta\end{matrix}\right), \\
\Gamma^{\phi}_{ij} &= \left(\begin{matrix}0 & \cot\theta \\ \cot\theta & 0 \end{matrix}\right).
\end{align}
$$

This example shows us that how the twist and changes of basis vectors are produced by the the metric tensor.
Next, we show how we can derive the Christoffel Symbols from arbitrary metric tensors.

## Parallel Transport for Arbitrary Metric Tensor

$$
\begin{align}
\partial_\gamma g_{\alpha\beta} &= \partial_\gamma (\bold{e}_\alpha \cdot \bold{e}_\beta) \\
&= (\partial_\gamma \bold{e}_\alpha)\cdot \bold{e}_\beta + \bold{e}_\alpha \cdot (\partial_\gamma\bold{e}_\beta) \\
&= \Gamma_{\gamma\alpha}^{\mu} \bold{e}_\mu \cdot \bold{e}_\beta + \Gamma_{\gamma\beta}^{\mu} \bold{e}_\mu \cdot \bold{e}_\alpha \\
&= \Gamma_{\gamma\alpha}^{\mu} g_{\mu\beta} + \Gamma_{\gamma\beta}^{\mu} g_{\mu\alpha}
\end{align}
$$

# Generalized "Parallel Transport"


# The Mathematical Rabbit Hole

## Differential Geometry

## Fiber Bundle

## Topology


