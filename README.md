# perspective

perspective is an API wrapper for Google's [Perspective API](http://www.perspectiveapi.com/)

## documentation

Some documentation is available [on readthedocs](http://perspective.readthedocs.io/en/latest/).

## Installation

To install, use `pip install perspective`

## Usage

A simple example:

```python
from perspective import Perspective
p = Perspective("API_KEY")
comment = p.score("This is a comment", tests=["TOXICITY"])
print("Toxicity score: " + comment["TOXICITY"].score)
```
