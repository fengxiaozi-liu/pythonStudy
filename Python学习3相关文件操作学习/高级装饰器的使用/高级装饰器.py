"""
高级装饰器：
    装饰器函数带参数
"""


def can_play(clock):
    def handle_action(fn):
        def inner(name,game):
            if clock >= 21:
                print('太晚了要睡觉了')
            else:
                return fn(name, game)
        return inner
    return handle_action



@can_play(22)
def play_game(name, game):
    print(f'{name}正在玩{game}')


play_game('张三', '王者荣耀')
