# 🎹 Virtual Bandoneon

Python + Pygame を使った、キーボード操作で演奏できる簡易バンドネオンアプリです。  
実際に録音した音源（WAV）を使って、PC上で本物のBandoneonの雰囲気を楽しめます。

> 🔰 初めてのアプリ公開につき、超シンプルな構成＆やさしい気持ちでご覧ください。

---

## 🚀 特徴

- A〜Kキーでバンドネオン音源を再生（C4〜C5）
- 自分で録音したリアル音源を使用
- Python 1ファイルだけで動作
- 音源切替や拡張もしやすい構造

---

## 💻 動作環境

- Python 3.6以降（macOS, Windows, Linux対応）
- `pygame` ライブラリ（以下の手順でインストール）

---

## 📦 インストールと実行方法

1. このリポジトリをクローン：
    ```bash
    git clone https://github.com/torutakenaga/virtual-bandoneon.git
    cd virtual-bandoneon
    ```

2. ライブラリをインストール：
    ```bash
    pip install pygame
    ```

3. アプリを実行：
    ```bash
    python3 bandoneon.py
    ```

🎵 A〜Kキーを押すとそれぞれの音が鳴ります  
❌ [X]キーで終了します

---

## 📁 フォルダ構成

````

virtual-bandoneon/
├── bandoneon.py        # メインアプリケーション
├── data/               # 音源フォルダ
│   ├── C4.wav
│   ├── D4.wav
│   └── ...
├── README.md
└── LICENSE

```

---

## 🎵 音源について

- 収録されている `.wav` ファイルは、作者本人がBandoneonで録音したものです。
- 非商用に限り、クレジット表記付きで自由にご利用いただけます（下記参照）。

---

## 📝 ライセンス

- **ソースコード**: [MIT License](./LICENSE)
- **音源ファイル**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)（非商用・クレジット表記要）

---

## 🙏 補足

このアプリは「まず動くものを作ってみる」を目的にした超入門作品です。  
今後、吸気/吐気の切り替えやWeb版（Streamlit等）も試してみたいと考えています。

---

Created by [Toru Takenaga](https://github.com/torutakenaga)  
Enjoy the sound of the Bandoneon! 🎶
```

