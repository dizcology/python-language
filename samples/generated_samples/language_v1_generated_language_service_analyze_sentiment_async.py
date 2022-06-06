# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for AnalyzeSentiment
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-language


# [START language_v1_generated_LanguageService_AnalyzeSentiment_async]
from google.cloud import language_v1


async def sample_analyze_sentiment():
    # Create a client
    client = language_v1.LanguageServiceAsyncClient()

    # Initialize request argument(s)
    document = language_v1.Document()
    document.content = "content_value"

    request = language_v1.AnalyzeSentimentRequest(
        document=document,
    )

    # Make the request
    response = await client.analyze_sentiment(request=request)

    # Handle the response
    print(response)

# [END language_v1_generated_LanguageService_AnalyzeSentiment_async]