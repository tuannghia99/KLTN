from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request
import json, requests, time
import sentencepiece as spm

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/.*": {"origins": "*"}})
#app.config['CORS_HEADERS'] = 'application/json'

DB_CONNECTION = None
TIMEOUT = 60


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/translate_paragraphs', methods=['POST'])
#@cross_origin()
def translate_paragraphs():
    # {"data": [{"src": "", "html_obj": }, {}], "direction": "en-vi"}
    try:
        ru_spm = spm.SentencePieceProcessor(model_file='~/Data/ru-vi/ru/spm.model')
        requestContent = request.get_json()
        # print(requestContent)
        sentence = requestContent["data"]
        from fairseq.models.transformer import TransformerModel

        ru2vi = TransformerModel.from_pretrained(
        '~/TestCode/fairseq/checkpoints/',
          checkpoint_file='checkpoint_best.pt',
          data_name_or_path='data-bin/ru-vi',
        #   bpe='sentencepic'
        )
        # print(sentence)
        sentence = ru_spm.encode(sentence, out_type=str)
        # print(sentence)
        sentence = " ".join(sentence).strip()
        print(sentence)
        result = ru2vi.translate(sentence).split()
        print(result)
        result = ru_spm.decode(result).replace("▁", " ").strip()
        print(result)
        # print(ru_spm.encode(sentence, out_type=str, enable_sampling=True, alpha=0.1, nbest_size=-1), sentence)
        data = result
        print(data)

        response = {
            "data":{
                "data": data,
                "status": True
            }
        }
    except Exception as e:
        print(e)
        response = {
            "data":{
                "data": data,
                "status": False
                }
        }
    return json.dumps(response)

if __name__ == '__main__':
    #app.run(debug=True, host="0.0.0.0", port="1711", ssl_context=("cert.pem", "key.pem"))
    app.run(debug=True, host="0.0.0.0", port="1715")

