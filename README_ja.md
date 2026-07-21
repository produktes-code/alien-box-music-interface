# Alien Box: ユニバーサルミュージカルバイブル 👽

![Alien Box](alien_imagotype/screen.png)

🌐 **他の言語で読む:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | **🇯🇵 日本語** | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

---

**Alien Box** は、最先端のマルチモーダル フォレンジック オーディオ分析エンジンおよび DAW テンプレート ジェネレーターです。グローバルな音楽ネットワークに直接接続して、あらゆるテキスト入力から実際のメタデータを抽出し、コマーシャルトラックの周波数とダイナミックパラメータを分析し、主要な DAW (Ableton、Logic Pro、Cubase、FL Studio、Pro Tools) 用にカスタマイズされたスターター テンプレートを生成します。

**CHUS BZN** による **produktes-code** による精密エンジニアリングにより構築されています。

## 🚀 特徴
- **ユニバーサル検索:** YouTube リンク、Spotify リンク、またはフリーテキスト (例: 「The Prodigy Poison」) を入力します。
- **ブルータル フォレンジック分析:** ターゲット LUFS、特定の EQ カーブ (キック/ベース クロスオーバー)、VCA 圧縮のアタック/リリース タイムを計算します。
- **マルチモーダル エクスポート:** 事前にルーティングされた DAW テンプレートを含む実際の ZIP ファイルを生成します。
- **オーガニック UI:** ダイナミックなパーティクル背景を備えた、流動的で呼吸するグラフィック インターフェイス。
- **ネイティブ ユニバーサル PDF マニュアル (V14):** 高解像度で生成された PDF マニュアルは 7 か国語に対称的に翻訳され、細心の注意を払ってフォーマットされ、DIN A5 印刷用に完璧に調整されています。

## 🛠 インストール

### 1. バックエンドのセットアップ
バックエンドは軽量の Python サーバー上で実行されます。
「」バッシュ
# 1. 分析サーバーを起動する
python3 エイリアンボックス_サーバー.py
「」

### 2. フロントエンド
最新の Web ブラウザで「splash_screen_organic_v3_final/code.html」を開くだけです。

### 3. マニュアルを生成する (V14)
絶対対称の V14 ユニバーサル マニュアルを DIN A5 レイアウトでコンパイルするには:
「」バッシュ
python3 build_universal_manual_v14.py
ノード print_multilingual_v14_pdf.js
「」

## 📦 インストーラーの構築 (macOS および Windows)
Alien Box をネイティブ デスクトップ アプリケーションにパッケージ化するために、Electron/PyInstaller 用のビルド スクリプトを提供しています。これにより、GitHub リポジトリ用のリリースが準備されます。

* **Mac OS (.dmg):** `./build_mac.sh` を実行します。
* **Windows (.exe):** `build_win.bat` を実行します。

---
*「produktes-code」エコシステムの一部。 CC BY-NC-SA 4.0。企業標準 - 小売対応。*