/litebird_game
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

exe化(しないほうがいい)
 pip install pyinstaller
 pyinstaller --onefile --windowed main.py


