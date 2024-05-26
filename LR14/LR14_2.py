import requests

prompt = {
    "modelUri": "gpt://b1gev6kshr38q7ic83em/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Найди ошибки в тексте и исправь их"
        },
        {
            "role": "user",
            "text": "Ламинат подойдет для укладке на кухне или в детской комнате – он не боиться влаги и механических повреждений благодаря защитному слою из облицованных меламиновых пленок толщиной 0,2 мм и обработанным воском замкам."
        }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVNwk7qd42FkS8hStBsT1uslpgmWp-kIEdvDhub"
}


response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result)
