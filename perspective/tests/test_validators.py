from perspective.validators import Validators
import unittest


class ValidatorsTest(unittest.TestCase):
    # Validators.validate_comment_type
    def test_validate_comment_type_plain_text(self):
        self.assertIsNone(Validators.validate_comment_type("PLAIN_TEXT"))

    def test_validate_comment_type_html(self):
        self.assertIsNone(Validators.validate_comment_type("HTML"))

    def test_validate_comment_type_none(self):
        self.assertIsNone(Validators.validate_comment_type(None))

    def test_validate_comment_type_invalid(self):
        with self.assertRaises(ValueError):
            Validators.validate_comment_type("ABCD")

    # Validators.validate_context
    def test_validate_context_none(self):
        self.assertIsNone(Validators.validate_context(None))

    def test_validate_context_empty_list(self):
        self.assertIsNone(Validators.validate_context([]))

    def test_validate_context_one_entry(self):
        context = [{"text": "abc", "type": "PLAIN_TEXT"}]
        self.assertIsNone(Validators.validate_context(context))

    def test_validate_context_invalid_type(self):
        context = [{"text": "abc", "type": "NOT_REAL"}]
        with self.assertRaises(ValueError):
            Validators.validate_context(context)

    def test_validate_context_multiple_entries(self):
        context = [{"text": "abc", "type": "PLAIN_TEXT"}, {"text": "def"}]
        self.assertIsNone(Validators.validate_context(context))

    def test_validate_context_invalid_key(self):
        context = [{"abc": "text", "type": "PLAIN_TEXT"}]
        with self.assertRaises(ValueError):
            Validators.validate_context(context)

    def test_validate_context_mixed_validity(self):
        context = [{"text": "abc", "type": "PLAIN_TEXT"}, {1: 2}]
        with self.assertRaises(ValueError):
            Validators.validate_context(context)

    # Validators.validate_requested_attributes
    def test_validate_requested_attributes_single(self):
        attributes = {"string": {"scoreType": "PROBABILITY", "scoreThreshold": 0.5}}
        self.assertIsNone(Validators.validate_requested_attributes(attributes))

    def test_validate_requested_attributes_multiple(self):
        attributes = {"string": {"scoreType": "PROBABILITY", "scoreThreshold": 0.5},
                      "abcdef": {"scoreType": "PROBABILITY", "scoreThreshold": 0.6}}
        self.assertIsNone(Validators.validate_requested_attributes(attributes))

    def test_validate_requested_attributes_invalid_score_type_value(self):
        attributes = {"string": {"scoreType": "NOT_REAL", "scoreThreshold": 0.5}}
        with self.assertRaises(ValueError):
            Validators.validate_requested_attributes(attributes)

    def test_validate_requested_attributes_invalid_score_type_type(self):
        attributes = {"string": {"scoreType": False, "scoreThreshold": 0.5}}
        with self.assertRaises(TypeError):
            Validators.validate_requested_attributes(attributes)

    def test_validate_requested_attributes_invalid_score_threshold_type(self):
        attributes = {"string": {"scoreType": "PROBABILITY", "scoreThreshold": "6"}}
        with self.assertRaises(TypeError):
            Validators.validate_requested_attributes(attributes)

    def test_validate_requested_attributes_invalid_score_threshold_too_high(self):
        attributes = {"string": {"scoreType": "PROBABILITY", "scoreThreshold": 1.001}}
        with self.assertRaises(ValueError):
            Validators.validate_requested_attributes(attributes)

    def test_validate_requested_attributes_invalid_score_threshold_too_low(self):
        attributes = {"string": {"scoreType": "PROBABILITY", "scoreThreshold": -0.001}}
        with self.assertRaises(ValueError):
            Validators.validate_requested_attributes(attributes)

    def test_validate_requested_attributes_invalid_key(self):
        attributes = {"string": {"scoreType": "PROBABILITY", "scoreThreshold": 0.5, "nothing": 2}}
        with self.assertRaises(ValueError):
            Validators.validate_requested_attributes(attributes)

    def test_validate_requested_attributes_none(self):
        with self.assertRaises(TypeError):
            Validators.validate_requested_attributes(None)

    # Validators.validate_type
    def test_validate_type_str(self):
        self.assertIsNone(Validators.validate_type("abc", str, "test"))

    def test_validate_type_str_invalid(self):
        with self.assertRaises(TypeError):
            Validators.validate_type(1, str, "test")

    def test_validate_type_none_disallowed(self):
        with self.assertRaises(TypeError):
            Validators.validate_type(None, str, "test", False)

    def test_validate_type_none_allowed(self):
        self.assertIsNone(Validators.validate_type(None, str, "test", True))

    # Validators.validate_languages
    def test_validate_languages_real(self):
        self.assertIsNone(Validators.validate_languages(["en", "es"]))

    def test_validate_languages_none(self):
        self.assertIsNone(Validators.validate_languages(None))

    def test_validate_languages_empty_list(self):
        self.assertIsNone(Validators.validate_languages([]))

    def test_validate_languages_fake(self):
        with self.assertRaises(ValueError):
            Validators.validate_languages(["xy", "zy"])

    # Validators.validate_attribute_scores
    def test_validate_attribute_scores_full(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": 2, "score": {"value": 1.0, "type": "PROBABILITY"}}]}}
        self.assertIsNone(Validators.validate_attribute_scores(attribute_scores))

    def test_validate_attribute_scores_only_summary(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"}}}
        self.assertIsNone(Validators.validate_attribute_scores(attribute_scores))

    def test_validate_attribute_scores_multiple(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": 2, "score": {"value": 1.0, "type": "PROBABILITY"}}]}}
        attribute_scores["key2"] = {"summaryScore": {"value": 0.3, "type": "PROBABILITY"},
                                    "spanScores": [{"begin": 6, "end": 10, "score": {"value": 0.2, "type": "PROBABILITY"}}]}
        self.assertIsNone(Validators.validate_attribute_scores(attribute_scores))

    def test_validate_attribute_scores_invalid_summary_score_value_type(self):
        attribute_scores = {"key": {"summaryScore": {"value": True, "type": "PROBABILITY"}}}
        with self.assertRaises(TypeError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_span_score_begin_type(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": True, "end": 2, "score": {"value": 1.0, "type": "PROBABILITY"}}]}}
        with self.assertRaises(TypeError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_span_score_end_type(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": False, "score": {"value": 1.0, "type": "PROBABILITY"}}]}}
        with self.assertRaises(TypeError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_span_score_value_type(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": 2, "score": {"value": True, "type": "PROBABILITY"}}]}}
        with self.assertRaises(TypeError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_span_score_value_bounds_high(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": 2, "score": {"value": 1.01, "type": "PROBABILITY"}}]}}
        with self.assertRaises(ValueError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_span_score_value_bounds_low(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": 2, "score": {"value": -0.01, "type": "PROBABILITY"}}]}}
        with self.assertRaises(ValueError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_span_score_type_type(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": 2, "score": {"value": 0.5, "type": True}}]}}
        with self.assertRaises(TypeError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_span_score_invalid_key(self):
        attribute_scores = {"key": {"summaryScore": {"value": 0.5, "type": "PROBABILITY"},
                            "spanScores": [{"begin": 1, "end": 2, "score": {"invalid": 0.5, "fake": "PROBABILITY"}}]}}
        with self.assertRaises(ValueError):
            Validators.validate_attribute_scores(attribute_scores)

    def test_validate_attribute_scores_invalid_key(self):
        attribute_scores = {"key": {"other": {"value": 0.5, "type": "PROBABILITY"}}}
        with self.assertRaises(ValueError):
            Validators.validate_attribute_scores(attribute_scores)
