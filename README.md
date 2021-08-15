# perspective

perspective is an API wrapper for Google's [Perspective API](http://www.perspectiveapi.com/)

## Installation

To install, use `pip install perspective`

## Usage

A simple example:

```python
from perspective import PerspectiveAPI
p = Perspective("API_KEY")
result = p.score("This is a comment")
print("Toxicity score: " + result["TOXICITY"])
```

More complex 
