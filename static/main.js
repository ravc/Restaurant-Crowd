'use strict';

$(() => {
  $('.button-collapse').sideNav('show');

  $("#autocomplete-input").on('keyup', e => {
    if(e.keyCode == 13) {
      $.post('/find', {q: $("#autocomplete-input").val(), p: $("input[name='group1']:checked").val()}, function(data) {
        if(data.length) $('ol').html(data);
        else alert("Nothing found");
      });
    }
  });

  $.getJSON('https://freegeoip.net/json/').done(location => {
    $.post('/init', location, data => {
      if(data.length) $('ol').html(data);
      else alert("Nothing found");
    });
  });
});
