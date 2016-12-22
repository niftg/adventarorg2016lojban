# nuntalyli'u プレイ記録 その三

* [準備篇](nuntalylihu_playkiroku_junbihen.md)
* [その一](nuntalylihu_playkiroku_pamoi.md)
* [その二](nuntalylihu_playkiroku_remoi.md)

## 前回までのあらすぢ

* 『nuntalyli'u[<sup id="inref_ntl">[1]</sup>](#ntl)』をプレイ中
  * 『nuntalyli'u』は『Colossal Cave Adventure[<sup id="inref_cca">[2]</sup>](#cca)』のロジバン訳版
    * 『Colossal Cave Adventure』（別名: 『ADVENT』、『Colossal Cave』、『Adventure』）は interactive fiction と呼ばれるゲームジャンルの創始的な作品
      * interactive fiction は、テキスト主体のアドベンチャーゲームで、CLI風のコマンド（`go north`とか`take lantern`とか）を入力してプレイヤーキャラを操作して物語を進める

### 前回までの出来事
* アイテムを携へて地下洞窟を探索開始
* 巨大な亀裂を飛び越さうとする自殺行為により主人公は死亡、その後コンティニューして蘇生
* 道を塞ぐ大蛇に道中捕獲した小鳥を生贄のつもりで差し出したら、小鳥が存外強くて、大蛇を退散させてしまつた

## 探検再開

先づは周囲の状況を再確認。
```
.i do gasnu le nu :zgana

.i balkumfa le ma'atru
.i do nenri le balkumfa po le ma'atru .i pluta fa'a roda

.i milxe ke klama sance vi le manku noi trixe do .i ledo gustci ca lenu do carna
fi lego'i cu gusni lo se firkre ke bloti zeicpa .i ri bevri lo barda dacru gi'e
krixa cusku lu

.ue.uose'i zo'e facki mi zo'e zo'e .i .e'u.ui mi sutra lenu mi klama le
lujlu'adi'u be zo'e bei zo'e zo'e zo'e zo'e zo'e zo'e kei mu'i lenu mi
mipstupu'i le dacru be zo'e bei zo'e beifo zo'e be'o po mi ge'ukei zo'e li'u

.i le zeicpa cu canci va'o le manku

.i do gasnu le nu :
```
場所的には`cmana zeicpa`とかかな…髭を生やした賊が登場。

zo'eの多用で攪乱しにかかつてるけど、`lujlu'adi'u`(←`pluja pluta dinju`: 迷宮？)に何か隠しに行くらしい。

それはともかく、探索再開。蛇が塞いでた道を再度確かめよう。
```
.i do gasnu le nu :berti

.i dizlo bersnanu pluta
.i do diklo lo dizlo pluta be lo berti .e lo snanu ne'a lo rajyke'a pevi le
loldi .i le rajyke'a cu ve klama lo cnita noi pluta lo stuna .e lo stici

.i loi grana noi rijno vi diklo

.i do gasnu le nu :lebna lo grana
.i lebna

[.i le do nilji'a cu te jmina ze.]
```
xekriぢやなくてrijnoな棒が出てきた。両方携へてたら特定が若干面倒やな。

下に通ずる縦穴があるのを認識したところで、一旦撤退。次は西にでも行こか。
```
.i do gasnu le nu :snanu

.i balkumfa le ma'atru

.i do gasnu le nu :berstici
.i .u'u so'a farna pluta cu zasti
```
「全方向に道が開けてると言つたな。あれは嘘だ。」

まあ単純に互ひの議論領域が異なつてただけやけどな。
```
.i do gasnu le nu :stici

.i nenri le stici mlana kumfa
.i do nenri le stici mlana kumfa pere'o le balkumfa po le ma'atru .i vi ranji
pluta lo stici joi gapru

.i so'i sicni cu diklo

.i do gasnu le nu :lebna roda
.i rirci sicni zo'u lebna

[.i le do nilji'a cu te jmina ze.]
```
コインをたくさん入手。
```
.i do gasnu le nu :stici

.i sunstici je bersnanu kruca
.i do diklo lo te kruca be lo galtu pluta be lo snanu .e lo berti be'o beilo
dizlo pluta be lo stici .e lo stuna
```
南北方向の通路との交叉点に来たが、さしあたり引き続き西へ。
```
.i do gasnu le nu :stici

.i zvati le stici jipno be le tcecla balkumfa
.i do diklo le stuna be lo tcecla balkumfa poila'a claxu lo lutku'a .i stuna fa
lo dizlo ganra ke cidydzu pluta poi mo'iga'u salpo .i berti fa lo cukla kevna
noi centre li xano leni ganra zi'enoi mo'ini'a salpo
```
西端に到達したみたいなので東に戻らう。
```
.i do gasnu le nu :stuna

.i zvati le stici jipno be le jaurbumru kumfa
.i do diklo le stici be le jaurbumru kumfa .i lo dizlo je ganra cidydzu pluta cu
ranji ve klama lo stici .i lo drata cu go'i lo berti .i snanu fa lo cmalu pluta
noi mitre li re leni darno lo loldi

.i do gasnu le nu :stuna

.i stici mlana le brafenra
.i do diklo le stici mlana be le brafenra vi le jaurbumru balkumfa

.i so'o rokcrnadamante to zoi gic. diamond gic.toi vi diklo
```
んんん？東に戻つて山の主の部屋（大蛇が居た部屋）に戻るつもりが、前回主人公が飛び降り自殺した巨大な亀裂の西側に出てしまつた模様。

まあダイヤモンドは回収しとこか。
```
.i do gasnu le nu lebna roda
.i rokcrnadamante. zo'u do ca'a bevri du'e dacti
.i brafenra zo'u  .i ri to'e se bevri
```
どうも一度に運べるアイテム数の制限があるらしい。小屋あたりに戻つて荷物を軽くしとくか。

しかし先づは山の主の部屋に戻らないと。
```
.i do gasnu le nu :stici

.i zvati le stici jipno be le jaurbumru kumfa

.i do gasnu le nu :stici

.i zvati le stici jipno be le tcecla balkumfa

.i do gasnu le nu :zgana

.i zvati le stici jipno be le tcecla balkumfa
.i do diklo le stuna be lo tcecla balkumfa poila'a claxu lo lutku'a .i stuna fa
lo dizlo ganra ke cidydzu pluta poi mo'iga'u salpo .i berti fa lo cukla kevna
noi centre li xano leni ganra zi'enoi mo'ini'a salpo
```
東のルートがさつきの巨大亀裂に通じてて駄目なら、次は北のルートを取るか。
```
.i do gasnu le nu :berti

.i sunstici je bersnanu kruca

.i pa lo te kajde ke cmalu cridrduarfa cu cliva loi ctino
```
え…ドワーフまで出てきよつた。ファンタジー世界か。さつきの賊もこれの仲間かな。

でも、この交叉点は見覚えあるな。ここを西に進んで西端に到達したんだもんな。戻るには東だ。
```
.i do gasnu le nu :stuna

.i nenri le stici mlana kumfa

.i le cridrduarfa cu te kajde ti'erkansa do

.i do gasnu le nu :stuna

.i balkumfa le ma'atru

.i le cridrduarfa cu te kajde ti'erkansa do
```
戻れたのはいいけど、しつこいドワーフやな…。
```
.i do gasnu le nu :gapru

.i nenri le jaurbumru balkumfa

.i le cridrduarfa cu te kajde ti'erkansa do

.i lo cmalu cridrduarfa puzi renro lo cmalu mruka'a do .i ri na'e snada lenu
darxi do .i le cridrduarfa cu dapma .i bajra cliva
```
ヒエッ…斧投げてきよつた。殺しにきとるやん。

ともかく、ドワーフは退散したみたいなので、この山の主の部屋からあの部屋まで自力で戻つてxyzyzyを唱へます。
```
.i nenri lo kumfa pelei fesydai

.i do gasnu le nu :xyzyzy

.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

.i do gasnu le nu :selbeiste
.i do bevri zo'u
  so'i rirci sicni
  loi grana noi rijno
  lo cmalu vasru pema'e loi jimca to poi ganlo toi
    lo cmalu cipni
  lo cmalu botpi
  lo kukte cidja
  lo girzu be loi ckiku
  lo lastu gustci to sabji lo gusni toi

.i do gasnu le nu :falcru lo sicni
.i snura se sorcu binxo

[.i le do nilji'a cu te jmina mu.]

.i do gasnu le nu :falcru lo grana
.i snura se sorcu binxo

[.i le do nilji'a cu te jmina mu.]

.i do gasnu le nu :falcru lo vasru
.i ca'a falcru
```
お宝はここで保管すると得点アップするんやな。

では、あのダイヤモンドを取りにまた洞窟へ。
```
.i do gasnu le nu :xyzyzy

.i nenri lo kumfa pelei fesydai
.i do nenri lo kumfa pelei fesydai zi'enoi culno loi se jaurbei befo lo gapru .i
lo dizlo je ganra pluta cu to'e se kliri'a tu'a loi cimdertu kujoi loi fesydai
.iku'i lo na'e frili se cadzu ma'arfe'a cu ve klama lo gapru joi stici .i lo
notci re'o le bitmu cu ve cusku lu lu xyzyzy li'u cu makfa valsi li'u 

.i do gasnu le nu :stici

.i na'e frili zei du'a je vu'a zei salpo ve klama ma'arfe'a

.i do gasnu le nu :stici

.i narju rirxe kumfa

.i do kakne le nu viska
lo xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu fanmo
vi le vi diklo
```
さういへば小鳥を捕獲するためにここで黒い棒を捨てたんだつけ…結局何処で使ふんやろ。まあ荷物軽くなつたし、また回収しようか。
```
.i do gasnu le nu :lebna
to le xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu
fanmo toi
.i ca'a lebna

.i do gasnu le nu :stici

.i gapru le cmalu rajyke'a

.i do gasnu le nu :cnita

.i nenri le jaurbumru balkumfa

.i le cmalu mruka'a cu vi diklo
```
ドワーフの投げてきた斧がまだ残つてた。これも回収。
```
.i do gasnu le nu :lebna
to le cridrduarfa mruka'a toi
.i ca'a lebna

.i pa lo te kajde ke cmalu cridrduarfa cu cliva loi ctino
```
またドワーフが現はれたか…
```
.i do gasnu le nu :cnita

.i balkumfa le ma'atru

.i le cridrduarfa cu te kajde ti'erkansa do

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi
```
ヒエッ…今度はナイフか何かを投げてきた。
```
.i do gasnu le nu :stici

.i nenri le stici mlana kumfa

.i le cridrduarfa cu te kajde ti'erkansa do

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi
```
しかも連続で投げてきよる。
```
.i do gasnu le nu :stici

.i sunstici je bersnanu kruca

.i do gasnu le nu :stici

.i zvati le stici jipno be le tcecla balkumfa

.i do gasnu le nu :stuna

.i zvati le stici jipno be le jaurbumru kumfa

.i pa lo te kajde ke cmalu cridrduarfa cu cliva loi ctino
```
あれ、さつき現はれてナイフ投げてきたドワーフはいつのまに消えて、また新しいドワーフが現はれてきたんかな。

しつこいから、何とか無力化したいところ。
```
.i do gasnu le nu :renro lo mruka'a
.i ca'a falcru

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :lebna lo mruka'a
.i ca'a lebna
```
アイテムを落とすのと大差無い操作だなこれ…腕力無いんか主人公？
```
.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :gunta lo cridrduarfa
to le te kajde ke cmalu cridrduarfa toi
.i na pilno le do xance .i na go'e

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :renro lo mruka'a lo cridrduarfa
to le te kajde ke cmalu cridrduarfa toi
.i .uu do na snada le nu darxi le cridrduarfa

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi
```
色々やつてみてるけどなかなか成功しませんね…
```
.i do gasnu le nu :renro lo cridrduarfa
to le cridrduarfa mruka'a toi
.i le cridrduarfa mruka'a cu ca'a diklo le vi stuzi


.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :lebna lo mruka'a
.i ca'a lebna

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :renro lo cridrduarfa
to le cridrduarfa mruka'a toi
.i ca'a falcru
```
renroのx2とx3があべこべのまま実装されてる可能性＋ドワーフ自体を投げ飛ばせる可能性に賭けてみたけど、`renro lo cridrduarfa`はどうやら`renro lo cridrduarfa mruka'a`としてシステムに認識される模様。うーん、ロジバンに不親切。
```
.i le cridrduarfa cu binxo le ka na cinri .iji'a cliva
```
ドワーフはどうやら飽きて退散したらしい。（一文目の訳は何か怪しいけど…）
```
.i do gasnu le nu :lebna lo mruka'a
.i ca'a lebna

.i do gasnu le nu :stuna

.i stici mlana le brafenra

.i so'o rokcrnadamante to zoi gic. diamond gic.toi vi diklo

.i do gasnu le nu :lebna roda
.i rokcrnadamante. zo'u lebna
.i brafenra zo'u  .i ri to'e se bevri

[.i le do nilji'a cu te jmina ze.]
```
ダイヤモンド全回収。賊やドワーフに見つかつたら多分奪はれてたな…。

no'ita'o ところで、例の黒い棒の使ひ道が分かりました。[Q: What is the rod good for?][rod]によると、この亀裂で黒い棒を振ると何か起こるみたいです。
```
.i do gasnu le nu :sligau lo grana
.i lo krili cripu le fenra ca ragve

.i do gasnu le nu :stuna

.i stuna korbi lo brafenra

.i lo krili cripu le fenra ca ragve

.i do gasnu le nu sligau lo grana
.i le krili cripu cu canci .ue
```
うん…橋を出現させる程度の力のある魔法の杖でしたね。これで何かを叩かうとしてた時もあつたな…罰当たりやな。

ダイヤモンドを保管しに小屋まで戻ります。
```
.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

.i do kakne le nu viska
lo cmalu vasru pema'e loi jimca to poi ganlo toi
  lo cmalu cipni
loi grana noi rijno
so'i rirci sicni
vi le vi diklo
```
さてダイヤを…ダイヤのfu'ivlaがどんなだつたか忘れてしまうた。.oiro'e
```
.i do gasnu le nu :selbeiste
.i do bevri zo'u
  loi rokcrnadamante.
  lo cridrduarfa mruka'a
  lo xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu
fanmo
  lo cmalu botpi
  lo kukte cidja
  lo girzu be loi ckiku
  lo lastu gustci to sabji lo gusni toi

.i do gasnu le nu :falcru lo rokcrnadamante
.i snura se sorcu binxo

[.i le do nilji'a cu te jmina mu.]
```
.uo

では、山の主の部屋までまた戻つて、残りの南方向を探査しますか。
```
.i balkumfa le ma'atru

.i do gasnu le nu :snanu

.i nenri le snanu mlana kumfa
.i do nenri le snanu mlana kumfa

.i loi kargu jadjme vi diklo
```
`jadjme`は多分`jadni jemna`（装飾的宝石）だよな…すかさず回収。
```
.i do gasnu le nu :lebna roda
.i kargu jadjme zo'u lebna

[.i le do nilji'a cu te jmina ze.]

.i do gasnu le nu :snanu
.i do na kanke le nu klama fo la'e di'u
```
他に無ければまた同じやうに小屋に戻つて保管。
```
.i nenri lo dinju
.i do nenri lo dinju noi djacu marbi lo barda jaukra

.i do kakne le nu viska
loi rokcrnadamante.
lo cmalu vasru pema'e loi jimca to poi ganlo toi
  lo cmalu cipni
loi grana noi rijno
so'i rirci sicni
vi le vi diklo

.i do gasnu le nu :falcru lo jadjme
.i snura se sorcu binxo

[.i le do nilji'a cu te jmina mu.]
```
そしてまた山の主の部屋へ蜻蛉返り。

探索中に選ばなかつた脇道があるから、そこも探査しておこか。さしあたり西へ。
```
.i balkumfa le ma'atru

.i do gasnu le nu :stici

.i nenri le stici mlana kumfa

.i do gasnu le nu :stici

.i sunstici je bersnanu kruca

.i do gasnu le nu :stici

.i zvati le stici jipno be le tcecla balkumfa

.i do gasnu le nu :stici
```
あ、入力失敗した。まあでも壁にぶち当たるだけやろ。
```
.i zvati le stuna jipno be le tcecla balkumfa
.i do diklo le stici be lo tcecla je tilcau balkumfa .i le balkumfa cu kruca lo
jarki pluta be lo berti .e lo snanu
```
あれ…？西端から西に進んだら東端に出た…？やはりこのゲーム、どこかで空間が歪んでゐる。

と思つたが、説明文はちやんと`stici be lo tcecla ...`とあるので、直前の文の`le stuna jipno`が誤りであるだけかな。

さしあたり南を選ばう。
```
.i do gasnu le nu :snanu
```

ここで突然のエラーダイアログ「`Frotz Fatal Error`: `Cal to non-routine`」が出てFrotz強制終了。こんなところでバグに遭遇するとは…。

（ちなみにこの地点のバグの調査のために再プレイしたのですが、ここで北を選ぶと、例の交叉点（`sunstici je bersnanu kruca`）に出ます。そしてその交叉点で北に進むとそこでもこれと同様のバグで強制終了します。）

## バグで気持ちが萎えつつ再プレイ

ダイヤモンドを回収するために小屋で荷物を軽くしたあたりでセーブしてあつたので、そこから再開。
```
.i do gasnu le nu :xyzyzy

.i nenri lo kumfa pelei fesydai
.i do nenri lo kumfa pelei fesydai zi'enoi culno loi se jaurbei befo lo gapru .i
lo dizlo je ganra pluta cu to'e se kliri'a tu'a loi cimdertu kujoi loi fesydai
.iku'i lo na'e frili se cadzu ma'arfe'a cu ve klama lo gapru joi stici .i lo
notci re'o le bitmu cu ve cusku lu lu xyzyzy li'u cu makfa valsi li'u 

.i do gasnu le nu :stici

.i na'e frili zei du'a je vu'a zei salpo ve klama ma'arfe'a

.i do gasnu le nu :stici

.i narju rirxe kumfa

.i do kakne le nu viska
lo xekri grana noi mitre li pa leni clani zi'enoi lo se kijyspo tartai cu fanmo
vi le vi diklo

.i do gasnu le nu :stici

.i gapru le cmalu rajyke'a

.i do gasnu le nu :stici
.i le fenra cu dukse leni cmalu kei lenu ve klama fo do

.i do gasnu le nu :cnita

.i nenri le jaurbumru balkumfa

.i le cmalu mruka'a cu vi diklo

.i do gasnu le nu :cnita

.i balkumfa le ma'atru

.i do gasnu le nu :berti

.i dizlo bersnanu pluta
```
確かここに下へ通ずる縦穴があつたのですが、更に北へ。
```
.i do gasnu le nu :berti

.i zvati lu .ybu re li'u
.i do nenri lo barda kumfa noi krasi lo pluta be lo snanu be'o .e lo pluta be lo
stici be'o .e lo stuna poi bitmu zi'enoi se zbasu fi lo se porpi rokci .i lu
.ybu re li'u cu barda se ciska filo rokci pevi le midju be le kumfa
```
おや、もしかして`.ybu re`も`xyzyzy`と同じくショートカット魔法なのでせうか。
```
.i do gasnu le nu :.ybu re
.i le bridi po di'u na slabu mi

.i do gasnu le nu :.ybure
.i le bridi po di'u na slabu mi

.i do gasnu le nu :ybu re
.i le bridi po di'u na slabu mi
```
うん、よく考へたら地点を示すだけのただの記号ですね。二語だし。
```
.i do gasnu le nu :berti
.i do na kanke le nu klama fo la'e di'u

.i do gasnu le nu :stici

.i zvati lo dizlo canko noi viska'eri'a filo cambarda rajyke'a
.i do lamji lo dizlo canko noi viska'eri'a filo cambarda rajyke'a poi ganra
ranji ji'e lo na'e se viska .i lo loldi cu na'e tcila se viska .i mitre li
za'upamu leni ra cnita do .i loi pagbu be lo blabi jaurbumru cu gacri le loldi
be le rajyke'a .i leni lego'i cu denmi cu selze'a vi le pritu .i lo barna be le
pulce pene'a le canko cu nibli ja'oru'e lenu zo'e puzavi zvati .i lo canko noi
simsa levi canko zi'enoi viska'eri'a filo se gusni kumfa cu ragve le rajyke'a do
.i lego'i cu mitre li mu leni darno do .i do viska lenu lo ctino pretai cu catlu
do
```
気持ちが萎えた状態でこの長文を読み解くのは止めておいて先に進むことにします。謎の人影らしきもの(`ctino pretai`)がこちらを見てるし。
```
.i do gasnu le nu :stici
.i lo pluta belo stuna bei fa'a la'e lu .ybu re li'u be'o po'o cu ve barkla
```
さつきの`.ybu re`の部屋への道しか無いとの事なので戻ります。
```
.i pa lo te kajde ke cmalu cridrduarfa cu cliva loi ctino
```
そしてドワーフ再来。
```
.i do gasnu le nu :catlu lo cridrduarfa
.i .e'u do na klama le jibni be le cridrduarfa
```
せやな。斧とかナイフとか投げてくるもんな。
```
.i do gasnu le nu :stuna

.i zvati lu .ybu re li'u

.i le cridrduarfa cu te kajde ti'erkansa do

.i do gasnu le nu :berti
.i do na kanke le nu klama fo la'e di'u

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :dunda lo cidja
to le te kajde ke cmalu cridrduarfa toi
.i doi bebna ro cridrduarfa cu citka lo kolme .enai lo drata .i do .iecai
fegygau le crida
```
ええ…ドワーフは石炭しか食べないとか知らんかつたで…
```
.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :dunda lo ckiku
to le te kajde ke cmalu cridrduarfa toi
.i le cridrduarfa na se cinri to la'a mukti le du'u le nu catra do cu rinka le
nu le cridrduarfa ponse roda
```
主人公を殺せば全て奪へるのだから、贈り物には興味が無い。なるほど合理的。どのみち彼等との殺し合ひは避けられないのだ…。
```
.i do gasnu le nu :catra lo cridrduarfa
.i na pilno le do xance .i na go'e

.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi

.i do gasnu le nu :catra lo cridrduarfa sepi'o lo mruka'a
.i na'e jimpe lei valsi poi se lidne lo'u catra le te kajde ke cmalu cridrduarfa
le'u

.i do gasnu le nu :renro lo cridrduarfa
.i le te kajde ke cmalu cridrduarfa cu ca'a diklo le vi stuzi


.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.iku'i na darxi
```
斧の使ひ方がいまいちようわからんな…
```
.i do gasnu le nu :renro lo cridrduarfa lo mruka'a
.i do na viska ri

.i do gasnu le nu :renro lo mruka'a lo mruka'a
.i do na viska ri

.i do gasnu le nu :renro lo mruka'a lo cridrduarfa
.i do na viska ri

.i do gasnu le nu :renro lo mruka'a
.i do na viska ri
```
あれ？
```
.i do gasnu le nu selbeiste
.i do bevri zo'u
  lo cmalu botpi
  lo kukte cidja
  lo girzu be loi ckiku
  lo lastu gustci to sabji lo gusni toi
```
斧拾ふの忘れてたか…
```
.i le cridrduarfa cu renro lo kinli ke na'e clite dakfu do.i xamgu darxi
```
そしてこんな時に限つてナイフが命中。
```
.i doi juxre bebna do'u do pujo'uca zukte lo mabla .i mi na djuno ledu'u mi ka'e
xamgu frati la'edi'u caza lokau temci .i xu do djica lenu mi krefu troci lenu
mivgau do
```
今回はもうここで止めとかうや。
```
.i do spuda fi lu :.ienai
.i ko ciska zo go'i .onai lu na go'i li'u> :nago'i
.i .ie


    *** .i do ca'a morsi ***


.i ca le pu se kelci do nilji'a 75 fi'u 350 ca'o le 154roi nu zukte cu kleri'a
la'e talyli'u li'u
```
今まであんまりポイントには気を留めてなかつたけれど、貯めたポイントが表示されてゲーム終了。

（自動出力されるやつはだいたい何か文がをかしいな…）
```
.i xu do djica le nu ba'e refcfa gi'onai ba'e veipli lo se kelci gi'onai sisti
> :go'i (ロジバン話者らしい意地悪回答)

.i pe'u ko sabji pa lo gapru danfu
> sisti
```

## 今後の抱負
さて、ドワーフを殲滅したいといふ気持ちよりもバグを殲滅したいといふ気持ちの方が強いので、もし次に現状のnuntalyli'uをプレイするとしたら、バグの調査が主目的になるでせう。そして可能であればソースを弄つて改善したいものです。むほ。

---
1. <a id="ntl"></a>ゲームの入手先等は[MediaWiki版の記事][ntl_mw]や[tiki版の記事][ntl_tiki]を参照。後者には制作時の作業データも。[↑](#inref_ntl)
2. <a id="cca"></a>Wikipedia記事の[日本語版][cca_wja]や[英語版][cca_wen]、[ファンサイト][cca_fan]をさしあたり参照先として挙げておく。[↑](#inref_cca)

[ntl_mw]: https://mw.lojban.org/papri/Colossal_Cave
[ntl_tiki]: http://tiki.lojban.org/tiki/Colossal+Cave
[cca_wja]: https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%AD%E3%83%83%E3%82%B5%E3%83%AB%E3%83%BB%E3%82%B1%E3%83%BC%E3%83%96%E3%83%BB%E3%82%A2%E3%83%89%E3%83%99%E3%83%B3%E3%83%81%E3%83%A3%E3%83%BC
[cca_wen]: https://en.wikipedia.org/wiki/Colossal_Cave_Adventure
[cca_fan]: http://rickadams.org/adventure/
[rod]: http://rickadams.org/adventure/d_hints/hint005.html