<!--
(zo detke'u mu'a .a zo datro mu'a)
(gu ga zo datro gi le bi'u lertcitydetri gi zo detke'u .a'ibu'onai)
-->

# zo detri jo'u zo datro

* 何でこの話題を選んだんだつけ…カレンダーからの聯想だつたかしら

## 今回話題にするgismu
* 引用はjbovlasteにおける英語と日本語の語義説明文から
<dl>
<dt>detri</dt>
<dd>
<ul>
<li><q cite="http://jbovlaste.lojban.org/dict/detri?bg=1;langidarg=2">x1 is the date [day,{week},{month},year] of event/state x2, at location x3, by calendar x4.</q>（<q cite="http://jbovlaste.lojban.org/dict/detri?bg=1;langidarg=10">x1 （数）は x2 （事）・ x3 （所）・ x4 （暦）の日付</q>）</li>
<li><q cite="http://jbovlaste.lojban.org/dict/detri?bg=1;langidarg=2">(time units in x1 are specified as numbers separated by pi'e or are unit values massified with joi)</q>（detriのx1については後ほど）</li>
</ul>
</dd>
<dt>datro</dt>
<dd>
<ul>
<li><q cite="http://jbovlaste.lojban.org/dict/datro?bg=1;langidarg=2">x1 (event) is dated/pertaining to day/occurring on day x2 of month x3 of year x4 in calendar x5</q>（<q cite="http://jbovlaste.lojban.org/dict/datru?langidarg=10">x1 （事）は x2 （日）・ x3 （月）・ x4 （年）・ x5 （暦） の日付 （に生じる）</q>）</li>
<li><q cite="http://jbovlaste.lojban.org/dict/datro?bg=1;langidarg=2">Moved from datru due to conflict with tatru.</q>（tatru（乳）とのgismu語形衝突が指摘される前はdatruの形で定義されてゐた。今現在の日本語の辞書データもdatruのもの。）</li>
<li><q cite="http://jbovlaste.lojban.org/dict/datro?bg=1;langidarg=2">We felt that detri just didn't work as a culturally-independent date system. The use of pi'e or joi as date mechanisms was insufficient and having the date components built into the place structure seems far more elegant.</q>（<q cite="http://jbovlaste.lojban.org/dict/datru?langidarg=10">detri は十分に文化中立的な日付システムとして機能していないという声がある。さらに日付の機構にpi'eやjoiを使うのは不十分であり、日・月・年の要素をそれぞれPSに設けたほうがより一層すっきりしているように思われる。</q>）</li>
</ul>
</dd>
</dl>
* datroはdetriをもぢつて作られた、detriとは別の形式で日付（と事象との関係）を表すための試験的gismu
  * 「『文化中立的な日付システム』として不十分である」と一部で認識されたdetri（の特にx1）を分解して、年月日を個別に指定するためのterbriを設けたもの

## datroのモヤッとする点
* 突然ですが自分はこのdatroの日付システムがいまいち好かんのです
  * detriのx1のやりかたが全面的に良いとも言へないものの、datroを選好するほどでもない
    * （数値だけでなく文字列とかその他のタイプのsinxaもdetri1にぶち込めれば個人的にはそれで満足 ta'osai）
* 「文化中立的な日付システムとして機能していない」といふ認識の具体的なところがよくわからない
  * 「日付の構成要素にpi'eやjoiを使用するのは不十分」といふ認識とのつながりであれば、まあ何となく解る：年月日の区切り記号だけでは、区切られた数値のどれが年でどれが月でどれが日でといふのを明示できない
    * もし全世界的に所謂西暦で統一されてゐたとしても、地域によつて我々みたく年月日の順で表記したり（2016年12月3日、2016/12/3）、逆に日月年の順で表記したり（3/12/2016）、年だけ最後にしたり（12/3/2016）（アメリカmu'aはこちららしいti'e）
    * そのあたりの文化的な揺らぎに対応しきれない…やうに見えてしまふのは、まあ仕方はない
  * しかし年月日用のterbriの順番を固定したりそもそも年月日による日付に限定するのはその「文化的中立性」の観点からして如何なものか
    * 週に基づく暦法とかそもそも年月に依らない暦法とか
* 自分はlojbanメーリングリストに投稿された[detriのx1についてのスレ][detri1]における[guskant氏の見解][gussan]に全く同意する立場：つまり、detri1の形式を制限するのではなく、detri4等でdetri1の形式について詳述する仕組みを解説・整備すべき
  * <blockquote><p>Those different answers gave you some different examples of convention, which are not suggestion for official definition.</p><p>The official definition of {detri} does not restrict the form of x1 to one convention: x1 of {detri} is any sumti that can be a symbol for a time point; the applicable symbol is defined with x4.</p><p>The form of x1 depends on context, and you can specify the form with x4 or any additional items like {fi'o}, {noi}, {ti'o}* and so on if necessary.</p></blockquote>
  * <blockquote>The official definition for {detri} should not specify the ordering because {detri} has x4 by nature to specify the calendar that defines the system of mapping of symbols to time points. If you think the current definition is confusing, we need to add explanation of usage of x4, not restriction to the form of x1.</blockquote>
* datroのやりかたはdetriのx1の形式のうちの一タイプだけを認めたにすぎないと自分は認識する

## detriのx1でなんとかする

* detriのx1における「time units」は:
  * specified as numbers separated by pi'e or（pi'eで区切られた数字として明示されるか）
  * are unit values massified with joi（joiで群化された数値たちである）

### pi'eやその他の何かで区切る仕方
* [lertcitydetri][ltd]
  * {li N2015 L5 D17 C22 M5 S23}みたいな形で、数値の前にそれが年なのか月なのか等を示すlerfuを置くらしい
    * ちなみに時分秒までも対応。他にもやたらオプションが多彩。
      * Mはmentuに譲つて、Lはlunra（天体としての月）から取つたらしい
* [ti'oで年月日の順番を明示する案][tiho]
  * 元々は演算子の優先順位を明示する目的で（未整備ではありつつも）導入されたSEI類だが([CLLの18.20][cll18_20])、色々な註を数式に入れる目的でもそれを応用しようとしてゐる模様
    * もしかして先に挙げたlertcitydetriもこれで明示可能？
  * 提案においてのti'oの使用例: <q>ti'o nanca ce'o masti ce'o djedi (se'u) li 2016 pi'e 5 pi'e 22 detri lo nu mi ciska kei lo gugdejupu la gregoris</q>
  * これは個人的にも開拓する甲斐を覚える

### joiでmassifyする仕方
* 色々試してみたもののこれはエレガントさで劣る感があるので今回は割愛（別にエレガントである必要も無いだらうけれど）

### その他の思ひつき
* [CLLの18.18][cll18_18]のmo'eの利用
  * detri1のためだけにmekso周りを真面目に勉強する必要に迫られようとは…
* lu'eに全部丸投げ

mu'o

[detri1]: https://groups.google.com/d/topic/lojban/1_LjXN5mq8Q/discussion
[gussan]: https://groups.google.com/d/msg/lojban/1_LjXN5mq8Q/xqlPKUg4AgAJ
[ltd]: https://mw.lojban.org/papri/Proposal:_loi_lerfu_tcita_detri;_the_final_word_on_the_problem_of_dates_and_times%3F
[tiho]: https://groups.google.com/d/msg/lojban/1_LjXN5mq8Q/QxLIqjlmEgAJ
[cll18_20]: https://lojban.github.io/cll/18/20/
[cll18_18]: https://lojban.github.io/cll/18/18/
