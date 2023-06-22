---
author: Ziyue Li
draft: true
date: 2023-06-20
layout: post
title: Things I've Learned Releasing My First iOS App
image: /images/2023/Long-Text-Pic-banner.png
featured_img_background: white
tag_line: A brief summary of the things I've learned while creating my first iOS app.
excerpt:
categories:
- Programming
tags:
- iOS
- Swift
- Xcode
---

## How to Submit Your App to the App Store

In general, I followed this video:

{{< youtube ykiD5wqwSe4 >}}

I won't repeat what's already said in this video.
Instead, I will focus on the things that I encountered that are not mentioned in this video.

## Bypass setting up export compliance in App Store Connect

After you archive your app,

You can bypass setting up export compliance in App Store Connect, you can specify your use of encryption directly in the information property list (Info.plist) in your Xcode project. If you need to provide documentation, Apple will provide you with a key value to add to the Info.plist. [Learn More](https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations)

## TestFlight

Use TestFlight to make sure your app works before submission!

## In-App Purchase

1. Product ID has to match those used in local testing!! (Product.storekit)

2. There are a few other things you need to set up for In-App Purchase:
  1. https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases
  4. Sole Proprietorship:
      1. Set up a business bank account (checking account)
      2. Connect stripe

## App Preview

The screenshots you provide need to be specific sizes.
If you want to create good looking screenshots, you can use [https://app-mockup.com](https://app-mockup.com/) or [https://app.flycricket.com/screenshots/edit/852e2653-1f16-4115-a222-8ef780006319](https://app.flycricket.com/screenshots/edit/852e2653-1f16-4115-a222-8ef780006319) to create screenshots for your app.

You may also need to prepare screenshots for 5.5" iphone.

## privacy policy

This is my first time creating an app, and I wasn't expecting that releasing the app requires things other than the app itself.

I have no idea how to create a privacy policy, and I definitely don't want to pay a lawyer to do it for me.

After some research, I found this website: [https://app-privacy-policy-generator.firebaseapp.com](https://app-privacy-policy-generator.firebaseapp.com/) which was used by many solo developers.

You can host your privacy policy on [https://www.flycricket.com](https://www.flycricket.com/pricing.html) for free.

## Support URL

This is required.
People are saying that you can just use your wordpress website, or even facebook page or other social media page.
But I created a dedicated page for this app which also serves as this app's marketing page:

You can use flycricket to create a support email.


3. Getting link to the app for sharing: https://tools.applemediaservices.com/apple-app-store-promote
