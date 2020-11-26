---
author: Ziyue Li
comments: true
date: 2019-04-27 19:08:08+00:00
layout: post
title: Cosmological Measurements
image:
featured_img_background: white
tag_line:
excerpt:
categories:
- Astrophysics & Cosmology
tags:
- Cosmology
---
<pre>We've discussed some basic cosmological concepts in the first chapter: Cosmological Perspective, and went through some thought experiments to have some conceptual understanding of the expanding universe. But how do we measure things and test these ideas? How do we measure the distance to a star? How do we infer that the universe is expanding? How do we measure the age of the universe? How do we test our standard cosmological model? These are all very important questions. The answer to them are complicated. Instead of going into details of every possible technique and associated errors and assumptions, I feel like it's much more beneficial to give some core ideas and leave the details of different methods for interested readers to explore on their own.</pre>

# A. Proving the theory vs. testing the theory

**The first thing we need to get across is that we are never really "proving the theory". All we can do is "testing the theory".** To "prove a theory", you have to have clear and unequivocal evidence that things work exactly as the theory says and the experimental or observational results are not due to some other possible effects. This is super hard, and probably will not be 100% realized in the near future, at least in cosmology. We can't go see the whole universe, we can't go out there and measure large distances instantaneously without spending anytime for signal to travel from one to the other. Philosophically, you even can push this to the extreme and say, even if you see how things work, do you really think your theory is the only possible theory for what you see and it will continue to work when including other future observed phenomenal? In that sense, one can never be 100% sure. It's like watching God play chase, and trying to guess the rules of the game. You may be quite satisfied with your theory and think it explains every move, but unless God tells you the secret you will never be sure the next move is not outside of your expectation. On the other hand, to "test a theory" is to see whether it fits all the things we can observe (or experiment on), and to carefully rule out other competing theories if possible. All we can say in the end, is that it seems that our current standard cosmological model fits with our observations and all different aspects of theory and its predictions seem to agree with each other. Therefore, we are not using observational facts to "deduce" the theory here, which is hardly ever possible, we are merely testing our model, and interpret observations using our model, and see whether these interpretations for different things and the extraction of the model parameters from different observations using different methods fit with each other. If everything fits well and there's no large tension, we say the theory works as far as we know.

So what things can we measure in the sky? The light, and the angle. The light has a few properties we can analyze, for example, the total intensity i.e. the luminosity, the intensity distribution in different wave length i.e. the spectrum, and the intensity distribution in time. The extended angle of the object gives the apparent size in the sky. And the position relative to other stars.

* * *

# B. Redshift

## I. The theory says that a photon's frequency will change when it travels from the source to us.

The basic expanding universe model and its two assumptions were introduced in Chapter I. Here we talk about some of its consequences:

### (1) First, the <span style="color:#ff6600;">cosmological expansion</span> induces a <span style="color:#000000;">frequency change</span><span style="color:#0000ff;"><span style="color:#000000;"> for photons.</span></span>

Let's say the photon has a wavelength of $latex \lambda_{t_s}$ at the time of emission at the source. As the space itself expands, some time later, the photon's wavelength will expand with space to $latex \lambda_{t_o}$ by the time it was detected by the observer. And because we use the scale factor $latex a(t)$ to characterize the expansion of space, we have

$latex \dfrac{\lambda_{t_o}}{\lambda_{t_s}}=\dfrac{f_s}{f_o}=\dfrac{a(t_o)}{a(t_s)}$.

If the universe is expanding, then $latex f_o>f_s$, the frequency will be decreased. **One should note that this change in frequency only depends on the scale factor at the time of emission and the time of the detection, and independent of how the universe expanded in between. In other words it's agnostic about the dynamics.**

### (2) On top of that, the <span style="color:#ff6600;">local motion</span> of objects induces a <span style="color:#0000ff;">Doppler shift</span> for photons.

When a light source moves relative to an observer, the detected frequency will be different from the original frequency of the photon. And this is called the Doppler effect. One can use Einstein's special relativity to derive the following relativistic Doppler shift equation when there's only motion along the line of sight:

### $f_{o}=\sqrt{\dfrac{1-v/c}{1+v/c}}f_{s}.$

v is positive (negative), when the source is moving away (towards) the observer. We will use the simple case when there's no transverse motion throughout this article to simplify the discussion. For arbitrary motions, and for detailed derivation of the above equation and corresponding Doppler shift equation for arbitrary motion, please refer to [this wikipage](https://en.wikipedia.org/wiki/Relativistic_Doppler_effect). Here, the detailed derivation is not important for our purpose. **All we need to know is that in a static universe with non-expanding and non-contracting space, the frequency of the photon emitted at the source and the frequency observed at the detector are related by the velocity of the relative motion between them.**

### (3) In an expanding universe, the change in a traveling photon's frequency is a combination of both effects.

One may express the total redshift as follows:

### $1+z\equiv\dfrac{f_{o}}{f_{s}}=\dfrac{a(t_s)}{a(t_o)}\sqrt{\dfrac{1-v/c}{1+v/c}}.$

The $z$ is defined to be the so called <span style="color:#0000ff;">redshift</span>.

When the star is very close, the first factor due to the expansion will be very close to one, and most of the frequency change will be coming from the local motion. **In this case, if one knows the frequency of the photon emitted at the source, namely $latex f_{s}$ and the observed frequency $latex f_{o}$, one can calculate the relative velocity between the source and the observer.**

When the star is so far away, the first factor is not negligible any more, the knowledge of $f_s$ and $f_o$ gives information about the combined effects. **But because one can assume the local motion is random in every direction, by looking at several different objects located at the same distance from us, the Doppler effect will scatter the data points around the** $\dfrac{f_o}{f_s}$ **value, which gives us the information about the ratio of the scale factor now and then.**

We will discuss how to measure distances in section C. But before we do that, let's first answer the following question:

## II. The observed frequency is simply measured at the detector, but how do we know the frequency of the photon emitted at the source?

![]({{ site.baseurl }}/assets/301px-Redshift.svg.png)

If it were just a single photon of a certain frequency, we will have no hope of knowing the original frequency. But the emitted light is not just at a single frequency, but rather a continuous spectra. Because different elements absorb light very strongly at different sets of frequencies, they leave dark lines in the observed spectra. These dark lines are called <span style="color:#0000ff;">absorption lines<span style="color:#000000;">. T</span></span>hey are the "fingerprints" one can use to identity the elements present on the distant object. If the object is moving away relative to us, these "fingerprints" will be shifted uniformly to a lower frequency. **Therefore, by identifying the shifted pattern of these dark lines in the observed spectra one can know which element they come from and thus also know their original frequencies.**

* * *

# C. Dynamic expansion of the universe => relation between the redshift and proper distance.

## I. The scale factor $latex a(t)$ can be expanded in Taylor series:

$latex a(t)=a(t_0)[1+H_0(t-t_0)+\cdots]$

with the Hubble constant at the present time $latex t0$

$latex H_0\equiv \dfrac{\dot{a}(t_0)}{a(t_0)}.$

In section B, we discussed how we can measure the redshift $latex z$ which tells us the ratio of the scale factors at a previous cosmological time $latex t$ and the present time $latex t_0$. But the redshift does not have any information about time itself. If there's someway we can know the time $latex t$, then by measuring the redshift $latex z$ and time $latex t$ of objects at different distances (i.e. different time) from us, we can map out the function of $latex a(t)$. However, as we will see later, the age measurement is very tough.

**This gives the standard model description of how the universe expands and the scale factor is now a function of some parameters:** **Much of the experimental work is to "test" or "extract" these model parameters using different methods and see whether everything agrees.**

# So let's first take a look at how we can measure distances.

## The core idea is called <span style="color:#0000ff;">"distance ladder"</span>.

### We use trigonometrical methods (parallax) to measure very close stars.

We study them and find some interesting correlations of their luminosity and color (Main Sequence Stars), or luminosity and period of luminosity (Cepheid variable stars).

### Then we use these *** vs. absolute luminosity relations to go further out.

**The idea is that if we know the absolute luminosity of a distant star through some other means, then we can just compare it to the observed apparent luminosity to deduce the distance.**

#### This gives the <span style="color:#0000ff;">"proper distance".</span>

## Extracted model parameters.

### Positive vacuum energy

## III. The detected frequency change rules out pure Doppler effect theory.

How do we know the frequency change is not entirely due to Doppler effect? Well, if we look at the Doppler shift formula in B.II.(2),

# **To get the scale factor as a function of time, we need to measure time.**

## Radioactive decay

## Main sequence turn off

### Age of the universe?

# Finally, how do we measure mass?

## Mass of stars

## Mass content of clusters, galaxies or even the universe