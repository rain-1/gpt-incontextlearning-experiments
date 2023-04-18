# Logic Gate

## Background

In this we test the ability of an LLM to learn and execute an encoded logic gate. Encoded in the sense that one related set of words represent 'true' and another related set of words represent 'false'. We only bothered to do the xor function in this example.

This problem was mentioned by **Chris Olah** in [CS25 I Stanford Seminar - Transformer Circuits, Induction Heads, In-Context Learning](https://www.youtube.com/watch?v=pC4zRb_5noQ).

## Summary of results

```
0:
tested with 30 examples of
encoded xor encoded: encoded
gpt-4 gave an incorrect answer.

1:
tested with 30 examples of
encoded xor encoded: bool
gpt-4 gave the correct answer, and explanation.

2:
tested with an explanation of the problem and 30 examples of
encoded xor encoded: encoded
gpt-4 gave the correct answer.

3:
tested with explanation and no examples.
gave the correct answer in 'easy' format.
(of course it could not know whch format to answer in without any examples)
```

## Conclusion

GPT-4 struggled to solve this problem when the outputs were encoded. It was capable not only of solving the problem when the output was not encoded but it was able to explain what the problem was in words. It was also able to solve the problem in a 0-set setting, learning from its own problem description rather than a list of examples.

