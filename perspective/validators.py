from typing import Any
from languages import iso_639
import attribute_types


class Validators(object):
    @staticmethod
    def validate_comment_type(type: str) -> None:
        if type is None:
            return
        if type not in ('PLAIN_TEXT', 'HTML'):
            raise ValueError(f"{type} is not a recognized comment type. Valid types are 'PLAIN_TEXT' and 'HTML'.")

    @staticmethod
    def validate_context(context: attribute_types.CONTEXT) -> None:
        if context is None:
            return
        # iterate over list of dicts
        for entry in context:
            # iterate over keys in dict
            for key in entry:
                # validate keys
                if key not in ('text', 'type'):
                    error = f"{key} was listed as a key in context[{entry}], but is not recognized as a valid key."
                    error += " Valid keys are 'text' and 'type'."
                    raise ValueError(error)
            # if 'type' is provided, validate it's value
            if 'type' in entry and entry['type'] not in ('PLAIN_TEXT'):
                raise ValueError(f"{entry['type']} is not a valid context type. Valid types are 'PLAIN_TEXT'.")

    @staticmethod
    def validate_requested_attributes(requested_attributes: attribute_types.REQUESTED_ATTRIBUTES) -> None:
        if requested_attributes is None:
            raise TypeError("requested_attributes can not be None.")
        # iterate over listed keys
        for attribute in requested_attributes:
            # iterate over keys within each dict
            for key in requested_attributes[attribute]:
                if key == 'scoreType':
                    if type(requested_attributes[attribute][key]) is not str:
                        error = f"requested_attributes.{attribute}.scoreType must be a string."
                        error += f"It currently is a(n) {type(requested_attributes[attribute][key])}."
                        raise TypeError(error)
                    elif requested_attributes[attribute][key] != "PROBABILITY":
                        error = f"PROBABILITY is the only accepted type for requested_attributes.{attribute}.scoreType."
                        raise ValueError(error)
                elif key == 'scoreThreshold':
                    if type(requested_attributes[attribute][key]) is not float:
                        error = f"requested_attributes.{attribute}.scoreThreshold must be a float."
                        error += f" It currently is a(n) {type(requested_attributes[attribute][key])}."
                        raise TypeError(error)
                    elif requested_attributes[attribute][key] > 1 or requested_attributes[attribute][key] < 0:
                        error = f"requested_attributes.{attribute}.scoreThreshold must be in the range [0, 1]."
                        raise ValueError(error)
                elif key not in ('scoreType', 'scoreThreshold'):
                    error = f"Invalid key '{key}' listed in requested_attributes.{attribute}."
                    error += " Valid keys are 'scoreType' and 'scoreThreshold'."
                    raise ValueError(error)

    @staticmethod
    def validate_type(attribute: Any, attr_type: Any, variable_name: str, can_be_none: bool = True) -> None:
        if attribute is None:
            if can_be_none:
                return
            else:
                raise TypeError(f"{variable_name} cannot be None.")
        if type(attribute) is not attr_type:
            raise TypeError(f"{variable_name} must be a {attr_type.__name__}.")

    @staticmethod
    def validate_languages(languages: attribute_types.LANGUAGES) -> None:
        if languages is None:
            return
        for language in languages:
            if language not in iso_639:
                raise ValueError(f"{language} is not a valid ISO 639-1 language.")

    @staticmethod
    def validate_attribute_scores(attribute_scores: attribute_types.ATTRIBUTE_SCORES) -> None:
        # attributeScores
        for group in attribute_scores:
            # attributeScores.<score_type>
            for key in attribute_scores[group]:
                if key == "summaryScore":
                    for inner_key in attribute_scores[group][key]:
                        # attributeScores.<score_type>.summaryScore.value
                        if inner_key == "value" and type(attribute_scores[group][key][inner_key]) is not float:
                            raise TypeError(f"attribute_scores.{group}.summaryScore.value must be a float.")
                        # attributeScores.<score_type>.summaryScore.type
                        elif inner_key == "type" and type(attribute_scores[group][key][inner_key]) is not str:
                            raise TypeError(f"attribute_scores.{group}.summaryScore.type must be a string.")
                elif key == "spanScores":
                    for idx in range(len(attribute_scores[group][key])):
                        for inner_key in attribute_scores[group][key][idx]:
                            # attributeScores.<score_type>.spanScores.(begin|end)
                            if inner_key in ("begin", "end") and type(attribute_scores[group][key][idx][inner_key]) is not int:
                                raise TypeError(f"attribute_scores.{group}.spanScores[{idx}].{inner_key} must be a int.")
                            # attributeScores.<score_type>.spanScores.score
                            elif inner_key == "score":
                                for innermost_key in attribute_scores[group][key][idx][inner_key]:
                                    value = attribute_scores[group][key][idx][inner_key][innermost_key]
                                    path = f"attribute_scores.{group}.spanScores[{idx}].score"
                                    # attributeScores.<score_type>.spanScores.score.value
                                    if innermost_key == "value":
                                        if type(value) is not float:
                                            error = f"{path}.value must be a float."
                                            raise TypeError(error)
                                        elif value > 1.0 or value < 0.0:
                                            error = f"{path}.value not in [0,1]."
                                            raise ValueError(error)
                                    # attributeScores.<score_type>.spanScores.type
                                    elif innermost_key == "type" and type(value) is not str:
                                        error = f"{path}.type must be a string."
                                        raise TypeError(error)
                                    elif innermost_key not in ('value', 'type'):
                                        error = f"Invalid key at {path}.{innermost_key}."
                                        raise ValueError(error)
                else:
                    raise ValueError(f"{key} is an invalid key in attribute_scores.{group}.")
