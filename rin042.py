# ゲームクラス
class menmenAI(OthelloAI):
    DRAW = -1

    # def __init__(self, turn=0, start_player=BLACK):
    #     super().__init__()
    #     self.player = start_player
    #     self.turn = turn
    #     self.winner = None
    #     self.was_passed = False

    def __init__(self):
        self.face = '🐇' # 自分の好きな絵文字
        self.name = 'みな' # 自分の好きな名前



    def is_finished(self):
        return self.winner is not None

    def list_possible_cells(self):
        return super().list_possible_cells(self.player)

    def get_color(self, player):
        if player == WHITE:
            return "WHITE"
        if player == BLACK:
            return "BLACK"
        else:
            return "DRAW"

    def get_current_player(self):
        return self.player

    def get_next_player(self):
        return WHITE if self.player == BLACK else BLACK

    def shift_player(self):
        self.player = self.get_next_player()

    def put_disk(self, x, y):
        if super().put_disk(x, y, self.player):
            self.was_passed = False
            self.player = self.get_next_player()
            self.turn += 1
        else:
            return False

    def pass_moving(self):
        if self.was_passed:
            return self.finish_game()

        self.was_passed = True
        self.shift_player()

    def show_score(self):
        """それぞれのプレイヤーの石の数を表示する"""
        print("{}: {}".format("BLACK", self.disks[BLACK]))
        print("{}: {}".format("WHITE", self.disks[WHITE]))

    def finish_game(self):
        self.disks = self.get_disk_map()
        white = self.disks[WHITE]
        black =self.disks[BLACK]

        if white < black:
            self.winner = BLACK
        elif black < white:
            self.winner = WHITE
        else:
            self.winner = self.on_draw()

        return self.winner

    def on_draw(self):
        """ゲーム終了時に両社の石の数が同数だった時の処理
        デフォルトでは引き分けを認める
        """
        return self.DRAW
