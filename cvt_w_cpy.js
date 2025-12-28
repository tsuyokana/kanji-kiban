function copyToClipboard() {
  // コピー対象をJavaScript上で変数として定義する
  const copyTarget = document.getElementById("text2");

  // コピー対象のテキストを選択する
  copyTarget.select();

  // 選択しているテキストをクリップボードにコピーする
  navigator.clipboard.writeText(copyTarget.value)
    .then(() => {
      // コピー成功時の処理
      console.log("コピーできました！ : " + copyTarget.value);
    })
    .catch((error) => {
      // コピー失敗時の処理
      console.error("コピーできませんでした", error);
    });
}
