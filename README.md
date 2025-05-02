# 🎹 Virtual Bandoneon

キーボード操作でBandoneonを演奏できる、Python + Pygame製の練習アプリです。  
実際に録音した音源を使い、リアルな感触で演奏できます。

## 🚀 特徴

- A〜Kキーで演奏可能（C4〜C5対応）
- 自作音源（Bandoneon録音）
- Pythonで簡単に実行
- カスタム拡張もしやすい構造

## 💻 動作環境

- Python 3.6以上
- `pygame` ライブラリ（インストールは `pip install pygame`）

## 📁 フォルダ構成

```

virtual-bandoneon/
├── bandoneon.py        # メインアプリケーション
├── data/               # 音源フォルダ
│   ├── C4.wav
│   ├── D4.wav
│   └── ...etc
└── README.md

````

## 🔧 使い方

```bash
git clone https://github.com/yourusername/virtual-bandoneon.git
cd virtual-bandoneon
pip install pygame
python3 bandoneon.py
````

* キーボードの A〜K を押すと、それぞれの音が鳴ります。
* [x] キーで終了します。

## 🎵 音源について

* 音源ファイル（`*.wav`）は作者自身によるBandoneon録音です。
* 非商用利用に限り使用可能です（下記ライセンスを参照）。

## 📝 ライセンス

* **ソースコード**: [MIT License](./LICENSE)
* **音源ファイル**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)（非商用・要クレジット）

---

Created by [Toru Takenaga](https://github.com/torutakenaga)
Enjoy the sound of Bandoneon! 🎶
