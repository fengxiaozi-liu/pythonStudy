def can_play(fn):
    def inner(name, game, **kwargs):
        clock = kwargs.get('clock', 21)
        if clock >= 21:
            print('太晚了不能玩了')
        else:
            return fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print(f'{name}正在玩{game}')


play_game('张三', '王者荣耀', clock = 22)
