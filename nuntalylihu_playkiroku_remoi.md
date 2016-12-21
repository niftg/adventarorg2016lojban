# nuntalyli'u プレイ記録 その二

* [準備篇](nuntalylihu_playkiroku_junbihen.md)
* [その一](nuntalylihu_playkiroku_pamoi.md)

## 前回までのあらすぢ

* 『nuntalyli'u[<sup id="inref_ntl">[1]</sup>](#ntl)』をプレイ中
  * 『nuntalyli'u』は『Colossal Cave Adventure[<sup id="inref_cca">[2]</sup>](#cca)』のロジバン訳版
    * 『Colossal Cave Adventure』（別名: 『ADVENT』、『Colossal Cave』、『Adventure』）は interactive fiction と呼ばれるゲームジャンルの創始的な作品
      * interactive fiction は、テキスト主体のアドベンチャーゲームで、CLI風のコマンド（`go north`とか`take lantern`とか）を入力してプレイヤーキャラを操作して物語を進める
  * 前回までの行動履歴
    * （プレイヤーの最初の地点のそばにある）小屋の中にあるアイテムを回収して
    * 周囲の森を散策したら方向感覚を失つて、漸く脱出したらそこは南の谷で
    * 北に進んで最初の地点に戻つて、小屋の周りの位置関係を再度確認して一旦終了

## 冒険再開

[このページ][annadv]を見ると、どうも森の散策は然して重要ではない模様。骨折り損か。とつとと谷の先にある洞窟の入り口へ行かう。

（今回から`>`ではなく`:`を挿入して入力開始部分を示してみます。）

```
.i do gasnu le nu :snanu

.i zvati le ma'arbi'i

.i do gasnu le nu :snanu

.i zvati lo fenra be le cmari'e sefta
.i vive'a ledo jamfu piji'iro lei djacu po'e le rirxe cu daxfle fi lo fenra be
le rokci be'o noi centre li mu leni clani .i pirole ve flecu sefta cu rokci
```
岩の亀裂に向かつて川は流れ落ちてる模様。`centre`が奇しくも英単語つぽい見た目ですけど、これは「～センチメートル（ある）」といふ意味の述語（`centi`+`mitre`）。英語のcentreはただのセンターやな。（英式綴り）

このまま南下して行きます。
```
.i do gasnu le nu :snanu

.i se bartu le ga'avro
.i do diklo lo rajyke'a noi mitre li ze leni condi zi'enoi se loldi loi dertu .i
ri te jarpu'i lo tsali ke gasta ga'avro noi se jicmu lo majrtsementa. to zoi gy.
cement gy. toi .i lo sudga ke flecu sefta cu clani fa'a le rajyke'a
```

`do diklo lo rajyke'a`の部分だけ見て一瞬「落とし穴に嵌つたか？！」と焦つたが、ga'avro（grate（鉄格子））がしつかり設置できる程度の床面積はあるはず。srajiだけどjarkiではなささう。このga'avroが洞窟の入り口か。

```
.i do gasnu le nu :snanu

.i zvati le ricfoi
```
あかん。また森に迷ひ込んでしまうた。
```
.i do gasnu le nu :berti

.i zvati le fanmo be lo dargu
```
この森、時空が歪んどるな…古いゲームだししやあないか。

ちなみに小屋に入るコマンドが目的語も何もない`nerkla`だけなのは、元々がさういふ仕様だつたらしい。訳者と実装者にごめんなさいしなきやね。

で、また同じく南下してga'avroのある穴に戻つてきました。
```
.i se bartu le ga'avro

.i do gasnu le nu :catlu
to le ga'avro toi
.i za'a fadni
```
`catlu`は`zgana`と違うて、物体に視線を集中させるんやな。
```
.i do gasnu le nu :zgana

.i se bartu le ga'avro
.i do diklo lo rajyke'a noi mitre li ze leni condi zi'enoi se loldi loi dertu .i
ri te jarpu'i lo tsali ke gasta ga'avro noi se jicmu lo majrtsementa. to zoi gy.
cement gy. toi .i lo sudga ke flecu sefta cu clani fa'a le rajyke'a
```
セメントで基盤に固めてある鉄格子をどうしたものか。
```
.i do gasnu le nu :daspo lo ga'avro
.i le nu vlile cu te snada noda
```
.uenai .uinai .uonai
```
.i do gasnu le nu :kargau lo ga'avro
.i ri cu se kikla'a
```
`kikla'a`されてる…つまりckikuでlasnaされてる…となれば、鍵が必要。アドベンチャーの超定番の関門やね。

鍵は今のところ小屋で回収したやつしか無いので、それを使用しよう。
```
.i do gasnu le nu :kargau lo ga'avro sepi'o lo ckiku
.i do gasnu le nu le ga'avro cu kikykalri
```
やつたぜ。.uosai .u'a

ついでに持ち物もう一度確認しとこ。
```
.i do gasnu le nu :selbeiste
.i do bevri zo'u
  lo cmalu botpi
  lo lastu gustci
  lo kukte cidja
  lo girzu be loi ckiku
```
je'e。`zo'u`の直前の部分は絶対後でソース弄つて修正したい。
```
.i do gasnu le nu :nenri
.i do na kanke le nu klama fo la'e di'u

.i do gasnu le nu :cnita
to pamai do kargau le ga'avro toi
.i cnita le ga'avro
.i do nenri lo cmalu kumfa peni'a lo gasta ga'avro noi kurtre li pa leni sefta
zi'enoi vorme fi lo gapru .i lo dizlo ke cidydzu pluta ga'ure'o loi lolro'iboi
cu ve klama lo nenri je stici

.i le ga'avro cu kalri
```
施錠を解いたのみで鉄格子開けるの忘れてたけど、自動でフォローしてくれるシステムや。.i'e

膝立ちせんと進めない道が内部且つ西方に続いてる模様。
```
.i do gasnu le nu :nenri
.i do na kanke le nu klama fo la'e di'u

.i do gasnu le nu :stici
```
東西南北移動の方が成功率高いんかな。
```
.i nenri la lolro'iboi cidydzu
.i do cidydzu loi lolro'iboi .oi vi lo dizlo pluta .i ruble gusni fi le stuna be
le pluta

.i lo cmalu vasru pema'e loi jimca cu se renro ne'aku
```
枝的な物で出来た入れ物が下の方に投げられてる模様。誰が投げたのかは知らんけど、特に変でなければ頂戴しとこか。
```
.i do gasnu le nu :catlu lo cmalu vasru
.i ri cu vasru pema'e loi jimca

.i do gasnu le nu :lebna lo vasru
.i ca'a lebna

.i do gasnu le nu :stici

.i ka manku
.i prane le ka manku .iseri'a do na kakne le nu viska
```
完璧な闇やん。ここでgustciの出番やな。漸く冒険らしうなつてきた。
```
.i do gasnu le nu :tolcadgau lo gustci
.i do kragau le lastu gustci

.i nenri lo kumfa pelei fesydai
.i do nenri lo kumfa pelei fesydai zi'enoi culno loi se jaurbei befo lo gapru .i
lo dizlo je ganra pluta cu to'e se kliri'a tu'a loi cimdertu kujoi loi fesydai
.iku'i lo na'e frili se cadzu ma'arfe'a cu ve klama lo gapru joi stici .i lo
notci re'o le bitmu cu ve cusku lu lu xyzyzy li'u cu makfa valsi li'u 

.i lo xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu
fanmo cu jibni
```

[Basic nuntalyli'u Instraction][bi]に孰れも載つてるとはいへ、`kragau`は何か違ふ気がするから個人的には`tolcadgau`を選好するところである。

この小汚い感じの部屋の壁に書かれてゐることによると、`xyzyzy`は魔法の言葉…あの有名なxyzzyやな。これを唱へれば何か起きるんかな。

```
.i do gasnu le nu :cusku lu xyzyzy li'u
to do toi
.i na spuda
```
図らず自問自答してしまつた。
```
.i do gasnu le nu :bacru lu xyzyzy li'u
.i le bridi po di'u na slabu mi
```
ん～どうすれば呪文唱へられるんやろ。
```
.i do gasnu le nu :xyzyzy

.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

.i do gasnu le nu :xyzyzy

.i nenri lo kumfa pelei fesydai
.i do nenri lo kumfa pelei fesydai zi'enoi culno loi se jaurbei befo lo gapru .i
lo dizlo je ganra pluta cu to'e se kliri'a tu'a loi cimdertu kujoi loi fesydai
.iku'i lo na'e frili se cadzu ma'arfe'a cu ve klama lo gapru joi stici .i lo
notci re'o le bitmu cu ve cusku lu lu xyzyzy li'u cu makfa valsi li'u 

.i lo xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu
fanmo cu jibni
```
ロジバン的には非文法的やけど、ともかく小屋とこのゴミ部屋とを瞬時に行き来できる呪文なんやな。

先が星形の黒い棒も頂戴しませう。
```
.i do gasnu le nu :lebna lo grana
.i ca'a lebna

.i do gasnu le nu :stici

.i na'e frili zei du'a je vu'a zei salpo ve klama ma'arfe'a
.i do diklo lo na'e frili ve klama ma'arfe'a noi salpo zi'enoi ve klama lo stici
.e lo stuna

.i do gasnu le nu :stici

.i narju rirxe kumfa
.i do nenri lo banli kumfa noi mitre li pano leni galtu .i le bitmu cu dunja
rirxe flecu lo narju rokci .i lo na'e frili ve klama ma'arfe'a kufa'u lo xamgu
pluta cu te barli'a vi le stuna fa'u stici mlana be le kumfa

.i lo gleki ke cmalu cipni vi zutse je sanga
```
何やこの鳥。炭鉱のカナリア的な存在か？オレンジ色の岩と相俟つてこの部屋の異様さが際立つてをる。

ともかく回収…いや捕獲か。
```
.i do gasnu le nu :kavbu lo cipni
.i le cipni na terpa ca lenu do nerkla .i ri ca lenu do jbibi'o ri co'a dunku
.iseki'ubo do na'eka'e kavbu ri
```
近づいたら何か苦しさうで捕まへられへん。
```
.i do gasnu le nu :dunda lo cidja
to le cmalu cipni toi
.i ri na'e xagji gi'esu'anai djisanga ra'a loi zbanrfiorde .iji'a do bevri no
cpidja tsiju
```
餌付けも失敗。鳥用の食べ物ではなかつた。
```
.i do gasnu le nu :kargau lo vasru
.i ri ca ca'a kalri

.i do gasnu le nu :kavbu lo cipni sepi'o lo vasru
.i le cipni na terpa ca lenu do nerkla .i ri ca lenu do jbibi'o ri co'a dunku
.iseki'ubo do na'eka'e kavbu ri

.i do gasnu le nu :kavbu lo cipni lo vasru
.i na'e jimpe lei valsi poi se lidne lo'u kavbu le cmalu cipni le'u

.i do gasnu le nu :kavbu lo cipni fi lo vasru
.i na'e jimpe lei valsi poi se lidne lo'u kavbu le cmalu cipni le'u
```
`kavbu`のx3はこのシステムだと認識せんのやな…ともかく道具のせゐでもないらしい。
```
.i do gasnu le nu :catlu lo cipni
.i lo gleki ke cmalu cipni vi zutse je sanga
```
う～ん、これ以上は何の手がかりも得られん。先に行かうか。
```
.i do gasnu le nu :stici

.i gapru le cmalu rajyke'a
.i ledo jamfu cu lamji lo cmalu rajyke'a noi vasxu krasi loi cmafle be loi blabi
jaurbumru .i lo pluta pefa'a lo stuna vi se fanmo .iku'i lo cmalu fenra cu ranji
ve klama

.i loi rufsu rokci se stapa cu ve klama le cnita be le rajyke'a
```
東へ戻れる道はここで行き止まりで、足下の穴の下方には粗い岩的な足の踏み場がある。ここで方向転換やな。となれば、一旦ルートマップをメモしておかうか。

東から西にリストアップすると…

* `cnita le ga'avro`
* `nenri la lolro'iboi cidydzu`
* `nenri lo kumfa pelei fesydai`
  * gustci無しだとka manku（闇）
  * 魔法の呪文`xyzyzy`で小屋と行き来できる
  * 先が星形の黒い棒をここで拾つた
* `na'e frili zei du'a je vu'a zei salpo ve klama ma'arfe'a`
* `narju rirxe kumfa`
  * ここで小鳥が歌ひよつてたけど、結局捕まへられなかつた
* `gapru le cmalu rajyke'a`
  * この部屋に空いてる穴の下に向かつて足の踏み場がある

では下に降りよう。
```
.i do gasnu le nu :cnita

.i nenri le jaurbumru balkumfa
.i do diklo lo fanmo be lo barda balkumfa noi clara'i ji'e lo no'e se viska
stici .i role mlana cu lutke'a .i so'o ganra ke rokci serti cu ve klama lo cnita
.i le balkumfa cu culno loi cmafle be loi blabi jaurbumru noi se muvdu ta'i
sa'enai tu'alo jmive .i lo lenku cu brife le serti .i pluta vi le gapru be lo
boldi'u noi trixe do

loi rufsu rokci se stapa cu ve klama le gapru be le boldi'u

[.i le do nilji'a cu te jmina remu.]
```
`remu`は`li remu`にせんとな…ta'osai

この部屋の西端はよく見えないほど遠い。で、下方に向かふ岩の階段がある。つまり西(`stici`)か下(`cnita`)に進める。その他の詳細な描写はさしあたり読み飛ばす。

先づは西へ。
```
.i do gasnu le nu :stici

.i stuna korbi lo brafenra
.i do diklo le stuna korbi be lo brafenra noi kuspe pirole balkumfa .i le
jaurbumru vi carmi denmi .i le fenra cu dukse leni ganra kei lenu do ravypi'e
```
霧の出元はこの大きい亀裂か…？跳び越すには広過ぎるとあるが…
```
.i do gasnu le nu :vreji
.i vi'o
```
遺書は書いた（セーブした）。さあ無限の彼方へ飛び立たう。
```
.i do gasnu le nu :ravypi'e
.i le bridi po di'u na slabu mi

.i do gasnu le nu :plipe
.i do na'e snada ba'unai


.i .uuru'e tu'a do ba'o rinka ja'o lenu do se catra .i.e'ecu'i mi ka'e sidju do
.iku'i mi puku'anoroi troci lo simsa be lenu go'i .i xu do djica lenu mi troci
lenu mivgau do

.i do spuda fi lu :
```
やはりただの自殺に終つた。しかし復活の機会が与へられてゐる。
```
.i do spuda fi lu :go'i
.i vi'odo'u.aunai ko na pante va'o lenu srera 



.i zoi san. pyff san. 

.i do se sruri lo narju danmo dilnu .i do kafke je nadvasxu gi'e barkla fi le
danmo gi'e facki .i .i .i

.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

[.i le do nilji'a cu te vimcu pano.]
```
復活の際にポイント減つてしまうた…（しかし初回プレイだしポイントを気にする余裕がない。）
```
.i do gasnu le nu :selbeiste
.i do bevri noda

.i do gasnu le nu :zgana

.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra
```
アイテムも全部失つた状態でどうすればいいんですかね…。
```
.i do gasnu le nu :cliva
.i ko nitcu le nu cusku le farna poi do djica

.i do gasnu le nu :bartu

.i zvati le fanmo be lo dargu

.i le minra ke lastu gustci cu jibni
```
gustciだけは発見。これが無いと洞窟の中は闇だからな…。
```
.i do gasnu le nu :lebna lo gustci
.i ca'a lebna

.i do gasnu le nu :nerkla

.i nenri lo dinju

.i do gasnu le nu :xyzyzy

.i ka manku
.i prane le ka manku .iseri'a do na kakne le nu viska

.i do gasnu le nu :gusni
.i do kragau le lastu gustci
```
それでは先程のbrafenraまで同じ道を辿りませうか。
```
.i stuna korbi lo brafenra

.i do kakne le nu viska
lo girzu be loi ckiku
lo kukte cidja
lo cmalu botpi to poi kunti toi
lo cmalu vasru pema'e loi jimca to poi kunti toi
lo xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu fanmo
vi le vi diklo
```
遺品が全部残つてますね。もれなく遺品回収しませう。
```
.i do gasnu le nu :lebna roda
.i girzu be loi ckiku zo'u ca'a lebna
.i kukte cidja zo'u ca'a lebna
.i cmalu botpi zo'u ca'a lebna
.i cmalu vasru pema'e loi jimca zo'u ca'a lebna
.i xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu fanmo
zo'u ca'a lebna
.i brafenra zo'u  .i ri to'e se bevri
.i jaurbumru zo'u  .i ri to'e se bevri
```
しかしまあ、さつきのもさうだけど、自動でアイテムのリスティングをする部分の文章はしばしば非文法的やな…やはり後でソース弄らんとな。

ともかく便利な機能に感謝せんとな。
```
.i do gasnu le nu :stici
.i le fenra cu dukse leni ganra
```
うん。ここでまた死んだら駄目だよね。
```
.i do gasnu le nu :stuna

.i nenri le jaurbumru balkumfa
```
亀裂を越えるのは後にして、次は下に行かうか。
```
.i do gasnu le nu :cnita

.i balkumfa le ma'atru
.i do nenri le balkumfa po le ma'atru .i pluta fa'a roda

.i lo barda ke crino ke fengu since cu to'e kligau le ve klama
```
え…何やこの大蛇。これが山の主か。

全方向に道はあるらしいから、さしあたり通れる道を探すか。
```
.i do gasnu le nu :stici
.i do na'eka'e backla le since

.i do gasnu le nu :berti
.i do na'eka'e backla le since
```
西と北は山の主に通せんぼされてまうた。
```
.i do gasnu le nu :stuna

.i nenri le jaurbumru balkumfa

.i do gasnu le nu :stici

.i stuna korbi lo brafenra

.i do gasnu le nu :zgana

.i stuna korbi lo brafenra
.i do diklo le stuna korbi be lo brafenra noi kuspe pirole balkumfa .i le
jaurbumru vi carmi denmi .i le fenra cu dukse leni ganra kei lenu do ravypi'e

.i do gasnu le nu :stici
.i le fenra cu dukse leni ganra
```
東に出ようとしたらいつのまにかさつきの大部屋に逆戻り。洞窟もしばしば空間が捻れとるんかな…。森の恐怖、再来。
```
.i do gasnu le nu :stuna

.i nenri le jaurbumru balkumfa

.i do gasnu le nu :cnita

.i balkumfa le ma'atru

.i lo barda ke crino ke fengu since cu to'e kligau le ve klama
```
この山の主の部屋から東に抜けたら、戻る時は下に進まんとあかんのやな。
```
.i do gasnu le nu :snanu
.i do na'eka'e backla le since
```
う～ん、この大蛇を退かさないとあかんのか…
```
.i do gasnu le nu :damba lo since
.i lenu gunta le since bana'e snada je ckape
```
`se snada`かなta'o。危険を承知で大蛇に抗ひます。
```
.i do gasnu le nu :darxi lo since sepi'o lo grana
.i na'e jimpe lei valsi poi se lidne lo'u darxi le since le'u

.i do gasnu le nu :sligau lo grana
.i noda fasnu

.i do gasnu le nu :sligau lo xance
.i do na viska ri

.i do gasnu le nu :sligau
.i do sligau le do xance to .oiro'a toi
```
棒や手では追ひ払へない。単にネガティヴな挨拶をしたのみか。
```
.i do gasnu le nu :ctigau lo cidja
to le since toi
.i ri djica lenu citka noda pevi zi'epo'u na'ebo do
```
ここにあるものではワイ以外の何物もお召しにならぬと仰せか。
```
.i do gasnu le nu :ctigau mi
to le since toi
to pamai do cpacu do toi
.i do ze'e ponse do
```
ワイは永遠にワイの所有やな…

ところで`ctigau`のPSとしては「x1(gasnuのx1)がx2(citkaのx1)にx3(citkaのx2)を食べさせる」だから、本当は{ctigau lo since mi}とか{selctigau mi lo since}が正しいはずだけど、まあこのシステムは仕様上ロジバン文法に優しくないみたいみたいだから、この世界では{`ctigau`}={selctigau}であると理解しておくか。{[tamgau][jvs_tamgau]}の例と同じく。
```
.i do gasnu le nu :dunda mi
to le since toi
to pamai do cpacu do toi
.i do ze'e ponse do
```
`dunda`してももちろん大差無いな。

う～ん、流石に手詰まりやな。[ヒント集][hints]に頼るか。

[Q: How do you get past the snake?][hint_snake]:
> Throw the bird at it. Of course, you have to catch the bird first. 

ええ…あの小鳥ちやんを生きたまま蛇に食はすんか…残酷やけど道理に適つてをる。

で、鳥はどう捕まへればいいのかな。

[Q: How do you catch the bird?][hint_bird]:
> Well, the help file mentions that the bird is afraid of the rod, so keep that in mind. If you have the rod in your possession, you won't be able to get near the bird. Also, you'll need a cage to keep the bird in. So if you've got the cage, and not the rod, you're all set.

ええ…ワイではなくてワイの持つてた棒に怯えてたんか…どんな棒やねん…ああ、例の魔法の呪文の部屋に落ちてたやつやから、魔法の杖か何かか。魔法で何か酷い目に遭はされたんかな…もしや元は鳥ではなくて…まあこれは後で考へよう。

さしあたり戻つて鳥肉を取りに行く。
```
.i do gasnu le nu :xyzyzy
.i noda fasnu
```
あの魔法の呪文の部屋以外では効かんのか…しやあないので自力であの鳥の部屋に戻りまして
```
.i narju rirxe kumfa

.i lo gleki ke cmalu cipni vi zutse je sanga

.i do gasnu le nu :falcru lo grana
.i ca'a falcru

.i do gasnu le nu :kavbu lo cipni
.i do kavbu le cipni sepi'o le vasru
```
やつたぜ。しかしこの関門はアイテムを一つづつ落として鳥に近付かんと解決できないやろ…一度に全部落とせば良かつたのか。
```
.i do gasnu le nu :catlu lo cipni
.i za'a le cmalu cipni cu badri le ka se vasru
```
まあこれから蛇の餌食になるし尚更やな…
```
.i do gasnu le nu :pencu lo cipni
.i le cmalu vasru pema'e loi jimca ganlo
```
これは`cu ganlo`とでもすべきかしらん。

で、また自力で山の主の部屋へ。
```
.i balkumfa le ma'atru

.i lo barda ke crino ke fengu since cu to'e kligau le ve klama
```
いよいよ小鳥ちやんを山の主たる怒れる大蛇の生贄にします…co'o sai lo cipni .iu
```
.i do gasnu le nu :renro lo cipni
to le cipni zifri'a le vasru

.i le cmalu cipni cu gunta le crino since .i ra va'o lonu macri'a damba cu
livbai le since 
```
え…何これ（呆然）。鳥、強過ぎやろ。食べられるどころか撃退しとるやん。
```
.i do gasnu le nu :zgana

.i balkumfa le ma'atru
.i do nenri le balkumfa po le ma'atru .i pluta fa'a roda

.i lo gleki ke cmalu cipni vi zutse je sanga
```
そして小鳥ちやんは平然と以前の如く歌ひよる。
```
.i do gasnu le nu :kavbu lo cipni
.i do kavbu le cipni sepi'o le vasru
```
入れ物の中は悲しいだらうに、また捕まつてくれた。

あの大蛇を撃退して道が開けたし、今回はここまでにしよか。むほ。

---
1. <a id="ntl"></a>ゲームの入手先等は[MediaWiki版の記事][ntl_mw]や[tiki版の記事][ntl_tiki]を参照。後者には制作時の作業データも。[↑](#inref_ntl)
2. <a id="cca"></a>Wikipedia記事の[日本語版][cca_wja]や[英語版][cca_wen]、[ファンサイト][cca_fan]をさしあたり参照先として挙げておく。[↑](#inref_cca)

[ntl_mw]: https://mw.lojban.org/papri/Colossal_Cave
[ntl_tiki]: http://tiki.lojban.org/tiki/Colossal+Cave
[cca_wja]: https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%AD%E3%83%83%E3%82%B5%E3%83%AB%E3%83%BB%E3%82%B1%E3%83%BC%E3%83%96%E3%83%BB%E3%82%A2%E3%83%89%E3%83%99%E3%83%B3%E3%83%81%E3%83%A3%E3%83%BC
[cca_wen]: https://en.wikipedia.org/wiki/Colossal_Cave_Adventure
[cca_fan]: http://rickadams.org/adventure/
[annadv]: http://jerz.setonhill.edu/if/gallery/adventure/
[bi]: http://tiki.lojban.org/tiki/Basic+nuntalylihu+Instructions
[jvs_tamgau]: http://jbovlaste.lojban.org/dict/tamgau
[hints]: http://rickadams.org/adventure/d_hints/
[hint_snake]: http://rickadams.org/adventure/d_hints/hint006.html
[hint_bird]: http://rickadams.org/adventure/d_hints/hint004.html
