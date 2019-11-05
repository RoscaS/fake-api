import random

import forgery_py, json, dataclasses
from dataclasses import dataclass


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


@dataclass
class Obj: id: str; description: str; name: str; price: str; photos: list


description = lambda: forgery_py.lorem_ipsum.sentence()
name = lambda: forgery_py.name.company_name()
price = lambda: "{:.2f}".format(random.randint(1, 15) + random.random())
photo = lambda: f'https://picsum.photos/id/{random.randint(100, 1000)}/800/600/'
pics = lambda: [{"filename": photo()} for _ in range(3)]
args = lambda: [description(), name(), price(), pics()]

products = {'products': [Obj(str(i + 1), *args()) for i in range(20)]}

app_json = json.dumps(products, cls=EnhancedJSONEncoder)

print(app_json)
