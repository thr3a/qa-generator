from lmqg import TransformersQG

model = TransformersQG(language='ja', model='lmqg/mt5-small-jaquad-qg')
# model = TransformersQG(language='ja', model='lmqg/mt5-base-jaquad-qg', max_length=100)
# model = TransformersQG(language='ja', model='lmqg/mbart-large-cc25-jaquad-qg', max_length=100)

# model = TransformersQG(language='ja', model='lmqg/mbart-large-cc25-jaquad-qg')

context = '「ぼっちざろっく」という漫画のあらすじを説明します。後藤ひとりは、ギターを愛する孤独な少女。 家で一人寂しく弾くだけの毎日でしたが、ひょんなことから伊地知虹夏が率いる「結束バンド」に加入することに。 人前での演奏に不慣れな後藤は、立派なバンドマンになれるのか！？ 全国のぼっちな少年少女に届ける、いま最高にアツい音楽漫画！！'
question_answer_pairs = model.generate_qa(context)
print(question_answer_pairs)
import pdb;pdb.set_trace()
# {'model': <class 'str'>,
# 'max_length': <class 'int'>,
# 'max_length_output': <class 'int'>,
# 'cache_dir': <class 'str'>,
# 'add_prefix': <class 'bool'>, 'language': <class 'str'>, 'label_smoothing': <class 'float'>,
# 'drop_overflow_text': <class 'bool'>, 'skip_overflow_error': <class 'bool'>, 'skip_highlight_error': <class 'bool'>, 'keyword_extraction_model': <class 'str'>, 'use_auth_token': <class 'bool'>}

# (Pdb) question_answer_pairs[0][1]
