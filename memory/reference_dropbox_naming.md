---
name: Google Drive file naming convention (書類格納)
description: Detailed rules for naming and organizing files in Google Drive (previously Dropbox) for visa management documents including 在留カード, 申請書類, etc.
type: reference
---

# Google Drive 書類格納 Naming Rules

## Base Path
`~/Library/CloudStorage/GoogleDrive-sandy@funtoco.jp/共有ドライブ/社内ファイルサーバ/`

## 登録人材フォルダ Structure
Path: `社内ファイルサーバ / 5.登録人材 / 登A001〜該当番号が属するフォルダ内 / 登A000 / フルネーム / 呼び名`

- / の前後は半角スペース開ける
- スラッシュ / とスペースは半角

## 在留カード Naming
Format: `［在留カード表or裏 / 在留資格種別］フルネーム / 呼び名`

Examples:
- ［在留カード表or裏 / 留学］フルネーム / 呼び名
- ［在留カード表or裏 / 技能実習2号ロ（3号ロ）］フルネーム / 呼び名
- ［在留カード表or裏 / 特定活動］フルネーム / 呼び名
- ［在留カード表or裏 / 特定技能１号◯回目］フルネーム / 呼び名
- ［在留カード表or裏 / 技人国］フルネーム / 呼び名

Notes:
- 回数は更新ごとに変更
- 表・裏・表裏など、該当する名前で保存
- 画像は明るく、背景を消す、在留カードの形に沿ってトリミング

## 申請フォルダ
- 1回目: `1.申請書類1回目`
- 2回目以降: `1.申請書類2回目〜` (前回のフォルダはoldへ移動)
- 資格変更・法人移動でも同じ人材フォルダ内に連番で保存

## 企業フォルダ
Path: `4. 企業関連 → 分野別 → 企業NO.別`
