from lmqg import TransformersQG

model_small = TransformersQG(language='ja', model='lmqg/mt5-small-jaquad-qg')
model_base = TransformersQG(language='ja', model='lmqg/mt5-base-jaquad-qg')
model_large = TransformersQG(language='ja', model='lmqg/mbart-large-cc25-jaquad-qg')
