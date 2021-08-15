from typing import Dict, List, Literal, Optional, Union

COMMENT_TYPE = Optional[Literal['PLAIN_TEXT', 'HTML']]
CONTEXT = Optional[List[Dict[Literal["text", "type"], str]]]
REQUESTED_ATTRIBUTES = Optional[Dict[str, Dict[Literal["scoreType", "scoreThreshold"], Union[str, float]]]]
LANGUAGES = Optional[List[str]]
SUMMARY_SCORE = Union[Dict[Literal["value"], float], Dict[Literal["type"], str]]
SPAN_SCORE_POSITION = Dict[Literal["begin", "end"], int]
SPAN_SCORE_VALUE = Dict[Literal["score"], Union[Dict[Literal["value"], float], Dict[Literal["type"], str]]]
SPAN_SCORES = List[Union[SPAN_SCORE_POSITION, SPAN_SCORE_VALUE]]
ATTRIBUTE_SCORES = Dict[str, Union[SUMMARY_SCORE, SPAN_SCORES]]
