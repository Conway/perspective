Getting Started
===============

.. contents:: Table of Contents


Installation
------------

The Perspective Python Wrapper can be installed using pip.

.. code-block:: bash

    pip install perspective

The latest version of this package can be installed using this command:

.. code-block:: bash

    pip install --upgrade https://github.com/conway/perspective/archive/master.zip

Acquiring an API Key
--------------------

Perspective is still in beta. API keys are available by request `here <http://www.perspectiveapi.com/>`_ (click on "Request API Access"). If your request is approved, you will receive a message by email from Google.

To get your API key once the request has been approved, navigate to the `Google API Console <https://console.developers.google.com/apis/>`_ and create a new project. Then go to the `Perspective Overview Page <https://console.developers.google.com/apis/api/commentanalyzer.googleapis.com/overview>`_ to enable the API. Finally, go to your project's `credential page <https://console.developers.google.com/apis/credentials>`_, click "Create credentials", and select "API key" from the dropdown menu. A popup will be shown containing your API key. Copy this, and don't share it with anyone.

Basic Usage
-----------

Using the API key you've acquired, it's simple to make a Perspective instance.

.. code-block:: python

   from perspective import Perspective

   perspective = Perspective("api_key") # replace with your actual key

Comments can be evaluated using Perspective.score, as demonstrated below.

.. code-block:: python

   from perspective import Perspective

   perspective = Perspective("api_key") # replace with your actual key
   comment_body = "text"
   comment = perspective.score(comment_body, tests=["TOXICITY"])
   print("Toxicity score: " + comment["TOXICITY"].score)
