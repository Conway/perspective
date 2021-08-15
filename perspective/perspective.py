from typing import List, Optional
from validators import Validators
from api_client import APIClient
import attribute_types


class PerspectiveAPI(object):
    def __init__(self, api_key: str, validator: object = Validators) -> None:
        self.api_client = APIClient(api_key)
        self.validator = validator

    def analyze_comment(self,
                        text: str,
                        validate: bool = True,
                        comment_type: attribute_types.COMMENT_TYPE = None,
                        context: attribute_types.CONTEXT = None,
                        requested_attributes: attribute_types.REQUESTED_ATTRIBUTES = {"TOXICITY": {}},
                        span_annotations: Optional[bool] = False,
                        languages: attribute_types.LANGUAGES = None,
                        do_not_store: Optional[bool] = False,
                        client_token: Optional[str] = None,
                        session_id: Optional[str] = None,
                        community_id: Optional[str] = None
                        ) -> dict:
        # validate if requested
        if validate:
            self.validator.validate_type(text, str, "text", False)
            self.validator.validate_comment_type(comment_type)
            self.validator.validate_context(context)
            self.validator.validate_requested_attributes(requested_attributes)
            self.validator.validate_type(span_annotations, bool, "span_annotations")
            self.validator.validate_languages(languages)
            self.validator.validate_type(do_not_store, bool, "do_not_store")
            self.validator.validate_type(client_token, str, "client_token")
            self.validator.validate_type(session_id, str, "session_id")
            self.validator.validate_type(community_id, str, "community_id")

        # assemble request data
        body = {'comment': {'text': text}, 'requestedAttributes': requested_attributes}

        if comment_type:
            body['comment']['type'] = comment_type

        if context:
            body['context'] = {'entries': context}

        if span_annotations:
            body['spanAnnotations'] = span_annotations

        if languages:
            body['languages'] = languages

        if do_not_store:
            body['doNotStore'] = do_not_store

        if client_token:
            body['clientToken'] = client_token

        if session_id:
            body['sessionId'] = session_id

        if community_id:
            body['communityId'] = community_id

        return self.api_client.request(body, "comments:analyze")

    def suggest_score(self,
                      text: str,
                      attribute_scores: attribute_types.ATTRIBUTE_SCORES,
                      validate: bool = True,
                      comment_type: attribute_types.COMMENT_TYPE = None,
                      context: attribute_types.CONTEXT = None,
                      languages: attribute_types.LANGUAGES = None,
                      client_token: Optional[str] = None,
                      community_id: Optional[str] = None
                      ) -> dict:
        # validate if requested
        if validate:
            self.validator.validate_type(text, str, "text", False)
            self.validator.validate_attribute_scores(attribute_scores)
            self.validator.validate_comment_type(comment_type)
            self.validator.validate_context(context)
            self.validator.validate_languages(languages)
            self.validator.validate_type(client_token, str, "client_token")
            self.validator.validate_type(community_id, str, "community_id")

        # assemble request data
        body = {'comment': {'text': text}, 'attributeScores': attribute_scores}

        if comment_type:
            body['comment']['type'] = comment_type

        if context:
            body['context'] = {'entries': context}

        if languages:
            body['languages'] = languages

        if client_token:
            body['clientToken'] = client_token

        if community_id:
            body['communityId'] = community_id

        return self.api_client.request(body, "comments:suggestscore")

    def score(self,
              text: str,
              tests: List[str] = ["TOXICITY"]
              ) -> dict:
        requested_attributes = {tests[i]: {} for i in range(len(tests))}
        result = self.analyze_comment(text, requested_attributes=requested_attributes)
        output = dict()
        for key in result["attributeScores"]:
            output[key] = result["attributeScores"][key]["summaryScore"]["value"]
        return output
