from perspective import PerspectiveAPI
import unittest
import uuid
import os


class PerspectiveAPITest(unittest.TestCase):
    def setUp(self):
        self.perspective = PerspectiveAPI(os.environ.get("PERSPECTIVE_API_KEY"))

    def test_analyze_comment_bare_minimum(self):
        result = self.perspective.analyze_comment("you're stupid")
        self.assertIsNotNone(result)

    def test_analyze_comment_all_fields(self):
        result = self.perspective.analyze_comment("you are a dummy",
                                                  validate=True,
                                                  comment_type="PLAIN_TEXT",
                                                  context=[{"text": "why are you this way", "type": "PLAIN_TEXT"}],
                                                  requested_attributes={"TOXICITY": {}},
                                                  span_annotations=True,
                                                  languages=["en"],
                                                  do_not_store=False,
                                                  client_token=str(uuid.uuid4()),
                                                  session_id=str(uuid.uuid4()),
                                                  community_id="github.com/conway/perspective testing")
        self.assertIsNotNone(result)

    def test_score(self):
        result = self.perspective.score("you look funny")
        self.assertIsNotNone(result)
