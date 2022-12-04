import json


def dump_json(obj, fp, encoding='utf-8', indent=4, ensure_ascii=False, json_lines=False):
    if not json_lines:
        with open(fp, 'w', encoding=encoding) as fout:
            json.dump(obj, fout, indent=indent, ensure_ascii=ensure_ascii)
    else:
        assert type(obj) == list
        with open(fp, "a+", encoding=encoding) as fout:
            for line in obj:
                fout.write(json.dumps(line)+"\n")


def load_json(fp, encoding='utf-8', json_lines=False):
    with open(fp, encoding=encoding) as fin:
        if not json_lines:
            return json.load(fin)
        else:
            ret = []
            for line in fin:
                ret.append(json.loads(line))
            return ret