import gradio as gr
from lmqg import TransformersQG

# keyword_extraction_model='biasedtextrank'
# VALID_METHODS = ['positionrank', 'textrank', 'biasedtextrank', 'positionrank', 'ner']
model_small = TransformersQG(language='ja', model='lmqg/mt5-small-jaquad-qg')
model_base = TransformersQG(language='ja', model='lmqg/mt5-base-jaquad-qg')
model_large = TransformersQG(language='ja', model='lmqg/mbart-large-cc25-jaquad-qg')

def generate(text, model_names, num_beams):
  print(num_beams)
  if model_names == 'mt5-small-jaquad-qg':
    question_answer_pairs = model_small.generate_qa(text, num_beams=num_beams)
    return question_answer_pairs
  if model_names == 'mt5-base-jaquad-qg':
    question_answer_pairs = model_base.generate_qa(text, num_beams=num_beams)
    return question_answer_pairs
  if model_names == 'mbart-large-cc25-jaquad-qg':
    question_answer_pairs = model_large.generate_qa(text, num_beams=num_beams)
    return question_answer_pairs

examples = [
  '「ぼっちざろっく」という漫画のあらすじを説明します。後藤ひとりは、ギターを愛する孤独な少女。 家で一人寂しく弾くだけの毎日でしたが、ひょんなことから伊地知虹夏が率いる「結束バンド」に加入することに。 人前での演奏に不慣れな後藤は、立派なバンドマンになれるのか！？ 全国のぼっちな少年少女に届ける、いま最高にアツい音楽漫画！！',
  'レオナルド・ダ・ビンチ作の婦人肖像画。 1503～06年頃フィレンツェで描かれたものと思われ，フランチェスコ・ダ・ジョコンドの依頼で彼の夫人を描いたものといわれる。そのため「ラ・ジョコンダ」とも呼ばれる。作品は未完成のままともいわれるが，ほのかな微笑を含んだ婦人の表情や，安らかな手の表現，背景は神秘性を深め公式的な肖像画の伝統に画期的な改革をもたらし，「モナ・リザの微笑」として世界に知られた。現在はルーブル美術館所蔵であるが，この絵の歴史的な経路には不明の点も多く，謎を深めている。 1974年日本に運ばれ，一般公開された。',
  'ルネサンス美術は、14世紀末から16世紀初頭にかけてイタリアを中心に広がった文化運動の一つであり、美術を中心に文学、建築、音楽などさまざまな分野で花開いた時期を指します。この時期のイタリアを代表する芸術家には、Leonardo da VinciやMichelangelo、Raphaelなどがいます。ルネサンス美術は、古代ローマやギリシアの文化を再評価し、それらを受け継ぎながらも、新しい表現方法を求める独自の美学を確立しました。その結果、自然を写実的に描くことが重視されるようになり、ヒューマニズム的で自然主義的な表現が普及しました。また、彫刻や装飾美術では、古代の美を踏襲しつつも、より自然的で個性的な表現が求められるようになりました。',
  '猫を飼う際には、以下の注意点があります。猫は独立した性格をもっているので、多少の放置は許されますが、基本的には毎日の飼育管理が必要です。猫のフードは、年齢や活動量、健康状態などによって異なるので、適切なフードを選ぶことが大切です。猫は毛をよくするので、毛を刈ることで毛が飛び散らないようにする必要があります。猫は自分で水を飲むことができるので、常に清潔で新鮮な水を用意することが大切です。猫は自分でトイレを掘ることができるので、トイレを用意してあげることが重要です。猫は非常に敏感で、ストレスを感じやすい動物です。そのため、家庭内での環境を安定させることが大切です。猫は基本的に外出を拒否する動物ですが、適度な散歩や遊びをすることで、ストレスを軽減させることができます。猫を飼う場合は、常に病院での予防接種や健康管理を行うことが大切です。猫を飼う場合は、猫が攻撃的になることもあるので、予め対処方法を知っておくことが重要です。猫を飼う場合は、周りの近所や近隣に猫を飼っている人がいる場合は、事前に相談をすることが大切です。',
  '主人公のハリー・ポッターは、幼いころに魔法使いの親戚であるダンブルドア一家に引き取られ、そこでは魔法界の隠れ家として知られるホグワーツ魔法魔術学校で魔法を学ぶことになります。ハリーは、自分が有能な魔法使いであることを知らずに育ちますが、それは、彼を巨大な悪を倒すための英雄とするためであることを知ることになります。それは、彼が小さい頃に、魔法界を支配しようとしている恐ろしい魔法使いであるヴォルデモートという人物によって、彼の両親を殺されたことが原因です。ヴォルデモートは、彼が最強の魔法使いであることを望んでおり、彼を倒すことができればその夢を叶えることができると考えています。ハリーは、ホグワーツで学んだ魔法を使い、ヴォルデモートを倒すために、魔法界の仲間たちとともに戦います。彼は、自分が有能な魔法使いであることを知ってから、多くの人々を救い、ヴォルデモートを倒すことに成功します。'
]

custom_css = 'footer {visibility: hidden} .gr-sample-textbox {overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}'
with gr.Blocks(css=custom_css, title="your title") as demo:
  gr.Markdown('# 問題自動生成')
  gr.Markdown('[lmqg](https://github.com/asahi417/lm-question-generation)を利用して文章から問題と回答を自動生成します')
  text = gr.Textbox(lines=5, placeholder="input here...",label='文章')
  model_names = gr.Radio(['mt5-small-jaquad-qg', 'mt5-base-jaquad-qg', 'mbart-large-cc25-jaquad-qg'], label='モデルの種類', value='mt5-small-jaquad-qg')
  num_beams = gr.Slider(1, 10, value=4,step=1,label='Number of Beam(degrees of explotaion at interface)')
  gr.Examples(examples, inputs=text)
  button = gr.Button('生成',variant='primary')
  outputs = gr.Dataframe(type='array')
  button.click(
    fn=generate,
    inputs=[text, model_names, num_beams],
    outputs=[outputs]
  )

demo.launch()
