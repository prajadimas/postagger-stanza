import json
import stanza

config = {
	# 'processors': 'tokenize,pos,depparse', # Comma-separated list of processors to use
	'lang': 'id', # Language code for the language to build the Pipeline in
	'tokenize_model_path': './resources/id/tokenize/gsd.pt', # Processor-specific arguments are set with keys "{processor_name}_{argument_name}"
	'pos_model_path': './resources/id/pos/gsd.pt',
    'depparse_model_path': './resources/id/depparse/gsd.pt',
    'lemma_model_path': './resources/id/lemma/gsd.pt',
	'pos_pretrain_path': './resources/id/pretrain/gsd.pt',
	'use_gpu': False,
	'tokenize_pretokenized': True # Use pretokenized text as input and disable tokenization
}

def postag(s):
	nlp = stanza.Pipeline(**config) # Initialize the pipeline using a configuration dict
	doc = nlp(s) # display results
	results = {}
	results['sentence'] = s
	results['tokens'] = []
  	# print(*[f'{word.id};{word.text};{word.upos};{word.xpos};{word.head};{sent.words[word.head-1].text if word.head > 0 else "root"};{word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
	for sent in doc.sentences:
		for word in sent.words:
			data = {}
			data['id'] = word.id
			# data['text'] = word.text
			data['token'] = word.text
			# data['upos'] = word.upos
			data['pos'] = word.upos
			# data['xpos'] = word.xpos
			# data['deprel'] = word.deprel
			data['parent_rel'] = word.deprel
			data['feats'] = word.feats if word.feats else "_"
			# data['head'] = sent.words[word.head-1].text if word.head > 0 else "root"
			data['parent_id'] = word.head
			json_data = json.dumps(data)
			results['tokens'].append(data)

	return results
