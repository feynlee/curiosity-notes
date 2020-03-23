---
title: How I solved the world's hardest logic puzzle
description: The logical paths I took to tackle the world's hardest logic puzzle
summary: Three gods A, B, and C are called, in no particular order, True, False, and Random. True always speaks truly, False always speaks falsely, but whether Random speaks truly or falsely is a completely random matter. Your task is to determine the identities of A, B, and C by asking three yes-no questions; each question must be put to exactly one god. The gods understand English, but will answer all questions in their own language, in which the words for yes and no are da and ja, in some order. You do not know which word means which.
author: Ziyue Li
toc: true
comments: true
layout: post
image: images/posts/3_Gods.png
hide: false
search_exclude: false
categories: [puzzle]
---

People often show solutions to a problem without showing their thinking process, just like a magician hiding his/her methods. Instead of knowing the answer, which is no fun at all, I think it's far more important to understand the logical process that helps one reach the answer. After all, this is where the satisfaction of understanding a problem comes from. So I thought it might be helpful to show my thinking process during my attempt to solve this puzzle.

# The Puzzle

![Missing image](https://fishlee919.files.wordpress.com/2017/01/7531_021f6dd88a11ca489936ae770e4634ad.png?w=1240)

_For simplicity, I will denote True, False, Random gods with T, F, and R respectively._

I've organized and cleaned up my thoughts for better clarity. I will present the version of the solution that felt most natural to me, and explain in the final section both the much simpler solution and the unnecessarily complicated solution I originally came up with in my hurried effort to solve this puzzle.

# Step 1. An Overall Assessment of the Problem:

The first thing I did was to figure out in principle, whether this problem is solvable.
There are 6 different orderings for the gods' positions: "T, F, R","T, R, F",  "F, T, R", "F, R, T", "R, T, F", "R, F, T". This is what we need to figure out. If each question is asked to a different god, then at maximum we have $2^3=8$ different possible answers "da, da, da", "da, da, ja", "da, ja, da", "da, ja, ja", etc. But R's answer provides no useful information at all, so R's "da" and "ja" are not distinguishable. This cuts down the useful information to 4. In other words, we would need to distinguish 6 different outcomes with only 4 different pieces of information (or 2 "bits"). This is impossible!

The assumptions must be wrong. The 6 different positions of gods seem inarguable. So what's wrong with the second deduction that gives us 4 pieces of info?

In order to distinguish 6 positions, we must have at least 6 pieces of info. Well, if we ask T or F 3 questions, we know we can get 8 pieces of info since their answers are distinguishable, and a careful reread of the question reveals that indeed it doesn't prevent us from doing that. Each question to one god, but one god can have multiple questions.

But there seems to be no way for us to avoid R in the first question since we have no information to know who R is. What about avoiding R in the second and third questions? The probability that it will be R that answers the first question is $1/3$. If we can avoid R during the second and third question, we would on average get $1/3 * 4+2/3 * 8=6.66666...$ pieces of information, which makes it possible to figure out the 6 different positions! If however, we can only avoid R till the 3rd question, we would on average have $2/3 * 4+1/3 * 8=5.333... < 6$, which is not enough to solve the puzzle.

**Conclusion: we must be able to _at least_ figure out _"who is not R"_ after the first question, in order for the puzzle to be solvable!**

# Step 2. General Strategy:

Let's do some more deductions to reason out the general strategy. We now know, that the first question should be able to tell us who's not R. How is that possibly achieved?

1. The answer to the first question can only be "da" or "jar", 1 bit of information, which we can use to distinguish 2 different things.
Conveniently, what we want to find out after question 1 is whether god 2 is not R or god 3 is not R, two things to distinguish.
Therefore, we can map the answer "da" to "2 is not R" and "jar" to "3 is not R" or the other way around.

2. After we figure out who is not R, we need to ask that god the second question to make sure R is not answering question 2. We can easily duplicate the first question to figure out which one of the other two gods is not R, and therefore combing question 1 and 2 to figure out the identity of god R.

3. That leaves us with one question to figure out T and F. Is that possible to do? If we ask this question to one of the non-random gods, we receive two distinguishable pieces of information, and we need to distinguish two things, so in principle, this is totally possible.
But how does one do it? Let's say we map "da" to god T, and "fa" to god F, meaning if the answer we receive is "da", then the god is T, otherwise F.
What question would make god T answer "da", and god F answer "fa"?
Since we don't know the meaning of "da" and "fa", we have to consider the following two scenarios: "da" means yes, "da" means no.
If "da" is yes, T needs to answer yes, and if "da" is no, T needs to answer no.
So the answer to the question depends on whether "da" is yes or no.
At this point, it should be obvious, that **the question can simply be "is 'da' yes?"**
You can check for yourself, that T will always say "da" to this question and F will always say "fa" to this question.

# Step 3. Deduce and Construct Question 1

Now that we've figured out question 3, and question 2 and question 1 are basically the same, we only need to figure out question 1.

So is it possible to choose between the rest of the 2 gods so that we can avoid the R?

Obviously, when the first god happens to be R, it doesn't matter what the answer is, and it doesn't matter how we choose between the rest of the 2 gods. Therefore, we only need a simple mapping from the 2 possible answers to god 2 and god 3 when the first god is either T or F.

## I. The Qualities Question 1 Needs to Satisfy:

Let's take the mapping of "da" -> "3 is not R" and "ja" -> "2 is not R" as an example to start our reasoning.
Since we don't have to think about god 1=R, either 2 or 3 is R. The mapping reduces to "da" -> "2 is R" and "ja" -> "3 is R".

This mapping requirement means no matter who (T or F) this question is asked, if the answer to "is 2 R" is yes, we should always get "da" as the answer, regardless of whether "da" means yes or no. If the answer to "is 2 R" is no, we should always get "ja" as the answer, regardless of what "ja" means.

To break this down further, we have

$$\text{2 is not R} + \left\{ \begin{matrix} \text{da} =\text{yes} \Rightarrow \text{yes (da)}\\ \text{da}=\text{no} \Rightarrow \text{no (da)} \end{matrix}\right.$$

$$\text{2 is R} + \left\{ \begin{matrix} \text{da}=\text{yes} \Rightarrow \text{no (ja)}\\ \text{da}=\text{no} \Rightarrow \text{yes (ja)}\end{matrix} \right.$$

  1. **Both T and R should give the same yes or no answer so that it doesn't matter which god is answering the question.**

  2. **Whether "da" is yes or no should flip the yes or no answer, so that when "da" means yes, the god says "da" (yes), and when "da" means no, the god also says "da" (no).**

  3. **Whether "2 is R" should also flip the yes or no answer, so that "da" flips to "ja".**

## II. Construction of the Question:

### a. Satisfying Requirement 1:

Let's look at requirement 1 first: how is it possible to ask a question, such that both gods would give the same answer? Since for most simple questions, T and F would give opposite answers, we need to combine their answers in some way to get agreements. A simple trick that can achieve this immediately comes to mind: **chain T's answer with R's answer with an embedded question.**

>Note: This was also my downfall. As I will explain later, there's another way of getting consistent answers between T and F gods that leads to a simpler overall solution. But I was so eager to test out this first strategy that came to my mind, that I didn't explore other possibilities. Let me now continue my reasoning following this way of constructing the question.

Still assuming we are only dealing with T and F, we can ask for example: "would the other god (one of T and F) answer yes to the question Q"? The question Q is just an embedded question. I will leave the details of the deduction to the readers, and just say no matter who answers the question (T or F) and who the other god is (F or T), if the truthful answer to Q is yes, then we will get a no answer, and vice versa, because F in the chain would flip the answer once.

### b. Satisfying Requirement 2:

Requirement 2 introduced 2 different scenarios: "da" is yes or "da is no. And depending on which is the case, the answer changes. The solution is very easy, we just compound this element on top of the chaining question we constructed above. Simply change "yes" to "da" (or "ja") to cover the ambiguity of "da": "_would the other god answer 'da' to the question Q_"?

When "da"=yes, the above question translates to the original "would the other god answer yes to the question Q", when "da"=no, it translates to "would the other god answer no to the question Q". The same chain structure guarantees the same answer between T and F gods as before, but now the answer also flips depending on the meaning of "da".

### c. Satisfying Requirement 3:

"is 2 R" should also flip the answer, which means we need to incorporate it into our question as well. Well, we haven't specified what Q is yet. Any simple question can replace Q's position and still meet requirement 1 and 2, and it's obvious that the truthful answer to this question Q would flip the chain since it changes the starting point of the chain. Therefore, the question now becomes: "_would the other god answer 'da' to the question 'is 2 R'_"?

Again, I leave the detailed deduction of the answers in different scenarios to the readers.

### d. Dealing with the Random God

The question would work, except, we have a random god between 2 and 3, so we can't simply say "the other god" to automatically pick out T or F from god 2 and god 3. But in order for our question to work, the answer to the question "is 2 R" has to be consistent and not random.

There's no way that we can know which one of the other 2 gods is not R before the first question since that's exactly what the first question is trying to figure out.
If we think carefully though, we notice that we don't really need to identify which one of the other 2 gods is not R in order for our question to work.
We only need the answer to be consistent.
One way to do that is to combine the answers of the other two gods in such a way that only the non-random god's answer is taken.

How to combine a consistent answer with a random answer so that the consistent answer is always taken?
Well, we can use the phrase "always" to single out the consistent answer.

**The question, therefore, becomes: "_would at least one of the other 2 gods always answer 'da' to the question 'is 2 R'_"?**

<!-- ## I. A straight forward solution: -->

# Step 4. Putting Everything Together

Having figured out the first question, the second and the third questions are easy to figure out. Here they are:

  1. **Ask one god: "would at least one of the other 2 gods always answer 'da' to the question 'is 2 the random god'"?** If the answer is "ja", then go to god 3 to ask the second question, if the answer is "da", then go to god 2 to ask the second question.

  2. **Ask the second god (god 2 or god 3 depending on the answer of question 1) the same question: "would at least one of the other 2 gods always answer 'da' to the question 'is 2 the random god'"? (Change it to "would at least one of the other 2 gods always answer 'da' to the question 'is 3 the random god'" or "would at least one of the other 2 gods always answer 'da' to the question 'is 1 the random god'" if the second god is god 2.)** If you get "da" as the answer, then the god mentioned in your question is not random, otherwise, between the other two gods, the god not mentioned in your question is not random one. Therefore, the god left (besides the god you are asking and the god you just figured out as the other non-random god) is the random god.

  3. **Ask one of the non-random gods: "Is 'da' yes?"** If you receive "da" as the answer, then the god you are asking is T, otherwise F.

---

# Alternative Solutions

## I. A Much Simpler Solution:

As mentioned in Step 3.II.a, there's another way to achieve requirement 1. Instead of chaining T and R's answer with each other, we chain them to themselves! This way, F and F double flips is the same as T and T. The question can be asked as "would you answer 'da' to the question ..."

The good thing about this is that since we don't need to consider the situation where we are asking the random god, the god we are asking can always be treated as non-random. Therefore, we don't need to group this god with another god, and the question becomes much simpler:

**"Would you say 'da' to the question 'is 2 the random god'"?**

Notice that this "would you say..." is an embedded question just like before "would the other god say..." It requires the god to answer about his answer to the question.

This dramatically simplifies the solution.

## II. My Original Very Complicated Solution

Besides the other chaining method I didn't think about, in my hurried effort to solve this puzzle, I also rushed to get to the end and ended up with a more complicated version of question 1. Instead of asking how the god would answer the question, I was so worried about dealing with the Random god that I also grouped two gods answers in constructing question Q. My original first question is unnecessarily more complicated:

**"Would at least one of the other 2 gods answer 'da' to the question 'would one of you and god 2 always disagree to the question is da yes'"**?

It should be easy to see that question Q "would one of you and god 2 always disagree to the question 'is da yes'" really is just asking is "is one of you and god 2 R"? Since T and F would always disagree on the answer to that question. And since we can ignore the case that the god you are asking the question is R, this question simplifies to "is god 2 R"?

I was in the mindset of grouping gods and totally forgot about the previous deduction that "_one does not need to consider the situation that the god you are asking the first question is R_". This really shows how important it is to actually go through the logical deduction steps more carefully.