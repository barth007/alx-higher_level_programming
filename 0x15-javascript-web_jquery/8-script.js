$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (movies) {
      console.log(movies);
      $.each(movies.results, function (i, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
