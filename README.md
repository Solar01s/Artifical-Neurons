# Artifical-Neurons
This is a project where I attempted to recreate the operation in two neurons with the same task, but using different approaches. One predicts intentions based on statistics and word frequency. While the other uses sentiment and word weights. The key difference from static algorithms is their learning ability.

# Difference in learning:
The statistical Neuron learns independently, while the emotional 
neuron, in contrast, learns with a teacher. Additional features
can also be used to monitor they learning progress.

# Statistical Neuron:
Write a phrase -> it stores updated statistics in links.json;
by typing "go" in the input, you can write a phrase(word) and
it will continue based no the statistics

# Emotional Neuron:
You type phrase, and it returns its score. Then it asks how
high it should be: the smaller the number(eben negative ones), the more 
negative the phrase, and vice versa. After you enter number(required to
be integer!), it updates the memory of word weights in know.json; by
enterirng "top"m you can see the top 5 of saddest and funnsit words
