$(function(){
  var $formNuovoProdotto, $bottoneNuovoProdotto;

  $formNuovoProdotto = $('#form-nuovo-prodotto');
  $bottoneNuovoProdotto = $('#mostra-form-nuovo-prodotto');

  $formNuovoProdotto.hide();
  $bottoneNuovoProdotto.on('click', function () {
    $formNuovoProdotto.show();
  })


});
