# nuntalyli'u プレイ記録 準備篇

## la nuntalyli'u とは

* [interactive fiction][if] と呼ばれる類ひのゲームの古典的な（といふか創始的な）作品であるところの「[Colossal Cave Adventure][advent]」（単に ADVENT とか Colossal Cave とか Adventure とか呼ばれる事が多い模様）をロジバンに訳したもの
  * [ロジバン公式ウィキのページ][mw_cc]からゲームデータを落とせる
    * [tiki時代のページ][tiki_cc]の方が情報量多いのは何なんですかね…ta'osai
* `nuntalyli'u` ← `nu zei talsa zei litru` （[～の事象]-[挑む]-[旅]）
  * 「Colossal Cave」ではなく「Adventure」の方をタイトルに採用したんやね
  * ta'o ba'anai ロジバン始めて間もない頃は、このlujvoの字面の、エキゾチックさを通り越しての得体の知れなさや気味悪さに大興奮したものだけど、今となつては何てことない構造の普通のlujvoなので、その頃の感覚が懐かしい

## interactive fiction とは

* テキスト主体のアドベンチャーゲームの一形態…といふか始祖的な形態のもの
  * 提示された選択肢やコマンドを選ぶのではなく、提示された状況描写を基に自分でCLI風のコマンドを入力する
* 百聞は一見に如かず、ゲーム画面を見る方が早い
  * ![オリジナル版Adventureの画面](https://upload.wikimedia.org/wikipedia/commons/3/35/ADVENT_--_Will_Crowther%27s_original_version.png)
  * ![Zorkといふゲームの画面](https://upload.wikimedia.org/wikipedia/en/3/32/Zork_I_screenshot_video_game_Gargoyle_interpreter_on_Ubuntu_Linux.png)
* 提示されたテキストからプレイヤーの置かれた状況を読み取り、適宜キーワードを拾ひつつコマンドを入力して、また別のテキストを提示させる、この繰り返しでゲームや物語を進めて行く
* ta'o jbovlasteには`frafi'a`といふlujvoが登録されてゐる: [`frafi'a`][frafiha]: x1 is interactive fiction about x2

## プレイに必要なソフトウェア

* nuntalyli'uはInformと呼ばれるinteractive fiction用のシステムで作られてをり、Z-machineと呼ばれる仮想機械のインタプリタを必要とする
  * [Z-machineインタプリタ][zmi]では最初にオススメされるし、[iOS版も提供されてる][frotz_ios]し、[Frotz][frotz]でいいかな

## いざ冒険へ…と、その前に準備運動も

Frotzで`nuntalylihu.z5`を読み込む。

```
no'i fi'ido'u do ca kelci la nuntalyli'u

la nuntalyli'u
The Interactive Original
By Will Crowther (1973) and Don Woods (1977)
Reconstructed in three steps by:
Donald Ekman, David M. Baggett (1993) and Graham Nelson (1994)
[In memoriam Stephen Bishop (1820?-1857): GN]
See source for translation credits.
Release 5 / Serial number 961209 / Inform v6.21 Library 6/9 SD

.i zvati le fanmo be lo dargu
.i do ca sanli le fanmo be lo dargu ca'u lo cmalu ke bliku dinju .i lo ricyci'e cu vanbi do .i lo cmalu rirxe cu flecu fi lo ma'arbi'i le dinju

.i do gasnu le nu _
```

やつたぜ。

（カーソル位置の表示は`_`で代用）

* `.i zvati le fanmo be lo dargu` `.i do ca sanli le fanmo be lo dargu`
  * ワイは今、道路の末端に立つてをるんやな…で
* `ca'u lo cmalu ke bliku dinju`
  * 道路の末端（に立つワイ）の前には、小さなブロック的建屋があるんやな
* `.i lo ricyci'e cu vanbi do .i lo cmalu rirxe cu flecu fi lo ma'arbi'i le dinju`
  * あと何か大自然の情景がワチャワチャとあるけど、これはまた後回しや

ぢやあ早速dinjuの中に入つてみよか。

```
.i do gasnu le nu nerkla lo dinju
```

```
.i ri na se nerkla

.i do gasnu le nu _
```

へ…？

「そこは入るとこと違ふで」て…dinjuは入るためのものやんか…

言葉が悪かつたんやろか…？

```
.i do gasnu le nu klama lo dinju
.i ri na se nerkla

.i do gasnu le nu nenri lo dinju
.i ri na se nerkla
```

何で？？？何で入れないん？？？

ちふか`nerkla`知つとるのに入れてくれないの何でなん？？？

```
.i do gasnu le nu tikpa lo dinju
.i le nu vlile cu te snada noda

.i do gasnu le nu darxi lo dinju
.i le nu vlile cu te snada noda

.i do gasnu le nu daspo lo dinju
.i le nu vlile cu te snada noda
```

思ひ通りに行かんからとて乱暴したワイが悪かつた…すまん。

（しかしこの`snada`のx3の使ひ方、ええな…ワイも今度`troci`の代りに使うたろ。）

`lo dinju`があかんのかな…これで十分特定できてるはずやけどな…

```
.i do gasnu le nu nerkla lo cmalu ke bliku dinju
.i do na viska ri

.i do gasnu le nu le dinju
.i le bridi po di'u na slabu mi

.i do gasnu le nu nerkla le dinju
.i ri na se nerkla

.i do gasnu le nu nerkla lo bliku dinju
.i do na viska ri
```

入れへんどころか見えへん…やて…？うそやん…

う～ん、`lo dinju`以外に適当なキーワードとか思ひ付かんで…どないしよ

```
.i do gasnu le nu nerkla
```

```
.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

.i so'o ckiku vi selstu le dertu

.i lo kukte cidja cu vi diklo

.i le minra ke lastu gustci cu jibni

.i lo botpi noi kunti vi zvati

.i do gasnu le nu _
```

何でこれで入れるんや？！

のつけから何だか幸先の思ひやられる仕様やけど、続きはまた今度にしよか。むほ。

[if]: https://en.wikipedia.org/wiki/Interactive_fiction
[advent]: https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%AD%E3%83%83%E3%82%B5%E3%83%AB%E3%83%BB%E3%82%B1%E3%83%BC%E3%83%96%E3%83%BB%E3%82%A2%E3%83%89%E3%83%99%E3%83%B3%E3%83%81%E3%83%A3%E3%83%BC 
[mw_cc]: https://mw.lojban.org/papri/Colossal_Cave
[tiki_cc]: http://tiki.lojban.org/tiki/Colossal+Cave
[frafiha]: http://jbovlaste.lojban.org/dict/frafi'a
[frotz]: http://frotz.sourceforge.net/
[frotz_ios]: https://itunes.apple.com/us/app/frotz/id287653015
[zmi]: http://inform-fiction.org/zmachine/interpreters.html
