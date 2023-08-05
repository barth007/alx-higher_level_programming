$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (say) {
      // console.log(say);
      $('#hello').text(say.hello);
    }
  });
});
