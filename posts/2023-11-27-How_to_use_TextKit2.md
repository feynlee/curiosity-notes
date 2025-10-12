---
author: Ziyue Li
# draft: false
date: 2023-11-27
layout: post
title: How to use TextKit2
image: images/2023/Long-Text-Pic-banner.png
featured_img_background: white
tag_line: Some learning notes on TextKit2
excerpt:
categories:
- Programming
tags:
- iOS
- Swift
- Xcode
---


```swift
struct TextEditorView: UIViewRepresentable {
    func makeUIView(context: Context) -> CustomTextView {
        // Use TextKit2
        let textContentStorage = NSTextContentStorage()
        let textLayoutManager = NSTextLayoutManager()
        let textContainer = NSTextContainer(size: CGSize(width: CGFloat.infinity, height: CGFloat.infinity))

        textLayoutManager.textContainer = textContainer
        textContentStorage.addTextLayoutManager(textLayoutManager)

        let textView = CustomTextView(frame: UIScreen.main.bounds, textContainer: textContainer, padding: 15)
        textLayoutManager.delegate = textView

        // Remove all paddings
        textView.textContainerInset = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
        // Set line fragment padding to 0 to remove default padding in UITextView
        textView.textContainer.lineFragmentPadding = 0

        // Set default font
        textView.typingAttributes = [.font: UIFont.preferredFont(forTextStyle: .body),
                                     .foregroundColor: UIColor(.black)]
        textView.isEditable = vm.isEditable
        textView.isSelectable = true

        // set delegate to handle text changes
        textView.delegate = context.coordinator
        return textView
    }

    ...
}
```

```swift
class CustomTextView: UITextView, NSTextLayoutManagerDelegate {
    var padding: CGFloat

    // Custom Initializer
    init(frame: CGRect, textContainer: NSTextContainer?, padding: CGFloat) {
        self.padding = padding
        super.init(frame: frame, textContainer: textContainer)
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: - NSTextLayoutManagerDelegate
    func textLayoutManager(_ textLayoutManager: NSTextLayoutManager,
                           textLayoutFragmentFor location: NSTextLocation,
                           in textElement: NSTextElement) -> NSTextLayoutFragment {
        let index = textLayoutManager.offset(from: textLayoutManager.documentRange.location, to: location)

        // Make sure the string is not empty
        if textStorage.length > 0 {
            let attributedString = textStorage.attributedSubstring(from: NSRange(location: index, length: 1))

            // Check for an NSTextAttachment at the first position
            if let attachment = attributedString.attribute(.attachment, at: 0, effectiveRange: nil) as? NSTextAttachment, attachment.image != nil {
                // The first character is an image
                // Return the default NSTextLayoutFragment
                return NSTextLayoutFragment(textElement: textElement, range: textElement.elementRange)
            }
        }

        // Otherwise, return a custom NSTextLayoutFragment with padding
        return TextLayoutFragment(textElement: textElement, range: textElement.elementRange, padding: padding)
    }
}


class TextLayoutFragment: NSTextLayoutFragment {
    var padding: CGFloat

    // custom initializer
    init(textElement: NSTextElement, range: NSTextRange?, padding: CGFloat) {
        self.padding = padding
        super.init(textElement: textElement, range: range)
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override var leadingPadding: CGFloat { return padding }
    override var trailingPadding: CGFloat { return padding }
}
```
