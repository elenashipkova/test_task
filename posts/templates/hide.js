$(function() {
  $('button').click(function() {
    $('p').slideToggle(200)
    
    if ($(this).text() === 'Скрыть')
      $(this).text('Показать')
    else
      $(this).text('Скрыть')
      
      
      $('p').slideToggle(200);
  });
});