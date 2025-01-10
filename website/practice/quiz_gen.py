from typing import List, Dict, Union
from pydantic import BaseModel
import openai
import os


class Choice(BaseModel):
    value: str
    text: str

class Question(BaseModel):
    number: int
    type: str
    paragraphRefs: list[int]
    instructions: str
    stem: str
    choices: list[Choice]
    correctAnswer: list[str]

class Paragraph(BaseModel):
    id: int
    text: str

class Passage(BaseModel):
    title: str
    paragraphs: list[Paragraph]
    questions: list[Question]

class CompletedReadingQuiz(BaseModel):
    passages: list[Passage]


class QuizGeneration:
    def __init__(self):
        self.schema = CompletedReadingQuiz
        self.client = openai.OpenAI(
            api_key="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")

    def generate_response(self):
        system_prompt = """\
        You are an assistant specialized in generating TOEFL Reading Part.  

        Here is how the TOEFL Part must look like: 
        {
          "passages": [
            {
              "title": "Flowers to Fruit",
              "paragraphs": [
                { "id": 1, "text": "Botanically, a fruit is an organ of a plant that contains and protects the seeds of the plant as they grow and often helps them to be dispersed.\nThis broad definition of fruit includes not only produce like apples, oranges, and grapes, but also many vegetables like tomatoes and cucumbers as well as the pods of legumes and the hulls of grain." },
                { "id": 2, "text": "Fruits are classified in many ways, but the simplest distinction is made between fleshy fruits and dry fruits. Fleshy fruits are composed of moisture-rich cells and they are often sweet and juicy, although there are exceptions like oil-rich olives and avocados. Conversely, dry fruits are composed of dry, dead cells and are generally not edible although the seeds they contain often are." },
                { "id": 3, "text": "Dry fruits are further divided into two categories; those that split open when they are ripe and those that do not. Within these three broad categories, there are many subcategories of specialized fruit types." },
                { "id": 4, "text": "Regardless of their categorization, all fruits began their existence as flowers. Flowers play a central role in the life cycle of most plants as they contain reproductive structures. The majority of flowering plants produce \"perfect\" flowers that are hermaphroditic—they contain both male and female reproductive structures. Other plants produce \"imperfect\" flowers that contain either male or female structures. When a plant species produces imperfect flowers, it may produce both distinctly male and female flowers on the same individual plant, or different plants will be exclusively male or exclusively female." },
                { "id": 5, "text": "The female structures of a flower are found in the pistil at the center, which includes the ovary at the base, the long stalk called a style that grows up from the ovary, and the stigma at the top of the style. Surrounding the pistil are the male structures called stamens. They are thin stalks with pollen producing anthers at their tops. In order for a plant to reproduce, pollen must be moved from the anthers to the stigma. The transfer of pollen between the two structures is usually accomplished via organisms that visit the flower, like bees, or by the wind. Once pollen reaches the stigma, it travels down the style to the ovary, where it fertilizes an ovule. With imperfect flowers, the transfer must take place between different flowers, but perfect flowers may be fertilized by their own pollen or pollen from other flowers. Once a flower is fertilized, its future seeds begin to form, and the ovary begins to grow into a protective fruit." },
                { "id": 6, "text": "Flowers share the same basic internal structure, but their subtle differences cause them to produce very different fruit. Fleshy fruits typically fall into one of four categories. Drupes such as peaches have a single seed with an extremely hard shell called a stone that is surrounded by a thick layer of flesh. Berries such as tomatoes have many seeds without a protective stone. Aggregate fruits such as raspberries develop from a flower with many pistils that fuse into a dense cluster of smaller fruits. Multiple fruits such as pineapples are formed by the fusion of several grouped flowers that eventually merge into one fruit. For example, a strawberry is called an accessory fruit because the juicy portion that is eaten is actually a part of the stem, while the genuine fruits are the small seeds that dot its surface.\nThe fruits that farmers raise today are vastly different from the original wild plants as thousands of years of selective breeding have substantially altered their size, sweetness, and nutritional value. Scientists have found samples of maize in Central and South America that revealed."},
                { "id": 7, "text": "The original plants look much like modern grass with a single row of small seeds on the stalk, unlike the corn cobs grown today. Paintings from centuries ago have shown that many fleshy fruits are quite different today as well. For example, a 400 year old still-life painting of fruit shows that watermelons used to be mostly bitter rind with pockets of edible red flesh around large seeds deep inside, while modern watermelons are predominately juicy red flesh and some are nearly seedless."}
              ],
              "questions": [
                {
                  "number": 1,
                  "type": "single-choice",
                  "paragraphRefs": [1],
                  "instructions": "According to paragraph 1...",
                  "stem": "What is true of seeds that are present in dry fruits?",
                  "choices": [
                    { "value": "A", "text": "They are divided into two types based on the fruit they are in." },
                    { "value": "B", "text": "They are mostly suitable for human consumption." },
                    { "value": "C", "text": "They are made up of moisture-rich cells." },
                    { "value": "D", "text": "They are typically present inside pods and hulls." }
                  ],
                  "correctAnswer": "D"
                },
                {
                  "number": 2,
                  "type": "single-choice",
                  "paragraphRefs": [2],
                  "instructions": "According to paragraph 2...",
                  "stem": "Which of the following is possible in plants that produce imperfect flowers?",
                  "choices": [
                    { "value": "A", "text": "Presence of both sexes in a single flower" },
                    { "value": "B", "text": "Presence of only male flowers" },
                    { "value": "C", "text": "Presence of both male and female reproductive structures" },
                    { "value": "D", "text": "Production of fruit with seeds" }
                  ],
                  "correctAnswer": "B"
                },
                {
                  "number": 3,
                  "type": "single-choice",
                  "paragraphRefs": [3],
                  "instructions": "According to paragraph 3...",
                  "stem": "Which of the following are mentioned as parts of the female reproductive structures?",
                  "choices": [
                    { "value": "A", "text": "stamens and anthers" },
                    { "value": "B", "text": "stigma and ovary" },
                    { "value": "C", "text": "stigma and anthers" },
                    { "value": "D", "text": "pistil and stamens" }
                  ],
                  "correctAnswer": "B"
                },
                {
                  "number": 4,
                  "type": "single-choice",
                  "paragraphRefs": [],
                  "instructions": "The word \"accomplished\" in the passage is closest in meaning to",
                  "stem": "The word \"accomplished\" in the passage is closest in meaning to",
                  "choices": [
                    { "value": "A", "text": "initiated" },
                    { "value": "B", "text": "supported" },
                    { "value": "C", "text": "achieved" },
                    { "value": "D", "text": "disrupted" }
                  ],
                  "correctAnswer": "C"
                },
                {
                  "number": 5,
                  "type": "single-choice",
                  "paragraphRefs": [3],
                  "stem": "According to paragraph 3, one advantage perfect flowers have over imperfect flowers is that...",
                  "choices": [
                    { "value": "A", "text": "they do not need pollen from other flowers to reproduce." },
                    { "value": "B", "text": "they can reproduce without the help of bees or the wind." },
                    { "value": "C", "text": "it is easier for the pollen to reach the stigma." },
                    { "value": "D", "text": "they are able to produce seeds faster than imperfect flowers." }
                  ],
                  "correctAnswer": "C"
                },
                {
                  "number": 6,
                  "type": "single-choice",
                  "paragraphRefs": [4],
                  "stem": "What is the author's primary purpose in paragraph 4?",
                  "choices": [
                    { "value": "A", "text": "To compare genuine fruits with accessory fruits" },
                    { "value": "B", "text": "To point out strengths and weaknesses of different fruit structures" },
                    { "value": "C", "text": "To show the importance of fruit structures in plant reproduction" },
                    { "value": "D", "text": "To illustrate how flower structures produce different fruits" }
                  ],
                  "correctAnswer": "D"
                },
                {
                  "number": 7,
                  "type": "single-choice",
                  "paragraphRefs": [5],
                  "stem": "Which of the sentences below best expresses the essential information...",
                  "choices": [
                    { "value": "A", "text": "Modern fruits are bigger, tastier, and have more nutritional value..." },
                    { "value": "B", "text": "Fruits today are very different from wild plants in size..." },
                    { "value": "C", "text": "A long period of selective breeding has caused significant variation..." },
                    { "value": "D", "text": "Selective breeding led to extinction of wild original plants..." }
                  ],
                  "correctAnswer": "C"
                },
                {
                  "number": 8,
                  "type": "single-choice",
                  "paragraphRefs": [5],
                  "stem": "It can be inferred from paragraph 5 that compared to the original plants, modern maize...",
                  "choices": [
                    { "value": "A", "text": "is much larger." },
                    { "value": "B", "text": "has a brighter color." },
                    { "value": "C", "text": "looks a lot more like grass." },
                    { "value": "D", "text": "has fewer seeds." }
                  ],
                  "correctAnswer": "A"
                },
                {
                  "number": 9,
                  "type": "single-choice",
                  "paragraphRefs": [],
                  "stem": "Look at the squares [®] that indicate where the following sentence can be added...",
                  "choices": [
                    { "value": "A", "text": "1st" },
                    { "value": "B", "text": "2nd" },
                    { "value": "C", "text": "3rd" },
                    { "value": "D", "text": "4th" }
                  ],
                  "correctAnswer": "C"
                },
                {
                  "number": 10,
                  "type": "multiple-select",
                  "paragraphRefs": [],
                  "instructions": "<strong>Directions:</strong> An introductory sentence for a summary is provided below...",
                  "stem": "Fruits are mainly used by plants to protect seeds and can be divided...",
                  "choices": [
                    { "value": "A", "text": "Fruits can be classified into many different types depending on shape." },
                    { "value": "B", "text": "Flowers play an important role in the life cycle of plants..." },
                    { "value": "C", "text": "Flowers that are male do not possess female reproductive structures." },
                    { "value": "D", "text": "The structure of a fruit can differ significantly due to minor variations in flower structure." }
                  ],
                  "correctAnswer": ["B","D"]
                }
              ]
            },
            {
              "title": "Seeds to Sprouts",
              "paragraphs": [
                { "id": 1, "text": "Seeds are the embryonic form of a new plant, enclosed in a protective covering..." },
                { "id": 2, "text": "Germination requires specific environmental conditions like moisture and temperature..." },
                { "id": 3, "text": "Dormancy can last for weeks, months, or even years, ensuring seeds remain viable..." },
                { "id": 4, "text": "Some seeds have specialized adaptations such as hooks or wings to aid in dispersal..." },
                { "id": 5, "text": "Once a seed germinates, it begins to develop roots, shoots, and leaves..." }
              ],
              "questions": [
                {
                  "number": 1,
                  "type": "single-choice",
                  "paragraphRefs": [1],
                  "stem": "According to paragraph 1, what is the primary role of the seed coat?",
                  "choices": [
                    { "value": "A", "text": "To attract pollinators" },
                    { "value": "B", "text": "To protect the embryonic plant" },
                    { "value": "C", "text": "To store essential nutrients" },
                    { "value": "D", "text": "To reduce water intake" }
                  ],
                  "correctAnswer": "B"
                },
                {
                  "number": 2,
                  "type": "single-choice",
                  "paragraphRefs": [2],
                  "stem": "Which of the following environmental conditions is mentioned as crucial for seed germination?",
                  "choices": [
                    { "value": "A", "text": "High humidity and low light" },
                    { "value": "B", "text": "Moisture and appropriate temperature" },
                    { "value": "C", "text": "Direct sunlight and nutrient-rich soil" },
                    { "value": "D", "text": "A constant supply of fertilizer" }
                  ],
                  "correctAnswer": "B"
                },
                {
                  "number": 3,
                  "type": "single-choice",
                  "paragraphRefs": [3],
                  "stem": "According to paragraph 3, dormancy helps seeds by...",
                  "choices": [
                    { "value": "A", "text": "allowing them to germinate only during the most favorable season." },
                    { "value": "B", "text": "ensuring they never germinate if conditions are harsh." },
                    { "value": "C", "text": "producing chemicals that deter predators." },
                    { "value": "D", "text": "attracting animals that can disperse them widely." }
                  ],
                  "correctAnswer": "A"
                },
                {
                  "number": 4,
                  "type": "single-choice",
                  "paragraphRefs": [4],
                  "stem": "Which of the following seed adaptations is mentioned to aid in dispersal?",
                  "choices": [
                    { "value": "A", "text": "Brightly colored seed coats" },
                    { "value": "B", "text": "Sticky surfaces that adhere to animals" },
                    { "value": "C", "text": "Hooks or wings" },
                    { "value": "D", "text": "Ability to float on water" }
                  ],
                  "correctAnswer": "C"
                },
                {
                  "number": 5,
                  "type": "single-choice",
                  "paragraphRefs": [5],
                  "stem": "What is the first major structure to emerge from a germinating seed?",
                  "choices": [
                    { "value": "A", "text": "The shoot" },
                    { "value": "B", "text": "The leaf" },
                    { "value": "C", "text": "The flower" },
                    { "value": "D", "text": "The root" }
                  ],
                  "correctAnswer": "D"
                },
                {
                  "number": 6,
                  "type": "single-choice",
                  "paragraphRefs": [1],
                  "stem": "The author mentions that some seeds have extra layers or thick seed coats. Why?",
                  "choices": [
                    { "value": "A", "text": "To provide additional nutrition to the embryo" },
                    { "value": "B", "text": "To protect from extreme weather and digestion by animals" },
                    { "value": "C", "text": "To reduce the need for sunlight" },
                    { "value": "D", "text": "To ensure faster germination" }
                  ],
                  "correctAnswer": "B"
                },
                {
                  "number": 7,
                  "type": "single-choice",
                  "paragraphRefs": [2],
                  "stem": "What can be inferred about seeds that germinate in the absence of sufficient moisture?",
                  "choices": [
                    { "value": "A", "text": "They quickly adapt by storing water internally." },
                    { "value": "B", "text": "They enter a second stage of dormancy to protect themselves." },
                    { "value": "C", "text": "They are less likely to survive to maturity." },
                    { "value": "D", "text": "They produce additional layers of seed coat." }
                  ],
                  "correctAnswer": "C"
                },
                {
                  "number": 8,
                  "type": "single-choice",
                  "paragraphRefs": [],
                  "stem": "Which of the following best defines 'dormancy' based on the passage?",
                  "choices": [
                    { "value": "A", "text": "A permanent state of inactivity" },
                    { "value": "B", "text": "A delay in germination until conditions are favorable" },
                    { "value": "C", "text": "An immediate response to poor soil nutrient levels" },
                    { "value": "D", "text": "A form of rapid seed growth under any conditions" }
                  ],
                  "correctAnswer": "B"
                },
                {
                  "number": 9,
                  "type": "single-choice",
                  "paragraphRefs": [4],
                  "stem": "Which seeds would likely have the easiest time dispersing in a windy environment?",
                  "choices": [
                    { "value": "A", "text": "Seeds with hooks" },
                    { "value": "B", "text": "Seeds that rely on animals to open them" },
                    { "value": "C", "text": "Seeds with wings" },
                    { "value": "D", "text": "Seeds that remain dormant for years" }
                  ],
                  "correctAnswer": "C"
                },
                {
                  "number": 10,
                  "type": "multiple-select",
                  "paragraphRefs": [],
                  "instructions": "Select the THREE answer choices that best complete the summary...",
                  "stem": "Seeds have several key requirements and adaptations that ensure their survival and successful germination.",
                  "choices": [
                    { "value": "A", "text": "Seeds that germinate immediately under any conditions have the highest survival rate." },
                    { "value": "B", "text": "Dormancy allows seeds to wait until the environment is favorable for growth." },
                    { "value": "C", "text": "Moisture and temperature play a crucial role in initiating germination." },
                    { "value": "D", "text": "Seeds may develop specialized structures like hooks or wings to spread out." },
                    { "value": "E", "text": "Most seeds cannot survive freezing temperatures." }
                  ],
                  "correctAnswer": ["B","C","D"]
                }
              ]
            }
          ]
        }
        Use double quotes only for dictionary keys and values.

        """
        human_prompt = f""" Generate TOEFL Reading Part. 1 passage and 10 questions to that passage."""

        response = self.client.beta.chat.completions.parse(
            model = "gpt-4o-2024-08-06",
            messages=[
                {"role":"system", "content": system_prompt},
                {"role":"user", "content": human_prompt}
            ],
            max_tokens=10000,
            response_format=CompletedReadingQuiz,
        )

        return response.choices[0].message.parsed