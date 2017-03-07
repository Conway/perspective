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
4. Improve unittests
5. Add support for context
6. Format code to meet PEP-8
7. Add support for "suggest score"