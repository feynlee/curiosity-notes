---
title: Parallel Transport and the Mathematical Rabbit Hole of Differential Geometry
author: ziyue li
categories:
- physics
- math
date: '2022-10-20'
# description: how parallel transport can be understood.
draft: true
# image: images/posts/
search_exclude: false
subtopic: riemannian geometry
tags:
- riemannian geometry
- vector bundle
- metric connection
toc: true
topic: general relativity

---

# introduction


# true parallel transport

## overview

how do we parallel transport a vector on a curved surface?

the most intuitive method is to look at parallel transport in a very small local area where it can be approximated as a flat surface.
in this small area, the parallel lines are easily defined, and we can therefore figure out how the coordinates rotate and twist relative to the parallel lines when we step in different directions.

we can denote the change of the basis vectors when we move on the surface as the follows:

$$\partial_{\mu}{\pmb{e}_j}=\gamma_{\mu j}^{i} \pmb{e}_i$$

the change of a arbitrary vector field is therefore

$$\partial_{\pmb{v}}\pmb{s} = v^{\mu}\partial_{\mu} (s^{i} \pmb{e}_{i}) = v^{\mu} (\partial_\mu s^i + \gamma_{\mu j}^{i} \pmb{e}_i s^j)$$

we can define the covariant derivate:

$$d_\mu = \partial_\mu s^i + \gamma_{\mu j}^{i} \pmb{e}_i s^j$$

which takes into account the change of coordinate basis on the curved surface, and thus is a true comparison of parallel transported vectors at the same location.

all we need to do now is figure out the Christoffel symbols $\gamma^{i}_{\mu j}$ for parallel transport.

## parallel transport on a 2d sphere

the metric tensor for the sphere encodes all the information we need to figure out how coordinates rotates relative to parallel transport.

let's use the surface of a sphere for illustration.
written on the spherical coordinates, the metric tensor for a sphere of radius $r=1$ is

$$g_{ij} = \left(\begin{matrix}
1 & 0 \\
0 & \sin^2\theta
\end{matrix}\right)$$

because $g_{ij}=\pmb{e}_i\cdot\pmb{e}_j$, we have

$$\begin{align}
|\pmb{e}_\theta|&=1 \\
|\pmb{e}_\phi|&=\sin\theta \\
\pmb{e}_\theta\cdot\pmb{e}_\phi&=0
\end{align}$$

this gives us the magnitude of each basis vector and the angle between them ($90\degree$).
we now have everything we need to draw the local changes of the coordinate basis as follows:

![fig 1. local changes of coordinate basis for a 2d sphere](images/2022/parallel_transport-coordinate_basis.png){fig-align=center}

we can clearly see, that because $\pmb{e}_\phi \propto \sin\theta$, the $\pmb{e}_\theta'$ is rotated.
the rotation angle $\alpha \approx \tan\alpha = d(\sin\theta)/d\theta = \cos\theta$.
and because the basis vectors here are alway orthogonal to each other, $\pmb{e}_\phi$ is also rotated by the same angle $\alpha$.
note that $\pmb{e}_\theta'$ should have the same length as $\pmb{e}_\theta$ according to the metric tensor, but it's impossible to draw this on a flat 2-d surface.
in order to satisfy the conditions spesified by the metric tensor, the surface has to be curved.
this demonstrates to us how the metric tensor specifies rotations and twist of coordinate basis and the geometry of the space.

focusing on the local changes of the basis vectors, we have

$$
\begin{align}
\frac{\partial\pmb{e}_\theta}{\partial\theta} &= \pmb{e}_\theta' - \pmb{e}_\theta=0 \\
\frac{\partial\pmb{e}_\theta}{\partial\phi} &= \pmb{e}_\theta'' - \pmb{e}_\theta=\cos\theta/\sin\theta \pmb{e}_\phi = \cot\theta \cdot\pmb{e}_\phi \\
\frac{\partial\pmb{e}_\phi}{\partial\theta} &= \pmb{e}_\phi' - \pmb{e}_\phi=\pmb{e}_\theta'' - \pmb{e}_\theta = \cot\theta \cdot\pmb{e}_\phi \\
\frac{\partial\pmb{e}_\phi}{\partial\phi} &= \pmb{e}_\phi'' - \pmb{e}_\phi=\tan\alpha \cdot|\pmb{e}_\phi| \cdot(-\pmb{e}_\theta)=-\cos\theta \sin\theta \cdot\pmb{e}_\theta\\
\end{align}$$

in other words,

$$
\begin{align}
\gamma^{\theta}_{ij} &= \left(\begin{matrix}1 & 0 \\ 0 & -\sin\theta\cos\theta\end{matrix}\right), \\
\gamma^{\phi}_{ij} &= \left(\begin{matrix}0 & \cot\theta \\ \cot\theta & 0 \end{matrix}\right).
\end{align}
$$

this example shows us that how the twist and changes of basis vectors are produced by the the metric tensor.
next, we show how we can derive the christoffel symbols from arbitrary metric tensors.

## parallel transport for arbitrary metric tensor

$$
\begin{align}
\partial_\gamma g_{\alpha\beta} &= \partial_\gamma (\pmb{e}_\alpha \cdot \pmb{e}_\beta) \\
&= (\partial_\gamma \pmb{e}_\alpha)\cdot \pmb{e}_\beta + \pmb{e}_\alpha \cdot (\partial_\gamma\pmb{e}_\beta) \\
&= \gamma_{\gamma\alpha}^{\mu} \pmb{e}_\mu \cdot \pmb{e}_\beta + \gamma_{\gamma\beta}^{\mu} \pmb{e}_\mu \cdot \pmb{e}_\alpha \\
&= \gamma_{\gamma\alpha}^{\mu} g_{\mu\beta} + \gamma_{\gamma\beta}^{\mu} g_{\mu\alpha}
\end{align}
$$

### Torsion Free and Metric Compatibility


# generalized "parallel transport"


# the mathematical rabbit hole

## differential geometry

## fiber bundle

## topology


