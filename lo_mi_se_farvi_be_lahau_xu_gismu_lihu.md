# lalxuさんのxugismuの時間制限版を作りました

* lalxuさんの「[xu gismu?][original]」
  * それを基にした拙作の[時間制限版][mypage]（さしあたり30秒で）

ランダムに生成される4つのgismuからひたすら公式のgismuを選び取るだけのシンプルなゲームです。自分のこの版では、時間内になるべく多くの正答をするのがゲームの目的です。

[専用のリポジトリ][myrepo]を新たに立てつつ[GitHubページで公開した][mypage]ので、先づはプレイしてみてください。（[オリジナルのリポジトリ][originalrepo]からのフォークの[派生ブランチの内容][losefarvi]を切り出したもの。）lalxuさんの[オリジナル版][original]を未プレイの方はそちらも是非。

<div class="iframe_wrapper"><iframe src="https://niftg.github.io/xugismu_to-losefarvi-toi/junla-johu-notci.html"></iframe></div>

## 機能追加の経緯

* [オリジナル版][original]は特にゲームオーバーも無く、際限無く出題されるので、自分で予めルールを設定しないと、ゲームの止め時を見失つてしまひます（自分だけ？）
* ゲーム終了条件の候補
  * 全gismuに相当する量の問題を制覇したら
    * [selpa'iさんがのべ1337問をノーミスで連続正答する様子を収めた動画][selpahi]
      * ここまで腰を据ゑてやる気力は自分には無いな…
  * 誤答を積み重ねてライフが切れたら
    * 時間を掛ければ殆ど誤答をしない自分にはそれほど意味をなさない
  * 単純に時間切れになつたら
    * 一回答あたりの制限時間？
    * 一ゲームあたりの制限時間？
      * 今回はこちらを選好
  * ライフ制＋時間制
* ゲームの結果の評価：つまりポイント計算
  * シンプルに正答数÷誤答数
    * 誤答数が0の時の事を思ふと面倒
  * シンプルに正答数－誤答数
    * 今回は各オペランドに何ら重み付けをせずにこれを採用
  * もつとずつと好い感じの評価方法があれば知らせてください

## プレイのコツ

* 記憶と勘
  * 予め多くの公式gismuを記憶しておく事は、正答のgismuを見つけ出すだけでなく、誤答のgismuを弾き出すのにも役に立つ
    * 公式のgismuは互ひに音が似過ぎてはならないといふ旨のルールがあるので、例へば公式のgismuの最後の母音が一字異なるだけのgismuは偽物である、等と断定可能
      * このルールについてはまた時間があれば追記
  * 丸諳記ではどうしても付け焼刃的で、その上で素早く判断するには「慣れ」や「勘」のレベルになるまで何らかの訓練や経験が要るかもしれない
  * それほど多くはない記憶や経験に基づく「勘」による当て推量がどの程度有効かは、また別の誰かに
* 正答数稼ぎ
  * 視点をなるべく揺らさずに一つのボタンに留めておくと、そこに正答のgismuが連続で現はれる時を見逃さずに正答数を比較的早く稼ぐ事が可能
    * 視野の狭い人向けの戦略か？（視野が広くて4つのgismuを一遍に見られる人はその視野の広さを活かす方が良ささう）

[originalrepo]: https://github.com/lynn/lynn.github.io
[losefarvi]: https://github.com/niftg/lynn.github.io/blob/losefarvi/xugismu/losefarvi/junla-johu-notci.html
[myrepo]: https://github.com/niftg/xugismu_to-losefarvi-toi/
[mypage]: https://niftg.github.io/xugismu_to-losefarvi-toi/junla-johu-notci.html
[original]: https://lynn.github.io/xugismu/
[selpahi]: http://selpahi.de/xugismu.mp4
