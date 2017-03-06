#perspective

perspective is an API wrapper for Google's [Perspective API](http://www.perspectiveapi.com/)

##Installation

To install, use `pip install perspective`

##Usage

A simple example:

```python
from perspective import Perspective
p = Perspective("API_KEY")
comment = p.score("This is a comment", tests=["TOXICITY"])
print("Toxicity score: " + comment["TOXICITY"].score)
```

##Todo

1. Full documentation
2. Comment splitting for comments >3000 characters
3. HTML stripping option (until the API supports this natively)
4. Tests