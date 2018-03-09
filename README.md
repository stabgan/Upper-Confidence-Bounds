# Upper-Confidence-Bounds
I implemented the reinforcement learning based model Upper Confidence Bound in both Python and R

If we use to check if which ad is pleasing customers among many ads then we can use the reinforcement learning approach :
- Let we have <i>X</i> ads to display to a customer when he connects to Web
- Each time an user logs in we consider it an round
- At each round<i>n</i> we choose one ad to display to the user
- At each round n , ad gives reward Ri(n)is the superset of {0,1} : Ri(n) = 1 , if the user clicked on the ad and 0 if the user didn't clicked .
- Our goal is to minimize the total rewards we get over many rounds

Steps :




![down](https://scontent.fccu3-1.fna.fbcdn.net/v/t1.0-9/19113894_185190832228130_7660961285161249482_n.jpg?oh=bfc875486be07a2258539488f9f01e76&oe=5AE5626F)

# Comparison between UCB and Thompson Sampling :

![down](https://scontent.fccu3-1.fna.fbcdn.net/v/t1.0-9/26991750_185190595561487_5082930645105234791_n.jpg?oh=7f0d38a0627b7f0be633d7f334044210&oe=5AE2471B)
