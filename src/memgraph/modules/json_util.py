import json
import mgp
import urllib.request


@mgp.read_proc
def load_from_path(ctx: mgp.ProcCtx,
                   json_path: str) -> mgp.Record(objects=mgp.List[object]):
    with open(json_path) as json_file:
        objects = json.load(json_file)
        if type(objects) is dict:
            objects = [objects]
        return mgp.Record(objects=objects)
