pip install ginza pytextrank lmqg psutil

python -m spacy download ja_core_news_sm


curl -XPOST localhost:3000/question_generation -F language='ja' -F input_text='Kiroroは玉城千春中心に楽曲制作を行っているが、結成したきっかけも、地元有線でリクエスト殺到、卒業記念制作CDがローカルCMに採用されて有線にリクエスト殺到してインディーズチャート一位になってデビューするのも全部金城さんが玉城さんを説得したって聞いたことがある。'

uvicorn app:app --reload --host 0.0.0.0 --port 3000

curl -XPOST -H "Content-Type: application/json" -d '@params.json' localhost:3000/question_generation


qg-ae
問題と回答

qg
文章と問題を
