from ..mbi.level2 import Level2DataApi

def find_existed_brick_ids():
    return Level2DataApi().find_existed_brick_ids()