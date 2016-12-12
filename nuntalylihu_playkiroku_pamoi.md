# nuntalyli'u プレイ記録 その一

* 前回: [nuntalyli'u プレイ記録 準備篇](https://github.com/niftg/adventarorg2016lojban/blob/master/nuntalylihu_playkiroku_junbihen.md)

## 辞書を携へて

何んな語が文中で出現して何んな語が入力できるかの手掛かりとして。

* [Basic nuntalyli'u Instructions][basic]
  * 特に General Notes 以降の Pronouns, Articles, Compass Directions, Meta Verbs, Ordinary Verbs の節
  * コマンド入力の際に役立つ
* [nuntalyli'u mini-dictionary][vlaste]
  * [HTML版][https://mw.lojban.org/images/8/8a/59.sip]
  * jbovlasteに未登録のlujvoが出てきた時に役立つ
    * ただ、いづれにせよ大意を示すキーワードのみの列挙でしかない。x1だけなら何となく解るかな。

### セーブとロードだけ試してみる

* セーブ(Save): `vreji` / `rejri'a` / `rejgau`
* ロード(Restore): `veipli`

あとはダイアログでセーブファイルを指定してやるだけ。

## いざ冒険へ（本番）

`refcfa`で最初からやり直し。

```
no'i fi'ido'u do ca kelci la nuntalyli'u
```

### アイテムを揃へる

```
.i zvati le fanmo be lo dargu
.i do ca sanli le fanmo be lo dargu ca'u lo cmalu ke bliku dinju .i lo ricyci'e cu vanbi do .i lo cmalu rirxe cu flecu fi lo ma'arbi'i le dinju

.i do gasnu le nu _
```
前回同様、`nerkla`で小屋に入ります。（今回から、入力した部分には先頭に`>`を挿入して判りやすくする事にします。）
```
.i do gasnu le nu >nerkla

.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

.i so'o ckiku vi selstu le dertu

.i lo kukte cidja cu vi diklo

.i le minra ke lastu gustci cu jibni

.i lo botpi noi kunti vi zvati

.i do gasnu le nu _
```
便利さうなアイテムだらけですね。全部頂戴して行きませう。
```
.i do gasnu le nu >cpacu lo ckiku
.i ca'a lebna
```
あ…ほんとはここに居ない誰かの持ち物なのかもしれませんね…まあ気にせず`lebna`していきませう。
```
.i do gasnu le nu >lebna lo kukte cidja
.i ca'a lebna

.i do gasnu le nu >lebna lo lastu gustci
.i ca'a lebna

.i do gasnu le nu >lebna lo botpi
.i ca'a lebna

.i do gasnu le nu >zgana

.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

.i do gasnu le nu _
```
全部取れたやうです。（ところで`djacu marbi lo barda jaukra`とあるので、この小屋は湧き水か井戸か何かを防護するためのものみたいですね。）

念のため、`selbeiste`(`beiste`/`b`)で持ち物を確認してみませう。
```
.i do gasnu le nu >selbeiste
.i do bevri zo'u
  lo cmalu botpi
  lo lastu gustci
  lo kukte cidja
  lo girzu be loi ckiku

.i do gasnu le nu _
```
う～～～ん、何か文法的にをかしいリスティングやな…他言語版においては元の英文のメッセージを逐語訳するしかできない仕様だつたとしても、もう少し何とかしたいところです。`lo do se bevri zo'u`にして次の各アイテムを`.i`で区切るとか、`do bevri la'edi'e .i`みたいにしてしまへばええやんな。

まあそれはさておき、鍵の組と美味しい食べ物と真鍮の燈りと小瓶を確かに携へて、この小屋を出ませう。

```
.i do gasnu le nu >barkla
.i le bridi po di'u na slabu mi
```
おう…`nerkla`は知つてて`barkla`は知らんのかい…
```
.i do gasnu le nu >bartu

.i zvati le fanmo be lo dargu

.i do gasnu le nu >zgana

.i zvati le fanmo be lo dargu
.i do ca sanli le fanmo be lo dargu ca'u lo cmalu ke bliku dinju .i lo ricyci'e cu vanbi do .i lo cmalu rirxe cu flecu fi lo ma'arbi'i le dinju

.i do gasnu le nu _
```

## 今一度周囲を観察

さういや周囲の大自然の情景描写にはノータッチやつたな前回は。行き先も決まらんし、もう一度よう見てみようや。

* `.i lo ricyci'e cu vanbi do`
  * 森がゲームの中のワイを取り囲む環境・文脈なんやな…虫とか熊とか出てくるんかな…怖
* `.i lo cmalu rirxe cu flecu fi lo ma'arbi'i le dinju`
  * `flecu`のterbri、どんなんやつたつけ…「x1 は x2 の／における、 x3 （終点）へ x4 （始点）からの流れ； x2 は流れる」か。ちなみにx2はガスとか液体とか、とにかくx3に向かふx4からの流れを内包する流動体たる物質を示すんやな。
  * 小川が山の間（つまり谷間）に向かつて先程の水源を防護する小屋から流れ落ちてゐる…て事か
    * この`le`を英語のtheつぽく使うてるとしたら何か嫌やけど、まあそこは目を瞑りませう
    * `catlu lo rirxe`してみても`.i do na viska da poi vajni zi'e po le cmari'e`て返されるから、まあ川の中を浚つたらお宝が！みたいな展開は期待出来なささうやな

となれば、行き先は森か谷か。どうしようかな。

```
.i do gasnu le nu >zgana lo ricyci'e
.i lei vi tricu cu barda jdari bo mudri ke cindu ke'e je tricrxakerake'a to zoi gy. maple gy. toi .i sosmei lei cmalu ricyci'e befi lo tricrpino to zoi gy. pine gy toi .a lo tricrpike'a to zoi gy. spruce gy. toi .i so'imei loi nitspa noi so'eke'a cu ctino ke tricrbetulake'a to zoi gy. birch gy. toi fa'u tricrfraksino. to zoi gy. ash gy. toi pa'a loi na'e pikyva'i ke mitfrica demspa .i ca leca citsi leka ka'e viska cu se jimte ki'u tu'a lei pezli .i ku'i lenu litru cu frili ni'i lenu do rivbi le tricrpike'a .e le se jbari

.i do gasnu le nu >zgana lo ma'arbi'i
.i do na viska ri

.i do gasnu le nu _
```

…うん、谷間は遠くて見えない。さういふことにしときませう。

森に入る前に、大自然の情景描写を一文づつ確認しとこか。

* `.i lei vi tricu cu barda jdari bo mudri ke cindu ke'e je tricrxakerake'a to zoi gy. maple gy. toi`
  * 近くにあるのは楓の木やな…「大きい、堅い材木のブナ科」てだけだと説明し切れなくて英単語を動員してるのが何か落胆を通り越して可愛い
* `.i sosmei lei cmalu ricyci'e befi lo tricrpino to zoi gy. pine gy toi .a lo tricrpike'a to zoi gy. spruce gy. toi`
  * 松か[唐檜属][spruce]（クリスマスツリーで有名な樅と形が似てるらしい）の何かで構成された小さい森が`sosmei`(←`so'omei`[いくらか（のものからなる群）])
    * どつちも`ckunu`（針葉樹）の範疇やんな…ちなみにjbovlasteを見ると`fadyku'u`と`konku'u`で両者を区別しようとしとる人も居る
* `.i so'imei loi nitspa noi so'eke'a cu ctino ke tricrbetulake'a to zoi gy. birch gy. toi fa'u tricrfraksino. to zoi gy. ash gy. toi pa'a loi na'e pikyva'i ke mitfrica demspa`
  * ワイに馴染みのない英語名が続々と出てきよるな…背の低い感じの小藪がたくさんあつて、そのうちの多数派の二種はコメントしてみたけど、後は特筆に値しない雑多な木々からなる藪なんかな…
    * `ctino ke tricrbetulake'a fa'u tricrfraksino`の`ctino`は影なのか陰なのか…まあともかく薄暗くて鬱蒼とした感じかしら
* `.i ca leca citsi leka ka'e viska cu se jimte ki'u tu'a lei pezli`
  * 今の季節は、例の葉つぱの群が理由で可視性に限りがある…つまり、枯れ木の季節やないから葉つぱに邪魔されて見通しは良うないんやな
*  `.i ku'i lenu litru cu frili ni'i lenu do rivbi le tricrpike'a .e le se jbari`
  * でもあなたが唐檜を、ベリーの生る木を避ける事で必然的に導かれる事に、徘徊は簡単である…つまりワイがさうした木を避けて歩けば簡単に歩き回れる程度の密度なんやな
    * といふかベリーの生る木(`le se jbari`)出てくるんか…見つけたら摘めるんかな

う～ん、最後の二文だけ読めば十分やつたな。とつとと森へ行きませう。

## しかしまたしても入場拒否

```
.i do gasnu le nu >nerkla lo ricyci'e
.i ri na se nerkla

.i do gasnu le nu >klama lo ricyci'e
.i ri na se nerkla

.i do gasnu le nu >nenri lo ricyci'e
.i ri na se nerkla`
```

`zgana lo ricyci'e`が通る以上、`riryci'e`に問題があるとは思へないんだよなあ。

谷になら行けるんやろか。
```
.i do gasnu le nu >klama lo ma'arbi'i
.i do na viska ri

.i do gasnu le nu >nerkla lo ma'arbi'i
.i do na viska ri

.i do gasnu le nu >nenri lo ma'arbi'i
.i do na viska ri
```
見えないなら川を辿つてでも行つてほしいんだけどな～～～

ロジバン実装の拙さのせゐで早々に手詰まりか…？いや、あれを試したろ。

## 方角移動

```
.i do gasnu le nu >berti

.i zvati le ricfoi
```
北方向でいきなり入れたやん。
```
.i do gasnu le nu >snanu

.i zvati le ricfoi

.i do gasnu le nu >snanu

.i zvati le ricfoi

.i do gasnu le nu >snanu

.i zvati le ricfoi

.i do gasnu le nu _
```
そしていきなり出れへん…。ツクール製RPGの見知らぬマップに足を踏み入れた途端に閉ぢ籠められた気分や。

方角を指定して移動するのはインタラクティブフィクションの基本操作の内らしいけど、これだとマップチップで構成された世界を十字キーで歩かせるのと大差無くて、テキスト主体である事の強みが活かされないんだよなあpe'i。なので行き先が分かるのであればなるべく使用したくなかつたが、まあ仕方が無い。

```
.i do gasnu le nu >stici

.i zvati le ricfoi

.i do gasnu le nu >stuna

.i zvati le ma'arbi'i
.i do zvati lo ma'arbi'i vaze'a le ricyci'e ne'a lo cmari'e noi kasfle re'o loi rokci
```
あれ、谷に出てまうた。南に行き過ぎたから、今度は北かな。
```
.i do gasnu le nu >berti

.i zvati le fanmo be lo dargu
```
戻れたやん。折角やから西と東も確認しとくか。
```
.i do gasnu le nu >stici

.i zvati le cmama'a poi nenri le dargu
.i do ba'o mo'iga'u cadzu lo cmama'a gi'e pujeca nenri le ricyci'e .i le dargu cu mo'ini'a salpo va le na'evi cmama'a mlana .i lo dinju cu darno se zgana

.i do gasnu le nu >stuna

.i zvati le fanmo be lo dargu

.i do gasnu le nu >stuna

.i nenri lo dinju

.i do gasnu le nu >stici

.i zvati le fanmo be lo dargu

.i do gasnu le nu _
```

ふむ。位置関係はこんな感じか。

```
(行きは良い良い帰りは怖い)lo ricfoi
                               |
lo cmama'a --(lo-dargu)-- lo fanmo --- lo dinju
(ne'i lo dargu)                |             ~
                               |             ~
                        lo ma'arbi'i~~lo~rirxe
```

森は怖い。西に新しく出よつたcmama'a（丘）とか南の谷とかを先に探検しようか。

ジボ語版の実装の不完全さに不安を覚えつつも、今日はここまで。中々冒険が始まらんな…もう少しザックリ進めよか。むほ。

[basic]: http://tiki.lojban.org/tiki/Basic+nuntalylihu+Instructions
[vlaste]: https://mw.lojban.org/papri/nuntalyli'u_mini-dictionary
[vlaste_html]: https://mw.lojban.org/images/8/8a/59.sip
[spruce]: https://en.wikipedia.org/wiki/Spruce
