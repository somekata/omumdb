# 大阪公立大学大学院医学研究科 細菌学 ホームページ

公開URL: https://somekata.github.io/omumdb/index.html
公式サイト: https://www.omu.ac.jp/med/bacteriology/
開設日: 2026年11月7日

## 構成

- 日本語: ルート直下（index.html ほか全11ページ）
- 英語: `en/` 以下（同じ11ページ）
- `assets/style.css` 共通CSS（外部依存なし）
- `assets/calendar/` 月間カレンダー画像（縦:横 = 1:4、2400×600 PNG）
- `_tools/build.py` 全ページの生成スクリプト
- `_tools/make_calendar.py` カレンダー画像の生成スクリプト（キャラクターは `_tools/chara/` の透過PNGを使用。ファイル名は同スクリプトの `CHARAS` で入れ替え）

## 公開（GitHub Pages）

このフォルダの中身を `omumdb` リポジトリのルートにそのまま置く。

## 更新のしかた

1. **お知らせ**: `_tools/build.py` の `INFO` に1件追加
2. **カレンダー**: `assets/calendar/YYYY-MM.png` を置き、`CALENDARS` の末尾に1件追加（トップには最後の1件が表示される）
3. **メンバー**: `MEMBERS` を編集
4. `python3 _tools/build.py` を実行（全ページが再生成される）

生成された *.html を直接編集すると、次回の実行時に上書きされる。

## 表記ルール

- 治療に関する記述は「抗菌薬」（antimicrobial agents）を使い、「抗生物質」は使わない
- 学名はイタリック（`<i class="sn">`）。血清型は立体
- 全ページのフッターにAI作成の注意書きを入れている
