'use strict';

$(() => {
  $('.button-collapse').sideNav('show');

  $("#autocomplete-input").on('keyup', e => {
    if(e.keyCode == 13) {
      $.ajax({
        url: '/find',
        type: 'POST',
        data: JSON.stringify([$("#autocomplete-input").val(), $("input[type='radio'][name='price']:checked").val(), $("#distance").val()]),
        contentType: 'application/json; charset=utf-8',
        success: data => {
          if(data.length) $('ol').html(data);
          else alert("Nothing found");
        }
      });
    }
  });

  navigator.geolocation.getCurrentPosition(location => {
    var coords = [location['coords']['latitude'], location['coords']['longitude']];
    $.ajax({
      url: '/init',
      type: 'POST',
      data: JSON.stringify(coords),
      contentType: 'application/json; charset=utf-8'
    });
  });
});
