# Wonderland Recall

# Background

The problem is to get the language model to recite pieces of alice of wonderland [from gutenberg](https://www.gutenberg.org/cache/epub/11/pg11.txt).

I found that adding `Continue the quote` after the passage was the best way to get it to try to recall the exact text rather than freeform generate plausible text.

# Graphs of Results

![](sin.png)

# Conclusion

This demonstrates near-exact recall of some pieces of the training data that was used. We are getting success on the majority of cases.

It's an interesting question to ask "how is this data stored?". We believe that larger models lead to better memorization [mentioned here](https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1).

I would like to see if anybody finds a way to make use of LLMs for the [Hutter compression challenge](http://prize.hutter1.net/).
