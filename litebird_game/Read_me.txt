/Chatch_game
├── main.exe # 実行ファイル　(画面比率はノートPC用)
└── image #4枚の画像

exe化する前のファイル
/game_test
├── image              
│   ├── litebird_satellite_2022-0220-2300.png # スタート画面のiltebird
│   ├── black_00080.jpg # ゲーム背景の画像
│   ├── earth01.png # 地球
│   └── cos.png # タート画面の背景
├──scores.txt # 過去のスコアを保存するテキストファイル
│
├── main.py # メインスクリプト,ゲームのスタート画面
├── game.py # ゲームループ,スコア管理など
├── player.py # プレイヤーに関するクラス
├── ball.py # B,Emodeクラス
└── settings.py #画面サイズ,色,ファイルパスなど

exe化
 pip install pyinstaller
 pyinstaller --onefile --windowed main.py


/Chatch_game_monitor,size #Chatch_gameの画面比率がmonitorサイズの物

